################################
########### LEVEL 01 ############
################################
##### REQUEST_01  About Girls #####
################################
label dap_request_01: #LV.1 (Whoring = 0 - 4)

    $music("Daphne Theme")

if IsRunNumber(1):
        $hero("Хорошо, мисс, тогда просто расскажите о тех, кто вас окружает. Мы должны понимать с кем имеем дело.")
        $daphne("~55 00 1 neu// Ну, мне они, в общем-то, неинтересны.// С какой стати мне обращать внимание на всяких недоволшебников?!")
        $hero("Однако, мисс, чтобы вы заняли на факультете подобающее положение, кто-то должен занять неподобающее.// Количество положений довольно ограничено. Вы меня понимаете?")
        $daphne("~46 01 1 pou// Понимаю,... кажется.")
        $hero("Поэтому я даю вам задание: вы должны интересоваться другими студентками.// Обращать внимание за счет чего они более популярны. Пока.")
        $daphne("~37 00 1 ope// Да, сэр. Именно \"пока\"! Вы очень точно выразились...")
        $hero("Находить их слабые места, всякого рода недостатки и, может быть, даже скелеты в шкафу...")
        $daphne("~26 00 1 ope// Э-э... Вы предлагаете мне стучать, сэр?// ~26 00 1 neu// Это недостойно волшебницы в Мерлин знает каком поколении!")
        $hero("Странно, что мне об этом говорит студентка Слизерина.// Вы не ошиблись факультетом, дорогая? Может, вам дорога в  прямой, как доска, Гриффиндор?")
        $daphne("~55 00 1 pri// Хм... Но я...")
        $hero("Я не предлагаю \"стучать\", как вы выразились.// Просто изучите своих однокурсниц. Напомню, многие из них будут выступать на конкурсе.//" 
            "Посмотрите за счет чего они могут выиграть и за счет чего проиграть.//"
            "Вам нужно заботиться не только о том, как красиво подать себя на сцене во время конкурса, мисс, но и о вашем месте на факультете.//"
            "Чем выше оно будет, тем вероятнее, что за вас проголосуют студенты, а их голоса тоже учитываются.")
        $daphne("~46 00 1 dis// Профессор! Я не верю своим ушам!// Вы предлагаете мне пресмыкаться перед мугродьем, чтобы повысить мои шансы?!")
        $hero("Я предлагаю быть более гибкой, мисс.// А сейчас сконцентрируйтесь на простой задаче и изучайте своих конкуренток.")
        $daphne("~46 00 1 pou// Хм... Я постараюсь, профессор.")
        $hero("Отлично. Тогда до вечера.")
elif IsRunNumberOrMore(2):
    if IsRunNumberOrMore(5): # Проверить на роботоспособность до 5-ого исполнения.
        pause 1.0
        felix "К большому сожалению, данная сюжетная линия пока дописана только до этого момента..."
        felix "{size=-3}(Но, вам остаются доступны другие сюжетные линии){/size}"
        felix "Оставьте ваши вопросы, благодарности и пожелания на нашем {a=http://wtrus.ixbb.ru/viewtopic.php?id=9}ФОРУМЕ{/a}."
        felix "Так вы простимулируете нас, и продолжение появится быстрее. :)"
        call daphne_main_menu_requests
        pass
        $hero("Так, мисс Гринграсс. Давайте-ка вы сегодня снова займетесь изучением ваших конкуренток.")
        $daphne("~64 00 1 neu// Опять, сэр?")
        $hero("Ну, если вы уже все о них знаете...")
        $daphne("~55 00 1 neu// Пока не все, сэр.")
        $hero("Тогда вперед, жду вас вечером с отчетом.")
return



