label alt_day6_uvao_prufung_sl:
    scene bg ext_stage_big_day
    "Ещё издалека со сцены доносилось странное копошение - последние приготовления к концерту были в самом разгаре."
    "Какая-то малышня толпилась у первого ряда разодетая в старые жёлтые костюмы, повидавшими не одну смену. Кажется, изображали они утят."
    "Мимо меня прошагал с крайне озадаченным видом взмыленный Электроник со странной тяжеленной бандуриной в руках, завёрнутой в плотную тряпку."
    th "Он что? Тоже в этом священнодействии собрался участвовать? Или как дармового переносчика тяжестей привлекли?"
    "Проводив его взглядом до самой сцены и прикидывая, что же именно он мог так бережно нести, я наконец увидел то, зачем пришёл сюда."
    scene bg ext_stage_near_clear
    "Славя с явно недовльным видом о чём-то активно спорила с Мику."
    show mi normal voca with dissolve
    show sl angry pioneer with dissolve
    sl "Ты ведь понимаешь, что Ольга Дмитриевна это так не оставит. Делай как знаешь - но я тебя предупредила."
    mi "Славичка, ну дай мне хоть раз за три недели одеться как я хочу!"
    "Недоумённо пригляделся и, наконец, обратил внимание сине-зелёное обтягивающее платье Мику."
    "Конечно для моего времени в нём не будет ничего необычного, но сейчас оно смотрелось явным перебором для местных пуританских нравов."
    mi "Это же специальное, сценическое. Нельзя же выступать как клуша!"
    "Взгляд Мику был очень обиженным - что-то, а свои экстравагантные наряды она, похоже, очень любила."
    "Чувствуя, что этот балаган может быть бесконечным, как и все споры о морали, я всё-таки решил подать голос:"
    me "Славя. Можно тебя?"
    "Лицо блондинки словно просияло. Она в два шага подлетела ко мне и возбуждённо затараторила."
    sl "Ты что-то хотел, Сёмушка?"
    sl "Что-то случилось или тебе что-то нужно? Ты говори скорее."
    me "Славя, я это..."
    sl "Или ты не знаешь где сесть. Я уже нам заняла места - там хорошо видно. Хочешь провожу?"
    dreamgirl "Опять двадцать пять. Заткни её и как можно быстрее."
    dreamgirl "Сил моих нет этих «Сёёёёмушек» слушать."
    "Набрав побольше воздуха в грудь, я медленно произнёс, чеканя каждое слово:"
    me "Славя, прекрати. Нам нужно серьёзно поговорить. Отойдём."
    show sl sad pioneer with dissolve
    "Славя растеряно тряхнула своими длиннющими косами и недоумённо спросила:"
    sl "К-куда?"
    sl "Ты видишь - я же занята сейчас, Сёмушка."
    show sl smile pioneer with dissolve
    "Впрочем, она тут же вернула свою фирменную улыбочку на место."
    sl "Давай после концерта. Ты ведь помнишь про наш разговор?"
    sl "Погуляем потом вместе и поговорим, о чём только захочешь."
    show sl smile2 pioneer with dissolve
    sl "Может и чем-то {i}важным{/i} займёмся..."
    #феффект
    me "Да прекратишь ты, наконец, или нет?!"
    show sl sad pioneer with dissolve
    me "Что сегодня с тобой такое?!"
    "Не дав сказать Славе и слова, я схватил её за руку и приказным тоном рявкнул:"
    me "Пошли, живее."
    show mi laugh voca with dissolve
    mi "Какой нетерпеливый у тебя сегодня кавалер, Славичка."
    me "Мику, у тебя там концерт? Вот и занимайся."
    show mi sad voca with dissolve
    "Я с ненавистью глянул на замолчавшую вдруг японку, от чего та сделала пару шагов назад, развернулся и потащил ничего не понимавшую Славю прочь от сцены."
    dreamgirl "А хорошо ты их уделал. Наконец-то ведёшь себя как мужик, а не половая тряпка!"
    dreamgirl "Встречайте - впервые на арене: типичный альфач, Семён «буйный психопат» Персунов."
    "В этой ситуации только этой проклятой шизофрении и могло быть весело."
    scene bg ext_stage_big_day
    "Когда мы отошли уже на почтительное расстояние от сцены активисточка вырвала руку и взволнованно прервала молчание:"
    sl "Что происходит, Сёмушка?! Куда ты меня тащишь?!"
    sl "Да объясни ты хоть что-то уже!"
    me "Нет. Это ты прекрати Славя."
    me "Что это ещё за выходки? Что ты задумала?! Признавайся!"
    "Моё негодование, как снежный ком, сорвалось с вершины и, набирая силу с каждым словом, было способно раздавить любого кто попадётся ему на пути."
    sl "К-какие в-выходки? О чём ты?"
    me "Не прикидывайся! Ты же не собака, чтобы бегать за мной, радостно виляя хвостом. Чего тебе от меня нужно?"
    sl "К-каким хвостом?"
    me "А как мне всё это понимать по твоему? Или ты сбрендила?"
    me "Чего это ты плакала вчера на пляже, а потом стала туман наводить своими вопросами?"
    if alt_uvao_true:
        if not alt_uvao_D6_CS_vetrov:
            me "А на кормёжке с чего вдруг такая приветливая была?"
        me "Я уже молчу про все эти недоэротические намёки на пляже про купание голышом."
    me "Ну и главный твой номер, прима балерина. Все эти «Сёёёёмушки» и «важные дела» за обедом."
    me "Не верю я тебе."
    me "Что ты со мной задумала сделать?! Чем я прогневал твоё кардинальское величество?!"
    "Сказать что Славя стояла ошарашенной - значит ничего не сказать. Её всю потряхивало, глаза уставились в пол и чувствовалось, что ещё немного и она будет готова разрыдаться."
    sl "Сёмушка, миленький мой, ты мне очень нравишься. Что мне сделать, чтобы мне поверил?"
    sl "У нас ведь так мало времени осталось. Вот я и решила..."
    "Она не закончила мысль. Было видно, что каждое слово даётся ей с большим трудом."
    th "А вдруг я ошибся?... Может, она и не врёт?"
    "Настала теперь и моя очередь впадать в ступор."
    dreamgirl "Да ты посмотри на неё! У неё же зрачки по пять копеек."
    dreamgirl "Сомневаюсь, что она вообще хоть как-то соображает, что говорит."
    sl "Сёмушка, вчера я поняла, что ты особенный. Что только ты мне и нужен, только с тобой я смогу всё..."
    sl "Но как нам быть вместе, если завтра уже расстанемся? Ты ведь такой замкнутый - сам и не сделаешь первый шаг."
    sl "А я ведь девушка. За что ты так со мной?"
    sl "Я ведь столько для тебя сделала, а ты меня {i}величеством{/i} называешь..."
    "Я стоял и не мог ответить ничего вразумительного, а Славя смотрела на меня умоляющими глазами и всё продолжала:"
    sl "Почему ты меня боишься? Я ведь обычная девушка."
    sl "И у меня тоже есть свои чувства."
    sl "Давай хотя бы попробуем, Сёмушка. Ну пожалуйста."
    #"Славя вдруг заглянула мне прямо в глаза."
    sl "Возьми меня с собой. Я готова ради этого отправиться куда угодно, только бы рядом c тобою быть."
    "Её взгляд был туманным - казалось, что для неё теперь это вопрос жизни и смерти. Не было больше той уверенной в себе паладинши: каждое её действие выражало только бесконечное отчаяние."
    me "Ты... ты это серьёзно?"
    sl "Да, Сёмушка."
         menu:
            "Я верю тебе.":
                th "Кто я такой, чтобы не поверить этому бесконечно светлому созданию? Разве не бывает любви с первого взгляда? Разве не может человек просто решить, что он нашёл нужного: того самого - единственного?"
                th "Кто я такой, чтобы разрушить её мечты и бесконечную веру в меня?"
                th "Быть может и себе стоит признаться наконец, что я с первого дня только и удивляюсь Славе - её искренности, открытости, добросердечности..."
                th "Разве не она первая заставила почувствовать меня снова живым? А ведь помимо прочего она ещё и красивая девушка..."
                th "Что же я за сволочь неблагодарная, когда такой человек предлагает мне свою любовь?.."
                me "Ты... ты мне тоже нравишься Славя."
                me "Прости. Прости, пожалуйста... Я такой олух..."
                me "Столько гадостей о тебе напридумывал, а всё оказалось так просто..."
                me "Мне так неловко перед тобой..."
                "На лице Слави просиял наконец маленький лучик надежды и подарил ей вымученную, но счастливую улыбку. Она встала рядом со мной, слегка приобняла и уткнулась носом мне в плечо."
                sl "Ничего страшного, Сёмушка. Ведь мы теперь вместе?"
                me "Конечно, вместе..."
                me "Но ты ведь даже не знаешь, что я такое. Всё так сложно, непонятно..."
                "Пришло время раскрыть перед этим внезапно ставшим при таких глупых обстоятельствах значимым мне человеком все карты."
                sl "Знаю, Сёмушка. Знаю..."
                "Я почувствовал, как она осторожно погладила меня по волосам и успокаивающе произнесла:"
                sl "Не бойся, я никуда от тебя не сбегу и психом считать не буду."
                sl "Я вчера кое-что узнала. Ты из параллельной реальности и, может, даже из будущего."
                me "Н-но откуда ты..."
                sl "Случайно Виолу и Ольгу подслушала..."
                me "Так ты из-за этого на пляже..."
                sl "Да, Сёмушка. Тогда я всё и поняла..."
                "Она чуть лукаво улыбнулась. Спокойствие постепенно возвращалось к ней."
                me "Но раз ты всё знаешь, то может скажешь как нам теперь быть?"
                me "Хотя я и сам догадываюсь..."
                if alt_uvao_true:
                    "Мне вспомнился утренний разговор с вожатой."
                    th "Она ведь говорила, что всё зависит от меня самого - от того что же именно я хочу. И не имеет значения правильно это или неправильно."
                else:
                    "Мне вспомнился утренний разговор с Виолой."
                    th "Она ведь говорила, что я всё равно отправлюсь домой. Быть может мне стоит просто захотеть этого по-настоящему?"
                sl "Ты особенный, Сёмушка. Тебе, наверное, достаточно будет это пожелать и всё будет исполнено..."
                me "Я сейчас подумал о том же самом, но неужели это всё? Неужели всё так просто?"
                sl "Чем гадать, давай проверим. Я верю в тебя. У нас всё получится."
                "Славя крепко взяла меня за руку и в который раз уже за сегодня посмотрела прямо в глаза - решительно, но в тоже время с надеждой и безграничным доверием." 
                $ set_mode_nvl()
                "Внезапно я ощутил решимость и поддержку, которую и не испытывал по-настоящему уже очень и очень давно - а быть может и вообще никогда." 
                "Мир с самого детства не стремился принять Семёна Персунова с распростёртыми объятьями - не срослось у меня ни с карьерой, ни с мечтой."
                "Я ведь даже не помню точно любил ли кого-то по-настоящему - что значит это чувство в жизни человека, как к нему идут тернистой дорогой другие."
                "Никогда и ни к чему я не пытался подойти серьёзно - боялся всего на свете и бежал от каждого по-настоящему близкого контакта. В моём мирке было место только для меня самого, моей желчи и моего одиночества."
                "Я верил в какие-то идеалы, но не следовал за ними, считая все моральные аспекты уделом глупцов. В начале потух детский огонёк в глазах, а потом опустились и руки."
                "Не сразу, но я научился обходиться без помощи и родителей, а в потом и вовсе старательно абстрагировался от любой попытки влезть в мою жизнь."
                "Но вот теперь, со мной человек, который не боится встать рядом, вытягивая меня из бесконечно глубокой ямы собственного безразличия. Человек, готовый рискнуть разделить со мной все тяготы моего бесцельного существования."
                "Кто знает, может быть у нас есть будущее? Ведь за эти шесть дней так и нашлось более близкой мне души."
                "Я гляжу на неё и вижу солнце, которое может светить для меня долгие и долгие годы. Я делаю это ради неё и ради самого себя."
                "И пусть я не знаю, что случится в дальнейшем. Но раз Славя готова рискнуть всем что имеет, то и я тоже."
                $ set_mode_adv()
                me "Ты готова?"
                sl "Я с тобой готова на всё, Сёмушка."
                "Я закрыл глаза, сильно сжал в объятьях Славю и умоляюще сказал:"
                me "Я не знаю кто ты и как ты меня суда забросил, но здесь мне больше нечего делать."
                me "Забери меня отс..."
                "Я не успел договорить: сверкнула ярчайшая вспышка света и сознание померкло."
                if alt_uvao_D5_hentai:
                    jump alt_uvao_ending_neutral_bad
                else:
                    jump alt_uvao_ending_neutral
            "Зачем ты мне врёшь?":
                me "Меня уже достала эта чушь, Славя!"
                me "Сейчас разве весна? Или ты на всех как мартовская кошка кидаешься? Нет, это не про тебя."
                me "Посмотри на меня: конченый неудачник, который шарахается от любого шороха и бежит от близких контактов с людьми."
                me "Такая как ты ни за что на свете не станет марать честь своего блестящего мундира об это серое и унылое убожество."
                sl "Неправда, ты не такой! Ты хороший!"
                me "Как бы не так, Славя! Я падаль рода человеческого - обычная дешёвка."
                me "Чего тебе от меня надо?! Хватит со мной в игры играть!"
                "Славя стояла с мертвенно-бледным лецом, а по её щекам тонкой струйкой потекли слёзы."
                show sl cry pioneer with dspr
                th "Театр одного актёра продолжается..."
                "У меня не было ни единого основания верить в искренность её чувств."
                "Она немного помялась и, не прекращая рыдать, произнесла:"
                sl "Я не могу без тебя жить, Семён. Ты мне очень нужен."
                me "Опять свою шарманку про любовь заводишь? Надоело, Славя! Давай, что-нибудь пооригинальнее, наконец."
                "Она немного уняла слёзы и тихо ответила:"
                sl "Для дела ты мне нужен..."
                dreamgirl "Ну неужели?! Подсекай её срочно!"
                "Я решил тоже несколько умерить свой пыл и попытался успокоиться - диалог в кои-то веки начал отдавать конструктивом."
                me "Хорошо, Славя. Для какого такого дела?"
                "Было видно как на её руках пробегают мурашки, а саму активисточку заметно потряхивает от волнения, но она всё же продолжила:"
                sl "Я знаю кто ты и откуда, Семён. Но я не знаю кто и откуда я."
                me "Что ты опять несёшь, милая? Как это ты не знаешь кто ты? Что за бред!"
                "От этих слов на её лице горе сменилось искренним раздражением - ещё пара глупых фраз и на меня набросятся с кулаками."
                show sl serious pioneer with dspr
                sl "Послушай меня, пожалуйста, и не перебивай."
                sl "Бред говоришь? Я не помню ничего, что было до этого проклятого лагеря - ясно это тебе?"
                sl "Я вечная помошница нашей ленивой вожатой - девочка-метла, у которой нет ни чувств, не воспоминаний."
                sl "Шурх-шурх, Семён. «Шурх-шурх» - это и есть вся я!"
                sl "А вокруг пустота, понимаешь? Как будто ничего и никогда не существовало. Я даже дома своего родного не помню!"
                me "А я здесь причём, Славя?"
                me "Тебе к доктору нужно. А лучше сразу в дурку. Сходи к Виоле - она-то тебя точно пристроит, куда следует."
                show sl angry pioneer with dspr
                "Славя с неприкрытой злобой сжала кулаки."
                sl "Я же просила не перебивать. Быть может я ничего и не помню, но точно знаю, что клеймо больной на голову мне ни к чему."
                sl "Я хочу делать что-то хорошее в этом мире, Семён - оставить после себя след. Зачем мне отталкивать людей от себя репутацией сумасшедшей дуры?!"
                dreamgirl "Ты посмотри-ка: и впрямь паладинша. И откуда столько идеалов в голову себе запихнула? Сектантша коммунистического покроя, прям."
                me "Так при чём тут я, Славя? Объясни мне наконец."
                sl "Я подслушала вчера разговор Виолы и вожатой о тебе: про попаданцев, про параллельные миры, про будущее."
                sl "И тогда всё встало на свои места. Этот мир, этот лагерь - всё ненастоящее."
                sl "И я ненастоящая!"
                "Она перешла почти на крик и снова заплакала."
                show sl cry pioneer with dspr
                dreamgirl "Без доктора тут не обойтись. Подумала и решила она - смешно."
                dreamgirl "Понять бы ещё что такое настоящее в её глазах."
                sl "Сделай меня настоящей, Сёмушка! Я жить хочу, понимаешь? По-настоящему жить!"
                sl "Ты же особенный! Ты можешь! Это ведь ты меня придумал такой."
                sl "Разве ты сам домой не хочешь? Тебя здесь ничего не держит! Чего тебе стоит просто захотеть?"
                sl "Возьми меня с собой! Дай мне шанс не быть пустышкой в чьём-то воображении!"
                show mt smile pioneer far at cleft with dspr
                mt "Ребята, уже скоро концерт - чего это вы тут стоите?"
                "Ольга шла нам навстречу со стороны эстрады. Славя тем временем быстро утёрла слёзы и выдавила свою дежурную улыбку."
                show sl normal pioneer with dspr
                mt "Давайте по местам. Всего пять минут осталось."
                "Вожатая издали оглядела нас и тут же пошла восвояси."
                me "Ольга Дмитриевна!"
                "Я было рванулся к вожатой, но Славя ловко удержала меня за руку и аккуратно заломила мой палец, всем своим видом показывая, что болтать сейчас совершенно не стоит."
                show mt normal pioneer far at cleft with dspr
                mt "Что, Семён?"
                sl "Мы сейчас подойдём, Ольга Дмитриевна. Ты ведь это хотел сказать, Семён?"
                "Славя посмотрела на меня так будто ей больше нечего было терять в жизни и сейчас она пойдёт на всё что угодно лишь бы сохранить нашу тайну."
                "Сопротивление было бесполезным, и я неуверенно пролепетал:"
                me "Д-да."
                mt "Ну и ладно."
                "Вожатая заторопилась и быстро пошла в сторону дальнего ряда скамеек."
                hide mt with dspr
                sl "Договорим после концерта, Семён. Надеюсь, ты меня хорошо понял."
                #И начинается концерт.                
                jump alt_day6_uvao_concert_insert
        #Далее уйма размышлизмов под аккомпанемент просмотра концерта, а после - в соответствии с бабблом.
