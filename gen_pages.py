# -*- coding: utf-8 -*-
"""Генератор всех страниц сайта. v8 «NYC»: один источник правды для шапки/футера/модалки."""
import io, json

SITE = 'https://damn8daniel.github.io/t1-2301c73a/'
V = 'v=8'

HEAD = '''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="robots" content="noindex,nofollow">
<meta name="description" content="{desc}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/favicon-64.png" type="image/png" sizes="64x64">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Сенсор Лицензирование">
<meta property="og:locale" content="ru_RU">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{site}assets/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="assets/fonts/it-cyrillic-400_900.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/it-latin-400_900.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/jbm-cyrillic-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/main.css?''' + V + '''">
{extra_head}</head>
<body>

<div class="progress" aria-hidden="true"><i id="pbar"></i></div>
<nav class="nav"><div class="nav-in">
  <a class="nav-logo" href="index.html"><img src="assets/real/logo.png" alt="Сенсор Лицензирование" width="125" height="45"></a>
  <div class="nav-links">
    <a {a1} href="licenziya-mchs.html">Лицензия МЧС</a>
    <a {a2} href="vidy-rabot.html">Виды работ</a>
    <a {a3} href="tseny.html">Цены</a>
    <a {a4} href="proverka.html">Проверка лицензии</a>
    <a {a5} href="o-kompanii.html">О компании</a>
    <a {a6} href="kontakty.html">Контакты</a>
    <a class="mtel" href="tel:+78002220986">8 800 222-09-86</a>
  </div>
  <div class="nav-right">
    <a class="nav-tel" href="tel:+78002220986">8 800 222-09-86</a>
    <a class="btn" href="kontakty.html#zayavka">Заявка</a>
    <button class="nav-burger" aria-label="Меню"><span></span><span></span><span></span></button>
  </div>
</div></nav>

<main>
'''

FOOT = '''
</main>

<footer>
  <div class="w"><div class="f-big">Сенсор<span>.</span></div></div>
  <div class="w f-cols">
    <div class="f-brand">
      <b>Сенсор Лицензирование</b>
      <p>Лицензии МЧС, СРО, ISO, электролаборатория и учебный центр. Работаем по всей России с 2016 года.</p>
    </div>
    <div><b>Услуги</b>
      <a href="licenziya-mchs.html">Лицензия МЧС</a>
      <a href="vidy-rabot.html">Виды работ</a>
      <a href="tseny.html">Цены и тарифы</a>
      <a href="proverka.html">Проверка лицензии</a>
    </div>
    <div><b>Компания</b>
      <a href="o-kompanii.html">О компании</a>
      <a href="o-kompanii.html#centr">Учебный центр</a>
      <a href="kontakty.html">Контакты</a>
    </div>
    <div><b>Контакты</b>
      <a class="f-tel" href="tel:+78002220986">8 800 222-09-86</a>
      <a href="kontakty.html">Москва, БП «Румянцево»,<br>корп. В, оф. 409В</a>
    </div>
  </div>
  <div class="w f-bottom">
    <div>© 2016-2026 ООО «НТЦ СпецПожСтандарт» · ИНН 7751144295</div>
    <div>Работаем по всей России</div>
  </div>
</footer>

<div class="mbar" id="mbar">
  <a class="btn line" href="tel:+78002220986">Позвонить</a>
  <a class="btn" href="kontakty.html#zayavka">Заявка</a>
</div>

<dialog class="modal" id="leadModal">
  <button class="modal-x" aria-label="Закрыть"></button>
  <form class="form" onsubmit="return submitForm(event)">
    <h3>Оставить заявку</h3>
    <p>Перезвоним в течение 15 минут в рабочее время, рассчитаем стоимость и срок.</p>
    <div class="fld"><label for="m-name">Ваше имя</label><input id="m-name" name="name" placeholder="Иван" required autocomplete="name"></div>
    <div class="fld"><label for="m-phone">Телефон</label><input id="m-phone" name="phone" type="tel" placeholder="+7 ___ ___-__-__" required autocomplete="tel"></div>
    <button class="btn" type="submit">Отправить</button>
    <div class="fine">Нажимая кнопку, вы соглашаетесь с политикой обработки персональных данных</div>
  </form>
</dialog>

<div class="toast" id="toast">Заявка принята. Перезвоним в течение 15 минут</div>

<script src="assets/js/main.js?''' + V + '''" defer></script>
</body>
</html>
'''

def breadcrumb_ld(crumb, fname):
    data = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Главная","item":SITE},
        {"@type":"ListItem","position":2,"name":crumb,"item":SITE+fname}]}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>\n'

def page(fname, nav_idx, title, desc, body, crumb=None, extra_head=''):
    acts = ['' for _ in range(6)]
    if nav_idx is not None:
        acts[nav_idx] = 'class="act"'
    extra = (breadcrumb_ld(crumb, fname) if crumb else '') + extra_head
    crumb_html = f'<div class="w crumbs"><a href="index.html">Главная</a><span>›</span>{crumb}</div>\n' if crumb else ''
    html = HEAD.format(title=title, desc=desc, extra_head=extra, url=SITE+(fname if fname!='index.html' else ''), site=SITE,
                       a1=acts[0], a2=acts[1], a3=acts[2], a4=acts[3], a5=acts[4], a6=acts[5]) + crumb_html + body + FOOT
    with io.open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print('written', fname)

LETTERS = '\n'.join(
    f'    <a class="hcard-img" href="assets/real/pismo_{i}.webp" target="_blank" rel="noopener"><img loading="lazy" src="assets/real/pismo_{i}.webp" width="815" height="1127" alt="Благодарственное письмо клиента, скан {i}"></a>'
    for i in range(1, 7))

