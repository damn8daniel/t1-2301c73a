/* Сенсор Лицензирование · общий JS: скролл-движок, навигация, формы, модалка, калькулятор */
(function(){
'use strict';
var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

/* Куда отправлять заявки. Поддерживается formsubmit.co / formspree / свой вебхук.
   Пусто = демо-режим: заявка сохраняется в localStorage и показывается тост. */
var LEAD_ENDPOINT = '';

/* ---------- навигация ---------- */
var nav = document.querySelector('.nav');
var burger = document.querySelector('.nav-burger');
if (burger){
  burger.setAttribute('aria-expanded','false');
  burger.addEventListener('click', function(){
    var open = nav.classList.toggle('open');
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
}
document.querySelectorAll('.nav-links a').forEach(function(a){
  a.addEventListener('click', function(){
    nav.classList.remove('open');
    burger && burger.setAttribute('aria-expanded','false');
  });
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

/* ---------- скролл-движок ---------- */
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
  scenes.forEach(function(s){
    var r = s.getBoundingClientRect();
    var total = r.height - vh;
    if (total <= 0) return;
    s.style.setProperty('--p', clamp01(-r.top / total).toFixed(4));
  });
  wordScenes.forEach(function(ws){
    var r = ws.el.getBoundingClientRect();
    var total = r.height - vh;
    if (total <= 0) return;
    var p = clamp01(-r.top / total);
    var lit = Math.floor(p * (ws.words.length + 2));
    ws.words.forEach(function(w, i){ w.classList.toggle('lit', i < lit); });
  });
  plxEls.forEach(function(el){
    var r = el.getBoundingClientRect();
    var center = (r.top + r.height / 2 - vh / 2) / vh;
    var depth = +el.dataset.parallax || 30;
    el.style.transform = 'translateY(' + (center * -depth).toFixed(1) + 'px)';
  });
  if (heroFx){
    var p = clamp01(scrollY / (vh * .9));
    heroFx.style.opacity = (1 - p * .9).toFixed(3);
    heroFx.style.transform = 'scale(' + (1 - p * .06).toFixed(4) + ') translateY(' + (p * -28).toFixed(1) + 'px)';
  }
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

/* ---------- маска телефона ---------- */
document.querySelectorAll('input[type="tel"]').forEach(function(inp){
  inp.addEventListener('input', function(){
    var d = inp.value.replace(/\D/g, '');
    if (d.charAt(0) === '8') d = '7' + d.slice(1);
    if (d && d.charAt(0) !== '7') d = '7' + d;
    d = d.slice(0, 11);
    var out = '';
    if (d.length){ out = '+7'; }
    if (d.length > 1) out += ' ' + d.slice(1, 4);
    if (d.length > 4) out += ' ' + d.slice(4, 7);
    if (d.length > 7) out += '-' + d.slice(7, 9);
    if (d.length > 9) out += '-' + d.slice(9, 11);
    inp.value = out;
  });
});

/* ---------- отправка заявки ---------- */
function showToast(msg){
  var t = document.getElementById('toast');
  if (!t) return;
  if (msg) t.textContent = msg;
  t.classList.add('show');
  setTimeout(function(){ t.classList.remove('show'); }, 4000);
}
window.submitForm = function(e){
  e.preventDefault();
  var form = e.target;
  var data = {
    name: (form.querySelector('[name="name"]') || {}).value || '',
    phone: (form.querySelector('[name="phone"]') || {}).value || '',
    page: location.pathname,
    ts: new Date().toISOString()
  };
  var btn = form.querySelector('[type="submit"]');
  var done = function(ok){
    if (btn) btn.disabled = false;
    if (ok){
      form.reset();
      var dlg = form.closest('dialog');
      if (dlg) dlg.close();
      showToast('Заявка принята. Перезвоним в течение 15 минут');
    } else {
      showToast('Не получилось отправить. Позвоните: 8 800 222-09-86');
    }
  };
  if (btn) btn.disabled = true;
  if (LEAD_ENDPOINT){
    fetch(LEAD_ENDPOINT, {
      method: 'POST',
      headers: {'Content-Type':'application/json','Accept':'application/json'},
      body: JSON.stringify(data)
    }).then(function(r){ done(r.ok); }).catch(function(){ done(false); });
  } else {
    /* демо-режим: складываем заявки локально */
    try {
      var leads = JSON.parse(localStorage.getItem('leads') || '[]');
      leads.push(data);
      localStorage.setItem('leads', JSON.stringify(leads));
    } catch(_){}
    setTimeout(function(){ done(true); }, 350);
  }
  return false;
};

/* ---------- модалка заявки ---------- */
var modal = document.getElementById('leadModal');
if (modal){
  var openModal = function(){
    modal.showModal();
    var f = modal.querySelector('input');
    if (f) setTimeout(function(){ f.focus(); }, 60);
  };
  /* перехватываем все ссылки на форму с других страниц */
  document.addEventListener('click', function(e){
    var a = e.target.closest('a[href*="zayavka"]');
    if (!a) return;
    var url = new URL(a.getAttribute('href'), location.href);
    var samePage = url.pathname === location.pathname;
    if (samePage && document.getElementById('zayavka')) return; /* якорь на этой же странице */
    e.preventDefault();
    openModal();
  });
  modal.querySelector('.modal-x').addEventListener('click', function(){ modal.close(); });
  modal.addEventListener('click', function(e){
    if (e.target === modal) modal.close(); /* клик по подложке */
  });
}

/* ---------- мобильная панель после первого экрана ---------- */
var mbar = document.getElementById('mbar');
var sentinel = document.querySelector('[data-mbar-after]');
if (mbar && sentinel){
  new IntersectionObserver(function(es){
    es.forEach(function(e){ mbar.classList.toggle('show', !e.isIntersecting && e.boundingClientRect.top < 0); });
  }, {threshold:0}).observe(sentinel);
}
})();
