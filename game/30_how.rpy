label howtoplay:
    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    play music "music/silly_fun_loop.mp3" fadein 1 fadeout 1 # LOLA'S THEME.
    if not persistent.tut: #Turns TRUE after tutorial happened once already. EVENT_01




        $ lola_face = "03_hp/22_lola/01.png"
        $ lola_body = "03_hp/22_lola/body_01.png"

        $ l_things = True
        #$ l_blush = True
        $ lx = 490
        $ ly = 190
        show screen l_head
        l "Привет интернет-извращугам!"
        hide screen l_head
        a5 "Следи за языком, сучка!"
        $ l_things = False
        $ lola_face = "03_hp/22_lola/02.png"
        show screen l_head
        l "Хах...?"
        hide screen l_head
        a6 "Что я тебе говорил о слове на букву \"и\"?"
        $ l_question = True
        $ lola_face = "03_hp/22_lola/03.png"
        show screen l_head
        l "Эм... Использовать его как можно чаще..?"
        hide screen l_head
        pause.01
        with hpunch
        a7 "{size=+7}Нет!{/size}"
        $ l_question = False
        $ l_drop = True
        $ lola_face = "03_hp/22_lola/04.png"
        show screen l_head
        l "Гх!"
        hide screen l_head
        pause.01
        with hpunch
        a7 "{size=+7}Мы не используем его! Никогда!{/size}"
        $ lola_face = "03_hp/22_lola/01.png"
        $ l_drop = False
        show screen l_head
        l "Потому что самый самый большой здесь папочка?"
        hide screen l_head
        a6 "Гх!"
        a6 "Тебе понравилось сниматься в \"Тренер Принцессы\"?"
        $ l_hearts = True
        $ lola_face = "03_hp/22_lola/01.png"
        show screen l_head
        l "Лучшее событие в моей жизни!"
        hide screen l_head
        a1 "Хочешь попасть в \"Золотое издание\"?"
        $ l_hearts = False
        $ lola_face = "03_hp/22_lola/05.png"
        show screen l_head
        l "!!!"
        $ lola_face = "03_hp/22_lola/06.png"
        show screen l_head
        l "Дамы и гопода, добро пожаловать в обучающий режим \"Тренера Гермионы\"."
        hide screen l_head
        a1 "Умница, девочка."
        $ l_drop = True
    else: # EVENT_02
        $ lx = 490
        $ ly = 190
        $ lola_body = "03_hp/22_lola/body_01.png"
        $ lola_face = "03_hp/22_lola/05.png"
        show screen l_head
        l "Хм...?"
        l "Ты хочешь прослушать обучение снова?"
        $ lola_face = "03_hp/22_lola/09.png"
        l "Хм...."
        $ lola_face = "03_hp/22_lola/11.png"
        l "Ты не смущен?"
        $ lola_face = "03_hp/22_lola/10.png"
        l "Хм..."
        $ l_things = True
        $ lola_face = "03_hp/22_lola/08.png"
        l "*Хихикает!*"
        $ l_things = False
        $ lola_face = "03_hp/22_lola/01.png"
        l "Ты хочешь, чтобы я учила тебя топлесс?"
        hide screen l_head
        $ d_flag_01 = False
        menu:
            "\"Еще бы!\"":
                $ lola_face = "03_hp/22_lola/01.png"
                show screen l_head

                $ d_flag_01 = True
                l "Океюшки!"
                hide screen l_head
                pause.1
                show screen blkfade
                with d3
                $ lola_body = "03_hp/22_lola/body_02.png"
                $ l_blush = True
                pause.5
                hide screen blkfade
                with d7


            "\"Нет.\"":
                $ lola_face = "03_hp/22_lola/12.png"
                show screen l_head
                l "Ты скучный..."
                $ lola_face = "03_hp/22_lola/09.png"
                l "Ладно, пофиг..."


    ### THE TUTORIAL ###
    play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1
    $ lola_face = "03_hp/22_lola/06.png"
    show screen l_head
    l "Вот краткий перечень вещей, которые стоит помнить..."
    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_02.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3')

    l "Гермиона захочет продавать сексуальные услуги в обмен на очки факультета, когда Гриффиндор отстает."

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_01.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3')
    l "Дружба с профессором Снейпом увеличит количество очков, получаемых Слизереном."
    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_03.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3')
    if d_flag_01: # TOPLESS.
        $ lola_face = "03_hp/22_lola/07.png"
    l "Чтение образовательных книг позволит тебе зарабатывать, но это по желанию."

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_04.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3')
    l "Покупка одной и той же сексуальной услуги может привести к разным последствиям, в зависимости от того, как далеко Гермиона зашла в своих тренировках."
    $ lola_face = "03_hp/22_lola/06.png"

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_07.png" #<---- SCREEN
    l "Все услуги разделены на две группы: \"приватные услуги\" и\"публичные услуги\"."
    l "Приватные услуги оказываются в кабинете и не сильно влияют на репутацию Гермионы."
    l "Публичные услуги оказываются во время уроков за пределами экрана."
    l "Каждая публичная услуга, не считая последней, имеет девять концовок."
    l "Кстати, несмотря на то, что покупка приватных услуг - необходима для тренировки Гермионы, публичные услуги не обязательны."

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_05.png" #<---- SCREEN

    $ renpy.play('sounds/boing02.mp3')
    l "Если обращаться с ней плохо, то настроение Гермиона ухудшится, она может обидеться и стать очень неподатливой..."
    l "Она остынет со временем, но ты можешь ускорить процесс, если подаришь ей что-нибудь..."

    with hpunch
    $ end_u_1_pic =  "03_hp/22_lola/tut_06.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3')
    l "Здесь нет временных ограничений. Так что можешь играть в нее столько дней, сколько захочешь."




    $ end_u_1_pic =  "03_hp/22_lola/tut_00.png" #<---- SCREEN
    $ l_drop = False

    if not persistent.tut: # FIRST TIME TUTORIAL. Turns TRUE after tutorial happened once already. EVENT_01
        $ persistent.tut = True #Turns TRUE after tutorial happened once already.
        hide screen l_head
        a1 "Ладно, этого хватит..."
        $ l_question = True
        $ lola_face = "03_hp/22_lola/05.png"
        show screen l_head
        l "Как я справилась?"
        hide screen l_head
        a1 "Ты отлично поработала. Хорошая девочка."
        $ l_question = False
        $ l_things = True
        $ lola_face = "03_hp/22_lola/08.png"
        show screen l_head
        l "Хе-хе-хе. Лола хорошая девочка!"
        $ l_things = False
        $ lola_face = "03_hp/22_lola/01.png"
        show screen l_head
        l "А что я получу?"
        hide screen l_head
        a1 "А что ты хочешь?"
        $ lola_face = "03_hp/22_lola/10.png"
        show screen l_head
        l "Хм..."
        $ l_exclamation = True
        $ lola_face = "03_hp/22_lola/01.png"
        l "Мы можем сделать сцену изнасилования со мной в \"Золотом издании\"?"
        hide screen l_head
        a6 "Не испытывай мое терпения, девочка."
        $ l_exclamation = False
        $ l_drop = True
        $ lola_face = "03_hp/22_lola/04.png"
        show screen l_head
        l "Извини, папочка."
        $ l_drop = False
        hide screen l_head
        a5 "............"

    else: ### NOT FIRST TUTORIAL. EVENT_02
        if d_flag_01: #TOPLESS.
            hide screen l_head
            stop music fadeout 1.0
            a1 "Что здесь происходит?"
            $ lola_face = "03_hp/22_lola/14.png"
            $ l_drop = True
            show screen l_head
            l "Упс!"
            hide screen l_head
            a1 "Что я говорил тебе о раздевании перед незнакомцами?"
            $ lola_face = "03_hp/22_lola/04.png"
            show screen l_head
            l "Это важная часть взросления?"
            hide screen l_head
            a6 "Нет!"
            $ l_drop = False
            $ l_tears = True
            $ lola_body = "03_hp/22_lola/body_01.png"
            $ lola_face = "03_hp/22_lola/04.png"
            show screen l_head
            l "Папочка, мне так жаль!"
            l "Этот случайный чувак из интернета заставил меня, я клянусь!"
            hide screen l_head
            a1 "Обучение закончено."
            $ l_blush = False
            $ l_tears = False
            $ lola_face = "03_hp/22_lola/15.png"
            show screen l_head
            l "Хе-хе! Ты попался!"
        else:
            $ lola_face = "03_hp/22_lola/09.png"
            l "И, это..."
            $ lola_face = "03_hp/22_lola/13.png"
            l "Может быть в следующий раз?"

