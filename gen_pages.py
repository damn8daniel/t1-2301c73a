# -*- coding: utf-8 -*-
"""Генератор страниц: общий шаблон шапки/футера/модалки + тела страниц."""
import io, json

SITE = 'https://damn8daniel.github.io/t1-2301c73a/'

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
<link rel="preload" href="assets/fonts/onest-cyrillic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/onest-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/main.css?v=5">
{extra_head}</head>
<body>

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

<div class="w crumbs"><a href="index.html">Главная</a><span>›</span>{crumb}</div>
'''

FOOT = '''
</main>

<footer><div class="w">
  <div class="f-cols">
    <div class="f-brand">
      <img src="assets/real/logo.png" alt="Сенсор Лицензирование" width="125" height="45">
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
  <div class="f-bottom">
    <div>© 2016-2026 ООО «НТЦ СпецПожСтандарт» · ИНН 7751144295</div>
    <div>Работаем по всей России</div>
  </div>
</div></footer>

<div class="mbar" id="mbar">
  <a class="btn ghost" href="tel:+78002220986" style="background:#fff">Позвонить</a>
  <a class="btn" href="kontakty.html#zayavka">Заявка</a>
</div>

<dialog class="modal" id="leadModal">
  <button class="modal-x" aria-label="Закрыть"></button>
  <form class="form" onsubmit="return submitForm(event)">
    <h3>Оставить заявку</h3>
    <p>Перезвоним в течение 15 минут в рабочее время, рассчитаем стоимость и срок.</p>
    <div class="fld"><label for="m-name">Ваше имя</label><input id="m-name" name="name" placeholder="Иван" required autocomplete="name"></div>
    <div class="fld"><label for="m-phone">Телефон</label><input id="m-phone" name="phone" type="tel" placeholder="+7 ___ ___-__-__" required autocomplete="tel"></div>
    <button class="btn big" type="submit">Отправить</button>
    <div class="fine">Нажимая кнопку, вы соглашаетесь с политикой обработки персональных данных</div>
  </form>
</dialog>

<div class="toast" id="toast">Заявка принята. Перезвоним в течение 15 минут</div>

<script src="assets/js/main.js?v=5" defer></script>
</body>
</html>
'''

def breadcrumb_ld(crumb, fname):
    data = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Главная","item":SITE},
        {"@type":"ListItem","position":2,"name":crumb,"item":SITE+fname}]}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>\n'

def page(fname, nav_idx, title, desc, crumb, body, extra_head=''):
    acts = ['' for _ in range(6)]
    if nav_idx is not None:
        acts[nav_idx] = 'class="act"'
    extra = breadcrumb_ld(crumb, fname) + extra_head
    html = HEAD.format(title=title, desc=desc, crumb=crumb, extra_head=extra,
                       url=SITE+fname, site=SITE,
                       a1=acts[0], a2=acts[1], a3=acts[2], a4=acts[3], a5=acts[4], a6=acts[5]) + body + FOOT
    with io.open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print('written', fname)

LETTERS = '\n'.join(
    f'    <a class="hcard-img" href="assets/real/pismo_{i}.webp" target="_blank" rel="noopener"><img loading="lazy" src="assets/real/pismo_{i}.webp" width="815" height="1127" alt="Благодарственное письмо клиента, скан {i}"></a>'
    for i in range(1, 7))

# ============================================================ vidy-rabot
V = [
 ('01','Системы пожаротушения','Монтаж, ТО и ремонт водяного, пенного, газового, порошкового и аэрозольного пожаротушения, включая пусконаладку. Самый востребованный вид: ТЦ, склады, производства, бизнес-центры.'),
 ('02','Пожарная сигнализация','АПС и ОПС, системы передачи извещений, диспетчеризация, пусконаладка. Нужен всем, кто ставит и обслуживает датчики и приёмно-контрольные приборы.'),
 ('03','Противопожарное водоснабжение','Внутренний противопожарный водопровод, наружные сети, пожарные гидранты, насосные станции.'),
 ('04','Противодымная вентиляция','Системы дымоудаления и подпора воздуха, огнезадерживающие клапаны, вентиляторы дымоудаления.'),
 ('05','СОУЭ','Системы оповещения и управления эвакуацией людей при пожаре всех пяти типов.'),
 ('06','Противопожарные преграды','Противопожарные двери, ворота, люки, окна, шторы: монтаж и обслуживание заполнений проёмов.'),
 ('07','Огнезащита','Огнезащитная обработка металлических и деревянных конструкций, кабелей, воздуховодов, тканей.'),
 ('08','Первичные средства','Огнетушители, пожарные шкафы, краны и рукава: установка, перезарядка, обслуживание.'),
 ('09','Тушение пожаров','Тушение пожаров в населённых пунктах и на объектах. Отдельное лицензирование с повышенными требованиями к персоналу и технике.'),
]
VIDY = '''
<section class="page-hero">
  <div class="w">
    <h1 class="t-big">Виды работ<br>по лицензии МЧС</h1>
    <p class="t-lead">Девять видов деятельности по Постановлению Правительства РФ № 1128. Оформим лицензию на любой набор: от одного вида до всех девяти.</p>
  </div>
