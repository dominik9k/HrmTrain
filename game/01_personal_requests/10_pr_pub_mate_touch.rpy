
###################REQUEST_10 (Level 03) (25 pt.) (Let a classmate touch you). (Available during daytime only).
label new_request_10:
    
    $herView.hideQQ()
    m "{size=-4}(Сказать ей, что бы её одноклассник облапал её?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, сделать это!)\"":
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
            
    $ pos = POS_140

    if request_10_points == 0: # <================================================================================ FIRST TIME
        m "Мисс Грейнджер?"
        $herView.showQQ( "body_01.png", pos )
        her "Сэр?"
        m "Тебе нравятся мальчики твоего возраста, не правда ли?"
        $herView.hideQQ()
        $herView.showQQ( "body_03.png", pos )
        her "...?"
        m "Может быть, кто-то из одноклассников?"
        $herView.hideQQ()
        $herView.showQQ( "body_10.png", pos )
        her "Ну..."
        her "Должна ли я обсуждать с вами такие вопросы... сэр?"
        $herView.hideQQ()
        $herView.showQQ( "body_29.png", pos )
        her "Я немного стесняюсь..."
        m "Конечно, я понимаю. Мне не стоит знать детали..."
        m "Но вот что мне нужно, что бы вы сделали, мисс Грейнджер."
        m "Подойдите к какому нибудь мальчику. Тому мальчику, \"о ком мечтаешь\", который нравится..."
        $herView.hideQQ()
        $herView.showQQ( "body_31.png", pos )
        her ".......?"
        m "И пусть он потрогает тебя..."
        if whoring <=5 or request_02_c_points <= 1: # Counts how many times Hermione been sent to flirt with teachers.
            jump too_much
        $herView.hideQQ()
        $herView.showQQ( "body_31.png", pos )
        her "Дать ему потрогать меня... сэр?"
        m "Да, потрогать тебя. Как мальчики трогают девочек?"
        m "Сколько тебе лет? Ты выглядишь достаточно взрослой..."
        m "Неужели твои родители еще не \"говорили\" с тобой?"
        $herView.hideQQ()
        $herView.showQQ( "body_34.png", pos )
        her "\"Говорили\", сэр?"
        m "Да-да, \"говорили\"! О том, чем мальчики отличаются от девочек...?"
        m "У мальчиков есть \"пиписька\" и девочкам нравится брать \"пипиську\" в рот?"
        $herView.hideQQ()
        $herView.showQQ( "body_03.png", pos )
        her "!!!"
        $herView.hideQQ()
        $herView.showQQ( "body_47.png", pos )
        her "Какие же родители будут такое говорить своим детям?"
        m "Думаю, Акабур будет."
        $herView.hideQQ()
        $herView.showQQ( "body_17.png", pos )
        her "Извините, сэр?"
        m "*Кхем!* Я имею ввиду, отвественные и заботливые!"
        m "Ну, в любом случае. Вот ваше задание на сегодня, мисс Грейнджер."
        m "Найти себе мальчика и уговорить его поласкать себя..."
        $herView.hideQQ()
        $herView.showQQ( "body_69.png", pos )
        her ".........."
        m "Ты симпатичная девочка и это будет не трудно для тебя."
        her "....................."
        $herView.hideQQ()
        $herView.showQQ( "body_66.png", pos )
        her "Сколько очков я получу за выполнение этого задания, сэр?"
        m "Хм... Думаю, 25 очков хватит..."
        $herView.hideQQ()
        $herView.showQQ( "body_69.png", pos )
        her "25 очков..."
        her "...."
        $herView.hideQQ()
        $herView.showQQ( "body_66.png", pos )
        her "Ладно, договорились..."
        m "Отлично..."
        $herView.hideQQ()
        $herView.showQQ( "body_05.png", pos )
        her "Я, наверно, пойду. Скоро начнутся уроки..."
        $herView.hideQ()
    else:
        if whoring >= 6 and whoring <= 8: # LEVEL 03 
            m "Мисс Грейнджер?"
            $herView.showQQ( "body_01.png", pos )
            her "Сэр."
            m "Как насчет того, что бы дать вашему однокласснику полапать вас?"
            $herView.hideQQ()
            $herView.showQQ( "body_120.png", pos )
            her "........"
            m "25 очков, мисс Грейнджер."
            $herView.hideQQ()
            $herView.showQQ( "body_69.png", pos )
            her "Сэр, это только..."
            $herView.hideQQ()
            $herView.showQQ( "body_79.png", pos )
            her "Я не понимаю, зачем мне делать такие вещи..."
            m "Что бы помочь своему факультету?"
            $herView.hideQQ()
            $herView.showQQ( "body_66.png", pos )
            her "Я не про это..."
            $herView.hideQQ()
            $herView.showQQ( "body_69.png", pos )
            her "Ладно, не обращайте внимание..."
            her "Скоро будет звонок, я, наверное, пойду..."
            m "Ты сделаешь это?"
            $herView.hideQQ()
            $herView.showQQ( "body_66.png", pos )
            her "Я не знаю... Наверное..."
            $herView.hideQ()
        elif whoring >= 9 and whoring <= 11: # LEVEL 04
            m "Мисс Грейнджер, нужно что бы вы подошли к своему однокласснику и предложили ему полапать вас."
            $herView.showQQ( "body_01.png", pos )
            her "Я поняла, сэр..."
            m "Тогда ступай."
            her "..........."
            $herView.hideQ()
        elif whoring >= 12: # LEVEL 05+
            m "Мисс Грейнджер, я хочу, что бы вы пошли..."
            m "И нашли привлекательного парня, который бы вас облапал!"
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            $herView.showQQ( "body_01.png", pos )
            her "В каком смысле...?"
            $herView.hideQQ()
            $herView.showQQ( "body_122.png", pos )
            her "В сексуальном, сэр?"
            m "Что? Нет, я имею ввиду, что бы он потрогал вас под одеждой..."
            $herView.hideQQ()
            $herView.showQQ( "body_24.png", pos )
            her "А, понятно..."
            $herView.hideQQ()
            $herView.showQQ( "body_68.png", pos )
            her "Хотелось бы, что бы это был..."
            $herView.hideQQ()
            $herView.showQQ( "body_117.png", pos )
            her "А ничего, если это будет не один парень, ведь так?"
            m "Ты ещё спрашиваешь! Конечно нет!"
            m "Если будет кто-нибудь еще - это считается." 
            $herView.hideQQ()
            $herView.showQQ( "body_122.png", pos )
            her "Отлично. Я зайду к вам после учебы, сэр, как обычно."
            m "Хорошо. Удачи."
            $herView.hideQ()

   

    $ request_10 = True

    hide screen bld1
    $herView.hideQ()
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3

    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)


    $ hermione_takes_classes = True
    jump day_main_menu

        


