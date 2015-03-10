label alt_uvao_D5_bunker:
    $ routetag = "uv"
    $ alt_chapter(5, u"Юля. Бункер")
    $ persistent.sprite_time = "day"
    $ day_time()
    
    #Flags
    $ alt_uvao_D5_hentai = False # Хентай7
    $ alt_uvao_D5_sleep = False # Сон, выход на Шурика
    $ alt_uvao_true = False # Будем считать, что мы любим кошкодевочку. Всё-равно текста нет на другую ветку, пока.
    
    scene bg int_catacombs_door
    play music music_list["orchid"] fadein 5 # Вообще его вставить надо по приходу в бункер \ лагерь. Мы же тут первый раз. Страх, все дела.
    
    me "Ого, мощно сделано. Интересно, что там, за этой дверью?"
    uv "Не знаю. У меня не получалось открыть."
    "Я попробовал повернуть колесо, но - увы, сил не хватало."
    "Немного пошаря глазами по сторонам я нашёл какую-то железяку."
    th "Хмм, а что если?…"
    "Подобрав свою находку, я вставил её в колесо."
    me "Дайте мне точку опоры, иииии…"
    "И нихрена. Я надавил ещё сильнее, потом пнул арматурину коленом, надеясь таки сдвинуть заржавевший механизм. Это было опрометчиво."
    me "Уййй!"
    dreamgirl "Сила есть - ум не поможет."
    "При ударе я, похоже, не рассчитал силу, вследствие чего моё правое колено немного взвыло."
    "Однако, я старался этого не показывать."
    me "Попытка номер два."
    "Я вцепился в железяку и повис на ней всем своим весом."
    "Раздался жуткий скрежет, и затвор стронулся с места. Юля от неожиданности отпрыгнула на пару метров и уставилась на дверь."
    show uv surprise at center with dissolve
    uv "Скрипит. Получилось?"
    "Я довернул затвор до конца и потянул. Дверь очень неторопливо провернулась на петлях."
    me "Похоже, что да."
    
    scene bg int_catacombs_living
    show uv normal at center with dspr
    play music music_list["waltz_of_doubts"] fadein 5
    
    "За дверью оказалось убежище, в его классическом виде. Двухъярусная кровать, какие-то приборы - работающие, что удивительно! - шкафчики с какими-то ящиками. Похоже, именно сюда стремился Шурик."
    "Правое колено начинало выть всё сильнее, и я, стараясь не беспокоить его, допрыгал до кровати на левой ноге."
    me "Подожди, давай передохнём. Я, похоже, сильно ногу ушиб, и не смогу идти какое-то время."
    uv "Хорошо, давай."
    "Я решил посмотреть, что с ногой и закатал штанину. На коленке красовалась небольшая ссадина."
    uv "Залижи."
    me "A?"
    uv "Залижи. Я всегда так делаю. Мне очень помогает."
    
    show uv smile at center with dissolve
    
    "Она задрала ногу и продемонстрировала, кося на меня желтым глазом."
    
    "Я усмехнулся. Ну и кошка!"
    dreamgirl "Может она и тебе коленку полижет, вдруг пройдёт?"
    "Шиза была как всегда в своём репертуаре."
    th "Отвали, не до этого сейчас."
    me "Не, мы так не делаем."
    "С некой гордостью сказал я."
    me "Мне бы немного льда. Да только где его тут взять?"
    uv "Вот поэтому зализывать лучше."
    "Но тут с ней не поспоришь. В лагере это не составило бы труда, но в каком-то подземном бункере лёд найти не такая уж и лёгкая задача."
    "Вставать с кровати не хотелось. Слишком рано встал, слишком много беготни по лесам, руинам и туннелям, а также бесед с этим… существом, Юлей."
    "Должно быть, именно так себя чувствует чересчур разогнанный комп во время серьёзных вычислений - мой мозг практически кипел. Я вытянулся на кровати и закрыл глаза."
    "Толчок в плечо."
    uv "Дверь закрой. А то этот, друг твой, нас найдёт."
    me "И не друг он мне вовсе!"
    "Возмутился я."
    "Но в целом - она была права, тут же ещё Шурик шляется где-то. Не хватало ещё что-бы он меня нашёл в подземном бункере с девочкой, которая помимо хорошей фигуры имеет пару кошачьих ушей и хвост."
    "Застонав, я поднялся, допрыгал на одной ноге до двери, закрыл её и свалился на кровать. А теперь - спать! Последнее что я почувствовал - как кто-то теплый подлез мне под руку и улегся рядом…"
    
    show blink
    $ renpy.pause(2, hard=True)
    
    "Проснулся я от ощущения какой-то тяжести на груди."
    "\"Завалило!\" - была первая паническая мысль."
    
    hide blink
    show uv smile close at center with dissolve
    show unblink
    
    "Но нет, это была всего лишь Юля."
    "Она лежала, опираясь локтями мне на грудь, и пристально изучала меня. Какое-то время мы молча смотрели друг на друга."
    uv "Я вчера двоих ваших видела, старших. У речки. Большой, тяжёлый такой, и та, с которой ты живёшь."
    me "Ага… И что они делали?"
    uv "Спаривались."
    "Я вытаращил глаза."
    me "Чего-о?! {w=.4}Ольга Дмитриевна и Саныч?!"
    dreamgirl "Вот это поворот!"
    uv "Ага. Интересно было, я раньше не видела, как это. Непохоже."
    me "На что непохоже?"
    uv "На других зверей. Не как белки. Или мыши. Их тогда легко ловить."
    if alt_uvao_true:
        "Семён как бог меняет тему."
        menu: #Я догадываюсь, что меню тут тоже не нужно, но оставлю на потом
            "Продолжить расспросы":
                $ alt_uvao_D5_sleep = True
                "Ему интересно, идём дальше. Ложный рут. Флаг сна."
                jump alt_uvao_D5_mines_begin
            "Задуматься":
                "Ему не интересно, забил. Идёт в шахты, никого не видит - обед. Нейтрал."
                jump alt_uvao_D5_mines_begin
    else:
        $ alt_uvao_D5_hentai = True
        jump alt_uvao_D5_hentai_scene

