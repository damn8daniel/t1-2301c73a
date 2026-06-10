# -*- coding: utf-8 -*-
"""Генератор всех страниц. v9 «Кобальтовый документ» (развитие варианта impeccable)."""
import io, json

SITE = 'https://damn8daniel.github.io/t1-2301c73a/'
V = 'v=9'

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
<link rel="preload" href="assets/fonts/bitter-cyrillic-normal-400_800.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/sofia-cyrillic-normal-400_700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/main.css?''' + V + '''">
{extra_head}</head>
<body>

<header class="nav"><div class="nav-in">
  <a class="brand" href="index.html">Сенсор <span>Лицензирование</span></a>
  <nav class="nav-links">
    <a {a1} href="licenziya-mchs.html">Лицензия МЧС</a>
    <a {a2} href="uslugi.html">Все услуги</a>
    <a {a3} href="tseny.html">Цены</a>
    <a {a4} href="proverka.html">Проверка лицензии</a>
    <a {a5} href="o-kompanii.html">О компании</a>
    <a {a6} href="kontakty.html">Контакты</a>
    <a class="mtel" href="tel:+78002220986">8 800 222-09-86</a>
  </nav>
  <div class="nav-right">
    <a class="nav-tel" href="tel:+78002220986">8 800 222-09-86</a>
    <a class="hbtn" href="kontakty.html#zayavka">Заявка</a>
    <button class="nav-burger" aria-label="Меню"><span></span><span></span><span></span></button>
  </div>
</div></header>

<main>
'''

FOOT = '''
</main>

<footer>
  <div class="w f-cols">
    <div class="f-brand">
      <b>Сенсор Лицензирование</b>
      <p>Лицензии МЧС, СРО, ISO, электролаборатория и учебный центр. Работаем по всей России с 2016 года.</p>
    </div>
    <div><b>Услуги</b>
      <a href="licenziya-mchs.html">Лицензия МЧС</a>
      <a href="vidy-rabot.html">Виды работ по лицензии</a>
      <a href="uslugi.html#sro">СРО</a>
      <a href="uslugi.html#iso">Сертификаты ISO</a>
      <a href="uslugi.html#centr">Учебный центр</a>
      <a href="uslugi.html">Все услуги</a>
    </div>
    <div><b>Клиентам</b>
      <a href="tseny.html">Цены и тарифы</a>
      <a href="proverka.html">Проверка лицензии</a>
      <a href="uslugi.html#oborudovanie">Оборудование в аренду</a>
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
  <a class="btn line" href="tel:+78002220986" style="background:#fff">Позвонить</a>
  <a class="btn fill" href="kontakty.html#zayavka">Заявка</a>
</div>

<dialog class="modal" id="leadModal">
  <button class="modal-x" aria-label="Закрыть"></button>
  <form class="form" onsubmit="return submitForm(event)">
    <h3>Оставить заявку</h3>
    <p>Перезвоним в течение 15 минут в рабочее время, рассчитаем стоимость и срок.</p>
    <div class="fld"><label for="m-name">Ваше имя</label><input id="m-name" name="name" placeholder="Иван" required autocomplete="name"></div>
    <div class="fld"><label for="m-phone">Телефон</label><input id="m-phone" name="phone" type="tel" placeholder="+7 ___ ___-__-__" required autocomplete="tel"></div>
    <button class="btn" type="submit">Отправить заявку</button>
    <div class="fine">Нажимая кнопку, вы соглашаетесь с политикой обработки персональных данных</div>
  </form>
</dialog>

<div class="toast" id="toast">Заявка принята: перезвоним в течение 15 минут</div>

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
    html = HEAD.format(title=title, desc=desc, extra_head=extra,
                       url=SITE+(fname if fname!='index.html' else ''), site=SITE,
                       a1=acts[0], a2=acts[1], a3=acts[2], a4=acts[3], a5=acts[4], a6=acts[5]) + body + FOOT
    with io.open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print('written', fname)

def phero(crumb, h1, sub):
    return f'''<section class="phero"><div class="w in">
  <div class="crumbs"><a href="index.html">Главная</a><span>›</span>{crumb}</div>
  <h1>{h1}</h1>
  <p class="sub">{sub}</p>
</div></section>
<div data-mbar-after></div>'''

LETTERS = '\n'.join(
    f'    <a href="assets/real/pismo_{i}.webp" target="_blank" rel="noopener"><img loading="lazy" src="assets/real/pismo_{i}.webp" width="815" height="1127" alt="Благодарственное письмо клиента, скан {i}"></a>'
    for i in range(1, 7))

