# Д6-Обед с Алисой или Славей (свободный выбор)
#
# Используется флаг alt_uvao_true
# Используется флаг alt_uvao_D5_sh_mines
# Используется флаг alt_uvao_D5_hentai
# используется флаг сопровождения в Д1 Славей от ворот до домика ОД alt_day1_sl_conv
# используется флаг обеда с Леной в 4Д alt_uvao_D4_lunch_un
# используется флаг обеда со Славей в 4Д alt_uvao_D4_lunch_sl
# используется флаг встречи со Славей на пляже в Д5 alt_uvao_D5_evening_sl
# используется флаг встречи с Леной и Алисой на площади вечером Д5 alt_uvao_D5_evening_dv_un
# используется флаг Полной Информированности alt_uvao_D6_CS_vetrov
#
label alt_day6_lunch_dv_sl:
# столовая изнутри, день 
#
# Возможно, здесь нужна минивилка, пришли мы с пляжа или с хозработ - пока что по хозработам ХЗ насчёт подробностей прибытия
#    
    th "Такое ощущение, что пионеров в лагере с каждым днём становится всё больше."
    "Я обвёл взглядом битком набитую столовую."
    "Кажется, столько народу одновременно в местной столовой я до сих пор не видел ни разу."
    th "Размножаются они что ли?"
    dreamgirl "Ага, почкованием, не иначе!"
    if not alt_uvao_D5_hentai:
        # ХЗ, может ли попасть сюда хентайный ГГ, так что проверяем
        dreamgirl "Кстати, и тебе тоже пора осваивать этот метод, судя по твоей вчерашней тормознутости."
        dreamgirl "Это надо же, девочка сама напрашивалась, а он!..."
    "Стараясь не обращать внимания на подколки Шизы, я получил свою порцию еды и снова завертел головой в поисках свободного места."
    "Впрочем, как и за пару минут до этого - безуспешно."
    "Сегодня здеь были буквально все сразу и одновременно."
    if (alt_uvao_true or (not alt_uvao_D5_sh_mines)):
        #Вчера обедали в столовой и Виола жаловалась на пионеров, объевшихся зелёных ягод
        "Даже вчерашние мелкие, наевшиеся зелёных ягод, превозмогли, похоже, свою смертельно опасную болезнь и явились-таки в столовую."
    th "Да что же это такое! Не стоя же мне есть, не лошадь, всё-таки! Вернее, не конь."
    "Неизвестно, сколько ещё я топтался бы на месте, если бы мне не пришли на помощь."
    show sl smile pioneer far at left
    show dv grin pioneer far at right
    with dissolve
    "Сразу две руки поднялись и практически синхронно помахали мне."
    "Лицо Слави выражало искреннее радушие, в жесте Алисы явно угадывалось \"Подь сюды!\"."
    show sl serious pioneer far at left
    show dv sad pioneer far at right
    with dissolve
    "Впрочем, заметив жест друг друга, девочки так же синхронно насупились."
    dreamgirl "Ого, вот это успех! Возможно, для тебя всё-таки не всё ещё потеряно."
    "Стараясь не рассмеяться, я без особых колебаний поспешил вперёд."
    menu:
        "Сесть с Алисой":
            hide sl
            show dv normal pioneer at center
            with dissolve
            "Старательно не замечая обиженный взгляд Слави, я подрулил со своим подносом к столику, за которым восседала Алиса."
            "Кажется, сейчас даже возможные подколки Алисы будут лучше, чем непривычное внимание Слави."
            me "Свободно, подруга?"
            show dv surprise pioneer close at center with dspr
            if alt_uvao_D4_lunch_un:
                "Сидевшая неподалёку Лена бросила на меня странный взгляд, но тут же снова уткнулась в тарелку."
                "Особого желания снова играть с ней в гляделки у меня не было, так что я предпочёл её проигнорировать."
            "Не дожидаясь ответа Алисы, я плюхнулся на свободное место напротив."
            dreamgirl "Что это с тобой? Был такой воспитанный мальчик..."
            th "Как говорится, с волками жить - по-волчьи выть! И вообще, я есть хочу!"
            show dv normal pioneer close with dspr
            "Впрочем, Алиса, кажется, отнеслась к моей решительности с одобрением."
            show dv smile pioneer close with dspr
            "Откинувшись на спинку стула и ехидно улыбнувшись, она ответила:"
            dv "Приятного аппетита... дружок!"
            "Тут она хихикнула, превратившись на несколько секунд из надменной задиры в обычную рыжеволосую девочку-подростка."
            dreamgirl "Не одна Славя сегодня демонстрирует неожиданные стороны характера.{w} Может, праздник какой, а мы и не знаем?"
            "Вообще-то, день сегодня и вправду был необычный."
            "Обратив наконец внимание на содержимое тарелки, я обнаружил, что повара расстарались и приготовили на первое солянку."
            "Настоящую, ароматную солянку, огненно-красную, с янтарными блёстками жира на поверхности, сквозь которые просвечивали уварившиеся кусочки копчёного мяса."
            th "Надо же, даже каперсы где-то добыли!"
            "Тут наконец до меня дошло:"
            th "Ну да, так последний же день! Прощальный обед и всё такое.{w} То, что половина лагеря будет животами маяться потом - непринципиально."
            "Впрочем, меня эти ньюансы сейчас волновали мало."
            "Бережно размешав сметану и отогнав в сторону подвернувшуюся некстати дольку лимона, я с вожделением зачерпнул первую, самую вкусную ложку..."
            dreamgirl "Эх, Семён, променял ты кошечку на солянку!"
            th "Изыди нечистый, не отравляй радость бытия!"
            "Алиса, до этого молча наблюдавшая за моими манипуляциями, подала наконец голос:"
            show dv grin pioneer close with dspr
            dv "А ты неплохо устроился!"
            "Не отрываясь от еды, я промычал невнятно:"
            me "Само собой, на том стоим!"
            "Но тут же поинтересовался на всякий случай:"
            me "А что, собственно, ты имеешь в виду?"
            dv "Ну как же! И в медпункт ходишь, как на работу, {i}болтаешь{/i} там с Виолой во время {i}процедур{/i}..."
            "Алиса так похоже изобразила бархатистый, с придыханием, голос Виолы, что мне пришлось прикусить губу, чтобы не рассмеяться."
            dv "...И активисточка наша всё время рядом с тобой вьётся..."
            # ===== TODO Задумываемся о поведении Слави
            "Обсуждать с Алисой тему внезапно прорезавшейся любезности со стороны Слави мне не очень-то хотелось, и я перебил рыжую, брякнув первое, что пришло в голову:"
            me "Ага, и на пляже бесплатно эротические шоу показывают. Я себя прямо-таки настоящим повелителем гарема чувствую!"
            show dv shy pioneer close with dspr
            "Наблюдая, как Двачевская заливается краской до самых ушей, я почувствовал себя отомщённым."
            show dv rage pioneer close with dspr
            "Воровато оглянувшись по сторонам, не подслушивает ли кто, она наклонилась и зашипела на меня:"
            dv "Да что ты мелешь, придурок! Кому ты нужен, чтобы тебе..."
            "Тут она гордо вздёрнула нос и бросила пренебрежительно:"
            show dv angry pioneer close with dspr
            dv "И вообще, ты сам на меня пялился!"
            "Я изобразил виноватую гримасу и притворно вздохнул:"
            me "Ну да, пялился немножко. Житие мое..."
            me "А с другой стороны, ну кто бы на моём месте устоял перед такой красотой?{w} Ручаюсь, что никто!"
            dreamgirl "Тоже мне, хентай-мастер нашёлся! С таким изяществом только носорогов очаровывать."
            "Алиса бросила на меня сердитый взгляд и буркнула:"
            dv "Поговори мне тут ещё!"
            show dv grin pioneer close with dspr
            "Странно, но судя по вновь проступившему на щеках румянцу и скользнувшей на её губы самодовольной ухмылке, мой неуклюжий \"комплимент\" попал в цель."
            "Мне даже немного жаль стало девочку - похоже, до меня на дистанцию прицельного комплиментометания ни один парень к ней не приближался."
            dreamgirl "Я так думаю, что если какие-то камикадзе и пытались, то она отстреливала их ещё на дальних рубежах."
            if not alt_day1_sl_conv:
                # ЛБ: уточнить по альтернативной версии Д1 !
                "Вспомнив непрошенный душ из пожарного ведра сразу по прибытии, я не мог не согласиться с Шизой."
            show dv normal pioneer close with dspr
            if alt_uvao_D4_lunch_un:
                # Если есть флаг обеда с Леной в 4Д alt_uvao_D4_lunch_un, Алиса упоминает о изменении поведения Лены.
                "Приканчивая остатки солянки, я заметил краем глаза, что Лена встала из-за стола и потащила свой поднос в сторону посудомойки."
                show dv sad pioneer close with dspr
                "Погрустневшая вдруг Алиса проводила её задумчивым взглядом. Потом, отставив в сторону суповую тарелку, так же задумчиво уставилась на плов."
                "Не то, чтобы мне жизнь была не мила без болтовни Алисы, но её дурное настроение не обещало ничего хорошего всем окружающим, включая меня, так что я попытался немного разрядить обстановку."
                me "Похоже, у Лены аппетит не то очень хороший, не то очень плохой, раз она так быстро закончила обед, да?"
                dv "Лена сильно изменилась за последнее время."
                "Сообщила мне Алиса, подняв на меня ставший непривычно серьёзным взгляд."
                dv "С тех пор, как ты приехал."
                dv "Я её хорошо знаю... Ну, вернее, как хорошо...{w=1.5} Лучше других, во всяком случае. Мы живём недалеко и не первый год уже дружим."
                dv "Она всегда была... немного замкнутая. Но сейчас совсем в себя ушла, молчит всё время."
                show dv angry pioneer close with dspr
                "Алиса с досадой качнула головой и угрожающе зыркнула на меня исподлобья."
                th "Эй, а я-то здесь при чём?"
                "Замкнутой мне Лена показалась с самого первого дня, тут и говорить не о чем. Но при чём здесь мой приезд?"
                show dv normal pioneer close with dspr
                "Молча покачав головой, Алиса принялась вяло ковырять вилкой плов."
            else:
                "Отставив в сторону суповую тарелку, Алиса задумчиво принялась ковырять вилкой плов."
            if alt_uvao_D5_evening_dv_un:
                # Если есть флаг вечера 5д alt_uvao_D5_evening_dv_un - о том, что, похоже, Лена втрескалась в Cемёна.
