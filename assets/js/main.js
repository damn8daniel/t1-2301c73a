/* Сенсор Лицензирование · общий JS: скролл-движок, навигация, формы, калькулятор */
(function(){
'use strict';
var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ---------- навигация ---------- */
var nav = document.querySelector('.nav');
var burger = document.querySelector('.nav-burger');
if (burger) burger.addEventListener('click', function(){ nav.classList.toggle('open'); });
document.querySelectorAll('.nav-links a').forEach(function(a){
  a.addEventListener('click', function(){ nav.classList.remove('open'); });
});

/* ---------- появление блоков ---------- */
var io = new IntersectionObserver(function(es){
  es.forEach(function(e){
    if (e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); }
  });
}, {threshold:.15, rootMargin:'0px 0px -40px 0px'});
document.querySelectorAll('.fx,.fx-scale,.zoom-img').forEach(function(el){ io.observe(el); });

/* ---------- счётчики ---------- */
var cio = new IntersectionObserver(function(es){
  es.forEach(function(e){
    if (!e.isIntersecting) return;
    cio.unobserve(e.target);
    var el = e.target, target = +el.dataset.cnt, suffix = el.dataset.suf || '';
    if (reduce){ el.textContent = target.toLocaleString('ru') + suffix; return; }
    var t0 = performance.now(), D = 1400;
    (function tick(t){
      var p = Math.min((t - t0) / D, 1);
      var v = Math.round(target * (1 - Math.pow(1 - p, 3)));
      el.textContent = v.toLocaleString('ru') + suffix;
      if (p < 1) requestAnimationFrame(tick);
    })(t0);
  });
}, {threshold:.6});
document.querySelectorAll('[data-cnt]').forEach(function(el){ cio.observe(el); });

/* ---------- скролл-движок: прогресс сцен + параллакс + слова ---------- */
var scenes = [].slice.call(document.querySelectorAll('[data-scene]'));
var plxEls = [].slice.call(document.querySelectorAll('[data-parallax]'));
var wordScenes = [].slice.call(document.querySelectorAll('.wordscene')).map(function(s){
  return { el: s, words: [].slice.call(s.querySelectorAll('.words span')) };
});
var heroFx = document.querySelector('[data-hero-fx]');
var ticking = false;

function clamp01(v){ return v < 0 ? 0 : v > 1 ? 1 : v; }

function update(){
  ticking = false;
  var vh = innerHeight;

  // прогресс длинных сцен: 0 в момент прилипания, 1 на излёте
  scenes.forEach(function(s){
    var r = s.getBoundingClientRect();
    var total = r.height - vh;
    if (total <= 0) return;
    s.style.setProperty('--p', clamp01(-r.top / total).toFixed(4));
  });

  // покадровое проявление слов
  wordScenes.forEach(function(ws){
    var r = ws.el.getBoundingClientRect();
    var total = r.height - vh;
    if (total <= 0) return;
    var p = clamp01(-r.top / total);
    var lit = Math.floor(p * (ws.words.length + 2));
    ws.words.forEach(function(w, i){ w.classList.toggle('lit', i < lit); });
  });

  // параллакс картинок
  plxEls.forEach(function(el){
    var r = el.getBoundingClientRect();
    var center = (r.top + r.height / 2 - vh / 2) / vh; // -1..1
    var depth = +el.dataset.parallax || 30;
    el.style.transform = 'translateY(' + (center * -depth).toFixed(1) + 'px)';
  });

  // hero: лёгкое уменьшение и растворение при прокрутке
  if (heroFx){
    var p = clamp01(scrollY / (vh * .9));
    heroFx.style.opacity = (1 - p * .9).toFixed(3);
    heroFx.style.transform = 'scale(' + (1 - p * .06).toFixed(4) + ') translateY(' + (p * -28).toFixed(1) + 'px)';
  }

  // тень навигации
  nav && nav.classList.toggle('scrolled', scrollY > 8);
}

function onScroll(){
  if (!ticking){ requestAnimationFrame(update); ticking = true; }
}
if (!reduce && (scenes.length || plxEls.length || wordScenes.length || heroFx)){
  addEventListener('scroll', onScroll, {passive:true});
  addEventListener('resize', onScroll, {passive:true});
  update();
} else if (nav){
  addEventListener('scroll', function(){ nav.classList.toggle('scrolled', scrollY > 8); }, {passive:true});
}

/* ---------- faq ---------- */
document.querySelectorAll('.fi .fq').forEach(function(b){
  b.addEventListener('click', function(){ b.parentElement.classList.toggle('open'); });
});

/* ---------- калькулятор ---------- */
var calcNum = document.getElementById('calcNum');
if (calcNum){
  var calcTerm = document.getElementById('calcTerm');
  var calc = function(){
    var base = 35000;
    document.querySelectorAll('.opts').forEach(function(g){
      var on = g.querySelector('.opt.on');
      if (on) base += +on.dataset.v;
    });
    calcNum.textContent = 'от ' + Math.max(30000, base).toLocaleString('ru') + ' ₽';
    var urg = document.querySelector('[data-g="urg"] .opt.on');
    calcTerm.textContent = (urg && urg.dataset.v !== '0' ? 'срок от 10 рабочих дней' : 'срок 15-25 рабочих дней') + ', плюс госпошлина 7 500 ₽';
  };
  document.querySelectorAll('.opts').forEach(function(g){
    g.querySelectorAll('.opt').forEach(function(o){
      o.addEventListener('click', function(){
        g.querySelectorAll('.opt').forEach(function(x){ x.classList.remove('on'); });
        o.classList.add('on'); calc();
      });
    });
  });
  calc();
}

/* ---------- формы и тост ---------- */
window.submitForm = function(e){
  e.preventDefault();
  var t = document.getElementById('toast');
  if (t){ t.classList.add('show'); setTimeout(function(){ t.classList.remove('show'); }, 4000); }
  e.target.reset();
  return false;
};

/* ---------- мобильная панель после первого экрана ---------- */
var mbar = document.getElementById('mbar');
var sentinel = document.querySelector('[data-mbar-after]');
if (mbar && sentinel){
  new IntersectionObserver(function(es){
    es.forEach(function(e){ mbar.classList.toggle('show', !e.isIntersecting && e.boundingClientRect.top < 0); });
  }, {threshold:0}).observe(sentinel);
}
})();