LEDGER = '''
  <div class="ledger mt fx">
    <div class="li-row"><span class="no">I</span><h3>Системы пожаротушения</h3><p>Водяное, пенное, газовое, порошковое и аэрозольное. Монтаж, ТО, ремонт.</p></div>
    <div class="li-row"><span class="no">II</span><h3>Пожарная сигнализация</h3><p>АПС и ОПС, диспетчеризация, пусконаладка.</p></div>
    <div class="li-row"><span class="no">III</span><h3>Противопожарный водопровод</h3><p>Внутренний и наружный, гидранты, насосные станции.</p></div>
    <div class="li-row"><span class="no">IV</span><h3>Противодымная вентиляция</h3><p>Дымоудаление и подпор воздуха, клапаны, вентиляторы.</p></div>
    <div class="li-row"><span class="no">V</span><h3>Оповещение и эвакуация</h3><p>СОУЭ всех пяти типов.</p></div>
    <div class="li-row"><span class="no">VI</span><h3>Противопожарные преграды</h3><p>Двери, ворота, люки, окна, шторы.</p></div>
    <div class="li-row"><span class="no">VII</span><h3>Огнезащита</h3><p>Конструкции, кабели, воздуховоды, ткани.</p></div>
    <div class="li-row"><span class="no">VIII</span><h3>Первичные средства</h3><p>Огнетушители, краны, рукава: установка и перезарядка.</p></div>
    <div class="li-row"><span class="no">IX</span><h3>Тушение пожаров</h3><p>Населённые пункты и производственные объекты.</p></div>
  </div>'''

TIERS = '''
    <div class="tiers">
      <div class="tier"><h3>Документы</h3><div class="pr">35 000 ₽</div><div class="tm">10 рабочих дней</div>
        <ul><li>Пакет документов</li><li>Проверка по требованиям</li><li>Консультация эксперта</li></ul>
        <a class="btn" href="{cta}">Выбрать пакет</a></div>
      <div class="tier star"><div class="tg">Выбирают чаще всего</div><h3>Под ключ</h3><div class="pr">от 80 000 ₽</div><div class="tm">15-25 рабочих дней</div>
        <ul><li>Сопровождение до реестра</li><li>Подбор специалистов</li><li>Аренда оборудования</li><li>Выездная проверка с нами</li><li>Гарантия в договоре</li></ul>
        <a class="btn" href="{cta}">Выбрать пакет</a></div>
      <div class="tier"><h3>Срочно</h3><div class="pr">от 130 000 ₽</div><div class="tm">от 10 рабочих дней</div>
        <ul><li>Всё из «Под ключ»</li><li>Приоритетная подача</li><li>Ускоренная проверка</li></ul>
        <a class="btn" href="{cta}">Выбрать пакет</a></div>
      <div class="tier"><h3>Готовая фирма</h3><div class="pr">от 299 000 ₽</div><div class="tm">1-3 дня</div>
        <ul><li>ООО с действующей лицензией</li><li>Чистая история</li><li>Переоформление на вас</li></ul>
        <a class="btn" href="{cta}">Выбрать пакет</a></div>
    </div>'''

CALC = '''
    <div class="calc mt fx">
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
        <a class="btn" href="{cta}">Получить точный расчёт</a>
        <div class="note">Рассрочка 0% · оплата по этапам · без предоплаты</div>
      </div>
    </div>'''

TIMELINE = '''
  <div class="timeline fx">
    <div class="tstep"><h3>Аудит и договор <span>1-2 дня</span></h3><p>Разбираем вашу ситуацию, подбираем виды работ, фиксируем цену, срок и гарантию результата.</p></div>
    <div class="tstep"><h3>Специалисты и оборудование <span>3-7 дней</span></h3><p>Персонал с профильным образованием и стажем, поверенные приборы по Приказу № 571 в аренду.</p></div>
    <div class="tstep"><h3>Пакет документов <span>2-4 дня</span></h3><p>Готовим полный комплект и перепроверяем перед подачей: ошибки исключены.</p></div>
    <div class="tstep"><h3>Подача и выездная проверка <span>до 15 рабочих дней</span></h3><p>Подаём через Госуслуги, готовим объект и сопровождаем оценку МЧС.</p></div>
    <div class="tstep"><h3>Запись в реестре <span>итог</span></h3><p>Компания в реестре МЧС России: можно работать и участвовать в тендерах. Лицензия бессрочная.</p></div>
  </div>'''

FAQ_MAIN = '''
  <div class="qa mt fx">
    <details><summary>Кому обязательно нужна лицензия МЧС?</summary><p class="ans">Организациям и ИП, которые выполняют монтаж, ТО и ремонт средств обеспечения пожарной безопасности, огнезащиту или тушение пожаров. В том числе для участия в тендерах по 44-ФЗ и 223-ФЗ.</p></details>
    <details><summary>Сколько это стоит в 2026 году?</summary><p class="ans">Госпошлина 7 500 ₽. Сопровождение: от 35 000 ₽ за подготовку документов до 80 000-130 000 ₽ за полный пакет со специалистами и оборудованием.</p></details>
    <details><summary>Нужны ли свои специалисты и приборы?</summary><p class="ans">Да, это лицензионные требования. Помогаем с подбором персонала и сдаём поверенное оборудование в аренду: покупать не обязательно.</p></details>
    <details><summary>Лицензия бессрочная?</summary><p class="ans">Да, действует бессрочно и по всей России. Раз в 3 года проходит периодическое подтверждение соответствия: сопровождаем и его.</p></details>
    <details><summary>Что будет, если лицензию не выдадут?</summary><p class="ans">Гарантия результата зафиксирована в договоре: при отказе по нашей вине вернём оплату полностью. На практике 98% клиентов проходят проверку с первого раза.</p></details>
    <details><summary>Чем грозит работа без лицензии?</summary><p class="ans">Штраф до 250 000 ₽ для юрлиц и приостановка деятельности до 90 суток по КоАП РФ, отстранение от тендеров.</p></details>
  </div>'''