#Хентай. После-хентайная развилка спать \ не спать тоже тут.
label alt_uvao_D5_hentai_scene:
    me "Как же они это делали?"
    uv "Ну вот так. Сначала просто сидели."
    
    "Она взяла мои руки и положила себе на спину. Опа, а куда это ее платье подевалось?"
    uv "Потом вот так."
    "Она прижалась носом к моему носу. Наверное, это должно означать поцелуй."
    uv "Потом вот."
    "Чуть повернулась боком, и прижала мою ладонь к своей груди."
    dreamgirl "Чувааааак? Кажется, нам дадут!"
    th "Но она же… не человек?"
    dreamgirl "Сиська вполне человеческая. И, кстати, совсем не маленькая. Да и все остальное, кроме хвоста и ушей - тоже."
    th "Да я не об этом! Если б такое устроила обычная девушка - все ясно на сто процентов. А вот что у нее в голове происходит… я ж вам не какой-нибудь контактер-уфолог!"
    dreamgirl "И разделась она просто так, ага. Поверь мне, если ее перестанет устраивать происходящее, тебе об этом сообщат. В виде огромных царапин на всю щёку. Ну или пощёчину влепит, если ей хоть немного понравилось."
    uv "А потом уже вот так!"
    "Она вскочила на четвереньки и повернулась ко мне, при этом хитро поглядывая через плечо, на манер избушки, так сказать. К стене передом, к Семёну задом."
    dreamgirl "Ну, убедился?"
    "Юлин хвост изогнулся эдаким приглашающим знаком вопроса. Не дождавшись от меня какой-нибудь реакции, она потопталась коленями и вопросительно наклонила голову."
    uv "М-рррр?"
    dreamgirl "Перевожу: Ну и долго тупить будем? Барышня готова и ждёт своего кавалера."
    "Нет смысла противиться неизбежному. Не то чтоб происходящее оставило меня равнодушным, совсем наоборот, но… Блин, это же бред какой-то! Или эротический сон."
    dreamgirl "Если сон, то тем более нечего тормозить. Короче, ты меня достал!"
    
    play music music_list["i_dont_blame_you"]
    scene bg black with fade2
    
    "Меня подняло с кровати каким-то внезапным импульсом - должно быть, это тот самый пресловутый \"Внутренний пендель\"."
    "Только сейчас я обнаружил, что и рубашка давно расстёгнута, и я лежу с полностью голым торсом."
    dreamgirl "А времени она зря не теряла. Поспал бы ты ещё полчасика - на тебе бы и шорт не осталось."
    "Руки сами собой легли на её талию, притянули к себе."
    uv "Мрррррра-а-у-у-у!"
    "Oдобрительно протянула она и соблазнительно прогнулась."
    th "Будь я котом, я бы просто взял её зубами за шкирку и хардкорно отымел…"
    dreamgirl "Как будто что-то плохое. Да и она вряд ли будет против."
    th "Цыц. Я пытаюсь не посрамить гордое звание Гомо Сапиенса в первом контакте с иной расой!"
    "Вместо этого, я наклонился и прикоснулся губами чуть выше копчика. Хвост немедля обвил мне шею, будто какой-то пушистый удав, и затрепетал кончиком у меня на груди."
    "Дальше - цепочка поцелуев вдоль позвоночника, руки, облапившие грудь… Когда я дошёл до места между лопаток…"
    uv "Мррра-а-а-у-у-а-а-у-у!"
    "Она немного приподнялась сзади и прижалась своими ягодицами ко мне."
    dreamgirl "Это означает: Ну не тяни уже! Ваш К.О. всегда рад помочь."
    "Желание девочки - закон. А уж кошкодевочки… Я в единый миг освободился от всего, что мешало мне ниже пояса, и, прицелившись…"
    dreamgirl "На ладонь ниже хвоста. Не промахнись, Ястребиный Глаз."
    uv "Мааааауууу…"
    "…единым махом скользнул внутрь."
    "Она со вздохом качнулась сначала от меня, потом обратно… И снова… И снова, вовлекая меня в движения."
    "Старая железная конструкция душераздирающе скрипела и качалась. Оставалось надеяться, что проектировщики заложили приличный запас прочности, и эта бандура не обрушится нам на головы. Впрочем, нас это мало беспокоило - мы как раз нашли подходящий ритм, и не собирались останавливаться несмотря ни на что!"
    "Юля с каждым движением старалась выгнуться все сильнее, её кошачьи стоны заглушали скрип, а я… Я так увлёкся ролью \"кота\", что стал даже подпевать ей. Кажется, мы движемся к финалу…"
    "Хвост её по-прежнему обвивался вокруг меня, щекоча и вздрагивая. Я прижал его рукой к животу, и тон её \"песен\" внезапно повысился на октаву, вместе с громкостью. Ого! Вот это находка!"
    "Я не преминул воспользоваться новым знанием эрогенных зон кошкодевочек - обхватил ладонью хвост у основания и несильно, но властно потянул к себе. Кошечка прогнулась совершенно невероятным образом, и натурально взвыла, продолжая насаживаться на меня."
    uv "А-а-а-а-х."
    "Это стало первым камешком лавины, и я совершенно потерял самоконтроль. Несколько секунд - или минут? - безумных телодвижений под дикие животные вопли, и мы оба, тяжело дыша, мокрые от пота и прочих жидкостей, повалились обратно на кровать."
    
    scene bg int_catacombs_living with fade2
    show uv smile close at center with dissolve
    
    uv "Мррррр… Да, примерно вот так и они тоже."
    "Тяжело дыша сказала она, устраиваясь головой на моём плече."
    me "Они? Кто?"
    "Мозг напрочь отказывался работать."
    uv "Тот большой и вожатая. Только у неё хвоста нет. Жалко ее. С хвостом лучше."
    "Я представил Ольгу Дмитриевну с пушистым кошачьим хвостом, торчащим из-под юбки, и фыркнул. А если ещё уши, да панаму сверху… Не удержавшись, я захихикал совершенно по-дурацки."
    uv "Ты что?"
    "Удивлённо подняла голову Юля."
    me "Представил ее с хвостом и ушами."
    uv "Ааа. Тогда ладно."
    "Она взяла мою ладонь и положила себе на голову. Негласно намекая - гладь давай, не отвлекайся!"
    
    hide uv with dissolve
    
    "Так мы и лежали, я - почесывая ей между ушами, она - уткнувшись мне в плечо и посапывая."
    dreamgirl "Поздравляю вас, многоуважаемый коллега!"
    stop music fadeout 3
    "С Шизой говорить желания не было, однако она не оставляла попытки докопаться до меня."
    dreamgirl "Видел бы ты себя со стороны, кошачий угодник."
    menu:
        "Проигнорировать":
            $ alt_uvao_D5_sleep = True
            "Шиза всё-ещё старалась привлечь моё внимание, однако ни сил, ни желания разговаривать с ней не было, и я, сам этого не замечая, провалился в сон."
            
            show blink
            $ renpy.pause(2, hard=True)
            hide blink
            
            #Тут должен быть сон с кошками, как я понял. Но как-нибудь после правок.
            
            scene bg int_catacombs_living
            show unblink
            
            "Проснулся, я, скорее всего, ближе к обеду."
            "На мне всё в такой же позе лежала Юля, тихо посапывая. Даже моя рука, которая была у неё в волосах, осталась, кажется, в той же позиции, что и перед сном."
            th "Наверное, вот оно какое, это счастье. Просыпаться с красивой девочкой. И не важно где, важно лишь с кем."
            dreamgirl "Угомонись, мечтатель. Конечно это не отменяет того факта, что вы несколько часов назад вытворяли тут \"Хау-ау\", но, чувак, у неё есть кое что, чего ты не в одной девушке не найдёшь."
            th "Её глаза?"
            "Мозг выдал первое что пришло в голову."
            dreamgirl "Какие глаза, придурок! У неё половина тела кошачья, тебя это вообще не смущает?"
            th "Ну может совсем чу-чуть."
            "Полюбовавшись своей кошечкой ещё минут пять - я решил что пора вставать."
            "Правой рукой я потормошил макушку Юле и немножко почесал за ушками."
            "Результат не заставил себя долго ждать и она тотчас же проснулась."
            
            show uv smile close at center with dissolve
            
            uv "Приве-е-т."
            "Радостно потянувшись сказала она, только вот она наверное забыла, что…"
            
            show uv guilty close at center with dspr
            
            uv "Ай… {w}Больно."
            "Ударившись о спинку кровати сверху, она резко плюхнулась обратно."
            "Почесав макушку с недовольным личиком она уставилась на меня."
            uv "Что?"
            "В ответ я лишь звонко рассмеялся."
            uv "Больно же, чего ты смеёшься?"
            "В её голосе были слышны нотки недовольства, однако после этой фразочки она и сама пару раз хихикнула."
            
            show uv smile close at center with dspr
            
        "Побеседовать с Шизой":
            "Судя по монотонному сопению девушки, та явно уснула. Все-таки есть в ней что-то человеческое…"
            "Ко мне же сон не шел. Мысли ураганом носились в моей голове."
            th "Чёрт, нехорошо как-то получилось. Развёл девушку…"
            dreamgirl "Развёл? Серьёзно? А не она тебя?"
            th "Ну она-то да… Но ты прекрасно понимаешь, что я имел в виду."
            dreamgirl "Опомнился, гусар. Раньше надо было думать."
            th "И все же, было в этом что-то неправильное."
            dreamgirl "Конечно, не мне тебя воспитывать, но стоит лишь взглянуть на её уши и хвост… В общем, зоофилией попахивает, дорогой."
            th "А кто подстрекал-то?"
            dreamgirl "Я всего-навсего голос в твоей голове. Не я же тут устроил порнографию и кошачьи ласки?"
            th "Заткнись, пожалуйста. И без тебя вопросов хватает."
            dreamgirl "Пф-ф. Больно надо общаться с зоофилами."
            "Скосив глаза, я присмотрелся к голове, лежащей у меня на плече. Уши как уши, обычные кошачьи. Вот только растут из человека… И хвост. Я прикрыл глаза, вспоминая недавние события. Хвост не выглядел как-то фальшиво. Вполне ощущался руками как обычный кошачий хвост."
            "Чтобы ещё раз в этом убедиться, я легонько потрогал её хвост, пока она спала."
            "Кто она вообще? Как такое возможно?"
            dreamgirl "Ну ко{w=.4}-неч{w=.4}-но, самое время! А ДО ты спросить не мог, неукротимый ты наш?"
            th "Отстань, я сказал."
            dreamgirl "Я-то отстану. Но если вдруг через 9 месяцев окрестные леса заполонят похожие на тебя котята… Мы оба будем знать, кто из нас виноват."
            th "Да чтоб тебя! Ты вообще на чьей стороне, скотина?"
            dreamgirl "Я твой внутренний голос, говорю же. Я озвучиваю твои потаённые желания и мысли, иногда подрабатываю совестью на полставки. И вот сейчас тебе позарез требуется потерзаться!"
            th "Мне?!"
            dreamgirl "Ну не мне же. Я тут сижу и угораю, глядя на происходящее. Зацени - встретил кошкодевочку, приманил плюшками, завёл в бомбоубежище и отодрал так, что шерсть дыбом. Одно слово - педозоофил!"
            "Не найдя слов для достойного ответа, я решил этот выпад проигнорировать."
            "В чем-то он прав, мой внутренний голос. Я всего лишь собирался разобраться, что за чертовщина происходит в этом лагере, выспросить у этой Юли все, что она знает, а дальше… дальше по обстоятельствам."
            "А вместо этого - поддался животным инстинктам!"
            dreamgirl "Девочка, девочка! А пойдём со мной в подвал! Я тебе там конфет дам!"
            "Шиза считала за должное поиздеваться надо мной, но я уже не слушал её, а лежал, просто наслаждаясь моментом."
            "Юля по-прежнему сопела, лёжа на моем уже затёкшем плече. Без одежды было неуютно, но встать я не мог. Кто знает, как она отреагирует на внезапное пробуждение?"
            "Я взглянул на нее."
            "Каштановые волосы были немного растрёпаны, ушки то и дело подрагивали, а хвост ходил из стороны в сторону. Ей явно что-то снилось."
            "А что ей может сниться? Охота на мышей или…"
            "Перед глазами вновь пронеслось наше действо, как раз в этот момент Юля замычала и сморщила носик. От удовольствия или от боли я не знаю, но хотелось верить что от первого."
            "Она заворочалась и я, изловчившись, вытащил руку из под её головы."
            "Стараясь не шуметь, я начал одеваться, изредка поглядывая на обнажённое спящее тело девушки."
            "Я опомнился не сразу, уже с полминуты наблюдая, как она мило дёргает ушками, как спящий котёнок, гоняющийся во сне за мышкой. Нога её изменила положение, обнажив пикантные места…"
            dreamgirl "Хороша, чертовка…"
            "И ведь не поспоришь."
            "Из-за двери донёсся какой-то шорох."
            "Я так и застыл, стоя на одной ноге, вдевая вторую в шорты."
            "Шорохи был непродолжительными, будто шаги, однако вскоре они затихли, но затем в дверь ударили."
            "Кошачье ушко дёрнулось и повернулось в сторону шума, у меня же в висках застучала кровь с такой силой, что мне даже показалось, будто кто-то продолжает барабанить в дверь бункера."
            
            show uv surprise close at center with dissolve
            
            "Юля открыла один глаз, обвела взглядом комнату, полуодетого меня, взглянула на железную дверь, откуда секунду назад доносились шорохи щебёнки. Она открыла второй глаз и потянулась."
            "Мне показалось, будто за дверью нас прекрасно слышали."
            "Я тут же жестами начал всячески призывать Юлю к тишине, но она, потупив взгляд, зевнула, обнажив слегка заострённые клыки."
            "За дверью снова начали доноситься шорохи, Юлины зрачки сузились, а хвост тут же вытянулся по струнке."
            "Шорохи удалялись."
            "Я выдохнул с облегчением."
            uv "Человек. Ушёл…"
            
            show uv normal close at center with dissolve
            
            "Она тут же упала на кровать, снова потянувшись. Я снова напряжённо вдохнул, так как кровать громко скрипнула, но шорохов слышно не было, и я успокоился."
            "Шорты были уже застёгнуты, я потянулся к рубашке, на которой устроилась Юля. Она смотрела, не мигая на меня, её хвост ходил туда-сюда."
    "Мне даже показалось, будто она смотрит на меня как на добычу."
    me "Позволь…"
    "Юля хмыкнула и села. Она прижала руки к обнажённой груди…"
    dreamgirl "Хэй, гусар-зоофил, поаккуратнее…"
    "Я только сейчас понял, что я пытаюсь почти вслепую завязать себе галстук, ибо мой взгляд не отходил от её груди ни на секунду."
    "Выдав себе мысленного леща, я всё-же отвернулся и попытался завязать, наконец, этот грёбаный пионерский галстук."
    "Юля хихикнула, наблюдая, как я в третий раз повязываю галстук и снова неудачно."
    uv "Не понимаю, зачем вам эта красная повязка? Ужасно неудобно."
    me "Сам не понимаю. Такой у нас строгий дресс-код."
    uv "Без одежды значительно удобней…"
    uv "Только ветки больно царапаются, и зимой холодно…"
    "Юля тоже стала натягивать свою нехитрую одёжку."
    me "Ты сказала человек. Ну, шуршал за дверью."
    uv "Ага. Наверное, тот самый… В очках."
    me "И как нам выбраться, чтобы он нас не заметил?"
    uv "Вот ещё дверь."
    "Юля ткнула пальчиком в сторону ещё одной железной двери."
    uv "Только она тоже не открывается."
    me "А куда она ведёт?"
    uv "В какой-то туннель… А там спуск в шахту, где я ловлю мышей."
    uv "Я была с другой стороны, но открыть так и не смогла."
    
    show uv smile close at center with dspr
    
    "Она игриво облизала губы и улыбнулась."
    "Мышей… Нелегко бедной девочке."
    me "Надо успеть до обеда. Не хотелось бы попасть под разнос от вожатой."
    uv "Так туннель ведёт под площадь. Я часто там бывала, когда бегала за едой."
    dreamgirl "Созналась, воровка. Пришло время её наказать, жестоко наказать, товарищ следователь."
    th "Оставь свои пошлые намёки. Да и к тому же - наказал уже."
    dreamgirl "Фи, какие мы серьёзные."
    me "Хм, как же её открыть?"
    "Я оглядел бункер, но ничего способного мне помочь, не нашёл."
    uv "Может, выйдем через эту дверь? Туннель я знаю как свои четыре лапки."
    me "Ну, ладно. Пошли."
    "Я подошёл к двери, не без труда повернул колесо и, навалившись всем весом, открыл её. Юля проворно выбралась за мной. Я закрыл дверь за собой и попробовал повернуть колесо, но то повернулось лишь на несколько градусов и его тут же заело."
    "Плюнув на бессмысленное занятие, я отряхнул ладони от ржавчины и поправил так и не повязанный галстук."
    "Нога уже немного отошла, хоть и ныла периодически. Тем не менее, я был в состоянии продолжать путь на своих двоих."
            
    jump alt_uvao_D5_mines_begin