label dap_request_01_complete:
    $daphne.Visibility()
    $daphne.chibi.State("door", speed="go").Trans(d4, "blink").Trans("go center", "blink") # Если делать dissolve в движении, то сбивается счетчик времени. Лучше выполнить появление чибика стоя, затем уже двигать его 
    pause.5
    $screens.ShowD3("bld1")

    $daphne.State(pos="door").Visibility("body+")("~55 00 1 smi// Добрый вечер, профессор Дамблдор.") 


    $music("Daphne Theme")

    if IsRunNumber(1):
        $hero("Итак, мисс Гринграсс, каковы успехи?")
        $daphne("~55 00 1 neu// Ну, я наблюдала за Джесси. Похоже, она не слишком прилежно учится.")
        $hero("И?")
        $daphne("~55 00 1 pur// Это пока все, сэр.")
        $hero("И как это поможет вам завоевать положение и подняться выше Джесси, мисс? Хотите сказать, что ее плохая учеба влияет на ее популярность?")
        $daphne("~55 00 1 pou// В общем-то, нет. Я потому и выбрала ее, что она довольно популярна.//"
            "~55 01 1 pou// К тому же она хвалилась, что может окрутить любого парня, вот я и решила...//"
            "~37 00 1 pou// Профессор, только не подумайте, что мне надо кого-то там окручивать!//"
            "Я выше этого! Просто вы дали задание и мне показалось, что она подойдет.")
        $hero("Я уже слышал, что вы выше этого, мисс.// Но получается, что задание вы сегодня не выполнили.")
        $daphne("~73 00 1 pou// Похоже, что так.")
        $hero("И тем не менее, я готов вас простимулировать, потому что верю в вас.// В конце концов вы волшебница древнего рода.// Уверен, в следующий раз у вас получится лучше.")
        $daphne("~73 00 1 smo// Спасибо, сэр, я буду очень стараться!")
        $daphne.whoring += 1
        $event.Finalize("daphne_pre_menu")
    elif IsRunNumber(2):
        $daphne("~55 00 1 neu// Сегодня, профессор Дамблдор, я решила подойти к вопросу системно.")
        $hero("Вот как?")
        $daphne("~46 00 1 neu// Да, сэр. Мне кажется, я начинаю понимать, почему одни девчонки популярнее других.")
        $hero("#(Тоже мне бином Ньютона.)// Слушаю вас, мисс.")
        $daphne("Мне надо еще кое-что проверить, сэр, в следующий раз я смогу рассказать вам.//" 
            "~46 00 1 pou// А сегодня я присматривалась к Мелиссе, она заигрывала с парнями.")
        $hero("И как вам это?")
        $daphne("~37 00 1 pur// Отвратительно, сэр. Как она может это делать – среди них были не только полукровки, но и мугродье!")
        $hero("Не может быть!")
        $daphne("Да, сэр, представьте себе.")
        $hero("И что же?")
        $daphne("~37 00 1 pri// Парни вились вокруг нее, сэр!//"
            "~37 00 1 dis// И знаете, мне показалось, что некоторые были не прочь зайти с ней дальше заигрываний.")
        $hero("Вот это неожиданность!")
        $daphne("~37 00 1 pri// Я тоже была шокирована, сэр!// Я никогда не обращала на это внимания, никогда об этом не задумывалась.//"
            "~37 n0 1 pou// Я была уверена, что чистая кровь откроет любые двери и всякие заигрывания никому не нужны.//"
            "~37 n2 1 pou// Но почему-то сегодня вокруг меня не было ни одного парня, а к этой девице они летели, как мухи на...")
        $hero("На мед?")
        $daphne("~37 00 1 pou// Я хотела употребить более сильное слово, сэр. Но пусть будет «мед»...")
        $hero("И что же теперь, мисс?")
        $daphne("~37 00 1 neu// Мне нужно время, чтобы во всем этом разобраться, сэр.")
        $hero("Хорошо, мисс Гринграсс, похоже, вы движетесь в верном направлении. Думаю, стоит вас наградить.")
        $daphne.whoring += 1
        $event.Finalize("daphne_pre_menu")
    elif IsRunNumber(3):
        $daphne("Мне кажется, я поняла, сэр.")
        $hero("Да?")
        $daphne("~55 00 1 ope// Популярность зависит от учебы, популярности у парней, и разумеется, чистоты крови.")
        $hero("#(О, великие пески! Заканчивай уже с банальностями и займи, наконец, свой очаровательный ротик полезным делом!)// Я, гхм... Я вижу, вы серьезно копали, мисс, я не ошибся в вас.")
        $daphne("~73 00 1 smi// Спасибо, сэр.")
        $hero("Ну, с чистотой крови у вас все в порядке.")
        $daphne("~55 00 1 ope// Да, это так сэр! Такой чистой крови нет ни у кого ни в Хогвартсе, но и в Дурмшанге.// ~55 c0 1 ope// Мы - Гринграссы ведем свой род от самого Салазара Сли...")
        $hero("#(Она опять!) Постойте, мисс. Мисс! Что скажете насчет учебы?")
        $daphne("~55 00 1 pur// Не думаю, что чистокровные волшебницы должны напрягаться, чтобы зарабатывать оценки у каких-то преподавателей с сомнительной родословной.//"
            "~37 00 1 dis// Пусть для этого тужится всякое мугродье вроде грязнокровки Грейнджер.//"
            "Я и так знаю, что я лучшая.")
        $hero("Хм. Тогда этот путь к популярности вычеркиваем.// Но одной чистоты крови, маловато, мисс.")
        $daphne("~55 00 1 pou// Я тоже думала об этом, сэр.")
        $hero("Остаются, мужчины?")
        $daphne("~73 01 1 ang// Что?... Мужчины, сэр?")
        $hero("По вашей теории, перед глубиной которой я снимаю шляпу...")
        $daphne("~73 01 1 smo// О...")
        $hero("...есть три пути получения популярности.//"
            "Как я понимаю: за вас - кровь, против вас - результаты в учебе.//"
            "Остаются мужчины - они могут склонить чашу весов и в одну и в другу сторону.")
        $daphne("~55 00 1 pou// Эм...// Но, сэр, я не думаю, что должна выпрыгивать из трусиков, чтобы добиться благосклонности каких-то парней.")
        $hero("#(Хе-хе, «выпрыгивать из трусиков» - славная метафора. Думаю, вскоре ты будешь из них выпрыгивать, дорогая).//"
            "Ну что ж, мисс. Тогда на конкурсе эти парни будут голосовать за своих грязнокровых подружек,...// а девушка, которая достойна всего самого лучшего с треском провалится.")
        $daphne("~37 00 1 pou// Сэр, как вы можете!")
        $hero("Просто я очень надеюсь, что вы пересмотрите свои взгляды, мисс Гринграсс.")
        $daphne("~26 00 1 ope// Профессор Дамблдор! Не забывайте, что моим предком был сам Салазар Слизерин!")
        $hero("Тот самый, который основал факультет в котором вы учитесь, кажется?")
        $daphne("Да, сэр, и вы лучше меня это знаете!")
        $hero("Наверное, все-таки не очень хорошо. Напомни, пожалуйста, какие качества отличают слизеринцев")
        $daphne("~55 01 1 neu// Хитрость, честолюбие, находчивость, сэр.")
        $hero("И как вы проявили эти качества, чтобы добиться победы в конкурсе (например, по отношению к мужчинам)?")
        $daphne("~55 01 1 pou// .........................")
        $hero("Идите, девушка, и подумайте, достойны ли вы своего великого предка!//" 
            "Впрочем, поскольку вы усердно работали, думаю, будет неправильно оставить вас совсем без подарка.")
        $daphne.whoring += 1
        $event.Finalize("daphne_pre_menu")
    elif IsRunNumber(4):
        $daphne("Эм....// Сэр...")
        $hero("Да мисс Гринграсс....// вы готовы мне что-то рассказать?")
        $daphne("..........//~55 00 1 ope// Вы оказались правы, профессор.//~37 n0 1 pou// Парням совсем наплевать на то, какая у меня кровь....//~37 00 2 dis//  ...Почему профессор?!//~37 02 2 dis//  ...Почему мой флирт, им важнее?!")
        $hero("Хм.....// Я так понял, вы пытались заигрывать с парнями мисс Гринграсс?")
        $daphne("~73 01 1 ang// Э-э... Я не хотела...// Просто....// Ну.... мне нужно было еще раз все проверить.")
        $hero("Мисс Гринграсс...// А вы бы не могли по конкретнее мне рассказать, с кем из парней вы флиртовали?")
        $daphne("~37 00 2 dis// Эм....// Нет профессор...// Я не стану делиться этим с вами, сэр...")
        $hero("...Почему же?")
        $daphne("~73 02 3 ang// Это очень низко...//  #(До сих пор не могу поверить что я решилась на это)")
        $hero("Низко?// Вы уже научились решаться на то, о чем раньше не могли даже думать.// По моему это достойно похвалы....// Как считаете?")
        $daphne("~55 00 1 ope// Эм... Я не знаю, сэр.//~46 00 1 neu//  Мне все еще не по себе от этого.")
        $hero(g9, "#(Ты у меня и не такое будешь вытворять, когда я закончу с тобой)")
        $daphne("~46 00 1 neu// Что вы сказали, сэр?")
        $hero(m, "Эм.... Я подумал, что на сегодня с вас достаточно того, что вы сделали.")
        $daphne("~37 00 1 dis// #(Черт... Лучше не напоминайте мне об этом)")
        $hero("На сегодня вы можете быть свободны, мисс Гринграсс.")
        $daphne("~46 00 1 neu// ...Хорошо, профессор.")
        $hero("И да... мисс Гринграсс, я думаю вы заслужили поощрение сегодня.")
        $daphne.whoring += 1
        $event.Finalize("daphne_pre_menu")

    return