BLANK = '''
  <div class="blank fx" id="zayavka">
    <div>
      <h2 class="t">{h2}</h2>
      <p class="note">Перезвоним в течение 15 минут в рабочее время: разберём вашу ситуацию и назовём точную цену и срок.</p>
    </div>
    <form class="form" onsubmit="return submitForm(event)">
      <div class="fld"><label for="f-name">Ваше имя</label><input id="f-name" name="name" placeholder="Иван" required autocomplete="name"></div>
      <div class="fld"><label for="f-phone">Телефон</label><input id="f-phone" name="phone" type="tel" placeholder="+7 ___ ___-__-__" required autocomplete="tel"></div>
      <button class="btn" type="submit">Отправить заявку</button>
      <div class="fine">Нажимая кнопку, вы соглашаетесь с политикой обработки персональных данных</div>
    </form>
  </div>'''

# ============================================================ ГЛАВНАЯ
INDEX = '''
<section class="hero">
  <div class="seal" aria-hidden="true">
    <svg viewBox="0 0 100 100"><defs><path id="c" d="M50,50 m-37,0 a37,37 0 1,1 74,0 a37,37 0 1,1 -74,0"/></defs>
    <text><textPath href="#c">реестр мчс россии · бессрочно · вся рф · реестр мчс россии · бессрочно ·</textPath></text></svg>
  </div>
  <div class="w in"><div class="grid">
    <div>
      <div class="doc-no"><span>Лицензируемая деятельность: <b>ПП РФ № 1128</b></span><span>Статус: <b>оформляем под ключ</b></span></div>
      <h1>Пожарная лицензия МЧС, <em>оформленная за вас</em></h1>
      <p class="sub">Специалисты, поверенное оборудование, документы и выездная проверка: всё берём на себя. <b>От 35 000 ₽, готово за 15-25 рабочих дней</b>, гарантия результата в договоре.</p>
      <div class="cta">
        <a class="btn" href="licenziya-mchs.html">Получить лицензию</a>
        <a class="btn deep" href="tseny.html">Цены и тарифы</a>
      </div>
    </div>
    <div class="doc" aria-hidden="true">
      <div class="paper"><img src="assets/real/license-sample.webp" width="1024" height="364" alt="" fetchpriority="high"></div>
      <div class="chip"><b>98%</b><span>проходят проверку<br>с первого раза</span></div>
    </div>
  </div></div>
</section>
<div data-mbar-after></div>

<div class="facts w">
  <div class="row fx">
    <div class="fact"><div class="v" data-cnt="1600">0</div><div class="l">лицензий оформлено с 2016 года</div></div>
    <div class="fact"><div class="v"><span data-cnt="98">0</span><i>%</i></div><div class="l">проходят проверку с первого раза</div></div>
    <div class="fact"><div class="v">15-25</div><div class="l">рабочих дней до записи в реестре</div></div>
    <div class="fact"><div class="v">4.9 <i>★</i></div><div class="l">по 450+ отзывам на картах</div></div>
  </div>
</div>

<section class="blk"><div class="w">
  <h2 class="t">Опись видов работ</h2>
  <p class="t-sub">Девять видов деятельности по Постановлению № 1128. Лицензия оформляется на любой набор: лишние виды удорожают, недостающие блокируют контракты.</p>
''' + LEDGER + '''
  <p class="mt" style="margin-top:28px"><a class="tlink" href="vidy-rabot.html">Подробное описание каждого вида</a></p>
</div></section>

<section class="blk" style="padding-top:0"><div class="w">
  <h2 class="t">Не только лицензия МЧС</h2>
  <p class="t-sub">Полный спектр разрешительных документов для работы в строительстве и пожарной безопасности.</p>
  <div class="cells mt fx">
    <a class="cell" href="uslugi.html#sro"><span class="k">СРО и реестры</span><h3>СРО строителей, проектировщиков, изыскателей</h3><p>Вступление под ключ, НРС НОСТРОЙ и НОПРИЗ, независимая оценка квалификации.</p></a>
    <a class="cell" href="uslugi.html#iso"><span class="k">Сертификация</span><h3>ISO 9001, 14001, 45001</h3><p>Сертификаты для тендеров и заказчиков, включая интегрированную систему.</p></a>
    <a class="cell" href="uslugi.html#centr"><span class="k">Учебный центр</span><h3>Обучение и аттестация</h3><p>Профпереподготовка для МЧС, повышение квалификации, рабочие профессии, охрана труда.</p></a>
    <a class="cell" href="uslugi.html#licenzii"><span class="k">Лицензии</span><h3>Минкульт, уведомления, подтверждение</h3><p>Лицензия Минкульта, подача уведомлений МЧС, периодическое подтверждение требований.</p></a>
    <a class="cell" href="uslugi.html#oborudovanie"><span class="k">Оборудование</span><h3>Аренда и продажа приборов</h3><p>Поверенные комплекты для лицензии МЧС, регистрация электролаборатории.</p></a>
    <a class="cell" href="uslugi.html"><span class="k">Каталог</span><h3>Все услуги списком</h3><p>Полный перечень из 20+ услуг компании на одной странице.</p></a>
  </div>
</div></section>

<section class="blk" style="padding-top:0"><div class="w">
  <div class="photoband fx">
    <img loading="lazy" src="assets/real/team2.webp" width="1024" height="683" alt="Команда компании Сенсор Лицензирование">
    <div class="cap">
      <div><b>Команда «Сенсор», Москва</b><span>лицензирование МЧС: основная практика, а не услуга в каталоге</span></div>
      <span>с 2016 года · 6 филиалов · свой учебный центр</span>
    </div>
  </div>
</div></section>

<section class="blk" style="padding-top:0"><div class="w spread">
  <div class="stick fx">
    <h2 class="t">Как документ становится <em>записью в реестре</em></h2>
    <p class="t-sub">Оплата привязана к этапам. Предоплаты нет, рассрочка 0%.</p>
    <p style="margin-top:24px"><a class="btn fill" href="licenziya-mchs.html">Подробнее об услуге</a></p>
  </div>
''' + TIMELINE + '''
</div></section>

<section class="blk" style="padding-top:0"><div class="w">
  <div class="shelf fx">
    <h2 class="t">Стоимость</h2>
    <p class="t-sub">Цена зависит от набора видов работ и того, что уже есть у вас: люди, приборы, документы.</p>
''' + TIERS.format(cta='kontakty.html#zayavka') + '''
    <p class="fee">Госпошлина отдельно: 7 500 ₽ за выдачу, 3 500 ₽ за переоформление. <a href="tseny.html" style="color:#fff;text-decoration:underline">Подробнее о ценах</a></p>
  </div>
</div></section>

<section class="blk" style="padding-top:0"><div class="w">
  <h2 class="t">Благодарственные письма</h2>
  <div class="desk mt fx">
''' + LETTERS + '''
  </div>
  <div class="praise fx">
    <div class="score">4.9 <i>★</i></div>
    <p>Средняя оценка по 450+ отзывам на Яндекс Картах, 2ГИС и Google. Сканы открываются по клику.</p>
  </div>
</div></section>

<section class="blk" style="padding-top:0"><div class="w team">
  <div class="ph fx"><img loading="lazy" src="assets/real/office.webp" width="1024" height="683" alt="Команда Сенсор Лицензирование в офисе"></div>
  <div class="fx">
    <h2 class="t">Кто ведёт ваше дело</h2>
    <ul>
      <li><div><b>Профильная команда с 2016 года</b><span>лицензирование МЧС: основная практика, не услуга в каталоге</span></div></li>
      <li><div><b>Собственный учебный центр</b><span>обучаем и аттестуем специалистов без посредников</span></div></li>
      <li><div><b>Своё поверенное оборудование</b><span>комплекты приборов в аренду, поверка в ФГИС «Аршин»</span></div></li>
      <li><div><b>Шесть филиалов</b><span>оформление полностью удалённое, по всей России</span></div></li>
    </ul>
    <p style="margin-top:24px"><a class="tlink" href="o-kompanii.html">Познакомиться с компанией</a></p>
  </div>
</div></section>

<section class="blk" style="padding-top:0"><div class="w" style="max-width:860px">
  <h2 class="t">Вопросы и ответы</h2>
''' + FAQ_MAIN + '''
</div></section>

<section class="blk" style="padding-top:0"><div class="w">
''' + BLANK.format(h2='Заполните бланк, <em>остальное оформим мы</em>') + '''
</div></section>
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

LIC = phero('Пожарная лицензия МЧС',
            'Пожарная лицензия МЧС <em>под ключ</em>',
            'От 35 000 ₽ за 15-25 рабочих дней: специалисты, оборудование, документы и сопровождение выездной проверки. Гарантия результата в договоре.') + '''