CALC = '''
    <div class="calc fx-scale">
      <div class="calc-q">
        <div class="cq"><div class="ql">1. Сколько видов работ нужно?</div><div class="opts" data-g="vid">
          <span class="opt on" data-v="0">1-2 вида</span><span class="opt" data-v="20000">3-5 видов</span><span class="opt" data-v="45000">6 и больше</span></div></div>
        <div class="cq"><div class="ql">2. Форма организации</div><div class="opts" data-g="org">
          <span class="opt on" data-v="0">ООО</span><span class="opt" data-v="-5000">ИП</span></div></div>
        <div class="cq"><div class="ql">3. Специалисты и оборудование</div><div class="opts" data-g="res">
          <span class="opt on" data-v="0">Всё своё</span><span class="opt" data-v="30000">Нужна аренда оборудования</span><span class="opt" data-v="55000">Нужны и специалисты, и оборудование</span></div></div>
        <div class="cq"><div class="ql">4. Срочность</div><div class="opts" data-g="urg">
          <span class="opt on" data-v="0">Стандарт, 15-25 дней</span><span class="opt" data-v="40000">Срочно, от 10 дней</span></div></div>
      </div>
      <div class="calc-r">
        <div class="rl">Ориентир под ключ</div>
        <div class="rv" id="calcNum" aria-live="polite">от 35 000 ₽</div>
        <div class="rs" id="calcTerm">срок 15-25 рабочих дней, плюс госпошлина 7 500 ₽</div>
        <a class="btn inv" href="{cta}">Получить точный расчёт</a>
        <div class="note">Рассрочка 0% · оплата по этапам · без предоплаты</div>
      </div>
    </div>'''

PLANS = '''
    <div class="plans">
      <div class="plan fx"><h3>Документы</h3><div class="price">35 000 ₽</div><div class="term">10 рабочих дней</div>
        <ul><li>Подготовка пакета документов</li><li>Проверка на соответствие требованиям</li><li>Консультация эксперта</li></ul>
        <a class="btn line" href="kontakty.html#zayavka">Выбрать</a></div>
      <div class="plan best fx"><div class="tag">Выбирают чаще всего</div><h3>Под ключ</h3><div class="price">от 80 000 ₽</div><div class="term">15-25 рабочих дней</div>
        <ul><li>Полное сопровождение до реестра</li><li>Подбор специалистов</li><li>Аренда поверенного оборудования</li><li>Сопровождение выездной проверки</li><li>Гарантия результата в договоре</li></ul>
        <a class="btn" style="background:#fff;color:#0A0A0B;border-color:#fff" href="kontakty.html#zayavka">Выбрать</a></div>
      <div class="plan fx fx-d1"><h3>Срочно</h3><div class="price">от 130 000 ₽</div><div class="term">от 10 рабочих дней</div>
        <ul><li>Всё из тарифа «Под ключ»</li><li>Приоритетная подача</li><li>Ускоренное прохождение проверки</li></ul>
        <a class="btn line" href="kontakty.html#zayavka">Выбрать</a></div>
      <div class="plan fx fx-d2"><h3>Готовая фирма</h3><div class="price">от 299 000 ₽</div><div class="term">1-3 дня</div>
        <ul><li>ООО с действующей лицензией МЧС</li><li>Переоформление на вас</li><li>Чистая история компании</li></ul>
        <a class="btn line" href="kontakty.html#zayavka">Выбрать</a></div>
    </div>'''

FAQ8 = '''
    <div class="faq">
      <div class="fi"><button class="fq">Кому обязательно нужна лицензия МЧС?</button><div class="fa"><div><p>Всем организациям и ИП, которые выполняют монтаж, ТО и ремонт средств обеспечения пожарной безопасности, огнезащиту или тушение пожаров. В том числе для участия в тендерах по 44-ФЗ и 223-ФЗ и обслуживания собственных систем на объектах.</p></div></div></div>
      <div class="fi"><button class="fq">Сколько стоит лицензия МЧС в 2026 году?</button><div class="fa"><div><p>Госпошлина: 7 500 ₽. Сопровождение под ключ: от 35 000 ₽ за подготовку документов до 80 000-130 000 ₽ за полный пакет с подбором специалистов и оборудования. Точную цену рассчитаем по вашим видам работ.</p></div></div></div>
      <div class="fi"><button class="fq">За сколько дней оформляется лицензия?</button><div class="fa"><div><p>Заявление рассматривается до 15 рабочих дней. Полный цикл с подготовкой и проверкой занимает 15-25 рабочих дней, в срочном режиме от 10 дней.</p></div></div></div>
      <div class="fi"><button class="fq">Нужно ли своё оборудование и специалисты?</button><div class="fa"><div><p>Да. Требуются штатные специалисты с профильным образованием и поверенное оборудование по Приказу МЧС № 571. Мы помогаем с подбором персонала и предоставляем оборудование в аренду, покупать его не обязательно.</p></div></div></div>
      <div class="fi"><button class="fq">Лицензия бессрочная? Нужно ли продлевать?</button><div class="fa"><div><p>Да, лицензия бессрочная и действует по всей России. Продление не требуется, но раз в 3 года проводится периодическое подтверждение соответствия. Сопровождаем и эту процедуру.</p></div></div></div>
      <div class="fi"><button class="fq">Чем грозит работа без лицензии?</button><div class="fa"><div><p>Штрафы для юрлиц до 250 000 ₽, приостановка деятельности до 90 суток, отстранение от тендеров. При причинении ущерба возможна уголовная ответственность.</p></div></div></div>
      <div class="fi"><button class="fq">Можно ли купить готовую фирму с лицензией?</button><div class="fa"><div><p>Да. Доступны готовые ООО с действующей лицензией МЧС и чистой историей. Переоформление на вас занимает 1-3 дня.</p></div></div></div>
      <div class="fi"><button class="fq">Как проверить лицензию в реестре?</button><div class="fa"><div><p>По ИНН организации в открытом реестре лицензий на сайте МЧС России. Подробная инструкция на странице проверки лицензии.</p></div></div></div>
    </div>'''