return

### ABOUT GAME ####
label abouttrainer:
    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 1 fadeout 1

    dev "Итак, сейчас перед вами \"Тренер Ведьм: Русская редакция\"."
    dev "Наша дружная команда взяла за основу небольшую, но очень приятную игру от Акабура."
    dev "И делает на основе ее идей и контента нечто новое."
    dev "Новые ивенты и персонажи, система гардероба и газетное издательство... Все это только у нас."
    dev "Кроме того, мы не считаем проект законченным и постоянно совершенствуем его."
    dev "А еще, перевели игру на русский язык, чтобы русским людям было приятно играть, и сделали мультиязычную версию."
    dev "Помните, что мы делаем это совершенно бесплатно. Для собственного и вашего удовольствия."
    dev "Все пожертвования в фонд развития игры пойдут не на пиво разработчикам, а на различные нужды проекта."

    return

########################
# From developers

label devel:

    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 1 fadeout 1

    dev "Итак, вы уже обратили внимание, что это не оригинальная игра Акабура..."
    menu :
        "Что ???" :
            dev "(facepalm)"
            dev "Я так и знал, что нужно давать больше информации общественности..."

        "Это же шутка ?" :
            dev "..........."

        "А разве ты не Акабур ?" :
            dev "В рот мне ноги..."

    dev "{size=+3}Т.е. вы все по-прежнему считаете, что игру для вас продолжает улучшать Акабур ?{/size}"
    dev "И это после того, как он сообщил, что считает ее законченной ?"
    dev "После того, как он решил никогда ее не переводить на русский ?"
    dev "После того, как я написал всю эту гору кода, не говоря уж об остальной команде разработчиков, переводчиков и художников, месяцами бесплатно трудящихся для вас ?"
    dev "{size=+4}Аргх...{/size}"
    dev "......."
    dev "Простите, наболело."

    dev "Итак, для вас трудились :"
    dev "Главный координатор (встречайте стоя !): {color=FF0000}Хан ( Khan ){/color}"
    dev "Главный разработчик, сценарии : {color=00FF00}Дрон (Dron){/color}"
    dev "Разработка и ивенты Дафны : {color=7789CA}Феликс{/color}"
    dev "Поддержка игры (на плаву) : {color=0000FF}Сказочник{/color}"
    dev "Перевод на английский язык : {color=0089BE}Хан и Sezt{/color}"
    dev "Сценарии : {color=008900}Tobie{/color}"
    dev "Разработка и обучающие ивенты : {color=4F4F4F}Nyarkohopter{/color}"
    dev "Чибики Дафны : {color=2F2F2F}Grending{/color} --> {a=http://skazgames.com/forum/memberlist.php?mode=viewprofile&u=85}Grendidg Forum{/a} | {a=https://vk.com/grendidg}Grendidg VK{/a} | {a=http://virink.com/GRENDIDG}Grendidg Virink{/a}"
    dev "Дафна : {color=6F6F6F}Zio Dyne{/color}"
    dev "Список особых благодарностей :"
    dev "{color=0F0F0F}Eskelsama{/color} - за великолепный кодинг и неоценимый вклад в развитие проекта !"

    $ hx = 370
    $ hy = 0
    $ h_red_angry = True
    $ h_angry = False
    $ h_smile = False

    dev "И несравненная Гермиона Грейнджер в роли офисной шл..."
    show screen l_hermiona
    her "Что-о-о-о ???"
    hide screen l_hermiona

    dev "Прости, в роли секретут..."
    $ h_red_angry = False
    $ h_angry = True
    $ h_smile = False
    show screen l_hermiona
    her "А на тебя давно в последний раз подавали в суд\n за половую дискриминацию ?"
    hide screen l_hermiona
    dev "Бхм. И наша главная офис-леди - мисс Грейнджер."
    $ h_red_angry = False
    $ h_angry = False
    $ h_smile = True
    show screen l_hermiona
    her "Так то лучше !"
    her "Всем до встречи в игре."
    hide screen l_hermiona
    dev "Недотрога..."
    dev "Ушла наконец."

    dev "Итак, приятной игры, друзья !"

    dev "А если хотите пообщаться с людьми, которые продолжают совершенствование и расширение игры, милости просим."
    dev "{a=http://skazgames.com/forum/}НАШ ФОРУМ ТУТ{/a}"


return

label forum:

    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN

    dev "Итак, перед вами модификация игры, которая развивается независимой (от Акабура) командой разработчиков. Добро пожаловать на {a=http://skazgames.com/forum/}НАШ ФОРУМ{/a}."

return