<div class="facts w">
  <div class="row fx">
    <div class="fact"><div class="v">от 35 000 ₽</div><div class="l">сопровождение, госпошлина 7 500 ₽ отдельно</div></div>
    <div class="fact"><div class="v">15-25</div><div class="l">рабочих дней полный цикл</div></div>
    <div class="fact"><div class="v">бессрочно</div><div class="l">действует по всей России</div></div>
    <div class="fact"><div class="v"><span data-cnt="98">0</span><i>%</i></div><div class="l">проходят проверку с первого раза</div></div>
  </div>
</div>

<section class="blk" id="vidy"><div class="w">
  <h2 class="t">Какие виды работ покрывает</h2>
  <p class="t-sub">Девять видов деятельности по ПП № 1128, оформляем на любой набор.</p>
''' + LEDGER + '''
</div></section>

<section class="blk" style="padding-top:0" id="calc"><div class="w">
  <h2 class="t">Рассчитайте стоимость <em>за минуту</em></h2>
  <p class="t-sub">Четыре вопроса. Ориентир сразу на экране, точный расчёт после заявки.</p>
''' + CALC.format(cta='#zayavka') + '''
</div></section>

<section class="blk" style="padding-top:0" id="etapy"><div class="w spread">
  <div class="stick fx">
    <h2 class="t">Путь до записи в реестре</h2>
    <p class="t-sub">Оплата привязана к этапам. Предоплаты нет, рассрочка 0%.</p>
  </div>
''' + TIMELINE + '''
</div></section>

