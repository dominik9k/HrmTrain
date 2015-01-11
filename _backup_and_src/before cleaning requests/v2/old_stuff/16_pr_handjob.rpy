#############################################################################################################################
### LEVEL 05 ################################################################################################################   
###################REQUEST_16 (Level 05) (HANDJOB) (Day/Night) #####################################################
label new_request_16: #LV.5 (Whoring = 12 - 14)
    #__#hide screen hermione_main 
    #__#with d3
    $herView.hideQQ()
    if request_16_points == 0:
        m "{size=-4}(Попросить ее вздрочнуть мне?){/size}"
    else:
        m "{size=-4}(Попросить ее еще раз подрочить мне?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Да, давай попробуем!)\"":
            show screen blktone
            with d3
            pass
        "\"(Не сейчас.)\"":
            jump new_personal_request
            
    
    s = POS_140
    
    $ current_payout = 45 #Used when haggling about price of th favor.  
    if request_16_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "Мисс Грейнджер."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ pos = POS_140
        #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                    #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_01.png", pos )
        her "Да, профессор?"
        m "Ты знаешь что такое \"работа ручками\"?"
        if whoring <=11:
            jump too_much
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                    #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                    
        $herView.showQQ( "body_79.png", pos )
        her "А что?"
        m "Я хочу, чтобы ты сделала это мне..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                    #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                    
        $herView.showQQ( "body_47.png", pos )
        her "Профессор!"
        m "Просто одна услуга. Ничего страшного, да?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                    #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                    
        $herView.showQQ( "body_66.png", pos )
        her "......"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                    #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                    
        $herView.showQQ( "body_34.png", pos )
        her "{size=-7}Я хочу 100 очков за это...{/size}"
        m "А? Что это было?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                    #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                    
        $herView.showQQ( "body_32.png", pos )
        her "Я хочу 100 очков за это!!!"
        m "100 очков, да?"
        m "И ты подрочишь мне и все такое, правильно?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                    #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                    
        $herView.showQQ( "body_66.png", pos )
        her "{size=-7}Да...{/size}"
        m "Прости, я не расслышал..."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                    #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                 
        $herView.showQQ( "body_32.png", pos )
        her "Да, я сказала да! Я подрочу вам, сэр!"
        label back_to_handjob_choices:
        menu:
            m "..."
            "\"Ты получишь 15 очков.\"":
                $ mad +=7
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__# h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                    #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                 
                $herView.showQQ( "body_69.png", pos )
                her "За 15 очков вы сможете немного поприставать ко мне, но это все, сэр."
                her "Я не продешевлю и не стану дрочить вам за 15 очков."
                her "Это оскорбительно, сэр."
                jump back_to_handjob_choices
            "\"Ты получишь 45 очков.\"":
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                 
                $herView.showQQ( "body_69.png", pos )
                her "....."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                    #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                 
                $herView.showQQ( "body_87.png", pos )
                her "45 очков...?"
                her "Это вернет \"Гриффиндор\" в лидеры..."
                m "Это значит \"Да\"?"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                    #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                 
                $herView.showQQ( "body_79.png", pos )
                her "Да! Это значит да, сэр."
                m "Отлично!"
            "\"Ты получишь 100 очков.\"":
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $ current_payout = 100 #Used when haggling about price of th favor.
                $ mad = 0
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_72.png" #Sprite of Hermione's upper body.                    #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                 
                $herView.showQQ( "body_72.png", pos )
                her "100 очков?!"
                her "Это вернет \"Гриффиндор\" в лидеры!"
                m "Это значит \"Да\"?"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_75.png" #Sprite of Hermione's upper body.                    #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                 
                $herView.showQQ( "body_75.png", pos )
                her "Конечно!"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_80.png" #Sprite of Hermione's upper body.                    #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                 
                $herView.showQQ( "body_80.png", pos )
                her "Если это принесет \"Гриффиндору\" 100 очков, то я согласна прикасаться... к вашей штуке."
        # GENIE STANDS WITH HIS COCK OUT
       
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        $herView.hideQ() #"WARNING_Z"
        hide screen genie
        $ genie_chibi_xpos = 5 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen chair_02
        show screen g_c_u
        show screen desk_02

        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        show screen bld1
        with d3
        #__#$ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        #__#$ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
		$ posHead = gMakePos( 390, 235 )        
        #__#show screen h_head2                                                             # HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
        $herViewHead.showQ( "body_31.png", posHead )
        her "..........."
        hide screen h_head2
        m "Начинай, как будешь готова, девочка."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
        her "Верно..."
        hide screen h_head2
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause.1
        show screen blkfade
        with Dissolve(1)
        pause.3
        label event_01_round_02:
        ">Гермиона берет своими худыми ручками ваш член..."
        m "Отлично. Теперь дрочи его."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
        her "Ага..."
        hide screen h_head2 
        #Stroking the cock.
        $ genie_chibi_xpos = 60 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "handjob_ani"
        hide screen hermione_walk_01 
        hide screen blkfade
        with d3
        show screen ctc
        pause
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        hide screen ctc
        show screen bld1
        with d3
        g9 "Отлично..."
        if request_16_points == 0:
            show screen h_head2                                                             # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
            her "!!!"
            her "Как насчет кончить, сэр?!"
            hide screen h_head2 
            m "Кончить?"
            m "Не будь глупа, мы только начали."
            show screen h_head2                                                             # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
            her "Ох..."
            her "......"
            show screen h_head2                                                             # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_44.png" # HERMIONE
            her2 "Вы предупредите меня, сэр?"
            hide screen h_head2 
        else:
            show screen h_head2                                                             # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
            her "Сэр...?"
            hide screen h_head2    
            m "Что такое?"
            show screen h_head2                                                             # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
            her "Вы могли бы предупредить меня... э-эм... когда вы..."
            hide screen h_head2    
        $ d_flag_01 = False #If TRUE Genie promised to warn her.
        menu:
            m "..."
            "\"Конечно я скажу тебе, когда буду готов.\"":
                $ d_flag_01 = True #If TRUE Genie promised to warn her.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Спасибо, сэр."
                hide screen h_head2 
            "\"Я и сам не всегда уверен...\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Правда? Но я думала..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Ну, тогда ладно..."
                hide screen h_head2 
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
        her "........"
        hide screen h_head2 
        m "............."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
        her "............."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
        her "Э-э... сэр?"
        hide screen h_head2 
        m "Да, что такое?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
        her "Как долго мне придется это делать?"
        hide screen h_head2 
        m "В смысле?"
        if daytime:
            show screen h_head2                                                             # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_44.png" # HERMIONE
            her2 "Просто, мои занятия вот-вот начнутся..."
        else: 
            show screen h_head2                                                             # HERMIONE
            $ h_body = "03_hp/13_hermione_main/body_44.png" # HERMIONE
            her2 "Ну, мне нужно заниматься, и хотелось бы это закончить побыстрее..."
            her2 "Завтра рано вставать, а уже довольно поздно..."
        hide screen h_head2 
        m "Вам нужны очки или нет?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_74.png" # HERMIONE
        her "Да, сэр! Мне жаль..."
        her "Просто я никогда не дрочила мужчине..."
        hide screen h_head2 
        m "Ну, есть кое-что, чтобы ускорить процесс..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_45.png" # HERMIONE
        her "Правда? Что это, сэр?"
        hide screen h_head2 
        menu:
            m "..."
            "\"Скажи мне насколько ты распутная шлюха!\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_47.png" # HERMIONE
                her "Что?"
                her "Но я не..."
                hide screen h_head2 
                m "Не нужно быть честной, девочка."
                m "Просто сделай это."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_44.png" # HERMIONE
                her "Правда?"
                hide screen h_head2 
                m "Конечно. Мы немного повеселимся."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Ну, раз так..."
                her "Я... я шлюха."
                hide screen h_head2 
                m "Хех... великолепно. Продолжай."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Я самая большая шлюха..."
                hide screen h_head2 
                m "Да, именно."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_79.png" # HERMIONE
                her "Я самая распутная шлюха во всей Англии!"
                her2 "Я пытаюсь казаться невинной, но на самом деле все, о чем я думаю, это члены!"
                hide screen h_head2 
                m "Да, ты малолетняя шлюха!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_69.png" # HERMIONE
                her "Да! Я шлюха!"
                her "Я постоянно жажду о членах."
                hide screen h_head2 
                m "Очень хорошо!"
                m "Но,как я уже сказал, не нужно быть честной."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "Что?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_44.png" # HERMIONE
                her "сэр, все это неправда!"
                hide screen h_head2 
                g9 "Хех... Я знаю. Я просто шучу."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_66.png" # HERMIONE
                her "сэр!"
                hide screen h_head2 
                m "Ты все делаешь отлично. Продолжай!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "....."
                her "Я обожаю члены..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_88.png" # HERMIONE
                her "И я люблю когда... меня шлепают..."
                her "И сперму..."
                her "Я люблю глотать сперму..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_65.png" # HERMIONE
                her "Я хочу, чтобы вы меня накормили спермой, сэр!"
                hide screen h_head2 
                g4 "!!!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_64.png" # HERMIONE
                her2 "Или лучше, наполните меня ею, сэр!"
                hide screen ctc
                hide screen h_head2 
                with hpunch
                g4 "{size=-4}(Я почти! Стоит мне предупредить ее?){/size}"
            
            "\"Высунь свой язык и смотри на меня!\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_45.png" # HERMIONE
                her "Что?"
                hide screen h_head2 
                m "Просто сделай это, шлюха."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_38.png" # HERMIONE
                her "Вот так?"
                hide screen h_head2 
                m "Да, отлично. Продолжай смотреть мне в глаза и дрочи."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_115.png" # HERMIONE
                her "....................."
                hide screen h_head2 
                m "Да... Отлично..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_115.png" # HERMIONE
                her "..........."
                her "..........."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her2 "Я не могу так долго сидеть с открытым ртом. У меня потекут слюни..."
                hide screen h_head2 
                m "Но я хочу, чтобы они потекли..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Что? Я буду выгядеть глупо!"
                hide screen h_head2 
                m "Именно это мне и нужно, девочка!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
                her "......."
                hide screen h_head2 
                m "Разве ты не хочешь, чтобы я кончил как можно быстрее?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "............"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_115.png" # HERMIONE
                her "А-ха....."
                hide screen h_head2 
                m "Отлично."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_115.png" # HERMIONE
                her ".............."
                hide screen h_head2 
                m "Да, продолжай дрочить мой член."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_115.png" # HERMIONE
                her ".................."
                hide screen h_head2
                g4 "Ох... Я хочу проскользнуть членом в твой влажный ротик!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_40.png" # HERMIONE
                her "................."
                hide screen h_head2 
                m "Нет, смотри на меня!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_115.png" # HERMIONE
                her "....................."
                hide screen h_head2 
                m "Да, маленькая шлюха!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_116.png" # HERMIONE
                her "......................"
                hide screen h_head2 
                m "Я хочу кончить в этот ротик, да..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_116.png" # HERMIONE
                her "................"
                hide screen h_head2 
                with hpunch
                g4 "{size=-4}(Я почти! Стоит мне предупредить ее?){/size}"
            "\"Поцелуй мой член!\"":
                show screen h_head2                                                               # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_47.png" # HERMIONE
                her "Простите?"
                hide screen h_head2 
                m "Ты поняла, просто поцелуй, своими губами."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_47.png" # HERMIONE
                her "............."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "...губами?"
                hide screen h_head2 
                m "Конечно... это очень ускорит приближение конца."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "*вздох!*.............."
                her "Ну, я бы могла попробовать, наверное..."
                hide screen h_head2 
                ">Гермиона нежно целует вашу головку."
                
                $ g_c_u_pic = "kiss_ani"
                $ renpy.play('sounds/kiss.mp3') 
                with kissiris
                pause
                show screen blkfade
                with d3
                $ g_c_u_pic = "handjob_ani"
                hide screen blkfade
                with d3

                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Вот так?"
                hide screen h_head2 
                m "Не так уж и плохо, правда?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_44.png" # HERMIONE
                her "Нет, кажется нет..."
                hide screen h_head2 
                m "Можешь это сделать снова?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Вероятно..."
                hide screen h_head2 
                m "Сделай это!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Ну, ладно..."
                hide screen h_head2
                ">Гермиона еще раз целует головку вашего члена..."
                $ g_c_u_pic = "kiss_ani"
                $ renpy.play('sounds/kiss.mp3') 
                with kissiris
                pause
                ">В этот раз поцелуй длится чуть дольше..."
                show screen blkfade
                with d3
                $ g_c_u_pic = "handjob_ani"
                hide screen blkfade
                with d3

                hide screen h_head2 
                m "Великолепно... Теперь сделай это еще разочек, но еще дольше."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Вы имеете в виде, поцеловать ваш... член, сэр?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
                her "Нет, я выгляжу глупо..."
                hide screen h_head2 
                m "Не глупи, девочка. Никто не смотрит."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Вы, сэр."
                hide screen h_head2 
                m "Но в этом весь смысл!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_79.png" # HERMIONE
                her "......"
                hide screen h_head2 
                m "Это поможет мне кончить почти сразу же!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_69.png" # HERMIONE
                her "..............."
                hide screen h_head2 
                m "И после этого вы сможете просто уйти, не заботясь о наших делах на сегодня."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_66.png" # HERMIONE
                her "............."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Ну, тогда ладно...."
                hide screen h_head2
                ">Гермиона снова касается вашего члена своими губками..."
                ">Она косается головки вашего члена своими губами и остается в таком положении..."
                $ g_c_u_pic = "kiss_ani"
                $ renpy.play('sounds/kiss.mp3') 
                with kissiris
                pause
                hide screen h_head2 
                show screen blktone
                with d3
                m "Очень хорошо..."
                m "Теперь дотронься до него языком."
                her "??!"
                hide screen h_head2 
                m "Это последнее, что я попрошу на сегодня."
                her "............"
                ">Вы чувствуете, как кончик языка Гермионы мягко касается головки вашего члена..."
                hide screen h_head2 
                m "Да, Вот так..."
                ">Гермиона немного шевелит своим язычком...."
                hide screen h_head2 
                m "Да... Отлично..."
                show screen blkfade
                with d3
                $ g_c_u_pic = "handjob_ani"
                hide screen blkfade
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her2 "Ну, сработало? Вы готовы... кончить, профессор?"
                hide screen h_head2 
                g4 "{size=-4}(Удивительно, но да! Я сейчас кончу! Мне стоит предупредить ее?){/size}"
                hide screen blktone
        menu:
            m "..."
            "- Предупредить ее -":
                g4 "Почти кончил! Тебе лучше подготовиться!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "Что? Так быстро?!"
                hide screen h_head2 
                g4 "{size=+5}Да, отличная работа!!!{/size}"
                g4 "{size=+5}Маленькая шлюха!!!{/size}"
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade 
                with d5
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Нет, профессор, подождите, Я--"
                hide screen h_head2 
                g4 "{size=+5}Слишком поздно, шлюха!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her2 "*хныкает*"
                hide screen h_head2       
                ">Гермиона резко засовывает ваш член себе под рубашку..."
                g4 "?!!"
                ">Ощущение трения вашего члена о ее мягую, теплую кожу переполняет вас и вы люто извергаетесь спермой."
                hide screen h_head2 
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}АРГХ! ДА!!!{/size}"
              
                
                
                
                
                
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!!!!!!!!!!"
                hide screen h_head2 
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "undershirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                stop music fadeout 1.0
                pause 
                        
                $ aftersperm = True
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=300 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_119.png" # HERMIONE
                her2 "......................."
                hide screen h_head2                
                m "..........................."
                show screen h_head2                   
                $ h_body = "03_hp/13_hermione_main/body_119.png" # HERMIONE
                her2 "......................."
                hide screen h_head2    
                m "....................?"
                show screen h_head2                   
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her2 "......................."
                hide screen h_head2    
                m "...Что за херня сейчас произошла?"
                show screen bld1
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her "Я не знаю... Я запаниковала..."
                hide screen h_head2    
                if daytime:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
                    her2 "Мои занятия вот-вот начнутся и я не хотела, чтобы вы испортили мою форму..."
                    hide screen h_head2 
                    m "И ты пойдешь на занятия вот так?"
                    m "В форме, полной изнутри спермы?"
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                    her2 "У меня есть другой выбор?"
                    her2 "Я могу просто пропустить занятия..."
                    hide screen h_head2
                else:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
                    her2 "Сейчас общая комната \"Гриффиндора\" будет полна людей..."
                    her2 "И я не хотела бы вернуться туда покрытой вашей спермой, сэр."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                    her2 "Ох, становится поздно..."
                    hide screen h_head2 
                    m "И ты вот так пойдешь?"
                    m "В форме, полной изнутри спермы?"
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                    her "У меня есть другой выбор?"
                    hide screen h_head2     
                    
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                ">Гермиона отпускает ваш все еще пульсирующий член."
                
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                show screen genie
                hide screen g_c_u
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Фи... Ваша сперма, сэр..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Она везде на форме..."
                hide screen h_head2          
                m "Просто вставляй его в рот в следующий раз."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_79.png" # HERMIONE
                her "Я... так не думаю, сэр."
                her "Мне правда нужно идти. Могу я получить свои очки?"
                hide screen h_head2   
                
                
                
                
                
                
