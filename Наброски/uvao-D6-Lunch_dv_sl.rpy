# Д6-Обед с Алисой или Славей (свободный выбор)
#
# Используется флаг alt_uvao_true
# Используется флаг alt_uvao_D5_sh_mines
# Используется флаг alt_uvao_D5_hentai
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
    "Впрочем, как и за минуту до этого - беуспешно."
    "Сегодня здеь были буквально все сразу и одновременно."
    if (alt_uvao_true or (not alt_uvao_D5_sh_mines)):
        #Вчера обедали в столовой и Виола жаловалась на пионеров, объевшихся зелёных ягод
        "Даже вчерашние мелкие, наевшиеся зелёных ягод, превозмогли, похоже, свою смертельно опасную болезнь и явились-таки в столовую."
    th "Да что это же такое! Не стоя же мне есть, не лошадь, всё-таки! Вернее, не конь."
    "Неизвестно, сколько ещё я топтался бы на месте, если бы мне не пришли на помощь."
    show sl smile pioneer far at left
    show dv grin pioneer far at right
    with dissolve
    "Сразу две руки поднялись и практически синхронно помахали мне."
    show sl serious pioneer far at left
    show dv sad pioneer far at right
    with dissolve
    "Заметив жест друг друга, девочки так же синхронно насупились."
    dreamgirl "Ого, вот это успех! Возможно, для тебя всё-таки не всё ещё потеряно."
    "Стараясь не рассмеяться, я без особых колебаний поспешил вперёд."
    menu:
        "Сесть с Алисой":
            hide sl
            show dv normal pioneer at center
            with dissolve
            "Старательно не замечая обиженный взгляд Слави, я подрулил со свои подносом к столику, за которым восседала Алиса."
            me "Свободно, подруга?"
            show dv surprise pioneer close at center with dspr
            "Не дожидаясь ответа, я плюхнулся на свободное место напротив Алисы."
            dreamgirl "Что это с тобой? Был такой воспитанный мальчик..."
            th "Как говорится, с волками жить - по-волчьи выть! И вообще, я есть хочу!"
            show dv normal pioneer close with dspr
            "Впрочем, Алиса, кажется, отнеслась к моей решительности с одобрением."
            show dv smile pioneer close with dspr
            "Откинувшись на спинку стула и хитро улыбнувшись, она ответила:"
            dv "Приятного аппетита... дружок!"
            "Тут она хихикнула, превратившись на несколько секунд из надменной задиры в обычную рыжеволосую девочку-подростка."
            dreamgirl "Кажется, не одна Славя сегодня демонстрирует неожиданные стороны характера.{w} Может, сегодня праздник какой, а мы и не знаем?"
            "Впрочем, день сегодня и вправду был необычный."
            "Обратив наконец внимание на содержимое тарелки, я обнаружил, что повара сегодня расстарались и приготовили на первое солянку."
            "Настоящую, ароматную солянку, огненно-красную, с янтарными блёстками жира на поверхности, сквозь которые просвечивали уварившиеся кусочки копчёной колбасы."
            th "Надо же, даже каперсы где-то добыли!"
            "Тут наконец до меня дошло:"
            th "Ну да, так последний же день! Прощальный обед и всё такое.{w} То, что половина лагеря будет животами маяться потом - непринципиально."
            "Впрочем, меня эти ньюансы сейчас волновали мало."
            "Бережно размешав сметану и отогнав в сторону подвернувшуюся некстати долку лимона, я с вожделением зачерпнул первую, самую вкусную ложку..."
            dreamgirl "Эх, Семён, променял ты кошечку на солянку!"
            th "Изыди нечистый, не отравляй радость бытия!"
            "Алиса, до этого молча наблюдавшая за моими манипуляциями, подала наконец голос:"
            show dv grin pioneer close with dspr
            dv "А ты неплохо устроился!"
            "Не отрываясь от еды, я промычал невнятно:"
            me "Само собой, на том стоим!"
            "но тут же поинтересовался на всякий случай:"
            me "А что, собственно, ты имеешь в виду?"
            # Взаимный троллинг
            # "Надо же, как хорошо устроился - и в медпункт, как на работу, и активисточка всё время рядом вьётся!"
            # Задумываемся о поведении Слави
            # Если есть флаг обеда с Леной в 4Д alt_uvao_D4_lunch_un, Алиса упоминает о изменении поведения Лены.
            # Если есть флаг вечера 5д alt_uvao_D5_evening_dv_un - о том, что, похоже, Лена втрескалась в Cемёна.
            # Если есть флаг эффекта alt_uvao_D6_CS_vetrov - Семён задумывается, вспоминает о Лене, начиная с первого дня, подозревает о кошочкином участии.
            if (alt_uvao_D6_CS_vetrov and alt_uvao_D4_lunch_un and alt_uvao_D5_evening_dv_un):
                menu:
                    "Поговорить с Мику":
                        #
                    "Искать Юлю":
                        #
                    "Не надо паники!": # (в баббле - "Свалить к Славе")
                        #jump "Разговор со Славей у столовой"
            else:
                #jump "Разговор со Славей у столовой"
        "Сесть со Славей":
            # Приглашение встретиться после танцев
            if (alt_uvao_D4_lunch_sl and alt_uvao_D5_evening_sl):
                # Как-то Славя внезапно переменилась. Другой человек прямо-таки!
                #jump "Обсудить подозрительное поведение Слави с ОД"
            else
                # Посчитать, что беседа будет о делах амурных (Можно помечтать на веранде столовой)
                # Топаем в домик
