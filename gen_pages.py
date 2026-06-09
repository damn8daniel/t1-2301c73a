# -*- coding: utf-8 -*-
"""Генератор остальных страниц: общий шаблон шапки/футера + тела страниц."""
import io

HEAD = '''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="robots" content="noindex,nofollow">
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/main.css">
{extra_head}</head>
<body>

<nav class="nav"><div class="nav-in">
  <a class="nav-logo" href="index.html"><img src="assets/real/logo.png" alt="Сенсор Лицензирование"></a>
  <div class="nav-links">
    <a {a1} href="licenziya-mchs.html">Лицензия МЧС</a>
    <a {a2} href="vidy-rabot.html">Виды работ</a>
    <a {a3} href="tseny.html">Цены</a>
    <a {a4} href="proverka.html">Проверка лицензии</a>
    <a {a5} href="o-kompanii.html">О компании</a>
    <a {a6} href="kontakty.html">Контакты</a>
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
      <img src="assets/real/logo.png" alt="Сенсор Лицензирование">
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
<div class="toast" id="toast">Заявка принята. Перезвоним в течение 15 минут</div>

<script src="assets/js/main.js" defer></script>
</body>
</html>
'''

def page(fname, nav_idx, title, desc, crumb, body, extra_head=''):
    acts = ['' for _ in range(6)]
    if nav_idx is not None:
        acts[nav_idx] = 'class="act"'
    html = HEAD.format(title=title, desc=desc, crumb=crumb, extra_head=extra_head,
                       a1=acts[0], a2=acts[1], a3=acts[2], a4=acts[3], a5=acts[4], a6=acts[5]) + body + FOOT
    with io.open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print('written', fname)

# ============================================================ vidy-rabot
VIDY = u'''
<section class="page-hero">
  <div class="w">
    <h1 class="t-big">Виды работ<br>по лицензии МЧС</h1>
    <p class="t-lead">Девять видов деятельности по Постановлению Правительства РФ № 1128. Разбираем, что входит в каждый и кому он нужен.</p>
  </div>
</section>
<div data-mbar-after></div>

<section class="sec sec-soft" style="padding-top:48px">
  <div class="w prose">
    <h2>1. Монтаж, ТО и ремонт систем пожаротушения</h2>
    <p>Водяное, пенное, газовое, порошковое и аэрозольное пожаротушение, включая их элементы и пусконаладку. Самый востребованный вид: его выбирают монтажные организации, обслуживающие ТЦ, склады, производства и бизнес-центры.</p>
    <h2>2. Монтаж, ТО и ремонт пожарной и охранно-пожарной сигнализации</h2>
    <p>АПС и ОПС, системы передачи извещений, диспетчеризация и пусконаладочные работы. Нужен всем, кто ставит и обслуживает датчики, приёмно-контрольные приборы и оповещатели.</p>
    <h2>3. Монтаж, ТО и ремонт противопожарного водоснабжения</h2>
    <p>Внутренний противопожарный водопровод, наружные сети, пожарные гидранты, насосные станции.</p>
    <h2>4. Монтаж, ТО и ремонт противодымной вентиляции</h2>
    <p>Системы дымоудаления и подпора воздуха, включая огнезадерживающие клапаны и вентиляторы дымоудаления.</p>
    <h2>5. Монтаж, ТО и ремонт СОУЭ</h2>
    <p>Системы оповещения и управления эвакуацией людей при пожаре всех пяти типов.</p>
    <h2>6. Заполнение проёмов в противопожарных преградах</h2>
    <p>Противопожарные двери, ворота, люки, окна и шторы, а также их обслуживание.</p>
    <h2>7. Огнезащита материалов, изделий и конструкций</h2>
    <p>Огнезащитная обработка металлических и деревянных конструкций, кабелей, воздуховодов, тканей.</p>
    <h2>8. Монтаж, ТО и ремонт первичных средств пожаротушения</h2>
    <p>Огнетушители, пожарные шкафы, краны и рукава: установка, перезарядка, обслуживание.</p>
    <h2>9. Деятельность по тушению пожаров</h2>
    <p>Тушение пожаров в населённых пунктах, на производственных объектах и объектах инфраструктуры. Отдельное лицензирование с повышенными требованиями к персоналу и технике.</p>
    <div class="callout"><b>Не знаете, какие виды выбрать?</b> Подберём оптимальный набор под ваши контракты и тендеры: лишние виды удорожают лицензию, недостающие блокируют работу.</div>
  </div>
</section>

<section class="sec cta-final">
  <div class="w">
    <h2 class="t-big fx">Оформим на любой набор видов</h2>
    <p class="t-lead fx fx-d1">От одного вида до всех девяти. Цена и срок зависят от набора: рассчитайте за минуту.</p>
    <div class="hero-cta fx fx-d2">
      <a class="btn big" href="licenziya-mchs.html#calc">Рассчитать стоимость</a>
      <a class="btn big ghost" href="tel:+78002220986">8 800 222-09-86</a>
    </div>
  </div>
</section>
'''

# ============================================================ tseny
TSENY = u'''
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
PROVERKA = u'''
<section class="page-hero">
  <div class="w">
    <h1 class="t-big">Проверка лицензии МЧС<br>в реестре</h1>
    <p class="t-lead">С 2021 года лицензия существует только как запись в реестре МЧС России. Рассказываем, как проверить себя или подрядчика за пару минут.</p>
  </div>