# ============================================================ ГЛАВНАЯ
INDEX = '''
<section class="hero">
  <div class="w">
    <div class="meta">
      <span class="mono dim">Сенсор Лицензирование</span>
      <span class="mono dim">Москва · вся Россия · с 2016</span>
    </div>
    <h1 class="d1" data-hero-fx>Лицензия МЧС<br><span class="acc">под ключ</span></h1>
    <div class="sub-row">
      <p class="lead">Оформляем пожарные лицензии: от аудита до записи в реестре за 15-25 рабочих дней. Гарантия результата зафиксирована в договоре.</p>
      <div class="cta-row">
        <a class="btn" href="licenziya-mchs.html">Получить лицензию</a>
        <a class="btn line" href="tseny.html">Цены</a>
      </div>
    </div>
  </div>
  <div class="hero-img"><img src="assets/real/license-sample.webp" width="1024" height="364" alt="Лицензия МЧС, оформленная для клиента" data-parallax="20" fetchpriority="high"></div>
</section>
<div data-mbar-after></div>

<div class="ticker" aria-hidden="true"><div class="tr">
  <span>Лицензия МЧС</span><span class="acc">/</span><span>Под ключ</span><span class="acc">/</span><span>С 2016 года</span><span class="acc">/</span><span>1600+ лицензий</span><span class="acc">/</span><span>По всей России</span><span class="acc">/</span>
</div></div>

<section class="blk">
  <div class="w stats">
    <div class="stat fx"><div class="v" data-cnt="1600" data-suf="+">0</div><div class="l mono dim">лицензий МЧС оформлено</div></div>
    <div class="stat fx fx-d1"><div class="v"><span data-cnt="9">0</span> <i>лет</i></div><div class="l mono dim">на рынке, с 2016 года</div></div>
    <div class="stat fx fx-d2"><div class="v" data-cnt="98" data-suf="%">0</div><div class="l mono dim">проходят проверку с первого раза</div></div>
    <div class="stat fx fx-d3"><div class="v">4.9 <i>★</i></div><div class="l mono dim">Яндекс Карты и 2ГИС</div></div>
  </div>
</section>

<section class="blk-ink wordscene" style="height:180vh">
  <div class="pin"><div class="w">
    <p class="words">
      <span>Работа</span> <span>без</span> <span>лицензии</span> <span>МЧС</span> <span>грозит</span>
      <span class="accent">штрафом</span> <span class="accent">до</span> <span class="accent">250 000 ₽</span>
      <span>и</span> <span>остановкой</span> <span>деятельности</span> <span>на</span> <span>90</span> <span>суток.</span>
      <span>Мы</span> <span>доводим</span> <span>до</span> <span>записи</span> <span>в</span> <span>реестре</span>
      <span class="accent">за</span> <span class="accent">15-25</span> <span class="accent">дней.</span>
    </p>
  </div></div>
</section>

<section class="blk">
  <div class="w">
    <div class="head-row"><h2 class="d2">Чем мы занимаемся</h2><span class="idx">5 направлений</span></div>
    <div class="svc-list">
      <a class="svc" href="licenziya-mchs.html">
        <span class="num">/01</span><h3>Лицензия МЧС под ключ</h3>
        <p>Монтаж, обслуживание и ремонт средств пожарной безопасности, огнезащита, тушение. От 35 000 ₽, 15-25 рабочих дней.</p>
        <span class="arr">→</span>
      </a>
      <a class="svc" href="licenziya-mchs.html#pereoformlenie">
        <span class="num">/02</span><h3>Переоформление</h3>
        <p>Добавление видов работ, смена адреса или реквизитов, периодическое подтверждение раз в 3 года.</p>
        <span class="arr">→</span>
      </a>
      <a class="svc" href="tseny.html">
        <span class="num">/03</span><h3>Готовая фирма</h3>
        <p>ООО с действующей лицензией МЧС и чистой историей. Переоформление на вас за 1-3 дня.</p>
        <span class="arr">→</span>
      </a>
      <a class="svc" href="o-kompanii.html#centr">
        <span class="num">/04</span><h3>Обучение специалистов</h3>
        <p>Собственный учебный центр: повышение квалификации и аттестация под лицензионные требования.</p>
        <span class="arr">→</span>
      </a>
      <a class="svc" href="proverka.html">
        <span class="num">/05</span><h3>Проверка лицензии</h3>
        <p>Проверим ваш статус или статус подрядчика по ИНН в реестре МЧС России. Бесплатно.</p>
        <span class="arr">→</span>
      </a>
    </div>
  </div>
</section>

<section class="blk blk-paper blk-rule">
  <div class="w">
    <div class="head-row"><h2 class="d2">Три шага до лицензии</h2><span class="idx">15-25 дней</span></div>
    <div>
      <div class="step-row fx"><div class="num">01</div><div><h3>Аудит и договор</h3><p>Разбираем вашу ситуацию, подбираем виды работ, фиксируем цену, срок и гарантию результата.</p></div><span class="dur">1-2 дня</span></div>
      <div class="step-row fx"><div class="num">02</div><div><h3>Специалисты, оборудование, документы</h3><p>Закрываем лицензионные требования: персонал со стажем, поверенные приборы в аренду, полный пакет документов.</p></div><span class="dur">5-10 дней</span></div>
      <div class="step-row fx"><div class="num">03</div><div><h3>Подача и запись в реестре</h3><p>Подаём через Госуслуги, сопровождаем выездную проверку МЧС. Итог: ваша компания в реестре.</p></div><span class="dur">до 15 раб. дней</span></div>
    </div>
    <div style="margin-top:40px" class="fx"><a class="tlink" href="licenziya-mchs.html#etapy">Все шесть этапов подробно</a></div>
  </div>
</section>

<section class="blk blk-rule" style="padding-bottom:0">
  <div class="w">
    <div class="head-row"><h2 class="d2">Нам пишут благодарности</h2><span class="idx">4.9 ★ · 450+ отзывов</span></div>
    <p class="head-sub lead">Средняя оценка на Яндекс Картах, 2ГИС и Google. Ниже реальные письма клиентов: нажмите, чтобы открыть скан.</p>
  </div>
  <div class="hscroll">
''' + LETTERS + '''
  </div>
</section>

<section class="blk" style="padding-bottom:0">
  <div class="w">
    <div class="head-row"><h2 class="d2">Команда в теме с 2016 года</h2></div>
    <p class="head-sub lead">Лицензирование МЧС наш основной профиль, а не одна из ста услуг.</p>
  </div>
  <div class="img-full zoom-img fx-scale"><img loading="lazy" src="assets/real/office.webp" width="1024" height="683" alt="Команда компании Сенсор Лицензирование в офисе"></div>
  <div class="w" style="padding-top:36px;padding-bottom:8px"><a class="tlink" href="o-kompanii.html">Познакомиться с компанией</a></div>
</section>

<section class="blk">
  <div class="w">
    <div class="head-row"><h2 class="d2">Коротко о главном</h2></div>
    <div class="faq">
      <div class="fi"><button class="fq">Сколько стоит лицензия МЧС?</button><div class="fa"><div><p>Госпошлина: 7 500 ₽. Сопровождение под ключ: от 35 000 ₽ за документы до 80 000-130 000 ₽ за полный пакет со специалистами и оборудованием. Подробности на странице цен.</p></div></div></div>
      <div class="fi"><button class="fq">Сколько ждать?</button><div class="fa"><div><p>Полный цикл занимает 15-25 рабочих дней, в срочном режиме от 10 дней. Заявление в МЧС рассматривается до 15 рабочих дней.</p></div></div></div>
      <div class="fi"><button class="fq">Лицензия бессрочная?</button><div class="fa"><div><p>Да, действует бессрочно и по всей России. Раз в 3 года проходит периодическое подтверждение соответствия, его мы тоже сопровождаем.</p></div></div></div>
      <div class="fi"><button class="fq">А если лицензию не выдадут?</button><div class="fa"><div><p>Гарантия результата зафиксирована в договоре: если отказ произойдёт по нашей вине, вернём оплату полностью. На практике 98% клиентов проходят проверку с первого раза.</p></div></div></div>
    </div>
    <div style="margin-top:36px" class="fx"><a class="tlink" href="licenziya-mchs.html#faq">Все вопросы и ответы</a></div>
  </div>
</section>

<section class="blk blk-ink cta-final">
  <div class="w">
    <h2 class="d1 fx">Начните<br>с бесплатного <span class="acc">аудита</span></h2>
    <div class="row fx fx-d1">
      <p class="lead">Перезвоним за 15 минут, разберём вашу ситуацию и назовём точную цену и срок.</p>
      <div style="display:flex;gap:14px;flex-wrap:wrap">
        <a class="btn inv" href="kontakty.html#zayavka">Оставить заявку</a>
        <a class="btn line" style="color:#FAFAF7;border-color:rgba(250,250,247,.4)" href="tel:+78002220986">8 800 222-09-86</a>
      </div>
    </div>
  </div>
</section>
'''