#                dv "Кстати, о гаремах... Ты знаешь, возможно, он больше, чем ты думаешь."
#                "Поперхнувшись пловом, я отчаянно закашлялся и уставился на Алису сквозь выступившие слёзы."
                dv "Кстати, о любовании красотой... Возможно, тебе стоило бы побольше пялиться немного в другую сторону."
                "Я недоумённо посмотрел на Алису."
                show dv angry pioneer close with dspr
                dv "Ну чего уставился? Можно подумать, кроме твоей активисточки здесь других девчонок нет!"
                "Алиса бросила на Славю злобный взгляд и, наклонившись над столом, продолжила вполголоса:"
                show dv normal pioneer close with dspr
                dv "В общем, я пристала к ней с расспросами, и она не выдержала, всё мне рассказала..."
                show dv shy pioneer close with dspr
                "Тут Алиса запнулась, явно смутившись. Отведя взгляд в сторону, она закончила невнятной скороговоркой:"
                dv "Короче, она в тебя втюрилась, вот!"
                "Выпрямившись, она скрестила руки на груди и бросила на меня сердитый взгляд, словно я только что заставил её признаться в чём-то постыдном."
                "Поняв, что продолжения не будет, я спросил вкрадчивым голосом:"
                me "Слушай, Алиса, а ты о ком, вообще-то, говоришь?"
                show dv angry pioneer close with dspr
                dv "Дурак!"
                "Окрысилась она на меня, и я тут же вспомнил это же самое слово, произнесённое этой же самой девочкой не далее, как вчера вечером!"
                th "Подождите, неужели всё-таки..."
                "Алиса не замедлила развеять остатки моих сомнений, вновь перейдя на угрожающее шипение:"
                dv "Да о Ленке я говорю, о ком же ещё! Нельзя же быть таким тупым!"
                "Проглотив оскорбление, я ошарашенно уставился на Алису."
                me "А...а... а ты уверена?"
                show dv surprise pioneer close with dspr
                dreamgirl "Да, ты действительно туповат. Это факт. Не повезло мне с носителем."
                "Похоже было, что Алиса тоже окончательно уверилась в невысоком уровне моих умственных способностей, потому что в ответ она лишь покачала головой и вздохнула:"
                show dv sad pioneer close with dspr
                dv "Верно говорят - \"любовь зла, полюбишь и козла\". Бедная Лена..."
                "После этого Двачевская скорчила зверскую рожу и процедила, угрожающе сжимая кулаки:"
                show dv angry pioneer close with dspr
                dv "Смотри мне, не вздумай ляпнуть кому-нибудь, что это я тебе рассказала!"
                "Я поспешно замахал руками, мол, буду нем как рыба, но она всё-таки закончила, перейдя на зловещий шёпот:"
                dv "Короче говоря, одно неосторожное слово, даже взгляд, и ты - покойник."
                show dv normal pioneer close with dspr
            "Остаток обеда прошёл в молчании."
            if alt_uvao_D5_evening_dv_un:
                "Алиса явно не была склонна продолжать разговор, а я тоже решил, что уже и так узнал больше, чем рассчитывал."
                "К тому же мне совсем не хотелось нарываться. Быть поколоченным девчонкой..."
                "Отчего-то я не сомневался ни в том, что угрозы Алисы не были шуткой, ни в том, что за ней не заржавеет их выполнить."
            if (alt_uvao_D4_lunch_un or alt_uvao_D5_evening_dv_un):
                # Наслушались Алису и задумываемся о Лене
                "Машинально работая челюстями, я обдумывал услышанное от Алисы."
                window hide
                $ set_mode_nvl()
                window show
                if alt_uvao_D5_evening_dv_un:
                    # Знаем про влюблённость Лены от Алисы
                    th "Неужели, Лена и вправду в меня... гм... \"втюрилась\"? Час от часу не легче."
                    "Приходилось взглянуть правде в глаза - большая часть Лениных заморочек этим вполне объяснялась.{w} Например, то, что она напросилась идти искать Шурика и жутко смутилась, когда Ольга об этом проболталась..."
                else:
                    # Алиса не рассказывала про влюблённость Лены (но всё равно обедали с Леной в Д4)
                    "По всему выходило, что не мне одному поведение Лены показалось странным."
                    "Да что там \"показалось\" - оно и было странным! Эти её неловкие попытки заговорить со мной, то, что она напросилась идти искать Шурика и её смущение, когда Ольга об этом проболталась..."
                    th "Неужели Лена и вправду в меня влюбилась? Час от часу не легче."
                th "Но странно, очень странно!{w} Это только в романах так бывает, что встретились глазами, и р-р-раз, готово, любовь до гробовой доски!"
                th "Внешность у меня заурядная, интеллектом-шутками блеснуть у меня возможности никакой не было. Да мы вообще, если на то пошло, почти и не общались, а Лена чуть ли не с первого дня демонстрировала все признаки..."
                th "Нет, определённо что-то здесь не так."
                "Меня не покидало смутное ощущение, что я что-то упускаю."
                if (alt_uvao_D4_lunch_un and alt_uvao_D5_evening_dv_un and alt_uvao_D6_CS_vetrov):
                    # собрали все три флага - Семён подозревает о кошочкином участии.
                    # Замечаем Мику. Они же соседки, вроде бы! Может, она тоже что-нибудь заметила? Хорошо бы поговорить с ней.
                    dreamgirl "Именно, упускаешь. Так и быть, дам тебе подсказку."                    
                    dreamgirl "Пораскинь мозгами - кто ещё в лагере вёл себя странно за это время?"
                    #th "Конечно Шурик! Шурик! Шурик, ну кто его не знает, е-е!"
                    #===== TODOtext
                else:
                    "В законченную мысль это ощущение, впрочем, так и не оформилось, а обычно болтливое не в меру эльтер-эго на этот раз помалкивало."
                window hide
                $ set_mode_adv()
                window show
                show dv angry pioneer close with dspr
                dv "Эй, ты чего?"
                "Тут я осознал, что уже пару минут сижу с недонесённой до рта вилкой и пялюсь куда-то в район Алисиного уха."
                show dv grin pioneer close with dspr
                dv "Может тебе в лоб двинуть? В лечебных целях?"
                "Смутившись, я буркнул что-то невнятное и уставился в свою тарелку."
                show dv normal pioneer close with dspr
            else:
                # О Лене не думаем.
                pass
            "Не сговариваясь, мы с Алисой прикончили свои порции, залпом выпили неизбежный компот и поспешили освободить помещение столовой."