#Сама шахта, начиная от похода к ней.
label alt_uvao_D5_mines_begin:
    scene bg int_catacombs_entrance
    show uv smile at center with dspr
    
    me "Ну-с, куда теперь?"
    "Юля с любопытством оглядела туннель и ткнула своим пальчиком в черноту."
    uv "Туда."
    "Ничего не оставалось, кроме как следовать за моим проводником."
    "На мгновение Юля пропала из виду."
    
    scene bg int_catacombs_hole
    play ambience ambience_catacombs fadein 3
    
    uv "Сюда."
    "Её голос донёсся откуда-то снизу. Передо мной возникла дыра, ведущая куда-то вниз. Какая-то шахта."
    uv "Здесь темно. Давай лапу."
    me "Руку."
    uv "А?"
    me "Мы зовём это рукой."
    uv "Как пожелаешь. Давай сюда, свою эту, руку."
    
    scene bg int_mine 
    show uv normal at center with dspr
    
    "Я скатился по насыпи в шахту и, отряхнув шорты, протянул руку в зияющую черноту. Нежные пальцы обвили мою ладонь и медленно потащили за собой."
    "Под ноги подворачивались камни и шпалы, я то и дело спотыкался, но Юля, будто не обращая внимания, вела меня дальше. Мы шли в тишине, и лишь изредка Юля останавливалась, громко говоря:"
    
    scene bg int_mine_crossroad with fade
    show uv normal at center with dspr
    
    uv "Направо."
    
    scene bg int_mine_crossroad with fade
    show uv normal at center with dspr
    
    uv "Налево."
    "Она видимо определялась, куда повернуть на развилке. Её голос эхом разносился по шахте и я беспокоился, слышит ли нас Шурик."
    
    scene bg int_mine_crossroad with fade
    show uv normal at center with dspr
    
    if alt_uvao_D5_sleep:
        uv "Кажется, не далеко от нас кто-то есть."
        uv "Пошли налево."
        "Я догадывался кто это может быть, и уже с неким интересном шел рядом с ней."
        uv "Стой!"

        "Я кого-то вижу в темноте, это Шурик."
        "Нужен хелп по тексту"
        jump alt_uvao_D5_mines_sh
    else:
        uv "Направо."
        "Я покорно следовал за моим всевидящим спутником. Да и что мне оставалось, в темноте я всё-равно ничего не вижу."
        "Кроме своих указаний, в какую сторону идти, она ничего не говорила. Да и мне не очень то и хотелось начинать разговор, так что я просто плёлся, держась за её руку."

        jump alt_uvao_D5_mines_dinner
    