<section class="blk" style="padding-top:0" id="trebovaniya"><div class="w">
  <h2 class="t">Лицензионные требования</h2>
  <p class="t-sub">Что проверяет МЧС перед выдачей и как мы закрываем каждый пункт.</p>
  <div class="cells mt fx">
    <div class="cell"><span class="k">Персонал</span><h3>Образование и стаж</h3><p>Для ИП от 3 лет, для руководителя ООО от 5 лет, плюс повышение квалификации.</p><p class="ok">Закрываем: подбираем специалистов и обучаем в своём учебном центре.</p></div>
    <div class="cell"><span class="k">Оборудование</span><h3>Поверенные приборы</h3><p>По Приказу МЧС № 571, с записью о поверке в ФГИС «Аршин»: манометр, мегаомметр, мультиметр и другие.</p><p class="ok">Закрываем: полный комплект в аренду, покупать не нужно.</p></div>
    <div class="cell"><span class="k">Документы</span><h3>Полный пакет</h3><p>Устав, выписка ЕГРЮЛ или ЕГРИП, дипломы и трудовые специалистов, договор на помещение, заявление.</p><p class="ok">Закрываем: готовим и перепроверяем всё за вас.</p></div>
  </div>
</div></section>

<section class="blk" style="padding-top:0" id="pereoformlenie"><div class="w">
  <div class="shelf fx">
    <h2 class="t">Лицензия сегодня: запись в реестре</h2>
    <p class="t-sub">С 2021 года бумажные бланки не выдаются. Сведения вносятся в реестр МЧС России и проверяются по ИНН.</p>
    <div class="tiers" style="grid-template-columns:repeat(3,1fr)">
      <div class="tier"><h3>Переоформление</h3><div class="pr">3 500 ₽</div><div class="tm">госпошлина</div>
        <ul><li>Добавление видов работ</li><li>Смена адреса или реквизитов</li><li>Сопровождаем под ключ</li></ul></div>
      <div class="tier"><h3>Подтверждение</h3><div class="pr">раз в 3 года</div><div class="tm">периодическое</div>
        <ul><li>Проверка соответствия требованиям</li><li>Готовим и сопровождаем процедуру</li></ul></div>
      <div class="tier"><h3>Правовая база</h3><div class="pr">ФЗ-99 · ПП 1128</div><div class="tm">и Приказ МЧС № 571</div>
        <ul><li>Без лицензии: штраф до 250 000 ₽</li><li>Приостановка до 90 суток</li></ul></div>
    </div>
    <p class="fee"><a href="proverka.html" style="color:#fff;text-decoration:underline">Как проверить лицензию в реестре</a></p>
  </div>
</div></section>

<section class="blk" style="padding-top:0" id="faq"><div class="w" style="max-width:860px">
  <h2 class="t">Частые вопросы</h2>
''' + FAQ_MAIN + '''
</div></section>

<section class="blk" style="padding-top:0"><div class="w">
''' + BLANK.format(h2='Получить лицензию МЧС <em>под ключ</em>') + '''
</div></section>
'''

# ============================================================ ВИДЫ РАБОТ
V9 = [
 ('I','Системы пожаротушения','Монтаж, ТО и ремонт водяного, пенного, газового, порошкового и аэрозольного пожаротушения, включая пусконаладку. Самый востребованный вид: ТЦ, склады, производства, бизнес-центры.'),
 ('II','Пожарная сигнализация','АПС и ОПС, системы передачи извещений, диспетчеризация, пусконаладка. Нужен всем, кто ставит и обслуживает датчики и приёмно-контрольные приборы.'),
 ('III','Противопожарное водоснабжение','Внутренний противопожарный водопровод, наружные сети, пожарные гидранты, насосные станции.'),
 ('IV','Противодымная вентиляция','Системы дымоудаления и подпора воздуха, огнезадерживающие клапаны, вентиляторы дымоудаления.'),
 ('V','СОУЭ','Системы оповещения и управления эвакуацией людей при пожаре всех пяти типов.'),
 ('VI','Противопожарные преграды','Противопожарные двери, ворота, люки, окна, шторы: монтаж и обслуживание заполнений проёмов.'),
 ('VII','Огнезащита','Огнезащитная обработка металлических и деревянных конструкций, кабелей, воздуховодов, тканей.'),
 ('VIII','Первичные средства','Огнетушители, пожарные шкафы, краны и рукава: установка, перезарядка, обслуживание.'),
 ('IX','Тушение пожаров','Тушение пожаров в населённых пунктах и на объектах. Отдельное лицензирование с повышенными требованиями к персоналу и технике.'),
]
VIDY_LEDGER = '\n'.join(
    f'    <div class="li-row"><span class="no">{n}</span><h2>{t}</h2><p>{d}</p></div>'
    for n, t, d in V9)

VIDY_PAGE = phero('Виды работ',
                  'Виды работ <em>по лицензии МЧС</em>',
                  'Девять видов деятельности по Постановлению Правительства РФ № 1128. Оформим лицензию на любой набор: от одного вида до всех девяти.') + '''

<section class="blk"><div class="w">
  <div class="ledger fx">
''' + VIDY_LEDGER + '''
  </div>
  <div class="callout fx" style="margin-top:32px"><b>Не знаете, какие виды выбрать?</b> Подберём оптимальный набор под ваши контракты и тендеры: лишние виды удорожают лицензию, недостающие блокируют работу. Консультация бесплатная.</div>
</div></section>

