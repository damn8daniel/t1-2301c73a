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

/* ---------- фоновые орбы ---------- */
var orbs = [];
if (!reduce){
  for (var oi = 1; oi <= 4; oi++){
    var o = document.createElement('div');
    o.className = 'orb orb-' + oi;
    document.body.appendChild(o);
    orbs.push(o);
  }
}

/* ---------- гибкая линия-маршрут через ключевые точки ---------- */
var SVGNS = 'http://www.w3.org/2000/svg';
var jWrap = null, jDraw = null, jComet = null, jNodes = [], jFracs = [], jLen = 0;

function keySections(){
  return [].slice.call(document.querySelectorAll('main section')).filter(function(s){
    return s.offsetHeight > 250 && s.querySelector('h1,h2');
  });
}

function buildJourney(){
  if (jWrap){ jWrap.remove(); jWrap = null; jDraw = null; jComet = null; jNodes = []; jFracs = []; jLen = 0; }
  if (reduce || innerWidth < 1360) return;
  var secs = keySections();
  if (secs.length < 3) return;

  var vw = document.documentElement.clientWidth;
  var H = document.documentElement.scrollHeight;
  var margin = Math.max(28, Math.min(90, (vw - 1320) / 2 * .55));

  // ключевые точки: чередуем стороны
  var pts = secs.map(function(s, i){
    var y = s.getBoundingClientRect().top + scrollY + 130;
    var x = (i % 2 === 0) ? margin : vw - margin;
    return {x: x, y: Math.min(y, H - 80), sec: s,
            label: (s.querySelector('h1,h2').textContent || '').trim().replace(/\s+/g, ' ')};
  });

  // ломаная со скруглениями: вниз по краю, поперёк в зазоре между секциями
  var startY = Math.max(90, pts[0].y - 260);
  var d = 'M ' + pts[0].x + ' ' + startY + ' L ' + pts[0].x + ' ' + pts[0].y;
  for (var i = 0; i < pts.length - 1; i++){
    var p = pts[i], q = pts[i + 1];
    if (p.x === q.x){
      d += ' L ' + q.x + ' ' + q.y;
      continue;
    }
    var yc = q.y - 120;                                  // поперечина чуть выше следующего узла
    var r = Math.min(70, (yc - p.y - 12) / 2, Math.abs(q.x - p.x) / 2 - 4);
    if (r < 16){ d += ' L ' + q.x + ' ' + q.y; continue; }
    var dir = q.x > p.x ? 1 : -1;
    d += ' L ' + p.x + ' ' + (yc - r)
       + ' Q ' + p.x + ' ' + yc + ' ' + (p.x + dir * r) + ' ' + yc
       + ' L ' + (q.x - dir * r) + ' ' + yc
       + ' Q ' + q.x + ' ' + yc + ' ' + q.x + ' ' + (yc + r)
       + ' L ' + q.x + ' ' + q.y;
  }
  d += ' L ' + pts[pts.length - 1].x + ' ' + Math.min(H - 60, pts[pts.length - 1].y + 220);

  jWrap = document.createElement('div');
  jWrap.className = 'journey';
  jWrap.style.height = H + 'px';
  var svg = document.createElementNS(SVGNS, 'svg');
  svg.setAttribute('viewBox', '0 0 ' + vw + ' ' + H);
  svg.setAttribute('preserveAspectRatio', 'none');

  var defs = document.createElementNS(SVGNS, 'defs');
  defs.innerHTML = '<linearGradient id="jgrad" x1="0" y1="0" x2="0" y2="1">' +
    '<stop offset="0" stop-color="#1D5BD6"/><stop offset=".5" stop-color="#5E8EE8"/>' +
    '<stop offset="1" stop-color="#1D5BD6"/></linearGradient>';
  svg.appendChild(defs);

  var track = document.createElementNS(SVGNS, 'path');
  track.setAttribute('d', d);
  track.setAttribute('class', 'jtrack');
  svg.appendChild(track);

  jDraw = document.createElementNS(SVGNS, 'path');
  jDraw.setAttribute('d', d);
  jDraw.setAttribute('class', 'jdraw');
  svg.appendChild(jDraw);

  jLen = jDraw.getTotalLength();
  jDraw.style.strokeDasharray = jLen;
  jDraw.style.strokeDashoffset = jLen;

  // доли длины пути для каждого узла (по ближайшей точке выборки)
  var SAMPLES = 600, cursor = 0;
  jFracs = pts.map(function(){ return 1; });
  for (var k = 0; k < pts.length; k++){
    var best = Infinity, bestT = 1;
    for (var t = cursor; t <= SAMPLES; t++){
      var sp = jDraw.getPointAtLength(jLen * t / SAMPLES);
      var dx = sp.x - pts[k].x, dy = sp.y - pts[k].y;
      var dist = dx * dx + dy * dy;
      if (dist < best){ best = dist; bestT = t; }
      if (dist < 16) break;
    }
    cursor = bestT;
    jFracs[k] = bestT / SAMPLES;
  }

  jNodes = pts.map(function(pt){
    var g = document.createElementNS(SVGNS, 'circle');
    g.setAttribute('cx', pt.x); g.setAttribute('cy', pt.y); g.setAttribute('r', 6);
    g.setAttribute('class', 'jnode');
    var title = document.createElementNS(SVGNS, 'title');
    title.textContent = pt.label;
    g.appendChild(title);
    g.addEventListener('click', function(){ pt.sec.scrollIntoView({behavior:'smooth', block:'start'}); });
    svg.appendChild(g);
    return g;
  });

  jComet = document.createElementNS(SVGNS, 'circle');
  jComet.setAttribute('r', 4.5);
  jComet.setAttribute('class', 'jcomet');
  svg.appendChild(jComet);

  jWrap.appendChild(svg);
  document.body.appendChild(jWrap);
}

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
  // линия-маршрут: прорисовка, комета, подсветка узлов
  var docH = document.documentElement.scrollHeight;
  var pj = docH > vh ? clamp01((scrollY + vh * .62) / docH) : 0;
  if (jDraw && jLen){
    var drawn = jLen * pj;
    jDraw.style.strokeDashoffset = (jLen - drawn).toFixed(1);
    var cp = jDraw.getPointAtLength(drawn);
    jComet.setAttribute('cx', cp.x.toFixed(1));
    jComet.setAttribute('cy', cp.y.toFixed(1));
    for (var ni = 0; ni < jNodes.length; ni++){
      jNodes[ni].classList.toggle('on', jFracs[ni] <= pj + .002);
    }
  }
  // орбы дрейфуют с разной скоростью
  var po = docH > vh ? clamp01(scrollY / (docH - vh)) : 0;
  for (var bi = 0; bi < orbs.length; bi++){
    orbs[bi].style.transform = 'translateY(' + (-po * (160 + bi * 90)).toFixed(1) + 'px)';
  }
  nav && nav.classList.toggle('scrolled', scrollY > 8);
}
function onScroll(){
  if (!ticking){ requestAnimationFrame(update); ticking = true; }
}
if (!reduce){
  buildJourney();
  addEventListener('load', function(){ buildJourney(); update(); });
  var rT;
  addEventListener('resize', function(){
    clearTimeout(rT);
    rT = setTimeout(function(){ buildJourney(); update(); }, 300);
    onScroll();
  }, {passive:true});
  addEventListener('scroll', onScroll, {passive:true});
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
  document.addEventListener('click', function(e){
    var a = e.target.closest('a[href*="zayavka"]');
    if (!a) return;
    var url = new URL(a.getAttribute('href'), location.href);
    var samePage = url.pathname === location.pathname;
    if (samePage && document.getElementById('zayavka')) return;
    e.preventDefault();
    openModal();
  });
  modal.querySelector('.modal-x').addEventListener('click', function(){ modal.close(); });
  modal.addEventListener('click', function(e){
    if (e.target === modal) modal.close();
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