label alt_uvao_D5_mines_sh:
    scene bg int_mine_coalface with dspr
    show uv normal at center with dspr

    "В темноте видит шурика. Дописать \ Написать"
    return
    
    
label alt_uvao_D5_mines_dinner:
    scene bg int_mine_door
    show uv normal at center with dspr
    
    uv "Пришли."
    "Она отпустила мою руку. Раздался скрип деревянной двери."
    uv "Сюда."
    
    #Надо добавить больше описания. У нас фоны каждую 3ую фразу сменяются. Это не считая право-лево.
    scene bg int_mine_room
    show uv normal at center with dspr
    
    "Под ногу подвернулась бутылка, и я мешком упал на пол."
    me "Ч-черт!"
    "В помещении проникало немного света и я, привыкший к темноте, разглядел обстановку. Изрисованные стены, бутылки, мусор по углам, Юля, смотрящая на меня своими светящимися глазами."
    uv "Дальше наверх, только там замок."
    "Я тут же подобрал лежащую рядом арматуру."
    me "Может этим?"
    uv "Не стоит." 
    uv "Я тут недавно кое-что нашла."
    "Она держала в руке какой-то ключик."
    "Юля осмотрела комнату, нырнула за большую трубу, покопошилась немного и вынырнула прямо под свет. Она забралась по лестнице к решётке в потолке, немного поковыряла в замке и спустилась вниз."
    
    scene bg int_mine_exit
    show uv normal close at center with dspr
    
    uv "Вот. Закрой замок за собой и брось ключ мне. Не хочу, чтобы ваши лазали сюда."
    "Я кивнул и взял из протянутой руки ключик."
    me "Эм-м… Спасибо."
    
    show uv smile close at center with dspr
    
    "Юля улыбнулась и ответила:"
    uv "Принесёшь ещё булочек? Я буду ждать."
    "Я кивнул ей и полез наверх."
    "Поворот ключа и уже старый ржавый замок вновь защищал лаз от посторонних. Я просунул ключик между прутьями решётки и бросил его вниз, после чего выпрямился и огляделся. Обед должен был начаться с минуты на минуту."
    
    scene bg ext_square_day with flash
    play ambience ambience_camp_entrance_day fadein 5
    
    "Солнце было ярким и мне пришлось сперва привыкнуть к свету. Когда мои глаза стали различать окружающие площадь деревья, я поднялся на ноги, держась за пыльный постамент, на котором стоял загадочный Генда. Он все так же надменно следил за происходящим на площади."
    un "Где ты был?"
    
    show un normal pioneer far at center with dissolve
    
    "От неожиданности я подпрыгнул."
    "Лена сидела на лавочке, неподалёку от того места, откуда я только что вылез."
    dreamgirl "Бегал… по шахтам… с девочкой-кошкой. Так ей и скажи."
    me "А, это ты. Ну, я…"
    un "Тебя вожатая искала."
    "Она старалась не смотреть на меня, и крепко обнимала книжку, будто надеясь, что та укроет её от моего бескрайнего сумасшествия."
    un "Почему ты такой грязный?"
    "Она бегло обвела меня взглядом и снова повторила вопрос:"
    un "Где ты был?"
    me "Я… Ну, это…"
    
    play music eat_horn fadein 3 
    
    "В голове уже пролетели тысячи отмазок как вдруг меня спас сигнал на обед."
    "Фух, пронесло."
    dreamgirl "Вышло, значит, господин гусар, и рыбку съесть, и на кошечку залезть."
    me "Обед уже. Давай поторопимся."
    "Я старался придать голосу небрежность, но как мне показалось, получилось не особо удачно. Оставив недоумевающую Лену на площади, я побежал в столовую, попутно отряхивая пыльные шорты и рубашку."

    "Джамп на столовую, если я не ошибаюсь"
    
    return
    