# ============================================================ ЛИЦЕНЗИЯ МЧС
FAQ_LD = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Service","serviceType":"Получение лицензии МЧС","provider":{"@type":"Organization","name":"Сенсор Лицензирование","telephone":"+7-800-222-09-86"},"areaServed":"RU","offers":{"@type":"Offer","price":"35000","priceCurrency":"RUB"}}
</script>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Кому обязательно нужна лицензия МЧС?","acceptedAnswer":{"@type":"Answer","text":"Всем организациям и ИП, которые выполняют монтаж, техническое обслуживание и ремонт средств обеспечения пожарной безопасности, огнезащиту или тушение пожаров. В том числе для участия в тендерах по 44-ФЗ и 223-ФЗ."}},
{"@type":"Question","name":"Сколько стоит лицензия МЧС в 2026 году?","acceptedAnswer":{"@type":"Answer","text":"Госпошлина составляет 7 500 ₽. Сопровождение под ключ стоит от 35 000 ₽ за подготовку документов до 80 000-130 000 ₽ за полный пакет с подбором специалистов и оборудования."}},
{"@type":"Question","name":"За сколько дней оформляется лицензия?","acceptedAnswer":{"@type":"Answer","text":"Орган лицензирования рассматривает заявление до 15 рабочих дней. Полный цикл с подготовкой и проверкой занимает 15-25 рабочих дней, в срочном режиме от 10 дней."}},
{"@type":"Question","name":"Нужно ли своё оборудование и специалисты?","acceptedAnswer":{"@type":"Answer","text":"Да. Требуются штатные специалисты с профильным образованием и поверенное оборудование по Приказу МЧС № 571. Мы помогаем с подбором персонала и предоставляем оборудование в аренду."}},
{"@type":"Question","name":"Лицензия бессрочная? Нужно ли продлевать?","acceptedAnswer":{"@type":"Answer","text":"Лицензия бессрочная и действует по всей России. Продление не требуется, но раз в 3 года проводится периодическое подтверждение соответствия лицензионным требованиям."}},
{"@type":"Question","name":"Чем грозит работа без лицензии?","acceptedAnswer":{"@type":"Answer","text":"Административная ответственность по КоАП РФ: штрафы для юрлиц до 250 000 ₽ и приостановка деятельности до 90 суток. При причинении ущерба возможна уголовная ответственность."}},
{"@type":"Question","name":"Можно ли купить готовую фирму с лицензией МЧС?","acceptedAnswer":{"@type":"Answer","text":"Да. Доступны готовые ООО с действующей лицензией МЧС и чистой историей. Переоформление занимает 1-3 дня."}},
{"@type":"Question","name":"Как проверить лицензию в реестре МЧС?","acceptedAnswer":{"@type":"Answer","text":"По ИНН организации в открытом реестре лицензий на сайте МЧС России. Запись в реестре и есть сама лицензия: бумажные бланки не выдаются с 2021 года."}}]}
</script>
'''

VIDY9 = [
 ('01','Системы пожаротушения','Монтаж, ТО и ремонт водяного, пенного, газового, порошкового и аэрозольного пожаротушения, включая пусконаладку.'),
 ('02','Пожарная сигнализация','АПС и ОПС, системы передачи извещений, диспетчеризация, пусконаладка.'),
 ('03','Противопожарное водоснабжение','Внутренний водопровод, наружные сети, гидранты, насосные станции.'),
 ('04','Противодымная вентиляция','Дымоудаление и подпор воздуха, огнезадерживающие клапаны, вентиляторы.'),
 ('05','СОУЭ','Системы оповещения и управления эвакуацией людей при пожаре всех пяти типов.'),
 ('06','Противопожарные преграды','Двери, ворота, люки, окна, шторы: монтаж и обслуживание заполнений проёмов.'),
 ('07','Огнезащита','Обработка металлических и деревянных конструкций, кабелей, воздуховодов, тканей.'),
 ('08','Первичные средства','Огнетушители, пожарные шкафы, краны и рукава: установка, перезарядка, обслуживание.'),
 ('09','Тушение пожаров','Тушение в населённых пунктах и на объектах. Повышенные требования к персоналу и технике.'),
]
VIDY_CELLS = '\n'.join(
    f'      <div class="cell fx"><span class="num">/{n}</span><h3>{t}</h3><p>{d}</p></div>'
    for n, t, d in VIDY9)

LIC = '''
<section class="hero" style="padding-top:32px">
  <div class="w">
    <h1 class="d1" style="font-size:clamp(38px,6.4vw,96px)">Пожарная лицензия<br>МЧС <span class="acc">под ключ</span></h1>
    <div class="sub-row">
      <p class="lead">От 35 000 ₽ за 15-25 рабочих дней: специалисты, оборудование, документы и сопровождение проверки. Гарантия результата в договоре.</p>
      <div class="cta-row">
        <a class="btn" href="#calc">Рассчитать стоимость</a>
        <a class="btn line" href="tel:+78002220986">8 800 222-09-86</a>
      </div>
    </div>
  </div>
  <div class="hero-img"><img src="assets/real/license-sample.webp" width="1024" height="364" alt="Лицензия МЧС, оформленная для клиента компании Сенсор" data-parallax="18" fetchpriority="high"></div>