#                g4 "You whore! You little nasty wore!"
#                g4 "There! Allover your fucking belly and tits!"
#                her "Ah! It's so hot!"
#                hide screen h_head2 
#                g4 "Ох, yes, this is so good!"
#                her "Ah..."
#                hide screen h_head2 
#                m "..............."
#                her "............"
#                hide screen h_head2 
#                m "I think I'm done..."
#                her "Ох..."
#                ">Hermione releases your still pulsating cock."
#                her "Ew... Your sperm, сэр..."
#                her "It's everywhere under my uniform..."
#                hide screen h_head2 
#                m "What possessed you to put my cock there, м?"
                

            "- Просто начать кончать -":
                hide screen ctc
                with hpunch
                g4 "АРГХ!"
                show screen blkfade
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "ЧТО?!"
                hide screen h_head2               
                g4 "Так тебе!"

                hide screen h_head2 
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}АРГХ! ДА!!!{/size}"
                
                
                
                  
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!!!!!!!!!!"
                hide screen h_head2 
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "on_shirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                show screen ctc
                hide screen bld1
                with d3
                pause
                show screen bld1
                with d3
                        
                $ aftersperm = True
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=300 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_119.png" # HERMIONE
                her2 "......................."
                hide screen h_head2          
                m "Да... Теперь мне лучше..."
                pause
                $ g_c_u_pic = "03_hp/08_animation_02/15_cum_21.png"
                
                $ u_sperm = "03_hp/13_hermione_main/auto_06.png"
                $ uni_sperm = True
                
                $ pos.xpos = 130
                #__#$ h_xpos=130 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                #__#$ h_body = "03_hp/13_hermione_main/body_19.png" #Flashing Трусики
                #__#show screen hermione_main
                $herView.showQ( "body_19.png", pos ) #"WARNING_Z"
                with d5
                pause
                her ".........."
                m "Ну, я думаю это все..."
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                hide screen g_c_u
                show screen genie
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                $herView.hideQ() #"WARNING_Z"
                with fade                                                                                                                                                                                                                      #HERMIONE
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ pos = POS_140
                #__#$ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                 
                $herView.showQQ( "body_32.png", pos )
                her "Профессор! Что вы наделали?!"
                m "Что?"
                if d_flag_01: #If TRUE Genie promised to warn her.
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $ mad += 11
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                    #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    #__#with d3                 
                    $herView.showQQ( "body_47.png", pos )
                    her "Вы обещали предупредить меня, сэр!"
                    m "Ох, верно... Моя оплошность."
                    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    #__#with d3                                                                                                                                                                                                                        #HERMIONE
                    $herView.hideQQ()
                    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                    #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    $herView.showQ( "body_69.png", pos ) #"WARNING_Z"
                    her "Моя форма испорчена..."
                    her "...Я хочу получить свои очки."
                    #__#hide screen hermione_main     
                    #__#with d3
                    $herView.hideQQ()
                    $ uni_sperm = False
                else:
                    if daytime:
                        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                        #__#with d3                                                                                                                                                                                                                        #HERMIONE
                        $herView.hideQQ()
                        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                        #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                        $herView.showQ( "body_69.png", pos ) #"WARNING_Z"
                        her "Моя форма испорчена!"
                        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                        #__#with d3                                                                                                                                                                                                                        #HERMIONE
                        $herView.hideQQ()
                        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                        #__#$ h_body = "03_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                        $herView.showQ( "body_87.png", pos ) #"WARNING_Z"
                        her "Мои занятия вот-вот начнутся и я не могу вот так пойти на них!"
                        m "Конечно можешь, просто протри ее и все..."
                        m "Никто даже не заметит."
                        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                        #__#with d3                                                                                                                                                                                                                        #HERMIONE
                        $herView.hideQQ()
                        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                        #__#$ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                        $herView.showQ( "body_79.png", pos ) #"WARNING_Z"
                        her "...Я хочу получить свои очки."
                        #__#hide screen hermione_main     
                        #__#with d3
                        $herView.hideQQ()
                        $ uni_sperm = False
                    else:
                        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                        #__#with d3                                                                                                                                                                                                                        #HERMIONE
                        $herView.hideQQ()
                        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                        #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                        $herView.showQ( "body_69.png", pos ) #"WARNING_Z"
                        her "Моя форма испорчена!"
                        her "И как я вернусь в комнату \"Гриффиндора\" в таком виде?!"
                        m "Почему нет? Ты выглядишь горячо, девочка!"
                        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                        #__#with d3                                                                                                                                                                                                                        #HERMIONE
                        $herView.hideQQ()
                        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                        #__#$ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                        $herView.showQ( "body_79.png", pos ) #"WARNING_Z"
                        her "Профессор!!!"
                        m "Ладно, хорошо. Просто вытри ее и все."
                        m "Никто и не заметит."
                        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                        #__#with d3                                                                                                                                                                                                                        #HERMIONE
                        $herView.hideQQ()
                        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                        #__#$ h_body = "03_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                        $herView.showQ( "body_79.png", pos ) #"WARNING_Z"
                        her "...Я хочу получить свои очки."
                        #__#hide screen hermione_main     
                        #__#with d3
                        $herView.hideQQ()
                        $ uni_sperm = False
        #her "Могу я получить свои очки?"

    elif request_16_points == 1: # SECOND EVENT <============================================================== EVENT 02
        m "Мисс Грейнджер?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ pos = POS_140
        #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                    #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_01.png", pos )
        her "Да, сэр?"
        m "Что вы знаете о \"работе ручками\"?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                    #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_66.png", pos )
        her "Вы меня уже спрашивали, сэр."
        m "Ах, верно."
        m "Ну, я хочу, чтобы вы снова поиграли с моим членом."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_120.png", pos )
        her "сэр, вы опять начинаете пошлить..."
        m "Ладно, ладно."
        m "Мисс Грейнджер, как насчет некоторой услуги на сегодня."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_69.png", pos )
        her "Конечно, сэр."
        g9 "Услуга в том, что вы должны поиграть с моим членом!"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_66.png", pos )
        her ".............."
        m "Ох, да ладно. Ради чести \"Гриффиндора\"?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.showQQ( "body_47.png", pos )
        her "............."
        g9 "Поиграй с моим членом  ради чести \"Гриффиндора\"!"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                               
        $herView.showQQ( "body_86.png", pos )
        her "Хватит так говорить, сэр..."
        #Genie with his cock out
        m "Ну же, девочка, я же не прошу тебя сделать это за просто так."
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                               
        $herView.showQQ( "body_69.png", pos )
        her "......."
        stop music fadeout 4.0
        

        #__#hide screen hermione_main            
        $herView.hideQ() #"WARNING_Z"
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause.1
        show screen blkfade
        with Dissolve(1)
        pause.3                                                                                                                                                                      #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = 5 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen chair_02
        show screen g_c_u
        show screen desk_02
        hide screen blktone

        jump event_01_round_02


    elif request_16_points >= 2: # THIRD EVENT <========================================================================================================= EVENT 03

        $ new_request_16_03 = True #  Hearts
        
        m "Мисс Грейнджер?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                    #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                    
        $herView.showQQ( "body_01.png", pos )
        her "сэр?"
        m "Как насчет дрочки?"
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                        #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_68.png" #Sprite of Hermione's upper body.                    #HERMIONE
        #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
        #__#with d3                                                                                                                                                                    
        $herView.showQQ( "body_68.png", pos )
        her "Пока вы даете мне очки..."
        m "Ну, тогда начнем. Заработай пару очков."
        
        
        #__#hide screen hermione_main            
        $herView.hideQ() #"WARNING_Z"
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause.1
        show screen blkfade
        with Dissolve(1)
        pause.3

        hide screen genie
        $ genie_chibi_xpos = 5 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen chair_02
        show screen g_c_u
        show screen desk_02
        hide screen blktone
        
        
        
        ">Гермиона хватает ваш член своими худенькими пальчками..."
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=290 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_68.png" # HERMIONE
        stop music fadeout 3.0
        her "Вам нравится, когда я делаю вот так, сэр?"
        hide screen h_head2         
        g9 "Конечно, да! Очень хорошо!"
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        hide screen h_head2 
        #Stroking the cock.
        $ genie_chibi_xpos = 60 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "handjob_ani"
        hide screen hermione_walk_01 
        hide screen blkfade
        with d7
        show screen ctc
        pause
        hide screen ctc
        show screen bld1
        with d3

        m "Да, да, вот так..."
        m "Хм... Ты, однако, наловчилась."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_74.png" # HERMIONE
        her "Спасибо, сэр."
        her2 "Я поняла, что лучше я буду делать это качественнее и быстрее."
        hide screen h_head2      
        m "Хм..."
        menu:
            m "..."
            "\"Что ты думаешь о моем члене?\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "А?"
                her2 "Ох, он неплохой..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
                her2 "Мне нужно похвалить ваш член! Совсем забыла об этом!"
                hide screen h_head2         
                m "Ну, ты не должна--"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
                her "сэр, позвольте мне быть честной с вами..."
                hide screen h_head2         
                m "Да?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_111.png" # HERMIONE
                her "У вас самый большой пенис, который я только видела!"
                hide screen h_head2         
                m "Ну, я полагаю--"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_30.png" # HERMIONE
                her "Еще не все!"
                hide screen h_head2         
                m "Извиняюсь."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Ваш член настоько большой, что пугает меня!"
                hide screen h_head2      
                g9 "Ах ты маленькая потаскуха. Ты знаешь, что нужно говорить..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her "И конечно же я жажду его..."
                her2 "Любая женщина была бы рада ощутить его в себе!"
                hide screen h_head2         
                m "...а ты хороша!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_30.png" # HERMIONE
                her "Есть еще!"
                hide screen h_head2         
                m "Несмотря ни на что..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_30.png" # HERMIONE
                her2 "Я думаю, что ваш член это благословение для всего мира!"
                hide screen h_head2         
                m "Ну, не стал бы так преувеличивать--"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_30.png" # HERMIONE
                her2 "Послушайте меня, сэр!"
                her2 "Я считаю, что стоит установить статуи в каждом городе на земле, посвященные вашему члену!"
                her2 "Так, чтобы люди всео мира могли поклоняться вашему члену!"
                hide screen h_head2         
                m "Ладно, Я услышал достаточно."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Слишком?"
                hide screen h_head2         
                m "Ага, немного."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_34.png" # HERMIONE
                her "Простите..."
                hide screen h_head2         
                m "Ничего. Продолжай дрочить."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her2 "................."
                hide screen h_head2  
                show screen blktone
                with d3
                ">Гермиона продолжает дрочить ваш член."
                ">у нее это отлично получается."  
                hide screen blktone
                with d3
                m "Да, да... Вот так."
                
            "\"Назови себя шлюхой!\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Простите?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_17.png" # HERMIONE
                her2 "Ох, точно! Я должна унижать себя, да?"
                hide screen h_head2  
                m "Ну, не обязательно, но..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
                her2 "Это отлично, я не возражаю."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_45.png" # HERMIONE
                her "И так. Я шлюха!"
                hide screen h_head2  
                m "Отлично. Рад, что мы выяснили это."
                m "Теперь, я хочу, чтобы ты сказала..."
                menu:
                    m "..."
                    "\"Я дешевая шлюха!\"":
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                        her "Конечно."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "Я дешевая шлюха."
                        her "Грязная маленькая шлюшка, вот кто я."
                        hide screen h_head2  
                        m "Да! Отлично!"
                    "\"Я живу, чтобы сосать член!\"":
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                        her "Эмм..."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_45.png" # HERMIONE
                        her2 "Я живу, чтобы сосать пенис... То есть член..."
                        hide screen h_head2  
                        m "Правда? Почему тогда ты сейчас его не отсасываешь?"
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_111.png" # HERMIONE
                        her2 "Сэр, Я просто отвечаю вам..."
                        hide screen h_head2  
                        m "Да ну? Может ты меня обманываешь...."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                        her2 "...................."
                        hide screen h_head2
                        m ".................."
                    "\"Я люблю глотать сперму!\"":
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                        her "Я люблю... Эм... глотать сперму."
                        hide screen h_head2  
                        m "Вы как-то неуверенно это произносите."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                        her "Да, я знаю...."
                        her "Дайте мне начать снова..."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "Я люблю глотать сперму!"
                        her "Глотать сперму - это самое лучшее!"
                        her "Я люблю это!"
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                        her2 "..................................."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                        her "Как вам это, сэр?"
                        hide screen h_head2  
                        m "Идеально." 
            "\"Это действительно неплохо. Ты практиковалась?\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_74.png" # HERMIONE
                her "Хм?"
                her "Вроде... На самом деле нет..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Я говорила с девочками, и..."
                hide screen h_head2    
                m "Про мастурбацию?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_80.png" # HERMIONE
                her "Помимо других вещей..."
                hide screen h_head2    
                m "Так эти твои подружки, они много об этом знают?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "На самом деле да. Я была удивлена."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_68.png" # HERMIONE
                her2 "Все странные и изощренные виды секса судя по всему случались в нашей школе..."
                her "Не скажу, что я это одобряю..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_74.png" # HERMIONE
                her "Но они научили меня некоторым... приемам."
                hide screen h_head2    
                m "Хм? И каким например?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_124.png" # HERMIONE
                her "Давайте посмотрим..."
                her "Если я положу одну руку сюда..."
                her "А другую сюда..."
                hide screen h_head2    
                m "О, я вижу... Да, это довольно приятно."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Да?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_68.png" # HERMIONE
                her "Джинни была права насчет этого..."
                hide screen h_head2
                g4 "Что ты сказала?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_74.png" # HERMIONE
                her "Джинни Уизли, она научила меня этому."
                hide screen h_head2    
                m "О, ясно..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_124.png" # HERMIONE
                her2 "Она сказала что любой парень влюбится в меня, если я ему так сделаю..."
                her2 "Еще одна вещь, когда я делаю колечко из моих пальцев..."
                her2 "И потом вставляю палец сюда..."
                hide screen h_head2    
                m "Хм... Я ничего не чувствую..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Правда?"
                her "Хм..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_124.png" # HERMIONE
                her "О! Точно!"
                her "Палец нужно вставит сюда! Какая же я глупая!"
                hide screen h_head2    
                with hpunch
                with kissiris
                g4 "О!!! Во имя великих песков пустыни, да!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_80.png" # HERMIONE
                her "Да? Вам хорошо?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_124.png" # HERMIONE
                her2 "Что, если я продолжу, но вставлю палец сюда и немного нажму..."
                hide screen h_head2    
                g4 "Девочка, ты меня убиваешь!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_80.png" # HERMIONE
                her "Правда? Правда?!"
                her "Это действительно довольно весело!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Эмм... Я имею в виду..."
                her "Я конечно же делаю это только для моего факультета..."
                hide screen h_head2    
                m "Да, да...  \"Гриффиндор\" гордится этим."
                m "Просто продолжай гладить это место..."
                m "О, да..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_124.png" # HERMIONE
                her "..............."
                hide screen h_head2
        m "Да... ."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
        her ".............."
        hide screen h_head2
        m "Теперь я хочу чтобы ты кое-что сказала..."
        menu:
            m "..."
            "{size=-4}\"Я мечтаю, чтобы меня изнасиловал отец.\"{/size}":
                $ mad += 11
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_77.png" # HERMIONE
                her "Я не мечтаю об этом!"
                hide screen h_head2
                m "Я знаю. Просто скажи это."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_76.png" # HERMIONE
                her "Мой отец? Это отвратительно, сэр!"
                hide screen h_head2
                m "Сделай, что я сказал."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_79.png" # HERMIONE
                her "..........."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Что же..."
                her "Иногда я мечтаю быть изнасилованной..."
                her "......."
                hide screen h_head2
                m "Я вижу. И в твоих фантазиях..."
                m "Кто тебя насилует?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Мой отец...?"
                hide screen h_head2
                m "Тебе это нравится?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Нет! Я плачу и умоляю его остановиться!"
                hide screen h_head2
                m "Хех... Неплохо."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_118.png" # HERMIONE
                her "......."
                hide screen h_head2
                m "Разве это было сложно?--"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_67.png" # HERMIONE
                her "Я зову мамочку, но она до сих пор на работе..."
                hide screen h_head2
                m "Хм?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Мой папа несет меня в мою комнату..."
                her "И кидает меня на кровать!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_32.png" # HERMIONE
                her "Я плачу \"Нет, папочка, я еще девственница!\""
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_123.png" # HERMIONE
                $ g_c_u_pic= "03_hp/08_animation_02/12_handjob_01.png"
                her "Но он не слушает! Он просто срывает мои трусики!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_22.png" # HERMIONE
                her "Я умоляю его остановиться! Я все кричу и кричу!"
                hide screen h_head2
                m "Мм, девочка?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_21.png" # HERMIONE
                her "Да?"
                hide screen h_head2
                m "Ты больше не дрочишь мой член..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_24.png" # HERMIONE
                her "О, я прошу прощения, сэр."
                her "Я просто задумалась..."
                $ g_c_u_pic = "handjob_ani"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Но все что я сказала, это конечно же неправда!"
                her "Я никогда о таком не фантазирую!"
                hide screen h_head2
                m "Хорошо."
            "{size=-4}\"Иногда мне становится одиноко и я даю моему псу трахнуть меня.\"{/size}":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_18.png" # HERMIONE
                her "Что?!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_17.png" # HERMIONE
                her "Это отвратительно."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_16.png" # HERMIONE
                her "Собаки разносчики {size=+5}болезней{/size}, сэр."
                hide screen h_head2
                m "На самом деле человеческие и собачьи {size=+5}болезни{/size} сильно отличаются..."
                m "Что означает, что они не смогут тебя заразить."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_08.png" # HERMIONE
                her "............"
                hide screen h_head2
                m "Я слышал, кстати, что многие женщины любят быть \"связанными\" ."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_07.png" # HERMIONE
                her "В каком смысле \"связанными\"?"
                hide screen h_head2
                m "Эм... Ну..."
                m "Не имеет значения."
                m "Просто скажи это!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_03.png" # HERMIONE
                her "Хорошо!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_08.png" # HERMIONE
                her "Иногда мне становится одиноко и я даю моему псу трахнуть меня."
                hide screen h_head2
                m "Звучит не очень..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_07.png" # HERMIONE
                her "Потому что у нас даже собаки нет!"
                hide screen h_head2
                m "Да все равно, просто продолжай..."
            "{size=-4}\"- Ввести вручную то, что нужно сказать -\"{/size}":

                # The phrase in the brackets is the text that the game will display to prompt 
                # the player to enter the name they've chosen.

                $ jasname = renpy.input("(Используйте клавиатуру, чтобы ввести предложение.)")

                $ jasname = jasname.strip()
                # The .strip() instruction removes any extra spaces the player may have typed by accident.

                #  If the player can't be bothered to choose a name, then we
                #  choose a suitable one for them:
                if jasname == "":
                    $ jasname="Я шлюха."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
                    her2 "Хм...?"
                    her2 "Должна ли я сказать что \"Я шлюха\" как обычно?"
                    hide screen h_head2
                if one_out_of_three == 1:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
                    her "Я не хочу этого говорить..."
                    hide screen h_head2
                    m "О, просто сделай это, девочка."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
                    her "..........."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_30.png" # HERMIONE
                    her2 "[jasname]"
                    hide screen h_head2
                    g9 "Хе-хе..."
                    hide screen h_head2
                elif one_out_of_three == 2:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
                    her "А?"
                    her2 "Что это значит?"
                    hide screen h_head2
                    m "Просто скажи это."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
                    her "......"
                    hide screen h_head2
                    m "Давай, развлеки меня."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_30.png" # HERMIONE
                    her2 "[jasname]"
                    hide screen h_head2
                    g9 "Хе-хе..."
                    hide screen h_head2
                elif one_out_of_three == 3:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_29.png" # HERMIONE
                    her "..........."
                    her2 "Я должна сделать это?"
                    hide screen h_head2
                    m "Просто скажи."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_30.png" # HERMIONE
                    her2 "[jasname]"
                    hide screen h_head2
                    g9 "Хе-хе..."
        
        #CUMMING
        m "Хм..."
        m "Мне нравится, то что ты делаешь ладонью!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
        her2 "Вы заметили...?"
        her2 "Мне продолжить?"
        hide screen h_head2 
        show screen blkfade
        with d3
        ">Гермиона прижимает ладонью ваш член и начинает очень нежно тереть его..."
        m "О да!!!"
        stop music fadeout 1.0
        g4 "{size=-5}(Я думаю что я готов! Нужно ли мне предупредить ее?){/size}"
        menu:
            m "..."
            "\"(Да, лучше сказать ей об этом).\"":
                g4 "Я думаю я близок к--"
                if whoring >= 18: # LEVEL 07
                    jump kiss_suck
                else:
                    pass
                ">Гермиона быстро поднимает свою блузку..."
                ">Она направляет ваш член себе на живот и быстро спускает ее..."
                ">Ощущение ее кожи на вашем разгоряченном члене вызывает у вас легкое головокружение..."
                ">Гермиона направляет ваш член чуть выше, чем вы ожидали..."
                ">Вы чувствуете ее невероятно мягкую грудь, трущуюся о ваш член..."
               
                
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}АГРХ! ДА!!!{/size}"
              
                
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                
                
                
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!!!!!!!!!!"
                hide screen h_head2 
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "undershirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                show screen ctc
                pause 
                        
                $ aftersperm = True
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=300 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                

                
                
                g4 "Агрх! Ты шлюха!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_124.png" # HERMIONE
                her2 "Да, сэр! Просто выпустите ее!"
                hide screen h_head2       
                g4 "Да! Ебаная шлюха!"
                #Cuming.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_64.png" # HERMIONE
                her2 "Ах!! Она такая горячая!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her2 "И она просто везде! Ее так много!"
                her2 "...профессор."
                hide screen h_head2       
                g4 "Агрх!!!"
                m "............"
                m "Я думаю я закончил..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her2 "Ах, хорошо..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_124.png" # HERMIONE
                her2 ".............."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_121.png" # HERMIONE
                her2 "Вы так много накончали на меня сегодня, сэр..."
                hide screen h_head2    
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d5
                ">Гермиона отпускает ваш все еще пульсирующий член."
                
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                show screen genie
                hide screen g_c_u
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                hide screen blkfade
                with d5
                
               
                
                
                
                
                if daytime:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_45.png" # HERMIONE
                    her2 "Наверное мне лучше уйти... мои уроки скоро должны начаться."
                else:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "03_hp/13_hermione_main/body_45.png" # HERMIONE
                    her2 "Наверное мне лучше уйти...  Уже довольно поздно."
                hide screen h_head2       
                m "Тебе нормально в такой одежде?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Что?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_68.png" # HERMIONE
                her "О. Да, со мной будет все в порядке..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_74.png" # HERMIONE
                her2 "Она может немного впитаться здесь и немного здесь, но я надеюсь что никто не заметит."
                hide screen h_head2    
                m "Хм... Тебе стоит заглотить мой член в следующий раз..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her "И проглотить вашу горячую сперму сэр?"
                hide screen h_head2    
                m "По крайней мере твоя одежда будет чистая."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_120.png" # HERMIONE
                her "Со всем уважением, сэр..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_122.png" # HERMIONE
                her2 "45 очков за это будет мало..."
                her2 "Кстати об этом. Могу ли я получить оплату?"
                hide screen h_head2    
                

            "\"(А, не нужно!).\"":
                g4 "Вот! Получай, шлюха!"
                if whoring >= 18: # LEVEL 07
                    jump kiss_suck
                else:
                    pass
                with hpunch
                g4 "АГРХ!"
                show screen blkfade
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "ЧТО?!"
                hide screen h_head2               
                g4 "Получай!"

                hide screen h_head2 
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}АГРРРХ! ДА!!!{/size}"
                
                
                
                  
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!!!!!!!!!!"
                hide screen h_head2 
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "on_shirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                show screen ctc
                hide screen bld1
                with d3
                pause
                show screen bld1
                with d3
                        
                $ aftersperm = True
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=300 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "03_hp/13_hermione_main/body_119.png" # HERMIONE
                her2 "......................."
                hide screen h_head2          
                m "Да... Я чувствую себя намного лучше..."
                pause
                $ g_c_u_pic = "03_hp/08_animation_02/15_cum_21.png"
                
                $ u_sperm = "03_hp/13_hermione_main/auto_06.png"
                $ uni_sperm = True
                #__#$ h_xpos=130 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                #__#$ pos = gMakePos( h_xpos, h_ypos )
                $ pos.xpos = 130
                #__#$ h_body = "03_hp/13_hermione_main/body_19.png" #Flashing Трусики
                #__#show screen hermione_main
                $herView.showQ( "body_19.png", pos, d5 )
                pause
                her ".........."
                m "Ну, кажется это все..."
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                hide screen g_c_u
                show screen genie
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                $herView.hideQ( fade )                                                                                                                                                                                                         #HERMIONE
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ pos = POS_140
                #__#$ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE          
                $herView.showQQ( "body_32.png", pos )
                her "Профессор! Что вы сделали?"
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                m "Что?"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                  #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE      
                $herView.showQQ( "body_32.png", pos )
                her "Вы всю меня обкончали, сэр..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                     #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE      
                $herView.showQQ( "body_118.png", pos )
                her "Что за ужас..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                         #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE      
                $herView.showQQ( "body_120.png", pos )
                her2 "Профессор, вы должны были предупредить меня."
                m "Это все твоя вина!"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                     #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE      
                $herView.showQQ( "body_117.png", pos )
                her2 "Моя вина?"
                m "Да! Ты делала мне так хорошо..."
                m "Что я позабыл вообще обо всем..."     
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE     
                $herView.showQQ( "body_122.png", pos )
                her2 "О..."
                her2 "Ну что сделано, то сделано..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                            #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_123.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE      
                $herView.showQQ( "body_123.png", pos )
                her "Я просто вытрусь и буду надеяться, что никто ничего не заметит..."
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                #__#with d3                                                                                                                                                                                                                   #HERMIONE
                $herView.hideQQ()
                #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                #__#$ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
                #__#with d3                                                                                                                                                                                                                        #HERMIONE      
                $herView.showQQ( "body_122.png", pos )
                her2 "Могу я получить свою оплату?"
                #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                $herView.hideQ() #"WARNING_Z"
                with fade   
    
    label done_with_handjob:
                
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_02 #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3
    
    m "Да, мисс Грейнджер. [current_payout]  \"Гриффиндору\"." 
    $ gryffindor +=current_payout
    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ pos = POS_140
    #__#$ h_body = "03_hp/13_hermione_main/body_13.png" #Flashing Трусики
    #__#show screen hermione_main
    $herView.showQ( "body_13.png", pos ) #"WARNING_Z"
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Спасибо, сэр..."

    if whoring <= 14:
        $ whoring +=1

    
    
    if whoring >= 12 and whoring <= 14:
        $ level = "05"
        $ new_request_16_01 = True #  Hearts
    if whoring >= 15 and whoring <= 17:
        $ level = "06"
        $ new_request_16_02 = True #  Hearts
    

    $ request_16_points += 1

    hide screen bld1
    #__#hide screen hermione_main
    $herView.hideQ() #"WARNING_Z"
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)

    $ aftersperm = False #Show cum stains on Hermione's uniform.
    call music_block
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
   

        
        