</section>
<div data-mbar-after></div>

<section class="sec sec-soft" style="padding-top:48px">
  <div class="w-wide">
    <div class="vlist">
''' + '\n'.join(
    f'      <article class="vcard fx"><span class="vn">{n}</span><h2>{t}</h2><p>{d}</p></article>'
    for n, t, d in V) + '''
    </div>
    <div class="w" style="max-width:760px;padding:48px 0 0">
      <div class="callout fx"><b>Не знаете, какие виды выбрать?</b> Подберём оптимальный набор под ваши контракты и тендеры: лишние виды удорожают лицензию, недостающие блокируют работу. Консультация бесплатная.</div>
    </div>
  </div>
</section>

<section class="sec cta-final">
  <div class="w">
    <h2 class="t-big fx">Оформим на любой набор видов</h2>
    <p class="t-lead fx fx-d1">Цена и срок зависят от набора: рассчитайте за минуту.</p>
    <div class="hero-cta fx fx-d2">
      <a class="btn big" href="licenziya-mchs.html#calc">Рассчитать стоимость</a>
      <a class="btn big ghost" href="tel:+78002220986">8 800 222-09-86</a>
    </div>
  </div>
</section>
'''

# ============================================================ tseny
TSENY = '''
<section class="page-hero">
  <div class="w">
    <h1 class="t-big">Цены и тарифы</h1>
    <p class="t-lead">Прозрачные пакеты без скрытых доплат. Госпошлина оплачивается отдельно: 7 500 ₽ за выдачу, 3 500 ₽ за переоформление.</p>
  </div>
</section>
<div data-mbar-after></div>

<section class="sec sec-soft" style="padding-top:40px">
  <div class="w-wide">
    <div class="plans">
      <div class="plan fx"><h3>Документы</h3><div class="price">35 000 ₽</div><div class="term">10 рабочих дней</div>
        <ul><li>Подготовка пакета документов</li><li>Проверка на соответствие требованиям</li><li>Консультация эксперта</li></ul>
        <a class="btn ghost" href="kontakty.html#zayavka">Выбрать</a></div>
      <div class="plan best fx"><div class="tag">Выбирают чаще всего</div><h3>Под ключ</h3><div class="price">от 80 000 ₽</div><div class="term">15-25 рабочих дней</div>
        <ul><li>Полное сопровождение до реестра</li><li>Подбор специалистов</li><li>Аренда поверенного оборудования</li><li>Сопровождение выездной проверки</li><li>Гарантия результата в договоре</li></ul>
        <a class="btn" href="kontakty.html#zayavka">Выбрать</a></div>
      <div class="plan fx fx-d1"><h3>Срочно</h3><div class="price">от 130 000 ₽</div><div class="term">от 10 рабочих дней</div>
        <ul><li>Всё из тарифа «Под ключ»</li><li>Приоритетная подача</li><li>Ускоренное прохождение проверки</li></ul>
        <a class="btn ghost" href="kontakty.html#zayavka">Выбрать</a></div>
      <div class="plan fx fx-d2"><h3>Готовая фирма</h3><div class="price">от 299 000 ₽</div><div class="term">1-3 дня</div>
        <ul><li>ООО с действующей лицензией МЧС</li><li>Переоформление на вас</li><li>Чистая история компании</li></ul>
        <a class="btn ghost" href="kontakty.html#zayavka">Выбрать</a></div>
    </div>
  </div>