</section>
<div data-mbar-after></div>

<section class="blk" id="vidy">
  <div class="w">
    <div class="head-row"><h2 class="d2">Виды работ по лицензии</h2><span class="idx">ПП РФ № 1128</span></div>
    <p class="head-sub lead">Девять видов деятельности. Оформим на любой набор: от одного до всех девяти.</p>
    <div class="grid3">
''' + VIDY_CELLS + '''
    </div>
    <div style="margin-top:36px" class="fx"><a class="tlink" href="vidy-rabot.html">Подробное описание каждого вида</a></div>
  </div>
</section>

<section class="blk blk-paper blk-rule" id="calc">
  <div class="w">
    <div class="head-row"><h2 class="d2">Рассчитайте стоимость</h2><span class="idx">4 вопроса · 1 минута</span></div>
''' + CALC.format(cta='#zayavka') + '''
  </div>
</section>

<section class="blk" id="etapy">
  <div class="w">
    <div class="head-row"><h2 class="d2">Шесть шагов до реестра</h2><span class="idx">оплата по этапам</span></div>
    <div>
      <div class="step-row fx"><div class="num">01</div><div><h3>Консультация и аудит</h3><p>Разбираем ситуацию, подбираем виды работ, считаем точную стоимость.</p></div><span class="dur">1 день</span></div>
      <div class="step-row fx"><div class="num">02</div><div><h3>Договор</h3><p>Фиксируем цену, сроки и гарантию результата. Без скрытых доплат.</p></div><span class="dur">1 день</span></div>
      <div class="step-row fx"><div class="num">03</div><div><h3>Специалисты и оборудование</h3><p>Подбираем штат с нужным образованием и стажем, оформляем аренду поверенных приборов.</p></div><span class="dur">3-7 дней</span></div>
      <div class="step-row fx"><div class="num">04</div><div><h3>Пакет документов</h3><p>Готовим и перепроверяем полный комплект по требованиям Постановления № 1128.</p></div><span class="dur">2-4 дня</span></div>
      <div class="step-row fx"><div class="num">05</div><div><h3>Подача и проверка</h3><p>Подаём через Госуслуги, готовим объект и сопровождаем выездную оценку МЧС.</p></div><span class="dur">до 15 раб. дней</span></div>
      <div class="step-row fx"><div class="num">06</div><div><h3>Запись в реестре</h3><p>Сведения внесены в реестр МЧС России. Можно работать и участвовать в тендерах.</p></div><span class="dur">итог</span></div>
    </div>
  </div>
</section>

<section class="blk blk-paper blk-rule" id="trebovaniya">
  <div class="w">
    <div class="head-row"><h2 class="d2">Лицензионные требования</h2></div>
    <div class="grid3">
      <div class="cell fx"><span class="num">Персонал</span><h3>Образование и стаж</h3><p>Для ИП от 3 лет, для руководителя ООО от 5 лет, плюс повышение квалификации.</p><p style="margin-top:10px;color:var(--acc);font-weight:600">Закрываем: подбираем специалистов и обучаем в своём учебном центре.</p></div>
      <div class="cell fx fx-d1"><span class="num">Оборудование</span><h3>Поверенные приборы</h3><p>По Приказу МЧС № 571, с записью о поверке в ФГИС «Аршин»: манометр, мегаомметр, мультиметр и другие.</p><p style="margin-top:10px;color:var(--acc);font-weight:600">Закрываем: полный комплект в аренду, покупать не нужно.</p></div>
      <div class="cell fx fx-d2"><span class="num">Документы</span><h3>Полный пакет</h3><p>Устав, выписка ЕГРЮЛ или ЕГРИП, дипломы и трудовые специалистов, договор на помещение, заявление.</p><p style="margin-top:10px;color:var(--acc);font-weight:600">Закрываем: готовим и перепроверяем всё за вас.</p></div>
    </div>
  </div>
</section>

<section class="blk blk-ink" id="pereoformlenie">
  <div class="w">
    <div class="head-row"><h2 class="d2">Лицензия сегодня: запись в реестре</h2></div>
    <p class="head-sub lead">С 2021 года бумажные бланки не выдаются. Сведения вносятся в реестр МЧС России и проверяются по ИНН. Лицензия бессрочная, раз в 3 года проходит периодическое подтверждение.</p>
    <div class="grid3" style="border-color:rgba(250,250,247,.25)">
      <div class="cell fill fx" style="border-color:rgba(250,250,247,.25)"><span class="num">3 500 ₽ пошлина</span><h3>Переоформление</h3><p>Добавление видов работ, смена адреса, реквизитов или наименования. Сопровождаем под ключ.</p></div>
      <div class="cell fill fx fx-d1" style="border-color:rgba(250,250,247,.25)"><span class="num">Раз в 3 года</span><h3>Подтверждение</h3><p>МЧС проверяет соответствие лицензионным требованиям. Готовим и сопровождаем процедуру.</p></div>
      <div class="cell fill fx fx-d2" style="border-color:rgba(250,250,247,.25)"><span class="num">Правовая база</span><h3>ФЗ-99 · ФЗ-69 · ПП № 1128</h3><p>Работа без лицензии грозит штрафом до 250 000 ₽ и приостановкой деятельности до 90 суток по КоАП РФ.</p></div>
    </div>
    <div style="margin-top:36px" class="fx"><a class="tlink" style="color:#FAFAF7;border-color:#FAFAF7" href="proverka.html">Проверить лицензию в реестре</a></div>
  </div>
</section>

<section class="blk" id="faq">
  <div class="w">
    <div class="head-row"><h2 class="d2">Частые вопросы</h2></div>
