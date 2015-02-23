﻿#День4 обед"
#
label uvao_uvao_D4_lunch:
    $ persistent.sprite_time = "day"
    play ambience ambience_dining_hall_full fadein 3
    scene bg int_dining_hall_people_day with fade
    window show

# Д4-обед
#
# используется флаг посещения медпункта uvao_D4_aidpost_visit
# устанавливает флаг ухода на концерт uvao_D4_concert
#
    "В столовой почему-то было просторнее, чем обычно."
    "То ли часть пионеров выбыла из строя, наевшись чего-то не того{w}, то ли их просто задержали на каком-то мероприятии, о котором я не знал."
    "Впрочем, не всё ли мне равно? Меньше народа - больше кислорода!{w} Главное, в столовой было достаточно свободных мест, что давало мне некоторую свободу выбора."
#
    "После акробатических упражнений на площади есть хотелось особенно сильно, но и любопытство, раззадоренное чтением статьи в библиотеке, тоже не давало покоя."
    th "Вообще-то, кто мешает мне совместить полезное с полезным? Можно подсесть к кому-нибудь и за едой попробовать ненавязчиво выведать что-нибудь о местных реалиях…"
    dreamgirl "«Ненавязчиво выведать» ты уже пробовал в первый день - у Лены. Гениально проведённая разведывательная операция, исполненная тонкого знания психологии."
    "Не удостоив Шизу ответом, я взял с раздачи поднос и окинул взглядом столовую, выбирая, к кому бы из знакомых присоседиться."
    show mi normal pioneer far at fleft with dspr
    "Ближе всего было свободное место рядом с Мику.{w} Определённо, никаких проблем с тем, чтобы её разговорить, не предвиделось - скорее уж наоборот."
    "Вопрос только в том, удастся ли направить фонтан её красноречия в интересующем меня направлении.{w} В своих способностях в этой области я не сомневался ни секунды{w} - однозначно, не справлюсь."
    hide mi with dspr
    th "Тем более, что она, можно сказать, иностранка. Так ли уж много она знает про {i}эту страну{/i}. Лучше попробовать с аборигенами пообщаться."
    dreamgirl "Ну ты, барин, и задачи ставишь! Где же их здесь взять, аборигенов-то?{w} Хотя подожди, вот же как раз сидят две прелестных рыжеволосых аборигенки. Как раз и место рядом свободно!"
    show dv smile pioneer far at fright with dspr
    show us grin pioneer far at right with dspr
    "Сидящие поотдаль Алиса с Ульянкой уже некоторое время на меня ехидно поглядывали."
    show dv grin pioneer far at fright with dspr
    $ renpy.pause (1.5)
    show us laugh pioneer far at right with dspr
    "Заметив, что я смотрю в их сторону, Двачевская что-то быстро зашептала подруге на ухо, та прыснула и состроила мне гримасу."
    th "Вот уж не думал, что у меня, оказывается, латентная склонность к мазохизму!"
    th "Если уж собственное альтер эго предлагает мне поучаствовать в комедии «Девочки с рыжими волосами, или Тридцать три подзатыльника»!{w} Меня будут обливать борщом, кормить саранчой, давать пощёчины… Словом, унижать морально и физически. Это очень смешная комедия…"
    hide dv with dspr
    hide us with dspr
    "Шиза изобразила демонический хохот, а я, рассудив, что обед в обществе сразу двух рыжих бандиток вряд ли принесёт какую-то пользу, а вот нервотрёпки избежать точно не удастся, огляделся в поисках более подходящей компании."
#
    menu:
        "Сесть с Леной":