<section class="blk" style="padding-top:0"><div class="w">
''' + BLANK.format(h2='Оформим на любой <em>набор видов</em>') + '''
</div></section>
'''

USLUGI = phero('Все услуги',
               'Полный спектр <em>услуг</em>',
               'Лицензии, СРО, ISO, реестры специалистов, учебный центр и оборудование. Всё для легальной работы вашей компании, в одном месте.') + '''

<section class="blk" id="licenzii"><div class="w">
  <h2 class="t">Лицензирование</h2>
  <p class="t-sub">Основная практика компании с 2016 года.</p>
  <div class="ledger mt fx">
    <a class="li-row" href="licenziya-mchs.html"><span class="no">01</span><h3>Лицензия МЧС под ключ</h3><p>Монтаж, ТО и ремонт средств пожарной безопасности, огнезащита, тушение. От 35 000 ₽, 15-25 рабочих дней.</p></a>
    <div class="li-row"><span class="no">02</span><h3>Лицензия Минкульта</h3><p>Работы на объектах культурного наследия: реставрация, ремонт, приспособление.</p></div>
    <div class="li-row"><span class="no">03</span><h3>Подтверждение лицензионных требований МЧС</h3><p>Периодическое подтверждение раз в 3 года: готовим и сопровождаем процедуру.</p></div>
    <div class="li-row"><span class="no">04</span><h3>Подача уведомлений МЧС</h3><p>Уведомления о начале и окончании работ через Госуслуги.</p></div>
    <a class="li-row" href="tseny.html"><span class="no">05</span><h3>Готовая фирма с лицензией МЧС</h3><p>ООО с действующей лицензией и чистой историей, переоформление за 1-3 дня.</p></a>
  </div>
</div></section>

<section class="blk" style="padding-top:0" id="sro"><div class="w">
  <h2 class="t">СРО и реестры специалистов</h2>
  <div class="ledger mt fx">
    <div class="li-row"><span class="no">01</span><h3>Вступление в СРО строителей</h3><p>Подбор СРО, документы, взносы: под ключ без отказов.</p></div>
    <div class="li-row"><span class="no">02</span><h3>Вступление в СРО проектировщиков</h3><p>Допуск к проектным работам, включая особо опасные объекты.</p></div>
    <div class="li-row"><span class="no">03</span><h3>Вступление в СРО изыскателей</h3><p>Инженерные изыскания: членство и специалисты под требования.</p></div>
    <div class="li-row"><span class="no">04</span><h3>Внесение в НРС НОСТРОЙ</h3><p>Национальный реестр специалистов в строительстве.</p></div>
    <div class="li-row"><span class="no">05</span><h3>Внесение в НРС НОПРИЗ</h3><p>Реестр специалистов по проектированию и изысканиям.</p></div>
    <div class="li-row"><span class="no">06</span><h3>НОК: независимая оценка квалификации</h3><p>Подготовка и сопровождение экзамена в ЦОК.</p></div>
  </div>
</div></section>

<section class="blk" style="padding-top:0" id="iso"><div class="w">
  <h2 class="t">Сертификация ISO</h2>
  <div class="ledger mt fx">
    <div class="li-row"><span class="no">01</span><h3>ISO 9001</h3><p>Система менеджмента качества: для тендеров и крупных заказчиков.</p></div>
    <div class="li-row"><span class="no">02</span><h3>ISO 14001</h3><p>Экологический менеджмент.</p></div>
    <div class="li-row"><span class="no">03</span><h3>ISO 45001</h3><p>Охрана труда и производственная безопасность.</p></div>
    <div class="li-row"><span class="no">04</span><h3>Интегрированный сертификат ISO</h3><p>9001 + 14001 + 45001 единой системой: дешевле и быстрее, чем по отдельности.</p></div>
  </div>
</div></section>

<section class="blk" style="padding-top:0" id="centr"><div class="w">
  <h2 class="t">Учебный центр</h2>
  <p class="t-sub">Собственный центр: обучаем и аттестуем без посредников.</p>
  <div class="ledger mt fx">
    <div class="li-row"><span class="no">01</span><h3>Профпереподготовка для аттестации МЧС</h3><p>Программы под лицензионные требования к специалистам.</p></div>
    <div class="li-row"><span class="no">02</span><h3>Аттестация проектировщика МЧС</h3><p>Подготовка к аттестации в области пожарной безопасности.</p></div>
    <div class="li-row"><span class="no">03</span><h3>Повышение квалификации</h3><p>Курсы для ИТР и руководителей с удостоверением установленного образца.</p></div>
    <div class="li-row"><span class="no">04</span><h3>Свидетельство о присвоении профессии</h3><p>Рабочие профессии: обучение и документ.</p></div>
    <div class="li-row"><span class="no">05</span><h3>Удостоверение рабочих профессий</h3><p>Допуски для монтажников, электромонтёров и других специальностей.</p></div>
    <div class="li-row"><span class="no">06</span><h3>Охрана труда и электробезопасность</h3><p>Обязательное обучение работников с проверкой знаний.</p></div>
  </div>
</div></section>