''' + FAQ8 + '''
  </div>
</section>

<section class="blk blk-paper blk-rule" id="zayavka">
  <div class="w" style="max-width:660px">
    <div class="head-row" style="margin-bottom:28px"><h2 class="d2">Получить лицензию</h2></div>
    <form class="form fx" onsubmit="return submitForm(event)">
      <p>Перезвоним в течение 15 минут в рабочее время, рассчитаем стоимость и срок.</p>
      <div class="fld"><label for="f-name">Ваше имя</label><input id="f-name" name="name" placeholder="Иван" required autocomplete="name"></div>
      <div class="fld"><label for="f-phone">Телефон</label><input id="f-phone" name="phone" type="tel" placeholder="+7 ___ ___-__-__" required autocomplete="tel"></div>
      <button class="btn" type="submit">Оставить заявку</button>
      <div class="fine">Нажимая кнопку, вы соглашаетесь с политикой обработки персональных данных</div>
    </form>
  </div>
</section>
'''

# ============================================================ ВИДЫ РАБОТ
VIDY_PAGE_CELLS = '\n'.join(
    f'      <article class="cell fx"><span class="num">/{n}</span><h2>{t}</h2><p>{d}</p></article>'
    for n, t, d in [
 ('01','Системы пожаротушения','Монтаж, ТО и ремонт водяного, пенного, газового, порошкового и аэрозольного пожаротушения, включая пусконаладку. Самый востребованный вид: ТЦ, склады, производства, бизнес-центры.'),
 ('02','Пожарная сигнализация','АПС и ОПС, системы передачи извещений, диспетчеризация, пусконаладка. Нужен всем, кто ставит и обслуживает датчики и приёмно-контрольные приборы.'),
 ('03','Противопожарное водоснабжение','Внутренний противопожарный водопровод, наружные сети, пожарные гидранты, насосные станции.'),
 ('04','Противодымная вентиляция','Системы дымоудаления и подпора воздуха, огнезадерживающие клапаны, вентиляторы дымоудаления.'),
 ('05','СОУЭ','Системы оповещения и управления эвакуацией людей при пожаре всех пяти типов.'),
 ('06','Противопожарные преграды','Противопожарные двери, ворота, люки, окна, шторы: монтаж и обслуживание заполнений проёмов.'),
 ('07','Огнезащита','Огнезащитная обработка металлических и деревянных конструкций, кабелей, воздуховодов, тканей.'),
 ('08','Первичные средства','Огнетушители, пожарные шкафы, краны и рукава: установка, перезарядка, обслуживание.'),
 ('09','Тушение пожаров','Тушение пожаров в населённых пунктах и на объектах. Отдельное лицензирование с повышенными требованиями к персоналу и технике.'),
])

VIDY_PAGE = '''
<section class="hero" style="padding-top:28px;padding-bottom:0">
  <div class="w">
    <h1 class="d1" style="font-size:clamp(36px,5.8vw,88px)">Виды работ<br>по лицензии <span class="acc">МЧС</span></h1>
    <div class="sub-row">
      <p class="lead">Девять видов деятельности по Постановлению Правительства РФ № 1128. Оформим лицензию на любой набор: от одного вида до всех девяти.</p>
    </div>
  </div>
</section>
<div data-mbar-after></div>

<section class="blk" style="padding-top:24px">
  <div class="w">
    <div class="grid3">
''' + VIDY_PAGE_CELLS + '''
    </div>
    <div class="callout fx" style="margin-top:40px"><b>Не знаете, какие виды выбрать?</b> Подберём оптимальный набор под ваши контракты и тендеры: лишние виды удорожают лицензию, недостающие блокируют работу. Консультация бесплатная.</div>
  </div>
</section>

<section class="blk blk-ink cta-final">
  <div class="w">
    <h2 class="d1 fx" style="font-size:clamp(34px,5.4vw,84px)">Оформим на любой<br><span class="acc">набор видов</span></h2>
    <div class="row fx fx-d1">
      <p class="lead">Цена и срок зависят от набора: рассчитайте за минуту.</p>
      <div style="display:flex;gap:14px;flex-wrap:wrap">
        <a class="btn inv" href="licenziya-mchs.html#calc">Рассчитать стоимость</a>
        <a class="btn line" style="color:#FAFAF7;border-color:rgba(250,250,247,.4)" href="tel:+78002220986">8 800 222-09-86</a>
      </div>
    </div>
  </div>
</section>
'''

# ============================================================ ЦЕНЫ
TSENY = '''
<section class="hero" style="padding-top:28px;padding-bottom:0">
  <div class="w">
    <h1 class="d1" style="font-size:clamp(36px,5.8vw,88px)">Цены<br>и <span class="acc">тарифы</span></h1>
    <div class="sub-row">
      <p class="lead">Прозрачные пакеты без скрытых доплат. Госпошлина оплачивается отдельно: 7 500 ₽ за выдачу, 3 500 ₽ за переоформление.</p>
    </div>
  </div>
</section>
<div data-mbar-after></div>

<section class="blk" style="padding-top:24px">
  <div class="w">
''' + PLANS + '''
  </div>
</section>

<section class="blk blk-paper blk-rule" id="calc">
  <div class="w">
    <div class="head-row"><h2 class="d2">Рассчитайте под свою задачу</h2><span class="idx">4 вопроса · 1 минута</span></div>
''' + CALC.format(cta='kontakty.html#zayavka') + '''
  </div>
</section>

<section class="blk">
  <div class="w">
    <div class="head-row"><h2 class="d2">Вопросы про оплату</h2></div>
    <div class="faq">
      <div class="fi"><button class="fq">Есть ли предоплата?</button><div class="fa"><div><p>Нет. Работаем по этапам: оплата привязана к выполненным шагам из договора. Доступна рассрочка 0%.</p></div></div></div>
      <div class="fi"><button class="fq">Что входит в цену «под ключ»?</button><div class="fa"><div><p>Подбор специалистов, аренда поверенного оборудования, подготовка документов, подача через Госуслуги и сопровождение выездной проверки МЧС. Госпошлина 7 500 ₽ оплачивается отдельно.</p></div></div></div>
      <div class="fi"><button class="fq">От чего зависит итоговая стоимость?</button><div class="fa"><div><p>От количества видов работ, наличия у вас специалистов и оборудования, формы организации и срочности. Точный расчёт делаем после короткого аудита.</p></div></div></div>
      <div class="fi"><button class="fq">Что будет, если лицензию не выдадут?</button><div class="fa"><div><p>Гарантия результата зафиксирована в договоре: при отказе по нашей вине возвращаем оплату полностью.</p></div></div></div>
    </div>
  </div>