# столовая снаружи вблизи, день 
            show dv normal pioneer far at right with dspr
            "Выйдя на улицу, Алиса бросила на меня косой взгляд и устремилась куда-то в сторону площади."
            hide dv with dissolve
            if (alt_uvao_D4_lunch_un and alt_uvao_D5_evening_dv_un):
                # Задумываемся, куда бежать дальше, чтобы выяснить всё-всё про Лену
                "Я же притормозил на крыльце, прикидывая, что делать дальше."
                menu:
                    "Поговорить с Мику" if alt_uvao_D6_CS_vetrov:
                        jump alt_day6_mi_talk
                    "Искать Юлю":
                        jump alt_day6_ask_uv_about_un
                    "Не надо суеты!":
                        # Валим из столовой без конкретных намерений - "там видно будет", нас ловит Славя
                        "Прислонившись к перилам, я сыто вздохнул."
                        th "Собственно говоря, чего я задёргался?"
                        th "Ну влюбилась в меня Лена, дальше-то что?"
                        th "Всё равно сегодня последний день. Выяснять отношения теперь уже в любом случае поздно - одно только расстройство получится."
                        th "Тем более, что Лена действительно... того... необщительная. Хватит с меня этих игр в гляделки-молчанки."
                        th "Через сутки мы всё равно, так или иначе, но разбежимся в разные стороны, так что лучше уж просто подождать."
                        "Что-то похожее на совесть попыталось было поднять голову, но я поспешил придавить этого гнусного червячка:"
                        th "А ну цыц! Не умею я эти разговоры о чувствах вести, а уж тем более - признаваться в отсутствии взаимности."
                        dreamgirl "Не кричи. Я вообще молчу, между прочим."
                        "Шолос Шизы показался мне укоризненным и я огрызнулся:"
                        th "А я, между прочим, и не к тебе обращаюсь!"
                        "Подспудно я ожидал в ответ какой-нибудь шуточки про растроение личности, но своенравное подсознание промолчало, что меня полностью устраивало."
                        if alt_uvao_D6_CS_vetrov:
                            #===== TODOtext Аннулируем обеденные подозрения о кошечкином участии - "да пофиг! само рассосётся. И вообще, мало ли что Алисе могло показаться."
                        #===== TODOtext "В голову пришла трусливая мысль - вдруг эта Двечавская всё наврала? Полез бы к Лене объясняться - полным бы идиотом себя выставил"
            else:
                pass
            # Разговор со Славей у столовой
            #===== TODOtext
            # "собрался туда-не-знаю-куда, как меня окликнул знакомый голос"
        "Сесть со Славей":
            hide dv
            show sl smile pioneer at center
            with dissolve
            "Постаравшись сделать вид, что не заметил Алису, я подрулил со своим подносом к столику, за которым устроилась Славя."
            "Пусть Славя и ведёт себя как-то странно, но садиться с рыжей - верное самоубийство."
            # Приглашение встретиться после танцев
            if (alt_uvao_D4_lunch_sl and alt_uvao_D5_evening_sl):
                # Как-то Славя внезапно переменилась. Другой человек прямо-таки!
                #jump "Обсудить подозрительное поведение Слави с ОД"
            else
                # Посчитать, что беседа будет о делах амурных (Можно помечтать на веранде столовой)
                # Топаем в домик

                
# Взаимный троллинг
# "Надо же, как хорошо устроился - и в медпункт, как на работу, и активисточка всё время рядом вьётся!"
# Задумываемся о поведении Слави
# Если есть флаг обеда с Леной в 4Д alt_uvao_D4_lunch_un, Алиса упоминает о изменении поведения Лены.
# Если есть флаг вечера 5д alt_uvao_D5_evening_dv_un - о том, что, похоже, Лена втрескалась в Cемёна.
# Если есть флаг эффекта alt_uvao_D6_CS_vetrov - Семён задумывается, вспоминает о Лене, начиная с первого дня, подозревает о кошочкином участии.