<section class="blk" style="padding-top:0" id="oborudovanie"><div class="w">
  <h2 class="t">Оборудование и лаборатории</h2>
  <div class="ledger mt fx">
    <div class="li-row"><span class="no">01</span><h3>Аренда оборудования для лицензии МЧС</h3><p>Поверенные приборы по Приказу № 571 с записью в ФГИС «Аршин».</p></div>
    <div class="li-row"><span class="no">02</span><h3>Продажа оборудования для лицензии МЧС</h3><p>Готовые комплекты под ваши виды работ.</p></div>
    <div class="li-row"><span class="no">03</span><h3>Регистрация электролаборатории</h3><p>Свидетельство о регистрации в Ростехнадзоре до 1000 В и выше.</p></div>
    <div class="li-row"><span class="no">04</span><h3>Аккредитация экспертной организации</h3><p>В области оценки соответствия объектов защиты требованиям пожарной безопасности.</p></div>
  </div>
</div></section>

<section class="blk" style="padding-top:0"><div class="w">
''' + BLANK.format(h2='Не нашли услугу? <em>Спросите нас</em>') + '''
</div></section>
'''

# ============================================================ ЦЕНЫ
TSENY = phero('Цены',
              'Цены <em>и тарифы</em>',
              'Прозрачные пакеты без скрытых доплат. Госпошлина оплачивается отдельно: 7 500 ₽ за выдачу, 3 500 ₽ за переоформление.') + '''

<section class="blk" style="padding-top:48px"><div class="w">
  <div class="shelf fx">
    <h2 class="t">Четыре пакета</h2>
    <p class="t-sub">Цена зависит от набора видов работ и того, что уже есть у вас.</p>
''' + TIERS.format(cta='kontakty.html#zayavka') + '''
    <p class="fee">Госпошлина отдельно: 7 500 ₽ за выдачу, 3 500 ₽ за переоформление.</p>
  </div>
</div></section>

<section class="blk" style="padding-top:0" id="calc"><div class="w">
  <h2 class="t">Рассчитайте под свою задачу</h2>
  <p class="t-sub">Четыре вопроса, ориентир сразу на экране.</p>
''' + CALC.format(cta='kontakty.html#zayavka') + '''
</div></section>

<section class="blk" style="padding-top:0"><div class="w" style="max-width:860px">
  <h2 class="t">Вопросы про оплату</h2>
  <div class="qa mt fx">
    <details><summary>Есть ли предоплата?</summary><p class="ans">Нет. Работаем по этапам: оплата привязана к выполненным шагам из договора. Доступна рассрочка 0%.</p></details>
    <details><summary>Что входит в цену «под ключ»?</summary><p class="ans">Подбор специалистов, аренда поверенного оборудования, подготовка документов, подача через Госуслуги и сопровождение выездной проверки МЧС. Госпошлина 7 500 ₽ оплачивается отдельно.</p></details>
    <details><summary>От чего зависит итоговая стоимость?</summary><p class="ans">От количества видов работ, наличия у вас специалистов и оборудования, формы организации и срочности. Точный расчёт делаем после короткого аудита.</p></details>
    <details><summary>Что будет, если лицензию не выдадут?</summary><p class="ans">Гарантия результата зафиксирована в договоре: при отказе по нашей вине возвращаем оплату полностью.</p></details>
  </div>
</div></section>
'''

# ============================================================ ПРОВЕРКА
PROVERKA = phero('Проверка лицензии',
                 'Проверка лицензии МЧС <em>в реестре</em>',
                 'С 2021 года лицензия существует только как запись в реестре МЧС России. Проверить себя или подрядчика можно за пару минут.') + '''

<section class="blk"><div class="w spread">
  <div class="stick fx">
    <h2 class="t">Три шага проверки</h2>
    <p class="t-sub">Реестр открытый, регистрация не нужна. Достаточно ИНН.</p>
  </div>
  <div class="timeline fx">
    <div class="tstep"><h3>Откройте реестр МЧС</h3><p>Реестр лицензий опубликован на официальном сайте МЧС России и доступен без регистрации.</p></div>
    <div class="tstep"><h3>Введите ИНН</h3><p>Название тоже работает, но ИНН надёжнее: исключает однофамильцев.</p></div>
    <div class="tstep"><h3>Сверьте карточку</h3><p>Статус лицензии, перечень разрешённых видов работ и дата записи. Виды работ должны покрывать предмет вашего договора.</p></div>
  </div>
</div></section>

<section class="blk" style="padding-top:0"><div class="w prose">
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
</div></section>

<section class="blk" style="padding-top:0"><div class="w">
''' + BLANK.format(h2='Нужна своя лицензия? <em>Оформим под ключ</em>') + '''
</div></section>
'''

# ============================================================ О КОМПАНИИ
OKOMP = phero('О компании',
              'Сенсор <em>Лицензирование</em>',
              'Полный спектр разрешительной документации: лицензии МЧС и Минкульта, СРО, ISO, НРС и НОК, электролаборатория, оборудование и собственный учебный центр.') + '''

<div class="facts w">
  <div class="row fx">
    <div class="fact"><div class="v" data-cnt="1600">0</div><div class="l">лицензий МЧС оформлено</div></div>
    <div class="fact"><div class="v"><span data-cnt="9">0</span> <i>лет</i></div><div class="l">на рынке, с 2016 года</div></div>
    <div class="fact"><div class="v" data-cnt="6">0</div><div class="l">филиалов по России</div></div>
    <div class="fact"><div class="v" data-cnt="20">0</div><div class="l">госконтрактов сопровождено</div></div>
  </div>
</div>