</section>
'''

# ============================================================ ПРОВЕРКА
PROVERKA = '''
<section class="hero" style="padding-top:28px;padding-bottom:0">
  <div class="w">
    <h1 class="d1" style="font-size:clamp(34px,5.4vw,82px)">Проверка лицензии<br>МЧС <span class="acc">в реестре</span></h1>
    <div class="sub-row">
      <p class="lead">С 2021 года лицензия существует только как запись в реестре МЧС России. Проверить себя или подрядчика можно за пару минут.</p>
    </div>
  </div>
</section>
<div data-mbar-after></div>

<section class="blk" style="padding-top:24px">
  <div class="w">
    <div>
      <div class="step-row fx"><div class="num">01</div><div><h3>Откройте реестр МЧС</h3><p>Реестр лицензий опубликован на официальном сайте МЧС России и доступен без регистрации.</p></div></div>
      <div class="step-row fx"><div class="num">02</div><div><h3>Введите ИНН</h3><p>Достаточно ИНН организации или ИП. Название тоже работает, но ИНН надёжнее: исключает однофамильцев.</p></div></div>
      <div class="step-row fx"><div class="num">03</div><div><h3>Сверьте карточку</h3><p>Статус лицензии, перечень разрешённых видов работ и дата записи. Виды работ должны покрывать предмет вашего договора.</p></div></div>
    </div>
  </div>
</section>

<section class="blk blk-paper blk-rule">
  <div class="w prose">
    <h2>Как читать результат</h2>
    <ul>
      <li><b>Запись есть, статус действующий:</b> подрядчик имеет право выполнять указанные виды работ.</li>
      <li><b>Записи нет:</b> лицензия отсутствует, договор с таким подрядчиком несёт риски для заказчика.</li>
      <li><b>Виды работ не совпадают с договором:</b> подрядчик выходит за рамки своей лицензии.</li>
    </ul>
    <div class="callout"><b>Важно:</b> бумажный бланк сам по себе ничего не подтверждает с 2021 года. Юридическую силу имеет только запись в реестре.</div>
    <h2>Что проверить кроме реестра</h2>
    <p>Для тендеров и крупных контрактов дополнительно смотрят выписку ЕГРЮЛ, наличие штатных специалистов и действующую поверку оборудования. Эти же требования МЧС проверяет при периодическом подтверждении раз в 3 года.</p>
    <h2>Поможем разобраться</h2>
    <p>Если со статусом что-то не так: лицензии нет, виды работ не совпадают или подходит срок периодического подтверждения, позвоните нам. Подскажем бесплатно, что делать дальше.</p>
  </div>
</section>

<section class="blk blk-ink cta-final">
  <div class="w">
    <h2 class="d1 fx" style="font-size:clamp(34px,5.4vw,84px)">Нужна своя<br><span class="acc">лицензия?</span></h2>
    <div class="row fx fx-d1">
      <p class="lead">Оформим под ключ за 15-25 рабочих дней с гарантией в договоре.</p>
      <div style="display:flex;gap:14px;flex-wrap:wrap">
        <a class="btn inv" href="licenziya-mchs.html">Получить лицензию</a>
        <a class="btn line" style="color:#FAFAF7;border-color:rgba(250,250,247,.4)" href="tel:+78002220986">8 800 222-09-86</a>
      </div>
    </div>
  </div>
</section>
'''

# ============================================================ О КОМПАНИИ
OKOMP = '''
<section class="hero" style="padding-top:28px;padding-bottom:0">
  <div class="w">
    <h1 class="d1" style="font-size:clamp(36px,5.8vw,88px)">Сенсор<br><span class="acc">Лицензирование</span></h1>
    <div class="sub-row">
      <p class="lead">Помогаем бизнесу легально работать в сфере пожарной безопасности: лицензии МЧС, СРО, ISO, электролаборатория и собственный учебный центр.</p>
    </div>
  </div>
</section>
<div data-mbar-after></div>

<div class="img-full zoom-img fx-scale"><img src="assets/real/office.webp" width="1024" height="683" alt="Команда компании Сенсор Лицензирование в офисе" fetchpriority="high"></div>

<section class="blk">
  <div class="w stats">
    <div class="stat fx"><div class="v" data-cnt="1600" data-suf="+">0</div><div class="l mono dim">лицензий МЧС оформлено</div></div>
    <div class="stat fx fx-d1"><div class="v"><span data-cnt="9">0</span> <i>лет</i></div><div class="l mono dim">на рынке, с 2016 года</div></div>
    <div class="stat fx fx-d2"><div class="v" data-cnt="6">0</div><div class="l mono dim">филиалов по России</div></div>
    <div class="stat fx fx-d3"><div class="v" data-cnt="20" data-suf="+">0</div><div class="l mono dim">госконтрактов сопровождено</div></div>
  </div>
</section>

<section class="blk blk-paper blk-rule">
  <div class="w">
    <div class="head-row"><h2 class="d2">Почему с нами спокойно</h2></div>
    <div class="grid2">
      <div class="cell fx"><span class="num">Гарантия</span><h3>Результат в договоре</h3><p>Если лицензию не выдадут по нашей вине, вернём оплату полностью. На практике 98% клиентов проходят проверку с первого раза.</p></div>
      <div class="cell fx fx-d1"><span class="num">Оплата</span><h3>Рассрочка 0% и оплата по этапам</h3><p>Без предоплаты: платите по мере выполнения шагов из договора.</p></div>
      <div class="cell fx"><span class="num">Оборудование</span><h3>Своё, поверенное</h3><p>Комплекты приборов по Приказу МЧС № 571 в аренду, поверка подтверждена в ФГИС «Аршин».</p></div>
      <div class="cell fx fx-d1" id="centr"><span class="num">Обучение</span><h3>Собственный учебный центр</h3><p>Повышение квалификации и аттестация специалистов под лицензионные требования, без посредников.</p></div>
      <div class="cell fill fx" style="grid-column:1/-1"><span class="num">География</span><h3>Работаем по всей России</h3><p>Шесть филиалов и полностью удалённое оформление: документы, подача и сопровождение проверки без вашего приезда в Москву.</p></div>
    </div>
  </div>