#
# Исходим из того, что в Д2-Д3 с Леной общались мало (конвой в Д2 невозможен, а остальные выборы в её пользу не использовались/использовались мало, иначе не проходим в ЮВАО по ЛП)"
# Соответственно, до сих пор Лена свою симпатию к ГГ с ним не обсуждала, ибо не имела возможности/стеснялась"
#
            show un sad pioneer far at center with dissolve
            "Я почувствовал на себе чей-то взгляд и, обернувшись, увидел как Лена поспешно отвела глаза и уткнулась носом в тарелку."
            th "Пожалуй, стоит с ней поговорить.{w} Извинюсь за странные расспросы в первый день, скажу что неудачно пошутил, или что-то вроде этого.{w} А там, глядишь, и разговоримся."
            show un sad pioneer at center with dissolve
            "Решительно подойдя к столу, за которым она сидела, я кивнул на свободное место напротив."
            me "Ты не против, если я присяду?"
            show un surprise pioneer at center with dspr
            "Лена как-то странно глянула на меня, но тут же снова уставилась в стол и неловко кивнула, слегка при этом покраснев."
            show un shy pioneer close at center with dissolve
            "Решив принять этот жест за знак согласия, я уселся и составил с подноса тарелки."
            me "Приятного аппетита."
            "Она снова кивнула и, не поднимая глаз, беззвучно шевельнула губами."
            "Слегка обескураженный таким приёмом, я принялся за еду, периодически поглядывая на Лену."
            stop ambience fadeout 15
            play music music_list["lets_be_friends"] fadein 10
            "Та сидела, гоняя вилкой по тарелке несколько оставшихся макаронин, и упорно не глядя на меня."
            th "Странно, до этого она вела себя вполне нормально.{w}\nНасколько это возможно для такой стесняши, разумеется."
            th "Неужели я так сильно смутил её тогда расспросами про Генду?"
            th "Это даже и расспросами-то назвать нельзя, для неё это должно выглядеть как неумная шутка или, максимум, проявление лёгкого слабоумия, но не более того."
            "Пауза явно затягивалась и, заканчивая с супом, я наконец решил попробовать ещё раз завести светскую беседу."
            me "Э-э-э… как дела?{w} Я имею в виду, как прошло утро?"
            show un surprise pioneer close at center with dspr
            "Кажется, даже Шиза не нашлась, что сказать на это вступление."
            "Лена подняла на меня озадаченный вгляд, но быстро опомнилась и снова принялась сосредоточенно разглядывать опустевшую тарелку."
            show un shy pioneer close at center with dspr
            "Внутренне поморщившись от собственного идиотизма, я решил, тем не менее, давить до последнего."
            me "Послушай, я извиниться перед тобой хотел. В первый вечер тебя про Генду спрашивал… Ты не обращай внимания, это я так… э-э-э…"
            show un surprise pioneer close at center with dspr
            "Теперь девочка уставилась на меня уже с явным недоумением, и дальнейшие слова сами собой замерли у меня на языке."
            dreamgirl "Знаешь, здесь даже я не понимаю, что происходит. Может быть, дело не в твоих дурацких расспросах?"
            show un sad pioneer close at center with dspr
            dreamgirl "Слушай, может быть, она в тебя влюбилась? Хотя нет, вы почти и не общались."
            dreamgirl "А с другой стороны, ты мужчина хоть куда - в самом рассвете сил. Точно, влюбилась!"
            "Скрипнув мысленно зубами, я попытался продолжить выступление."
            me "Э-э-э… Видишь ли, это у меня такое задание на лето, провести э-э-э… своего рода социологический опрос…"
            show un shy pioneer close at center with dspr
            "Тут я окончательно потерялся и понял, что единственное спасение для меня - это быстренько всё доесть и свалить отсюда поскорее."
            "С минуту всё было тихо. Я поспешно заглатывал свою порцию макарон по-флотски. Лена сидела напротив и продолжала гипнотизировать тарелку, постепенно краснея всё больше."
            "Я уже схватился за стакан с компотом, когда вдруг она отложила вилку в сторону и решительно посмотрела мне прямо в глаза."
            show un serious pioneer close at center with dspr
            un "Семён, я хотела тебя спросить…"
            "От неожиданности я чуть компотом не захлебнулся."
            show un shy pioneer close at center with dspr
            "Лена смутилась и снова отвела было взгляд{w}, но неожиданно быстро взяла себя в руки и продолжила, пусть и запинаясь после каждого слова, но совершенно отчётливо, вместо своей тарелки гипнотизируя теперь уже меня своими бездонными зелёными глазами."
            show un sad pioneer close at center with dspr
            un "Понимаешь…{w} последние… несколько дней…{w} Вернее, с того дня…{w} как ты приехал… я…{w} Вернее, со мной…"
            show sl happy pioneer at fright
            stop music fadeout 1
            play ambience ambience_dining_hall_full fadein 1
            show un surprise pioneer close at center with dspr
            sl "А! Я смотрю, вы обед уже закончили!"
            "Раздался откуда-то сверху жизнерадостный до отвращения голос."
            "Я вперил в его обладательницу полный ненависти взгляд, но Славя этого то ли не заметила, то ли её такие мелочи не смущали."
            sl "Ну что, пойдёмте на концерт? Посмотрим, что ребята приготовили!"
            show un sad pioneer close at center with dspr
            th "Вот делать мне больше нечего, только самодеятельностью любоваться!{w} Меня мирового масштаба тайны ждут, а она…"
            me "Славя, мне бы…"
            show sl serious pioneer at fright with dspr
            sl "Нет-нет, ты и так, Семён, всё время отрываешься от коллектива, а концерт это важное общественное мероприятие, все старались, готовились, Мику там изо всех сил…"
            "Наша активисточка продолжала разливаться дальше про ответственность перед обществом и что-то ещё в том же духе, но я её уже не слушал."
            show un normal pioneer at center with dissolve
            show sl normal pioneer at fright with dspr
            "Лена тем временем встала и, нацепив на лицо отстранённо-нейтральное выражение, покорно пошла на выход.{w} Словно и не было только что этого странного разговора."
            "Словно это не она пыталась не то спросить у меня что-то, не то рассказать о чём-то для неё очень важном."
            hide un with easeoutright
            dreamgirl "Знаешь, а вот это уже и в самом деле свинство.{w} Сидят люди, непринуждённо общаются со взаимным удовольствием, и вдруг эта Славя подкрадывается со своими глупостями."
            dreamgirl "Хотя с другой стороны - а не оказала ли тебе активисточка только что любезность?"
            th "Какую ещё любезность?!{w} Что, моя карманная Шиза тоже сошла с ума?"
            dreamgirl "Чем обзываться, лучше пораскинь мозгами.{w} Лена явно собиралась основательно тебя загрузить какими-то своими проблемами, это даже тебе должно быть понятно."
            dreamgirl "А теперь подумай - оно тебе надо?{w} Нет, я понимаю, ты немного поплыл - такая милая скромная девочка, фигурка что надо, глазища эти… Так и хочется её утешить по самое не балуйся."
            dreamgirl "Но ты, вроде бы, собирался делом заниматься, разве нет?"
            show sl angry pioneer at fright with dspr
            sl "…меня слушаешь вообще?!"
            "Вздрогнув, я отвлёкся от увлекательного диалога с самим собой и обратил внимание на Славю. Кажется, она уже успела всерьёз рассердиться."
            sl "Имей в виду, на концерт ты пойдёшь обязательно."
            sl "Если понадобится - за руку потащу! Не сможешь идти - понесём на носилках."
            sl "Ольга Дмитриевна сказала собрать всех - значит пойдут все!"
            show sl serious pioneer at fright with dspr
            "Сказала она, как отрезала."
            "Посмотрев ещё раз на Славю я понял, что у меня на выбор только два варианта - либо я иду добровольно, либо меня действительно силком отведут за руку, как маленького."
            "Обречённо вздохнув, я поплёлся за Славей."
            hide sl with easeoutright
            $ uvao_D4_concert = True