<section class="blk"><div class="w team">
  <div class="ph fx"><img src="assets/real/team2.webp" width="1024" height="683" alt="Команда компании Сенсор Лицензирование" fetchpriority="high"></div>
  <div class="fx">
    <h2 class="t">Почему с нами спокойно</h2>
    <ul>
      <li><div><b>Гарантия результата в договоре</b><span>при отказе по нашей вине вернём оплату полностью</span></div></li>
      <li><div><b>Рассрочка 0% и оплата по этапам</b><span>без предоплаты, платите по мере выполнения</span></div></li>
      <li><div><b>Своё поверенное оборудование</b><span>приборы по Приказу № 571 в аренду, поверка в «Аршине»</span></div></li>
      <li id="centr"><div><b>Собственный учебный центр</b><span>повышение квалификации и аттестация без посредников</span></div></li>
      <li><div><b>Работаем по всей России</b><span>шесть филиалов и полностью удалённое оформление</span></div></li>
    </ul>
  </div>
</div></section>

<section class="blk" style="padding-top:0"><div class="w">
  <h2 class="t">Письма от клиентов</h2>
  <div class="desk mt fx">
''' + LETTERS + '''
  </div>
  <div class="praise fx">
    <div class="score">4.9 <i>★</i></div>
    <p>Средняя оценка по 450+ отзывам на Яндекс Картах, 2ГИС и Google.</p>
  </div>
</div></section>

<section class="blk" style="padding-top:0"><div class="w prose">
  <h2>Реквизиты</h2>
  <div class="callout">
    <b>ООО «НТЦ СпецПожСтандарт»</b><br>
    ИНН 7751144295<br>
    Москва, Киевское шоссе, 22-й км, БП «Румянцево», корпус В, офис 409В<br>
    Телефон: 8 800 222-09-86, звонок по России бесплатный
  </div>
</div></section>
'''

# ============================================================ КОНТАКТЫ
KONTAKTY = phero('Контакты',
                 'Контакты',
                 'Отвечаем быстро: по телефону, в WhatsApp и Telegram. Перезвоним в течение 15 минут в рабочее время.') + '''

<section class="blk" style="padding-top:48px"><div class="w">
  <div class="cells fx" style="grid-template-columns:1fr 1fr;margin-bottom:40px">
    <div class="cell"><span class="k">Телефон</span>
      <h3 style="font-size:26px"><a href="tel:+78002220986">8 800 222-09-86</a></h3>
      <p>Звонок по России бесплатный. WhatsApp и Telegram по этому же номеру.</p></div>
    <div class="cell"><span class="k">Офис в Москве</span>
      <h3>БП «Румянцево»</h3>
      <p>Киевское шоссе, 22-й км, корпус В, офис 409В</p>
      <p style="margin-top:8px">ООО «НТЦ СпецПожСтандарт» · ИНН 7751144295</p></div>
  </div>
''' + BLANK.format(h2='Заполните бланк, <em>остальное оформим мы</em>') + '''
  <div class="map fx" style="margin-top:40px">
    <iframe src="https://yandex.ru/map-widget/v1/?text=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%20%D0%9A%D0%B8%D0%B5%D0%B2%D1%81%D0%BA%D0%BE%D0%B5%20%D1%88%D0%BE%D1%81%D1%81%D0%B5%2022%20%D0%BA%D0%BC%20%D0%91%D0%9F%20%D0%A0%D1%83%D0%BC%D1%8F%D0%BD%D1%86%D0%B5%D0%B2%D0%BE&z=14" title="Офис Сенсор Лицензирование на карте" loading="lazy"></iframe>
  </div>
</div></section>
'''

ORG_LD = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Organization","name":"Сенсор Лицензирование","legalName":"ООО «НТЦ СпецПожСтандарт»","telephone":"+7-800-222-09-86","address":{"@type":"PostalAddress","addressLocality":"Москва","streetAddress":"Киевское шоссе, 22-й км, БП Румянцево, корп. В, оф. 409В"},"foundingDate":"2016","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"450"}}
</script>
'''

page('index.html', None,
     'Сенсор Лицензирование: пожарная лицензия МЧС под ключ | Москва и вся Россия',
     'Лицензия МЧС под ключ за 15-25 рабочих дней, переоформление, готовые фирмы, обучение специалистов. С 2016 года, 1600+ лицензий, гарантия в договоре.',
     INDEX, extra_head=ORG_LD)

page('licenziya-mchs.html', 0,
     'Пожарная лицензия МЧС под ключ от 35 000 ₽ за 15-25 дней | Сенсор Лицензирование',
     'Оформим лицензию МЧС на монтаж, обслуживание и тушение под ключ: специалисты, оборудование, документы, сопровождение проверки. Гарантия в договоре, рассрочка 0%.',
     LIC, crumb='Пожарная лицензия МЧС', extra_head=FAQ_LD)

page('uslugi.html', 1,
     'Все услуги: лицензии МЧС и Минкульта, СРО, ISO, обучение | Сенсор Лицензирование',
     'Полный каталог услуг Сенсор Лицензирование: лицензия МЧС и Минкульта, вступление в СРО, сертификаты ISO, НРС, НОК, учебный центр, аренда оборудования, электролаборатория.',
     USLUGI, crumb='Все услуги')

page('vidy-rabot.html', None,
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