label new_request_10_complete: #<==========================================================================EVENING
    
    $ walk_xpos=520 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    $ pos = POS_370
    $herView.showQ( "body_01.png", pos )
    show screen hermione_02
    with Dissolve(.3)
    
    her "Добрый вечер, сэр."
    m "Мисс Грейнджер..."
    m "Вы выполнили задание?"
    her "Я сделала так, как вы просили..."
    menu:
        "\"Отлично. Вот твои очки.\"":
            pass
        "\"Расскажи подробнее.\"":
            $herView.hideQQ()
            m "Расскажи подробнее."
            show screen blktone
            with d3
            
            if whoring >= 6 and whoring <= 8: # LEVEL 03 # EVENT LEVEL 01.
                stop music fadeout 3.0
                $herView.hideQQ()
                $herView.showQQ( "body_12.png", pos )
                her "......"
                $herView.hideQQ()
                $herView.showQQ( "body_13.png", pos )
                her "Ну... Эм..."
                m "Говори, девочка."
                m "Ты дала себя потрогать какому-нибудь везунчику?"
                    
                if one_out_of_three == 1: ### EVENT (A)
                    her "Да, дала, сэр..."
                    m "Ну же? Расскажи."
                    her "Ну, вообще-то, мало чего рассказывать..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_31.png", pos )
                    her "Я сказала одному парню, что он может немного меня потрогать, если захочет..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_29.png", pos )
                    her "Сначала он подумал, что это шутка..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_33.png", pos )
                    her "Так стыдно..."
                    m "Так он трогал тебя или нет?"
                    $herView.hideQQ()
                    $herView.showQQ( "body_33.png", pos )
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Да, трогал..."
                    m "Ну и где же он тебя трогал?"
                    $herView.hideQQ()
                    $herView.showQQ( "body_29.png", pos )
                    her "Эм... мои ноги..."
                    her "И мою грудь, немного..."
                    m "Это всё?"
                    $herView.hideQQ()
                    $herView.showQQ( "body_31.png", pos )
                    her "Да, сэр..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_33.png", pos )
                    her "Уже поздно... я думаю мне пора..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_34.png", pos )
                    her "Извините, сэр..."
                    m "Тебе не стоит извиняться, девочка."
                    m "Ты молодец. Этого достаточно... пока что..."
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    stop music fadeout 3.0
                    $herView.hideQQ()
                    $herView.showQQ( "body_69.png", pos )
                    her "Я сделала это, сэр!"
                    her "Но это было так отвратительно и стыдно..."
                    m "Это всё, что ты хочешь сообщить мне?."
                    m "Лучше расскажи где он тебя трогал..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Эм..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_117.png", pos )
                    her "Ну, он трогал меня под юбкой, немного..."
                    her "Я дала ему потрогать мою..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_118.png", pos )
                    her "...киску, через юбку, сэр."
                    m "Хорошо. Что было потом?"
                    $herView.hideQQ()
                    $herView.showQQ( "body_131.png", pos )
                    her "Затем он начал трогать себя..."
                    her "И я решила уйти..."
                    m "Ясно..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_33.png", pos )
                    her "............."
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    her "Я сделала это, сэр..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_31.png", pos )
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Я завела одного парня из \"Пуффендуя\" в пустую комнату и предложила ему потрогать себя, если он захочет."
                    her "И..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_29.png", pos )
                    her "..........."
                    m "И?"
                    $herView.hideQQ()
                    $herView.showQQ( "body_31.png", pos )
                    her "Ну, он сначала трогал меня..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_33.png", pos )
                    her "......"
                    m "Не заставляй меня вытаскивать из тебя каждое слово!"
                    m "Что произошло потом?"
                    $herView.hideQQ()
                    $herView.showQQ( "body_87.png", pos )
                    her "Ну..."
                    stop music fadeout 1.0
                    her "Я думала ему понравилось лапать {size=+5}меня{/size} {size=+5}собой{/size}..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_44.png", pos )
                    her "Он просил меня называть его \"Сисястым мальчиком\"..."
                    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
                    $herView.hideQQ()
                    $herView.showQQ( "body_31.png", pos )
                    her "И потом он рассказал мне, что у него очень маленький член..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_22.png", pos )
                    her "Он просто повторял это *всхлип*..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_21.png", pos )
                    her "Почему есть такие идиоты, как он?"
                    her "*Хнык!* Я больше не могла находиться рядом с ним и убежала...."
                    m "Извините, что рассказываю вам это..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_21.png", pos )
                    her "Это было просто ужасно, сэр..."
                    m "Ладно тебе, ладно..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_23.png", pos )
                    her "*Хнык!*"
                    m "Если я накину тебе 10 дополнительных очков, тебе будет легче?"
                    $herView.hideQQ()
                    $herView.showQQ( "body_19.png", pos )
                    her "М? Это было бы мило с вашей стороны."
                    $ gryffindor += 10
                    m "Конечно... 10 дополнительных очков \"Гриффиндору\"."
                    $herView.hideQQ()
                    $herView.showQQ( "body_140.png", pos )
                    her "Спасибо, сэр..."
                    m "А вот и остальные баллы..."
            
            elif whoring >= 9 and whoring <= 11: # LEVEL 04
                if one_out_of_three == 1: ### EVENT (A)
                    $herView.hideQQ()
                    $herView.showQQ( "body_16.png", pos )
                    her "Ну... Тут нечего рассказывать..."
                    her "Я нашла одного мальчика из \"Когтерван\"..."
                    her "Завела его в свободную аудиторию в восточном крыле..."
                    her "Он подумал, что я хочу посмотреть на его мускулы..."
                    her "Но я сказала, что хочу, что бы он потрогал меня..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_33.png", pos )
                    her "...ну и он начал меня трогать."
                    m "Ясно..."
                    m "Хорошая работа, Мисс Грейнджер."
                    $herView.hideQQ()
                    $herView.showQQ( "body_44.png", pos )
                    her "Я получу свои очки, сэр?"
                    m "Одну минуту, мисс Грейнджер. Я хочу получить ответ на вопрос, который сейчас задам."
                    $herView.hideQQ()
                    $herView.showQQ( "body_31.png", pos )
                    her "???"
                    m "Вам понравилось?"
                    m "Вам понравилось то чувство, когда он трогал вас?"
                    $herView.hideQQ()
                    $herView.showQQ( "body_127.png", pos )
                    her "Хм..."
                    her "Ну, он был симпатичным..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_120.png", pos )
                    her "Я не злилась на него за то, что он трогает меня, если вы это хотели услышать, сэр..."
                    m "Ясно..."
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    $herView.hideQQ()
                    $herView.showQQ( "body_16.png", pos )
                    her "Ну..."
                    her "Я не уверена в том, что вы это хотите услышать, но..."
                    her "Во время того, как нас учили собирать траву..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_44.png", pos )
                    her "Я дала одному парну дотронуться до себя под юбкой..."
                    her "И пока профессор Стебель обьясняла разницу между \"мандрейк\" и \"мандрагоры\"..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_08.png", pos )
                    her "Конечно, кое что я уже знала..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_44.png", pos )
                    her "Я дала потрогать своему партнеру по лабораторным мою попу..."
                    her "Ну, вот и всё..."
                    m "Хм..."
                    menu:
                        "\"Ты могла бы и постараться, что бы выполнить задание.\"":
                            $herView.hideQQ()
                            $herView.showQQ( "body_31.png", pos )
                            her "Да, я знаю, извините."
                            m "Просто в следующий раз приложи больше усилий."
                            her "Хорошо, я постараюсь, сэр."
                        "\"Хвалю, что сделала это во время занятий.\"":
                            $herView.hideQQ()
                            $herView.showQQ( "body_74.png", pos )
                            her "Спасибо, сэр."
                            m "Вижу, что ты заслужила награду."
                            
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    $herView.hideQQ()
                    $herView.showQQ( "body_69.png", pos )
                    her "................."
                    m "???"
                    $herView.hideQQ()
                    $herView.showQQ( "body_69.png", pos )
                    
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    
                    her "Я не хочу говорить об этом, сэр..." 
                    m "Что случилось, малышка? Выговорись."
                    $herView.hideQQ()
                    $herView.showQQ( "body_79.png", pos )
                    her "................."
                    $herView.hideQQ()
                    $herView.showQQ( "body_31.png", pos )
                    her "Но... мне так стыдно..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_33.png", pos )
                    her "Мне правда нужно рассказывать, сэр?"
                    m "Да, я люблю слушать такие вещи!"
                    $herView.hideQQ()
                    $herView.showQQ( "body_69.png", pos )
                    her "................."
                    her "Ладно..."
                    her "Я подошла к парню, которого всегда считала привлекательным..."
                    her "Нашла в себе силы и попросила его идти за мной..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_31.png", pos )
                    her "Обычно, я бы даже не подошла к нему..."
                    her "Но тот факт, что я выполняю задание, каким-то образом заставил меня собрать свою волю в кулак..."
                    her "Это придало мне смелости..."
                    m "Рад помочь, Мисс Грейнджер."
                    $herView.hideQQ()
                    $herView.showQQ( "body_87.png", pos )
                    her "Я завела его в библиотеку..."
                    her "Мы нашли тихое место, между книжными шкафами..."
                    her "И я сказала ему, что он может трогать меня как пожелает..."                 
                    her "И...."
                    $herView.hideQQ()
                    $herView.showQQ( "body_88.png", pos )
                    her ".........."
                    m "Что?"
                    $herView.hideQQ()
                    $herView.showQQ( "body_33.png", pos )
                    her "....................."
                    $herView.hideQQ()
                    $herView.showQQ( "body_32.png", pos )
                    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
                    her "Он начал трогать мои... ноги, сэр."
                    m "Эм?"
                    m "Ваши \"ноги\"? Это как тот малый с большими сиськами на днях?"
                    $herView.hideQQ()
                    $herView.showQQ( "body_66.png", pos )
                    her "Нет, сэр..."
                    her "Он попросил, чтобы я сняла свою обувь..."
                    her "Потом он..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_21.png", pos )
                    her "Он стал нюхать мои лодыжки, сэр!"
                    $herView.hideQQ()
                    $herView.showQQ( "body_22.png", pos )
                    her "Я почувствовала себя такой... разбитой!"
                    m "И он даже не притронулся к твоей груди или попке?"
                    $herView.hideQQ()
                    $herView.showQQ( "body_143.png", pos )
                    her "Нет, сэр... *хнык!*"
                    m "Ладно, что случилось потом?"
                    $herView.hideQQ()
                    $herView.showQQ( "body_142.png", pos )
                    her "Ничего! Я не выдержала этого унижения и... убежала..."
                    her "Я даже забыла там свою обувь и спустя пару часов пришлось возвращаться за ней..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_145.png", pos )
                    her "*Хнык!*............"
                    m "Хм..."
                    m "Получается он тебя облапал..."
                    m "Правда, немного в своеобразной манере..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_145.png", pos )
                    her "*Хнык!* Как бы я хотела, что бы он просто потрогал мою грудь или попу, как обычный мальчик, сэр... *Хнык!*"
                    m "Успокойся, успокойся..."
                    m "Ты заработала свою награду сегодня..."
        
        
        
            elif whoring >= 12: # LEVEL 05+
                if one_out_of_three == 1: ### EVENT (A)
                    stop music fadeout 1.0
                    $herView.hideQQ()
                    $herView.showQQ( "body_29.png", pos )
                    her "......"
                    $herView.hideQQ()
                    $herView.showQQ( "body_31.png", pos )
                    her "Ну..."
                    her "Во время зельеварения, сегодня..."
                    her "Я написала записку на клочке бумаги..."
                    her "И передала её моему партнёру по лабораторным работам, и затем..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_69.png", pos )
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Профессор Снейп вытащил её из моей руки..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_79.png", pos )
                    her "Он прочитал её перед всем классом, который был полностью заполнен..."
                    m "О чем говорилось в записке?"
                    $herView.hideQQ()
                    $herView.showQQ( "body_87.png", pos )
                    her "Ну..."
                    her "Там было сказано: \"Ты можешь потрогать мою попку, если захочешь. Я думаю, Профессор Снейп не догадается.\""
                    $herView.hideQQ()
                    $herView.showQQ( "body_118.png", pos )
                    her "Все сильно смеялись..."
                    her "Было так стыдно, что я хотела провалиться на месте..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_47.png", pos )
                    her "Я ненавижу профессора Снейпа, сэр..."
                    m "Что случилось потом?"
                    $herView.hideQQ()
                    $herView.showQQ( "body_87.png", pos )
                    her "Ничего..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Но, когда закончились занятия..."
                    her "Я заметила, как три парня из \"Слизерин\" жадно и пошло смотрят на меня..."
                    her "Вообще-то они для меня ничего не значат..."
                    her "Поэтому мы ждали, пока все выйдут из класса..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_117.png", pos )
                    her "И потом я дала им потрогать себя..."
                    her "Они трогали меня везде, профессор..."
                    m "\"Везде\"?"
                    her "Да... Везде, сэр..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_128.png", pos )
                    her "Их руки были под моей юбкой, под моей блузкой..."
                    her "И потом моё дыхание участилось..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_121.png", pos )
                    her "И один из них засунул свои пальчики ко мне в рот..."
                    her "И их прикосновения были такими... ненасытными..." 
                    her "У меня аж закружилась голова..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_128.png", pos )
                    her "Это было очень возбуждающе, сэр."
                    m "Очень хорошо, Мисс Грейнджер. Просто прекрасно."
                    
                    
                if one_out_of_three == 2: ### EVENT (B)
                    $herView.hideQQ()
                    $herView.showQQ( "body_01.png", pos )
                    her "Вообще-то, кое что необычное произошло сегодня со мной, сэр..."
                    her "После занятий по Защите от темных чар..."
                    her "Ко мне подошёл коренастый парень из \"Пуффендуя\"..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_122.png", pos )
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Он рассказал, что до него дошли слухи, что я даю мальчикам трогать себя..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_128.png", pos )
                    her "Обычно, я бы даже ничего не сделала..."
                    her "Но я решила не упускать возможность..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_78.png", pos )
                    her "Я завела парня в тихое место и разрешила ему потрогать себя..."
                    her "Я позволила ему потрогать меня под одеждой..."
                    her "Потом попросила ему потрогать мою грудь..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_128.png", pos )
                    her "Ну, в общем, как обычно..."
                    m "Отлично, мисс Грейнджер."
                    
                if one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    $herView.hideQQ()
                    $herView.showQQ( "body_44.png", pos )
                    her "Ну..."
                    her "Я сделала то, о чем вы меня просили, сэр..."
                    her "Но... в некотором роде... эм..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_78.png", pos )
                    her "Но, в некотором роде, это задание перешло в кое что другое..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    m "Хм?"
                    $herView.hideQQ()
                    $herView.showQQ( "body_44.png", pos )
                    her "Хм..."
                    her "Ну, в общем... я была поймана за тем, что давала трогать свою грудь одному мальчику..."
                    m "Ты была поймана? Учителем?"
                    $herView.hideQQ()
                    $herView.showQQ( "body_45.png", pos )
                    her "Нет, сэр..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_46.png", pos )
                    her "Девушкой этого парня..."
                    m "Интересно..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_117.png", pos )
                    her "Сначала, она была зла на него..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_122.png", pos )
                    her "Но потом..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_124.png", pos )
                    her "Эмм... Она начала трогать мою грудь..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_111.png", pos )
                    her "Точно так же, как минуту назад меня трогал её парень..."
                    her "Затем она повернулась к нему и сказала..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_16.png", pos )
                    her "\"Я люблю тебя, дорогой, И хочу разделить с тобой всё...\""
                    her "\"...включая твоих шлюх.\""
                    $herView.hideQQ()
                    $herView.showQQ( "body_117.png", pos )
                    her "Я была возмущена тем, что она назвала меня шлюхой..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_06.png", pos )
                    her "Но это был такой милый и романтический жест..."
                    her "Вы согласны со мной, сэр?"
                    m "Абсолютно..."
                    m "Вот, что значит настоящая любовь - она {size=+5} должна {/size} проходить через всё."
                    m "И что же случилось потом?"
                    $herView.hideQQ()
                    $herView.showQQ( "body_24.png", pos )
                    her "Эм... Они поцеловались, конечно же..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_44.png", pos )
                    her "И парень начал трогать меня снова..."
                    $herView.hideQQ()
                    $herView.showQQ( "body_29.png", pos )
                    her "И потом он трогал её и она трогала его..."
                    her "И они целовались..."
                    her "Я почувствовала себя третьей лишней и решила тихо удалиться......"
                    m "Ясно..."
                    

    $ gryffindor +=25
    m " \"Гриффиндор\" получает 25 очков!"
    her "Спасибо, сэр."
    
    hide screen bld1
    $herView.hideQ()
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3

    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)



    $ touched_by_boy = True #Makes sure that Public favours do not get locked after reaching Whoring level 05.
    
    call music_block
    
    $ request_10_points += 1 
    $ request_10 = False 
    $ hermione_sleeping = True
    return