</section>

<section class="sec" id="calc">
  <div class="w">
    <div class="sec-head">
      <h2 class="t-h2">Рассчитайте под свою задачу</h2>
      <p class="t-lead">Четыре вопроса, ориентир сразу на экране.</p>
    </div>
    <div class="calc fx-scale">
      <div class="calc-q">
        <div class="cq"><div class="ql">1. Сколько видов работ нужно?</div><div class="opts" data-g="vid">
          <span class="opt on" data-v="0">1-2 вида</span><span class="opt" data-v="20000">3-5 видов</span><span class="opt" data-v="45000">6 и больше</span></div></div>
        <div class="cq"><div class="ql">2. Форма организации</div><div class="opts" data-g="org">
          <span class="opt on" data-v="0">ООО</span><span class="opt" data-v="-5000">ИП</span></div></div>
        <div class="cq"><div class="ql">3. Специалисты и поверенное оборудование</div><div class="opts" data-g="res">
          <span class="opt on" data-v="0">Всё своё</span><span class="opt" data-v="30000">Нужна аренда оборудования</span><span class="opt" data-v="55000">Нужны и специалисты, и оборудование</span></div></div>
        <div class="cq"><div class="ql">4. Срочность</div><div class="opts" data-g="urg">
          <span class="opt on" data-v="0">Стандарт, 15-25 дней</span><span class="opt" data-v="40000">Срочно, от 10 дней</span></div></div>
      </div>
      <div class="calc-r">
        <div class="rl">Ориентир под ключ</div>
        <div class="rv" id="calcNum" aria-live="polite">от 35 000 ₽</div>
        <div class="rs" id="calcTerm">срок 15-25 рабочих дней, плюс госпошлина 7 500 ₽</div>
        <a class="btn on-dark" href="kontakty.html#zayavka">Получить точный расчёт</a>
        <div class="note">Рассрочка 0% · оплата по этапам · без предоплаты</div>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-soft">
  <div class="w">
    <div class="sec-head"><h2 class="t-h2">Вопросы про оплату</h2></div>
    <div class="faq">
      <div class="fi"><button class="fq">Есть ли предоплата?</button><div class="fa"><div><p>Нет. Работаем по этапам: оплата привязана к выполненным шагам из договора. Доступна рассрочка 0%.</p></div></div></div>
      <div class="fi"><button class="fq">Что входит в цену «под ключ»?</button><div class="fa"><div><p>Подбор специалистов, аренда поверенного оборудования, подготовка документов, подача через Госуслуги и сопровождение выездной проверки МЧС. Госпошлина 7 500 ₽ оплачивается отдельно.</p></div></div></div>
      <div class="fi"><button class="fq">От чего зависит итоговая стоимость?</button><div class="fa"><div><p>От количества видов работ, наличия у вас специалистов и оборудования, формы организации и срочности. Точный расчёт делаем после короткого аудита.</p></div></div></div>
      <div class="fi"><button class="fq">Что будет, если лицензию не выдадут?</button><div class="fa"><div><p>Гарантия результата зафиксирована в договоре: при отказе по нашей вине возвращаем оплату полностью.</p></div></div></div>
    </div>
  </div>
</section>
'''

# ============================================================ proverka
PROVERKA = '''
<section class="page-hero">
  <div class="w">
    <h1 class="t-big">Проверка лицензии МЧС<br>в реестре</h1>
    <p class="t-lead">С 2021 года лицензия существует только как запись в реестре МЧС России. Проверить себя или подрядчика можно за пару минут.</p>
  </div>
</section>
<div data-mbar-after></div>

