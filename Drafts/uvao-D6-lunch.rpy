# Бегуну
# Ветка обеда со славей, адаптируй в свой файл, этот можешь удалить

# Обед
label alt_day6_uvao_lunch:
    window hide
    scene bg ext_dining_hall_near_day with dissolve
    window show
    "Около столовой уже стояла толпа, которая пыталась пробиться внутрь."
    window hide
    scene bg int_dining_hall_people_day with dissolve
    play music music_list["so_good_to_be_careless"] fadein 4
    play ambience ambience_dining_hall_full fadein 4
    window show
    "Конечно же на раздаче уже стоит очередь из голодающих пионеров. И почему я всегда прихожу в столовую последним?"
    dreamgirl "Дай угадаю… Может это потому что ты тормоз?"
    # Тут где-то должен быть выбор на Алису \ Славю, и в соответствии с этим надо чутка переписать этот кусок, либо сделать выбор Сесть с Алисой \ Сесть одному(Где потом подходит к нам Славя). -R
    # Ниже ветка Слави
    th "Очередная шпилька от Шизы. Мой внутренний голос - мастер оскорблений меня любимого…"
    "С подносом в руках, шаг за шагом я продвигался к раздаче и думал о том, чем сегодня будут кормить мой растущий организм. Так, молочный суп – неплохо. Макароны по флотски – обожаю! Ну и традиционный компот. Жить можно."
    "Высмотрев свободный стол в углу, я направился к нему. Может хоть сегодня удастся поесть в одиночестве и спокойно."  
    "Может и прав мой внутренний собеседник. Сколько себя помню, я везде и всегда был в последних рядах. Где-то действительно сказывалась моя нерасторопность, а где-то просто желание, по возможности, избежать человеческого общества."
    dreamgirl "Да ты не обижайся, я же помочь хочу."
    th "Интересно как?"
    dreamgirl "Вытащить  тебя надо из этого состояния вечной заторможенности. Я пытаюсь тебя растормошить."
    th "Не в обиду, но таким способом у тебя ничего не выйдет. Если человеку всё время говорить, что он свинья, то он и в самом деле захрюкает."
    dreamgirl "Можешь не верить, но я в самом деле хочу помочь. В конце концов – ты это я."
    "Сочувствие у Шизы? У моего вечного внутреннего циника и скептика?"
    dreamgirl "Да, и возможно наше с тобой плодотворное общение уже даёт свои плоды. Ты уже не так шарахаешься от людей. Девочки тебя вниманием не обделяют. Да ещё и какие! Кстати, посмотри-ка кто к нам идёт."
    show sl smile pioneer at center with dissolve
    "Я поднял голову и увидел Славю, тоже с подносом, подходившую к моему столу."
    sl "Не занято?"
    me "Нет, садись конечно."
    show sl normal pioneer close at center with dissolve
    "Славя поставила поднос с едой на стол и села напротив."
    me "Приятного аппетита!"
    "Совершенно искренне пожелал я."
    show sl smile2 pioneer close at center with dspr
    sl "Спасибо, Сеня."
    "Ответила она и улыбнулась своей сногсшибательной улыбкой."
    sl "Тебе тоже."
    "От всех этих хозяйственных работ у меня разыгрался жуткий аппетит. Я накинулся было на еду, но тут же спохватился. Всё же девочка рядом, которая в отличие от меня, ест очень аккуратно."
    "Подумает ещё, что я свинтус какой - с обеими лапами в кормушке. Хотя за столько дней ко мне уже все привыкнуть были должны."
    "Славя отложила вилку и задумчиво, как-то по особому смотрела на меня. Также как и в первый день, когда мы впервые коротали вечер за этим же самым столиком…"
    dreamgirl "Не думаю что это совпадение."
    "Куда же без ехидства Шизы? Да ещё случай удобный какой."
    me "Что такое, Славя? У меня снова на носу кефир?"
    show sl laugh pioneer close at center with dspr
    "Славя рассмеялась. Уже не в первый раз мои неловкие шутки заставляют эту девочку веселиться. Кажется ей со мной и правда хорошо. А это может означать только одно."
    dreamgirl "Ну, а что я тебе толкую? Ты изменился и отношение к тебе изменилось"
    show sl smile2 pioneer close at center with dspr
    sl "Слушай, Семён. Мне нужно поговорить с тобой об одном Очень Важном Деле."
    th "Интересно…"
    me "Ну говори, я слушаю."
    sl "Не здесь. И не сейчас. Давай встретимся после концерта."
    th "Ого! А ведь жизнь-то налаживается."
    me "Отлично. Конечно. А ты можешь хотя бы намекнуть, о чём будет этот разговор?"
    sl "Нет. Не могу."
    show sl smile pioneer close at center with dspr
    "Девочка лукаво улыбнулась."
    sl "Это секрет.{w} А если я тебе расскажу заранее, то это уже секретом быть перестанет, правда?"
    "Тут она сделала большие глаза и добавила в голос таинственности."
    sl "Но я повторюсь – Очень Важное Дело. Поэтому никому ни слова."
    me "Хорошо, хорошо."
    "Легко пообещал я."
    "В конце-концов, несколько часов до этого Очень Важного Разговора я переживу как-нибудь."
    sl "Очень хорошо."
    "Славя снова улыбнулась."
    sl "Обещаю, ты не будешь разочарован. Ладно, мне на репетицию пора."
    hide sl with dissolve
    "Ещё раз легонько улыбнувшись мне, она удалилась."
    "У нас закон такой: поел - убери за собой. Поднос с посудой в мойку, меня – на выход."
    jump alt_day6_uvao_mt_house