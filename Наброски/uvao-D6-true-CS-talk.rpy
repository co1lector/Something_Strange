# Д6-общение с Виолой в медпункте и допрос Шурика
#
# используется флаг выхода на тру-энд alt_uvao_true
#
label alt_day6_true_CS_talk:
	# Долгий разговор с Виолой под чай с печеньками
	#Чайййник! https://ru.wikipedia.org/wiki/%D0%AD%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA#/media/File:%D0%9D%D0%B5%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D1%8D%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D1%87%D0%B0%D0%B9%D0%BD%D0%B8%D0%BA.jpg
	"Вволю наумывавшись ледяной водой, я направился к медпункту как был - прямо с полотенцем. Ничего, свои люди."
	"Впрочем, подойдя к двери, я всё-таки решил постучаться. Как-никак, медицинский кабинет, мало ли что…"
	cs "Открыто, открыто!"
	"Увидев меня, Виолетта рассеянно помахала рукой и снова забарабанила по клавиатуре передового достижения отечественного компьютеростроения."
	"К некоторому моему удивлению, Шурика в медпункте видно не было."
	# уселся на кушетку и приготовился ждать.
	# th "где же, где же Шурик???"
	"От скуки я покосился на монитор"
	#th "Кажется, это называется алфавитно-цифровым?"
	th "Жаль, я в подобных раритетах не разбираюсь."
	#dreamgirl "А зачем?"
	#th "Понял бы что-нибудь умное. Или хоть покопался бы, приведись возможность"
	

	#//Шурик проснулся утром и был выпущен умываться-завтракать

	$ alt_uvao_D6_CS_vetrov = True
	jump alt_day6_true_SH_exam
	
label alt_day6_true_CS_talk_short:
	# Короткий разговор с Виолой
	# Про эф.Ветрова не узнаём

label alt_day6_true_SH_exam:
	#допрос Шурика
	#//Аккуратно расспрашивем с Виолой на предмет взаимодействия с аномалией
	#//Шурик проснулся утром и был выпущен умываться-завтракать