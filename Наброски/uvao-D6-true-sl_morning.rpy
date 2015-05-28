# Д6 - завтрак со Славей
#
# используется флаг встречи со Славей на пляже alt_uvao_D5_evening_sl
# устанавливает флаг завтрака со Славей в Д6 alt_uvao_D6_morning_sl
#
label alt_day6_true_sl_morning:
# Умывальники или кран, день. льющаяся вода, всё по шаблону
    "От умывания привычно ледяной водой в голове немного прояснилось, и я начал хоть что-то соображать."
    "В частности, обнаружил, что полотенца я с собой не захватил."
    "Утёршись кое-как ладонью, я потряс головой, выгоняя из неё остатки сонного тумана, и принялся соображать, что делать дальше."
# Умывальники, день
    "С одной стороны, время уже приближалось к полудню, а Виола велела зайти к ней в медпункт прямо с утра, так что чем позже я приду, тем тем сильнее она рассердится - если вообще станет меня дожидаться."
    "С другой стороны, есть хотелось страшно.{w} Даже нет, не есть - {b}жрать{/b}."
    th "Хотя вряд ли мне сейчас светит что-нибудь в столовой. То самое время, когда время завтрака давно уже миновало, а обед ещё и не думал начинаться..."
    dreamgirl "Вообще-то у Виолы вполне может найтись что-нибудь съестное. Она женщина самостоятельная, в медпункте проводит много времени - не может быть, чтобы у неё хотя бы чаем разжиться нельзя было."
    dreamgirl "А где есть чай, там и к чаю наверняка что-нибудь найдётся."
    "Идея показалась мне вполне резонной, и я потопал к медпункту."
    "Впрочем, вскоре выяснилось, что проснулся я явно не до конца и умудрился пропустить поворот к медпункту."
# площадь, день
    "Спохватился я только когда передо мной замаячила спина Генды."
    "Чертыхнувшись, я развернулся было в обратную сторону, как вдруг меня окликнул знакомый голос:"
    sl "Семён! Семён!"
    show sl normal pioneer far at left with dissolve
    "Подбежав ко мне, она выпалила:"
    show sl smile pioneer at cleft with dissolve
    sl "Доброе утро, Семён!"
    me "Доброе утро..."
    show sl normal pioneer with dissolve
    "Кажется, приветствие получилось не слишком любезным, так что я поспешил улыбнуться и добавил:"
    me "Рад тебя видеть!"
    show sl happy pioneer with dissolve
    "Простая светская любезность произвела на Славю прямо-таки волшебное действие - она буквально расцвела от радости, только что в ладоши не захлопала."
    th "Что это с ней? Можно подумать, мы год не виделись. Вчера она меня гораздо спокойнее приветствовала."
    if alt_uvao_D5_evening_sl:
        th "Впрочем, вчера вечером она тоже какая-то странная была."
    show sl smile pioneer with dissolve
    sl "Семен, а где ты был-то всё утро? Тебя и на зарядке не было, и на линейке, и на завтраке!"
    me "Да я..."
    "Я замялся, не зная, признаваться ли мне в том, что я проспал, или соврать что-нибудь правдоподобное, но Славя не стала дожидаться ответа."
    sl "Ой, так ты же голодный, наверное, раз на завтраке не был?"
    me "Ну, да, если честно."
    show sl laugh pioneer with dissolve
    sl "Так пойдём, я тебя покормлю!"
    "Схватив за руку, она потащила меня за собой в сторону столовой."
    hide sl with dissolve
    "С трудом поспевая за девочкой, я подумал:"
    th "Кажется, не судьба мне сегодня позавтракать с Виолой. Впрочем, лучше синица в руке, чем журавль в небе.{w} Тем более, в исполнении Слави синица наверняка окажется размером с курицу, не меньше."
    if alt_uvao_D5_evening_sl:
        th "Заодно попробую узнать, что происходит с нашей активисткой. То она на пляже плачет, то при виде меня от радости прыгает. Странно всё это."
        dreamgirl "Ты только смотри, осторожнее! Вдруг она психическая!"
        th "Ну конечно! Мне, как человеку с собственной карманной шизой, это очень-очень страшно."
        "Голос самодовольно хмыкнул, но тем и ограничился."
# столовая изнутри, день
    "Испытывая лёгкое ощущение дежавю, я, как и в самый первый свой день здесь, уселся за столик возле раздачи, а Славя ушла на кухню."
    "Не было её довольно долго. Я уже начал сомневаться, не лучше ли было мне пойти всё-таки сразу медпункт, как я и собирался сначала, но тут она появилась, нагруженная подносом и солидных размеров общепитовским чайником."
    show sl serious pioneer far at right with dissolve
    "Судя по её недовольному раскрасневшемуся лицу, еду пришлось добывать с боем, но, подойдя к столику, Славя снова разулыбалась."
    show sl smile pioneer at cright with dissolve
    "Я помог поставить поднос на стол, за ним последовал чайник."
    show sl smile pioneer close with dissolve
    "Славя уселась напротив, а я произвёл краткую ревизию добычи. Хлеб, масло, остывший перестоявшийся чай и, почему-то, изрядных размеров кусок варёной говядины."
    "Поймав мой недоумённый взгляд, Славя пояснила:"
    sl "Это мясо предназначалось для супа. Ну, осталось немножко. Будешь есть?"
    me "Буду!"
    "Несколько минут я был совершенно некоммуникабелен. Оценив весь размах моего сражения с пищей, Славя не стала отвлекать меня разговорами, а с лёгкой улыбкой молча наблюдала, подперев кулаком подбородок, как я ем."
    "Ожесточённо пережёвывая мясо, я снова подумал, что ситуация "

# //Пересечься со Славей во имя жратвы
# //Перекус, общение, предложение пообедать вместе
# Chess:  Славя кормит в пустой столовой, осторожно пытается Семёна разговорить, усиленно демонстрирует свой интерес к нему.
    # Умывание ледяной водой несколько проясняет мысли, начинаем соображать, что делать дальше.
    # С одной стороны, Виола ждёт, с другой - очень уж жрать охота.
    # Еду всё равно взять негде, влечёмся в строну медпункта. Проходя мимо площади, замечаем Славю.
    # Голос желудка побеждает чувство долга (если был пляж - думаем, что заодно можно будет попытаться что-то понять, хотя нам и ссыкотно немного. (Шиза:"Вдруг она психическая?"))
    # Славя прямо-таки радостно вызывается покормить и тащит в столовую. Даём сравнение с вечером Д1 - как-то она подозрительно себя ведёт. Или просто кажется?
    # Прибываем в столовую. Славя притаскивает хлеб с маслом, кусок варёной говядины ("Это мясо предназначалось для супа. Вот, немного... хм... осталось") и напрочь остывший перестоявшийся чай.
    # Жрём всё подряд.
    # if alt_uvao_D5_evening_sl:
        # Сквозь еду пытаемся завести разговор про вчерашний пляж.
    # else
        # Славя заговаривает сама, частично повторяя инфу из вчерашнего пляжа.
        # Недоумеваем и пытаемся узнать, к чему этот разговор.
    # Славя мнётся и уходит от разговора - "Долгий разговор... Давай лучше пообедаем вместе, а там видно будет".
    # Благодарим Славю. Разбегаемся.
    $ alt_uvao_D6_morning_sl = True
    jump alt_day6_true_CS_talk_short