</section>
<div data-mbar-after></div>

<section class="sec sec-soft" style="padding-top:48px">
  <div class="w prose">
    <h2>Как проверить лицензию по ИНН</h2>
    <p>Откройте реестр лицензий на официальном сайте МЧС России и введите ИНН организации или ИП. В карточке вы увидите статус лицензии, перечень разрешённых видов работ и дату внесения записи.</p>
    <ul>
      <li>Запись есть и статус действующий: подрядчик имеет право выполнять указанные виды работ.</li>
      <li>Записи нет: лицензия отсутствует, договор с таким подрядчиком несёт риски для заказчика.</li>
      <li>Виды работ в карточке не совпадают с предметом договора: подрядчик выходит за рамки своей лицензии.</li>
    </ul>
    <div class="callout"><b>Важно:</b> бумажный бланк лицензии сам по себе ничего не подтверждает с 2021 года. Юридическую силу имеет только запись в реестре.</div>
    <h2>Что проверить кроме реестра</h2>
    <p>Для тендеров и крупных контрактов дополнительно смотрят выписку ЕГРЮЛ, наличие штатных специалистов и действующую поверку оборудования. Эти требования МЧС проверяет и при периодическом подтверждении раз в 3 года.</p>
    <h2>Поможем разобраться</h2>
    <p>Если со статусом что-то не так: лицензии нет, виды работ не совпадают или подходит срок периодического подтверждения, позвоните нам. Подскажем бесплатно, что делать дальше.</p>
  </div>
</section>

<section class="sec cta-final">
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
OKOMP = u'''
<section class="page-hero">
  <div class="w">
    <h1 class="t-big">Сенсор Лицензирование</h1>
    <p class="t-lead">Помогаем бизнесу легально работать в сфере пожарной безопасности: лицензии МЧС, СРО, ISO, электролаборатория и собственный учебный центр.</p>
  </div>
</section>
<div data-mbar-after></div>

<section class="sec" style="padding-top:32px">
  <div class="w">
    <div class="zoom-img fx-scale"><img src="assets/real/office.jpg" alt="Команда компании Сенсор Лицензирование в офисе" fetchpriority="high"></div>
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
    <a class="hcard-img" href="assets/real/pismo_1.jpg" target="_blank" rel="noopener"><img loading="lazy" src="assets/real/pismo_1.jpg" alt="Благодарственное письмо клиента, скан 1"></a>
    <a class="hcard-img" href="assets/real/pismo_2.jpg" target="_blank" rel="noopener"><img loading="lazy" src="assets/real/pismo_2.jpg" alt="Благодарственное письмо клиента, скан 2"></a>
    <a class="hcard-img" href="assets/real/pismo_3.jpg" target="_blank" rel="noopener"><img loading="lazy" src="assets/real/pismo_3.jpg" alt="Благодарственное письмо клиента, скан 3"></a>
    <a class="hcard-img" href="assets/real/pismo_4.jpg" target="_blank" rel="noopener"><img loading="lazy" src="assets/real/pismo_4.jpg" alt="Благодарственное письмо клиента, скан 4"></a>
    <a class="hcard-img" href="assets/real/pismo_5.jpg" target="_blank" rel="noopener"><img loading="lazy" src="assets/real/pismo_5.jpg" alt="Благодарственное письмо клиента, скан 5"></a>
    <a class="hcard-img" href="assets/real/pismo_6.jpg" target="_blank" rel="noopener"><img loading="lazy" src="assets/real/pismo_6.jpg" alt="Благодарственное письмо клиента, скан 6"></a>
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
KONTAKTY = u'''
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
     u'Виды работ по лицензии МЧС: все 9 видов деятельности по ПП № 1128 | Сенсор',
     u'Какие виды работ входят в лицензию МЧС: пожаротушение, сигнализация, водопровод, дымоудаление, СОУЭ, двери, огнезащита, первичные средства, тушение пожаров.',
     u'Виды работ', VIDY)

page('tseny.html', 2,
     u'Цены на лицензию МЧС 2026: тарифы от 35 000 ₽, калькулятор | Сенсор',
     u'Сколько стоит лицензия МЧС: тарифы от 35 000 ₽, под ключ от 80 000 ₽, срочно от 130 000 ₽. Калькулятор стоимости, рассрочка 0%, оплата по этапам.',
     u'Цены', TSENY)

page('proverka.html', 3,
     u'Проверка лицензии МЧС в реестре по ИНН: инструкция | Сенсор',
     u'Как проверить лицензию МЧС в реестре по ИНН: пошаговая инструкция, на что смотреть в карточке, какие риски у работы с подрядчиком без лицензии.',
     u'Проверка лицензии', PROVERKA)

page('o-kompanii.html', 4,
     u'О компании Сенсор Лицензирование: 1600+ лицензий МЧС с 2016 года',
     u'Сенсор Лицензирование: лицензии МЧС, СРО, ISO, учебный центр. 9 лет на рынке, 6 филиалов, 1600+ оформленных лицензий, рейтинг 4.9.',
     u'О компании', OKOMP)

page('kontakty.html', 5,
     u'Контакты Сенсор Лицензирование: 8 800 222-09-86, Москва, БП Румянцево',
     u'Контакты компании Сенсор Лицензирование: телефон 8 800 222-09-86 (бесплатно по РФ), офис в Москве, БП Румянцево. Заявка на лицензию МЧС онлайн.',
     u'Контакты', KONTAKTY)