</section>

<section class="blk" style="padding-bottom:0">
  <div class="w">
    <div class="head-row"><h2 class="d2">Письма от клиентов</h2><span class="idx">4.9 ★ · 450+ отзывов</span></div>
  </div>
  <div class="hscroll">
''' + LETTERS + '''
  </div>
</section>

<section class="blk">
  <div class="w prose">
    <h2>Реквизиты</h2>
    <div class="callout">
      <b>ООО «НТЦ СпецПожСтандарт»</b><br>
      ИНН 7751144295<br>
      Москва, Киевское шоссе, 22-й км, БП «Румянцево», корпус В, офис 409В<br>
      Телефон: 8 800 222-09-86, звонок по России бесплатный
    </div>
  </div>
</section>
'''

# ============================================================ КОНТАКТЫ
KONTAKTY = '''
<section class="hero" style="padding-top:28px;padding-bottom:0">
  <div class="w">
    <h1 class="d1" style="font-size:clamp(36px,5.8vw,88px)">Контакты<span class="acc">.</span></h1>
    <div class="sub-row">
      <p class="lead">Отвечаем быстро: по телефону, в WhatsApp и Telegram. Перезвоним в течение 15 минут в рабочее время.</p>
    </div>
  </div>
</section>
<div data-mbar-after></div>

<section class="blk" style="padding-top:24px">
  <div class="w">
    <div class="grid2" style="margin-bottom:48px">
      <div class="cell fx"><span class="num">Телефон</span>
        <h3 style="font-size:clamp(22px,2.6vw,34px)"><a href="tel:+78002220986">8 800 222-09-86</a></h3>
        <p>Звонок по России бесплатный. WhatsApp и Telegram по этому же номеру.</p></div>
      <div class="cell fx fx-d1"><span class="num">Офис в Москве</span>
        <h3>БП «Румянцево»</h3>
        <p>Киевское шоссе, 22-й км, корпус В, офис 409В</p>
        <p style="margin-top:8px">ООО «НТЦ СпецПожСтандарт» · ИНН 7751144295</p></div>
    </div>
    <div style="max-width:660px" id="zayavka">
      <form class="form fx" onsubmit="return submitForm(event)">
        <h3>Оставить заявку</h3>
        <p>Рассчитаем стоимость и срок под ваши виды работ.</p>
        <div class="fld"><label for="f-name">Ваше имя</label><input id="f-name" name="name" placeholder="Иван" required autocomplete="name"></div>
        <div class="fld"><label for="f-phone">Телефон</label><input id="f-phone" name="phone" type="tel" placeholder="+7 ___ ___-__-__" required autocomplete="tel"></div>
        <button class="btn" type="submit">Отправить</button>
        <div class="fine">Нажимая кнопку, вы соглашаетесь с политикой обработки персональных данных</div>
      </form>
    </div>
  </div>
</section>
'''

ORG_LD = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Organization","name":"Сенсор Лицензирование","legalName":"ООО «НТЦ СпецПожСтандарт»","telephone":"+7-800-222-09-86","address":{"@type":"PostalAddress","addressLocality":"Москва","streetAddress":"Киевское шоссе, 22-й км, БП Румянцево, корп. В, оф. 409В"},"foundingDate":"2016","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"450"}}
</script>
<link rel="preload" href="assets/real/license-sample.webp" as="image">
'''

page('index.html', None,
     'Сенсор Лицензирование: лицензия МЧС под ключ, СРО, обучение | Москва и вся Россия',
     'Лицензия МЧС под ключ за 15-25 рабочих дней, переоформление, готовые фирмы, обучение специалистов. С 2016 года, 1600+ лицензий, гарантия в договоре.',
     INDEX, extra_head=ORG_LD)

page('licenziya-mchs.html', 0,
     'Пожарная лицензия МЧС под ключ от 35 000 ₽ за 15-25 дней | Сенсор Лицензирование',
     'Оформим лицензию МЧС на монтаж, обслуживание и тушение под ключ: специалисты, оборудование, документы, сопровождение проверки. Гарантия в договоре, рассрочка 0%.',
     LIC, crumb='Пожарная лицензия МЧС',
     extra_head=FAQ_LD + '<link rel="preload" href="assets/real/license-sample.webp" as="image">\n')

page('vidy-rabot.html', 1,
     'Виды работ по лицензии МЧС: все 9 видов деятельности по ПП № 1128 | Сенсор',
     'Какие виды работ входят в лицензию МЧС: пожаротушение, сигнализация, водопровод, дымоудаление, СОУЭ, двери, огнезащита, первичные средства, тушение пожаров.',
     VIDY_PAGE, crumb='Виды работ')

page('tseny.html', 2,
     'Цены на лицензию МЧС 2026: тарифы от 35 000 ₽, калькулятор | Сенсор',
     'Сколько стоит лицензия МЧС: тарифы от 35 000 ₽, под ключ от 80 000 ₽, срочно от 130 000 ₽. Калькулятор стоимости, рассрочка 0%, оплата по этапам.',
     TSENY, crumb='Цены')

page('proverka.html', 3,
     'Проверка лицензии МЧС в реестре по ИНН: инструкция | Сенсор',
     'Как проверить лицензию МЧС в реестре по ИНН: пошаговая инструкция, на что смотреть в карточке, какие риски у работы с подрядчиком без лицензии.',
     PROVERKA, crumb='Проверка лицензии')

page('o-kompanii.html', 4,
     'О компании Сенсор Лицензирование: 1600+ лицензий МЧС с 2016 года',
     'Сенсор Лицензирование: лицензии МЧС, СРО, ISO, учебный центр. 9 лет на рынке, 6 филиалов, 1600+ оформленных лицензий, рейтинг 4.9.',
     OKOMP, crumb='О компании')

page('kontakty.html', 5,
     'Контакты Сенсор Лицензирование: 8 800 222-09-86, Москва, БП Румянцево',
     'Контакты компании Сенсор Лицензирование: телефон 8 800 222-09-86 (бесплатно по РФ), офис в Москве, БП Румянцево. Заявка на лицензию МЧС онлайн.',
     KONTAKTY, crumb='Контакты')