<section class="sec sec-soft" style="padding-top:48px">
  <div class="w">
    <div class="sec-head"><h2 class="t-h2">Три шага</h2></div>
    <div class="checksteps">
      <div class="cstep fx"><div class="cn"></div><h3>Откройте реестр МЧС</h3><p>Реестр лицензий опубликован на официальном сайте МЧС России и доступен без регистрации.</p></div>
      <div class="cstep fx fx-d1"><div class="cn"></div><h3>Введите ИНН</h3><p>Достаточно ИНН организации или ИП. Название тоже работает, но ИНН надёжнее: исключает однофамильцев.</p></div>
      <div class="cstep fx fx-d2"><div class="cn"></div><h3>Сверьте карточку</h3><p>Статус лицензии, перечень разрешённых видов работ и дата записи. Виды работ должны покрывать предмет вашего договора.</p></div>
    </div>
  </div>
</section>

<section class="sec">
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

<section class="sec sec-soft cta-final">
  <div class="w">
    <h2 class="t-big fx">Нужна своя лицензия?</h2>
    <p class="t-lead fx fx-d1">Оформим под ключ за 15-25 рабочих дней с гарантией в договоре.</p>
    <div class="hero-cta fx fx-d2">
      <a class="btn big" href="licenziya-mchs.html">Получить лицензию</a>
      <a class="btn big ghost" href="tel:+78002220986">8 800 222-09-86</a>
    </div>
  </div>
</section>
'''

# ============================================================ o-kompanii
OKOMP = '''
<section class="page-hero">
  <div class="w">
    <h1 class="t-big">Сенсор Лицензирование</h1>
    <p class="t-lead">Помогаем бизнесу легально работать в сфере пожарной безопасности: лицензии МЧС, СРО, ISO, электролаборатория и собственный учебный центр.</p>
  </div>
</section>
<div data-mbar-after></div>

<section class="sec" style="padding-top:32px">
  <div class="w">
    <div class="zoom-img fx-scale"><img src="assets/real/office.webp" width="1024" height="683" alt="Команда компании Сенсор Лицензирование в офисе" fetchpriority="high"></div>
  </div>
</section>

<section class="sec sec-soft">
  <div class="w">
    <div class="stats">
      <div class="stat fx"><div class="v" data-cnt="1600" data-suf="+">0</div><div class="l">лицензий МЧС оформлено</div></div>
      <div class="stat fx fx-d1"><div class="v"><span data-cnt="9">0</span> <i>лет</i></div><div class="l">на рынке, с 2016 года</div></div>
      <div class="stat fx fx-d2"><div class="v" data-cnt="6">0</div><div class="l">филиалов по России</div></div>
      <div class="stat fx fx-d3"><div class="v" data-cnt="20" data-suf="+">0</div><div class="l">госконтрактов сопровождено</div></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="w-wide">
    <div class="sec-head">
      <h2 class="t-h2">Почему с нами спокойно</h2>
    </div>
    <div class="tiles">
      <div class="tile fx"><h3>Гарантия результата в договоре</h3><p>Если лицензию не выдадут по нашей вине, вернём оплату полностью. На практике 98% клиентов проходят проверку с первого раза.</p></div>
      <div class="tile fx fx-d1"><h3>Рассрочка 0% и оплата по этапам</h3><p>Без предоплаты: платите по мере выполнения шагов из договора.</p></div>
      <div class="tile fx"><h3>Своё поверенное оборудование</h3><p>Комплекты приборов по Приказу МЧС № 571 в аренду, поверка подтверждена в ФГИС «Аршин».</p></div>
      <div class="tile fx fx-d1" id="centr"><h3>Собственный учебный центр</h3><p>Повышение квалификации и аттестация специалистов под лицензионные требования, без посредников.</p></div>
      <div class="tile dark span2 fx"><h3>Работаем по всей России</h3><p>Шесть филиалов и полностью удалённое оформление: документы, подача и сопровождение проверки без вашего приезда в Москву.</p>
        <a class="alink" href="kontakty.html">Связаться с нами</a></div>
    </div>
  </div>
</section>