### KISS SUCK! ###

label kiss_suck: #Jumps here after event #03 and if WHORING >= LEVEL 07
    ">Гермиона нежно тянется своими губами к вашему члену и целует его..."
    ">Это простое действие заставило ваш член практически взорваться потоком спермы."
    show screen white 
    pause.1
    hide screen white
    pause.2
    show screen white 
    pause .1
    hide screen white
    with hpunch
    g4 "{size=+5}Агрх! ДА!!!{/size}"
    $ genie_chibi_xpos = 60 #-185 behind the desk.
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "kiss_cum_ani"
    
    hide screen blkfade
    with d3
    show screen ctc
    hide screen bld1
    with d3
    pause
    
    
    
    show screen bld1
    with d3
                        
   
    her2 "*Глп!-Глп!-Глп!*"
    hide screen h_head2          
    g4 "Аргх! Ты маленькая шлюха!"
    g4 "Да, блядь! Пей мою сперму! Выпей ее всю!"
    her2 "*Глп!-Глп!-Глп!*"
    g4 "Арх... Да!"
    ">Вы замечаете что Гермиона едва справляется с таким потоком спермы в своем рту."
    her2 "*Глп!-Глп!-Глп!*"
    g4 "Ах..."
    g4 "Просто великолепное чувство..."
    her2 "*Глп!-Глп!-Глп!*"
    m "Я думаю это все, девочка..."
    m "Можешь идти..."
    pause
    show screen blkfade
    with d5
    show screen hermione_01 
    hide screen chair_02
    hide screen desk_02
    hide screen g_c_u
    show screen genie
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    $herView.hideQ() #"WARNING_Z"
                                                                                                                                                                                                                         #HERMIONE
    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
    $ pos = POS_140
    #__#$ h_body = "03_hp/13_hermione_main/body_125.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    #__#with d3       
    $herView.showQQ( "body_125.png", pos )
    show screen ctc
    pause
    her2 "........................................."
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    #__#with d3                                                                                                                                                                                                                   #HERMIONE
    $herView.hideQQ()
    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
    #__#$ h_body = "03_hp/13_hermione_main/body_126.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    $herView.showQ( "body_126.png", pos ) #"WARNING_Z"
    her2 "ГЛП!!!"
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    #__#with d3                                                                                                                                                                                                                   #HERMIONE
    $herView.hideQQ()
    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
    #__#$ h_body = "03_hp/13_hermione_main/body_39.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    $herView.showQ( "body_39.png", pos ) #"WARNING_Z"
    her2 "Гу-а-а..."
    hide screen blkfade
    with d3
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    #__#with d3                                                                                                                                                                                                                   #HERMIONE
    $herView.hideQQ()
    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
    #__#$ h_body = "03_hp/13_hermione_main/body_123.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    $herView.showQ( "body_123.png", pos ) #"WARNING_Z"
    her2 "Я проглотила ее всю, сэр!"
    m "Хорошая девочка..."
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    #__#with d3                                                                                                                                                                                                                   #HERMIONE
    $herView.hideQQ()
    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
    #__#$ h_body = "03_hp/13_hermione_main/body_123.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    $herView.showQ( "body_123.png", pos ) #"WARNING_Z"
    her "В один момент я думала что задохнусь..."
    her2 "Ее было так много..."
    hide screen h_head2
    m "Что же, дело сделано и твоя форма идеально чистая."
    #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    #__#with d3                                                                                                                                                                                                                   #HERMIONE
    $herView.hideQQ()
    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
    #__#$ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    #__#show screen hermione_main                                                                                                                                                                                 #HERMIONE
    $herView.showQ( "body_124.png", pos ) #"WARNING_Z"
    her2 "Да! Я знаю! Этот вариант намного лушче!"
    if daytime:
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                   #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main       
        #__#with d3                                                                                                                                                                                                                                 #HERMIONE
        $herView.showQQ( "body_122.png", pos )
        her "Я лучше просто пойду в класс, как будто ничего и не было."
    else:
        #__#hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        #__#with d3                                                                                                                                                                                                                   #HERMIONE
        $herView.hideQQ()
        #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        #__#$ h_body = "03_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        #__#show screen hermione_main                  
        #__#with d3 #HERMIONE
        $herView.showQQ( "body_124.png", pos )
        her "Я могу просто пойти и провести время с парнями в Общей Комнате и никто не узнает..."
    hide screen h_head2
    m "Да... С полным животом спермы..."
    #__#hide screen hermione_main                                                                                                                                                                                     #HERMIONE
    #__#with d3                                                                                                                                                                                                                           #HERMIONE
    $herView.hideQQ()
    #__#$ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                           #HERMIONE
    #__#$ h_body = "03_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
    #__#show screen hermione_main                                                                                                                                                                                      #HERMIONE
    #__#with d3                                                                                                                                                                                                                             #HERMIONE
    $herView.showQQ( "body_117.png", pos )
    her2 "Профессор!"
    her2 "...Могу ли я получить оплату, сэр?"
    hide screen h_head2
    jump done_with_handjob #^^^ (<-That's to a smiley. That's a arrow up).
    
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     