#
        "Сесть со Славей":
            show sl normal pioneer far at center with dissolve
            "Поймав мой вопросительный взгляд, Славя улыбнулась и помахала мне рукой."
            th "А что, хорошая идея!"
#
#необходимо добавить проверку на флаги ивентов со Славей в дни 1-3 (если они возможны при сычевании) и соответствующие трогательные упоминания о них."
#
            show sl normal pioneer at center with dissolve
            "Славя все эти дни относилась ко мне доброжелательно."
            "Кроме того, она наверняка назубок знает историю страны и партии и может рассказать мне что-нибудь полезное, если удастся придумать походящую отмазку для расспросов."
            me "Я так понимаю, ты не против моей компании?"
            "Спросил я, подходя к её столу."
            show sl happy pioneer at center with dspr
            sl "Ну конечно же не против! Садись!"
            "Она гостеприимным жестом указала на место напротив."
            show sl normal pioneer close at center with dissolve
            "Я уселся, сгружая посуду с подноса на стол."
            show sl smile pioneer close at center with dspr
            sl "Приятного аппетита!"
            "Улыбнулась мне Славя."
            me "И тебе приятного."
            "С удовольствием ответил я."
            play music music_list["take_me_beautifully"] fadein 10
            stop ambience fadeout 15
            show sl normal pioneer close at center with dspr
            sl "Спасибо ещё раз, что помог с уборкой на площади. В одиночку Электроник до сих пор бы с гирляндами возился."