<section class="sec sec-soft" style="overflow:hidden">
  <div class="w">
    <div class="sec-head">
      <h2 class="t-h2">Письма от клиентов</h2>
      <p class="t-lead">4.9 из 5 по 450+ отзывам на Яндекс Картах, 2ГИС и Google.</p>
    </div>
  </div>
  <div class="hscroll">
''' + LETTERS + '''
  </div>
</section>

<section class="sec">
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

# ============================================================ kontakty
KONTAKTY = '''
<section class="page-hero">
  <div class="w">
    <h1 class="t-big">Контакты</h1>
    <p class="t-lead">Отвечаем быстро: по телефону, в WhatsApp и Telegram. Перезвоним в течение 15 минут в рабочее время.</p>
  </div>
</section>
<div data-mbar-after></div>

<section class="sec sec-soft" style="padding-top:48px">
  <div class="w">
    <div class="tiles" style="margin-bottom:20px">
      <div class="tile fx">
        <h3>Телефон</h3>
        <p style="font-size:24px;font-weight:800;color:var(--ink)"><a href="tel:+78002220986">8 800 222-09-86</a></p>
        <p>Звонок по России бесплатный. WhatsApp и Telegram по этому же номеру.</p>
      </div>
      <div class="tile fx fx-d1">
        <h3>Офис в Москве</h3>
        <p>Киевское шоссе, 22-й км, БП «Румянцево», корпус В, офис 409В</p>
        <p>ООО «НТЦ СпецПожСтандарт» · ИНН 7751144295</p>
      </div>
    </div>
    <div class="w" style="max-width:640px;padding:40px 0 0" id="zayavka">
      <form class="form fx" onsubmit="return submitForm(event)">
        <h3>Оставить заявку</h3>
        <p>Рассчитаем стоимость и срок под ваши виды работ.</p>
        <div class="fld"><label for="f-name">Ваше имя</label><input id="f-name" name="name" placeholder="Иван" required autocomplete="name"></div>
        <div class="fld"><label for="f-phone">Телефон</label><input id="f-phone" name="phone" type="tel" placeholder="+7 ___ ___-__-__" required autocomplete="tel"></div>
        <button class="btn big" type="submit">Отправить</button>
        <div class="fine">Нажимая кнопку, вы соглашаетесь с политикой обработки персональных данных</div>
      </form>
    </div>
  </div>
</section>
'''

page('vidy-rabot.html', 1,
     'Виды работ по лицензии МЧС: все 9 видов деятельности по ПП № 1128 | Сенсор',
     'Какие виды работ входят в лицензию МЧС: пожаротушение, сигнализация, водопровод, дымоудаление, СОУЭ, двери, огнезащита, первичные средства, тушение пожаров.',
     'Виды работ', VIDY)

page('tseny.html', 2,
     'Цены на лицензию МЧС 2026: тарифы от 35 000 ₽, калькулятор | Сенсор',
     'Сколько стоит лицензия МЧС: тарифы от 35 000 ₽, под ключ от 80 000 ₽, срочно от 130 000 ₽. Калькулятор стоимости, рассрочка 0%, оплата по этапам.',
     'Цены', TSENY)

page('proverka.html', 3,
     'Проверка лицензии МЧС в реестре по ИНН: инструкция | Сенсор',
     'Как проверить лицензию МЧС в реестре по ИНН: пошаговая инструкция, на что смотреть в карточке, какие риски у работы с подрядчиком без лицензии.',
     'Проверка лицензии', PROVERKA)

page('o-kompanii.html', 4,
     'О компании Сенсор Лицензирование: 1600+ лицензий МЧС с 2016 года',
     'Сенсор Лицензирование: лицензии МЧС, СРО, ISO, учебный центр. 9 лет на рынке, 6 филиалов, 1600+ оформленных лицензий, рейтинг 4.9.',
     'О компании', OKOMP)

page('kontakty.html', 5,
     'Контакты Сенсор Лицензирование: 8 800 222-09-86, Москва, БП Румянцево',
     'Контакты компании Сенсор Лицензирование: телефон 8 800 222-09-86 (бесплатно по РФ), офис в Москве, БП Румянцево. Заявка на лицензию МЧС онлайн.',
     'Контакты', KONTAKTY)