# Перефразировать бы, сократив количество "бы" на квадратный сантиметр
            me "Да не вопрос. Тем более, если бы ещё и он сверзился с лестницы, то пришлось бы закрывать кружок кибернетики, а это стало бы серьёзным ударом по общественной деятельности в лагере."
            show sl angry pioneer close at center with dspr
            "Кажется, моя шутка не слишком понравилась Славе, потому что она нахмурилась и даже есть перестала."
            me "Извини, глупость сказал. Надеюсь, что с Шуриком всё будет в порядке."
            "Поспешил исправиться я."
            show sl serious pioneer close at center with dspr
            if uvao_D4_aidpost_visit:
                me "Я сегодня в медпункте был, так Виола говорит, что ещё денёк его подержит для порядка и отпустит."
            else:
# хорошо бы добавить в Д4-умывание-с-Элом или в Д4-уборка-гирлянд соответствующий диалог с Элом о Шурике"
                me "Мне Электроник сегодня сказал, что забегал в медпунк. Виола ему пообещала, что Шурика ещё денёк подержит для порядка и отпустит."
                sl "Да, я знаю."
            sl "Но всё равно, не шути так больше."
            me "Не буду, обещаю. Честное пионерское!"
            show sl normal pioneer close at center with dspr
            th "А кстати…"
            me "Тем более, у меня найдётся другой повод тебя немного шокировать."
            show sl surprise pioneer close at center with dspr
            "Хитро улыбнулся я."
            me "Я тебе сейчас задам неожиданный, но действительно важный для меня вопрос, а ты постарайся не задумываясь на него ответить - если сочтёшь возможным, разумеется."
            me "Обещаю, что сразу после твоего ответа я всё объясню."
            show sl shy pioneer close at center with dspr
            "Можно было догадаться, о чём подумала Славя, потому что на мгновение она явно смутилась, но быстро взяла себя в руки и решительно кивнула."
            show sl serious pioneer close at center with dspr
            sl "Ладно, спрашивай. Не обещаю, что отвечу на {i}любой{/i} твой вопрос, но постараюсь."
            dreamgirl "Да, да! Спроси, сколько у неё было парней, какая у неё любимая поза и… и…{w} Блин, такое раздолье для фантазии, что поневоле растеряешься!"
            "С серьёзным лицом я выдержал паузу…"
            me "Не могла бы ты коротко, буквально в несколько фраз, обрисовать роль товарища Генды в становлении нашего государства?"
            show sl surprise pioneer close at center with dspr
            "Разумеется, я бил наугад, но вряд ли этот самый Генда мог быть вовсе уж незначительной личностью, раз в пионерском лагере ему памятники ставят."
            "Смотреть на Славю было одно удовольствие. Определённо, она ожидала услышать что угодно, но только не это."
            "Мне стоило немалых усилий удержаться от смеха, но я справился."
            me "Я совершенно серьёзно - именно такой вопрос. И ты обещала ответить на него, если сможешь."
            "Спокойно заявил я."
            me "Или эта тема тебя смущает?{w} Разумеется, тогда я не буду настаивать."
            "Здесь я позволил себе улыбнуться, но только самую малость. Так, намёк на улыбку."
            show sl serious pioneer close at center with dspr
            sl "Подожди, ты и вправду хочешь, чтобы я…"
            "Наконец-то пришла в себя Славя."
            me "Да, я именно прошу тебя рассказать своими словами про Генду. Потом, как обещал, объясню зачем."
            "Девочка взмахнула косами и улыбнулась."
            show sl normal pioneer close at center with dspr
            sl "Ну хорошо. Стоит постараться как минимум для того, чтобы услышать потом твоё объяснение."
            "Как я и предполагал, со знанием истории у нашей активисточки всё было в полном порядке."
            "Я слушал, затаив дыхание, хотя и пытался делать безразличное лицо, как будто речь шла о фактах, известных мне с пелёнок."
# в следующей фразе должны упоминаться обрывочные фразы про Руководящую-Роль-Генды. Необходимо согласовать с Д4-Чтение-в-домике-после-обеда, чтобы исключить повторы."
            th "Генда… Руководящая роль… Верные соратники и продолжатели дела В.И.Ленин и И.В.Сталин…"
            "В голове творилось чёрт знает что. Либо это часть какой-то колоссальной мистификации, жертвой которой я всё-таки стал, либо…"
            show sl serious pioneer close at center with dspr
            "Возможно, мне не слишком хорошо удалось совладать с лицом, потому что, закончив, Славя посмотрела на меня как-то странно.{w} Пожалуй, даже с подозрением."
            sl "А теперь твоя очередь."
            me "Что?"
            "Растерялся я."
            show sl serious pioneer close at center with dspr
            sl "Ты же обещал объяснить, зачем тебе это было нужно!"
            "Возмутилась Славя."
            show sl angry pioneer close at center with dspr
            sl "Я надеюсь, это не какая-то глупая шутка?"
            "Спросила она с упрёком."
            me "Да нет, что ты! На самом деле всё очень просто.{w} Даже немного скучно, если честно."
            show sl serious pioneer close at center with dspr
            "Заторопился я с ответом.{w} Что бы здесь ни происходило, совсем незачем портить отношения со Славей.{w} Да и просто не хотелось обижать хорошего человека."
            show sl normal pioneer close at center with dspr
            me "Всего лишь часть школьного проекта по истории. Своего рода небольшой социопсихологический опрос."
            me "Мы с ребятами за лето опрашиваем всех, кого сможем, на такие вот темы.{w} Потом, осенью, всё это соберём воедино, обработаем…"
            me "В общем, такой вот эксперимент."
            show sl serious pioneer close at center with dspr
            sl "Экспериментатор!"
            "С упрёком бросила мне Славя, надув губки и рассеяно обводя черенком ложки клеточки на клеёнке, слегка смахивающей на шахматную доску."
            me "Славя, извини, я совсем не хотел тебя обидеть, но здесь всё дело именно в неожиданности вопроса.{w} К тому же, всё-таки общественное поручение…"
            sl "Да ладно тебе, ничего я не обижаюсь!"
            "Буркнула Славя."
            show sl normal pioneer close at center with dspr
            sl "Но чтобы окончательно загладить свою вину, тебе придётся принять участие ещё в одном общественно важном мероприятии."
            show sl happy pioneer close at center with dspr
            "Заулыбалась вдруг она, глядя на моё насторожившееся лицо."
            sl "Мы сейчас вместе идём на концерт.{w} И не вздумай отказываться! Ольга Дмитриевна велела всех собрать, так что явка обязательна."
            show sl smile pioneer close at center with dspr
            sl "И вообще, что ты будешь один сидеть, как сыч какой-нибудь?!"
            show sl normal pioneer at center with dissolve
            stop music fadeout 3
            play ambience ambience_dining_hall_full fadein 1
            "Встав из-за стола, она выжидающе посмотрела на меня."
            "Меньше всего мне сейчас хотелось любоваться на какую-то дурацкую самодеятельность."
            "В конце концов, в домике меня под подушкой дожидалась «<книга_что-то_там_про_Генду>», но выбора у меня, похоже, не было."
            th "Кажется, отказаться в такой ситуации будет не только рискованно, но и попросту невежливо…"
            hide sl with easeoutright
            "Стараясь не слишком показывать своё разочарование, я встал и поплёлся следом за Славей."
            $ uvao_D4_concert = True
#
        "Сесть одному":
            "Идея болтать с пионерами об истории страны нравилась мне всё меньше и меньше. Только время зря терять!{w} Совсем не обязательно, что я смогу узнать хоть что-то полезное, а вот за сумасшедшего очень даже могут принять. Мало мне разговора с Леной насчёт Генды!"
            th "Лучше сначала почитать добытую в библиотеке книгу, а уже потом, если приспичит, доставать окружающих вопросами.{w}\nПо крайней мере, не буду похож на совсем уж наивного дурачка."
            "Я уселся за свободный столик в углу, изобразил самое мрачное выражение лица, на какое был способен, и принялся торопливо поглощать пищу."
            "Обед прошёл довольно спокойно.{w} Пару раз в поисках места к столу подходили было незнакомые пионеры, но встретив мой взгляд, благоразумно ретировались подальше."
            "Залпом проглотив компот, я поспешно встал из-за стола и, пока меня никто не успел перехватить, выскочил вон из столовой."
            "Очень хотелось поскорее добраться до домика и наконец-то заняться «<книгой_что-то_там_про_Генду>»."
            $ uvao_D4_concert = False

    stop ambience fadeout 5
    window hide

    return