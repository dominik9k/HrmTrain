label nsp_theme_rights :
    
    $herView.hideshowQQ( "body_01.png", pos )
    m "Итак, пришло направить твою стропт... настойчивость на новую цель."
    her "Сэр ?"
    m "Ты помнишь, зачем приходила в этот кабинет в первый раз ?"
    $herView.hideshowQQ( "body_15.png", pos )
    her "Э... Это когда вы попросили меня..."
    m "Нет, в самый первый раз."
    her "А, вы имеете ввиду, на первом курсе, когда мы с Гарри и Роном..."
    g4 "(Кактус мне в ухо.)"
    m "В первый раз с тех пор, как я здесь появ... Нет опять не то."
    m "Я говорю про твои обвинения в адрес преподавателей, проявляющих дискриминацию."
    $herView.hideshowQQ( "body_75.png", pos )
    her "Да, понимаю. Пришло время раскрыть правду общественности ?"
    her "Отлично, я готова !"
    $herView.hideshowQQ( "body_01.png", pos )
    g1 "Кхм-кха."
    m "На самом деле, я предлагаю сначала подготовить почву для этого."
    g9 "Есть пара идей, как это сделать."
    her "Хорошо, сэр."

    return

label nsp_event_rights_1 :

    if cur_level == 1 :
        $herView.hideshowQQ( "body_01.png", pos )
        
        if nsp_event_rights_1 == 0 :
            m "Сегодня тебе предстоит составить репортаж о том, как некоторые ученики пристают к девочкам. Возможно, это слизеринцы."
            m "Нам действительно нужен этот материал."
            $herView.hideshowQQ( "body_02.png", pos )
            her "Вы хотите, чтобы я провела расследование ?"
            m "Не ты ли жаловалась, что такое происходит ? Теперь есть возможность привлечь внимание читателей к проблеме."
            $herView.hideshowQQ( "body_24.png", pos )
            her "Да, но я..."
            her "Возможно, я немного преувеличила."
            her "То есть некоторые ученики действительно ведут себя неподобающе, но это происходит не так часто."
            m "Это не важно, от тебя требуется только придумать сюжет и убедительно пересказать его мне."
            $herView.hideshowQQ( "body_13.png", pos )
            her "Ну, если вы так считаете... Хорошо."
            $herView.hideshowQQ( "body_01.png", pos )
        else :
            m "Сегодня тебе снова предстоит придумать рассказ о домогательствах."
            m "Есть вдохновение ?"
            $herView.hideshowQQ( "body_06.png", pos )
            her "Наверное да, сэр."
            
        $herView.hideshowQQ( "body_01.png", pos )
        
    elif cur_level == 2 :
        ">текст преивента прав 1-2"
    elif cur_level == 3 :
        ">текст преивента прав 1-3"            
    elif cur_level == 4 :
        ">текст преивента прав 1-4"            
    elif cur_level == 5 :
        ">текст преивента прав 1-5"        
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_rights_1_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о правах "
    $ nsp_genie_sphere_req = nsp_germiona_rights_1_photo
    
    if nsp_germiona_rights_1_statimg == "New" :
        $ cur_level = nsp_event_rights_1 + 1
    else :
        $ cur_level = nsp_event_rights_1

    if cur_level == 1 :
    
        show screen hermione_02
        $herView.hideshowQQ( "body_01.png", pos )
        g9 "Ты пришла ? Отлично, я готов записывать."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Хорошо, сэр"
        her "Сегодня я шла по улице в сторону оранжереи."
        her "Вот."
        g9 "Отлично, продолжай."
        $herView.hideshowQQ( "body_09.png", pos )
        her "И у двери стояла группа слизеринцев. Один из них позвал меня и я..."
        m "И ты пошла с ним в укромное место ?"
        $herView.hideshowQQ( "body_13.png", pos )
        her "Э... Нет, сэр. Я попыталась пройти мимо. Но один из них загородил мне дорогу."
        her "Пока я пыталась его обойти, подошли остальные."
        $herView.hideshowQQ( "body_24.png", pos )
        her "И они... Они трогали меня..."
        m "Трогали ? Как именно трогали ?"
        $herView.hideshowQQ( "body_31.png", pos )
        her "Я ..."
        $herView.hideshowQQ( "body_33.png", pos )
        ">Гермиона покраснела и замолчала."
        $herView.hideshowQQ( "body_30.png", pos )
        her "Сэр, напоминаю вам, что это выдуманная история !"
        m "Да, но у любой истории должно быть окончание."
        $herView.hideshowQQ( "body_45.png", pos )
        her "Ммм. Хорошо."
        her "Один из них схватил меня за локоть и начал поглаживать плечо."
        her "Другой погладил по щеке."
        $herView.hideshowQQ( "body_54.png", pos )
        her "Третий... Третий..."
        m "И что же третий ?"
        her "Третий подошел сзади и положио руку мне на живот."
        $herView.hideshowQQ( "body_85.png", pos )
        her "Сэр, я больше не могу."
        m "Ну же, еще пару фраз для завершения."
        her "Мне очень стыдно такое представлять."
        g4 "Сосредоточься !"
        $herView.hideshowQQ( "body_81.png", pos )
        her "Ладно. Четвертый парень усмехнулся и посмотрел мне в глаза. Маленькая шлюха, сказал он."
        her "И..."
        m "И ?"
        $herView.hideshowQQ( "body_59.png", pos )
        her "И приподняв край моей юбки провел рукой по обнаженному бедру."
        her "А потом я вырвалась и убежала."
        her "Вот и вся история, сэр."
        g9 "Ну что же, совсем неплохо."
        $herView.hideshowQQ( "body_02.png", pos )
        her "Правда, сэр ?"
        m "Да. До следующего раза."
        $herView.hideshowQQ( "body_14.png", pos )
        her "Следующего ра... Да, профессор, как скажете."
        $herView.hideshowQQ( "body_01.png", pos )
        
        if nsp_germiona_mediawhoring < 10 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_rights_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 10
        
        call nsp_bonus_calc
            
    elif cur_level == 2 :
        ">текст ивента прав 1-2"
        
        if nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_rights_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 20

        call nsp_bonus_calc
            
    elif cur_level == 3 :
        ">текст ивента прав 1-3" 
        
        if nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_rights_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 30

        call nsp_bonus_calc
            
    elif cur_level == 4 :
        ">текст ивента прав 1-4"  
        
        if nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_rights_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 40

        call nsp_bonus_calc
        
    elif cur_level == 5 :
        ">текст ивента прав 1-5"
        
        if nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_rights_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc
        

    call nsp_hermione_goout

    $wtevent.Finalize() 

    return

label nsp_event_rights_2 :

    if cur_level == 1 :
        ">текст преивента прав 2-1"        
        
    elif cur_level == 2 :
        ">текст преивента прав 2-2"
        
    elif cur_level == 3 :
        ">текст преивента прав 2-3"
        
    elif cur_level == 4 :
        ">текст преивента прав 2-4" 
        
    elif cur_level == 5 :
        ">текст преивента прав 2-5" 
        
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_rights_2_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о правах "
    $ nsp_genie_sphere_req = nsp_germiona_rights_2_photo
    
    if nsp_germiona_rights_2_statimg == "New" :
        $ cur_level = nsp_event_rights_2 + 1
    else :
        $ cur_level = nsp_event_rights_2

    if cur_level == 1 :
        ">текст ивента прав 2-1"  
        
        if nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_rights_2 = cur_level
        
        $ nsp_newspaper_bonus_base = 20

        call nsp_bonus_calc        

    elif cur_level == 2 :
        ">текст ивента прав 2-2"
        
        if nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_rights_2 = cur_level 
        
        $ nsp_newspaper_bonus_base = 30

        call nsp_bonus_calc
            
    elif cur_level == 3 :
        ">текст ивента прав 2-3"   
        
        if nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_rights_2 = cur_level
        
        $ nsp_newspaper_bonus_base = 40

        call nsp_bonus_calc
            
    elif cur_level == 4 :
        ">текст ивента прав 2-4"            
        
        if nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_rights_2 = cur_level
        
        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc
            
    elif cur_level == 5 :
        ">текст ивента прав 2-5" 
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_rights_2 = cur_level 
        
        $ nsp_newspaper_bonus_base = 80

        call nsp_bonus_calc

    call nsp_hermione_goout

    $wtevent.Finalize() 

    return

label nsp_event_rights_3 :

    if cur_level == 1 :
    
        $herView.hideshowQQ( "body_01.png", pos )
        ">текст преивента прав 3-1"
        $herView.hideshowQQ( "body_01.png", pos )
        
    elif cur_level == 2 :
        ">текст преивента прав 3-2"
    elif cur_level == 3 :
        ">текст преивента прав 3-3"            
    elif cur_level == 4 :
        ">текст преивента прав 3-4"            
    elif cur_level == 5 :
        ">текст преивента прав 3-5"        
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_rights_3_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о правах "
    $ nsp_genie_sphere_req = nsp_germiona_rights_3_photo
    
    if nsp_germiona_rights_3_statimg == "New" :
        $ cur_level = nsp_event_rights_3 + 1
    else :
        $ cur_level = nsp_event_rights_3

    if cur_level == 1 :
        ">текст ивента прав 3-1"
        
        if nsp_germiona_mediawhoring < 10 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_rights_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 10

        call nsp_bonus_calc
        
        $ nsp_event_rights_3_unpub = True
        
    elif cur_level == 2 :
        ">текст ивента прав 3-2"
        
        if nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_rights_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 30

        call nsp_bonus_calc
        
        $ nsp_event_rights_3_unpub = True
        
    elif cur_level == 3 :
        ">текст ивента прав 3-3" 
        
        if nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1 
            
        $ nsp_event_rights_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc
        
        $ hermi.liking -= 10
        
        $ nsp_event_rights_3_unpub = True
        
    elif cur_level == 4 :
        ">текст ивента прав 3-4" 
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_rights_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 80

        call nsp_bonus_calc
        
        $ nsp_event_rights_3_unpub = True
            
    elif cur_level == 5 :
        ">текст ивента прав 3-5"  
        
        if nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_rights_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc        

    call nsp_hermione_goout

    $wtevent.Finalize() 

    return

label nsp_event_rights_4 :

    if cur_level == 1 :
        ">текст преивента прав 4-1"
    elif cur_level == 2 :
        ">текст преивента прав 4-2"
    elif cur_level == 3 :
        ">текст преивента прав 4-3"            
    elif cur_level == 4 :
        ">текст преивента прав 4-4"            
    elif cur_level == 5 :
        ">текст преивента прав 4-5"        
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_rights_4_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о правах "
    $ nsp_genie_sphere_req = nsp_germiona_rights_4_photo
    
    if nsp_germiona_rights_4_statimg == "New" :
        $ cur_level = nsp_event_rights_4 + 1
    else :
        $ cur_level = nsp_event_rights_4
        
    if cur_level == 1 :
        ">текст ивента прав 4-1"
        
        if nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_rights_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 40

        call nsp_bonus_calc
        
    elif cur_level == 2 :
        ">текст ивента прав 4-2"
        
        if nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_rights_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 50

        call nsp_bonus_calc
            
    elif cur_level == 3 :
        ">текст ивента прав 4-3" 
        
        if nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_rights_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 70

        call nsp_bonus_calc
            
    elif cur_level == 4 :
        ">текст ивента прав 4-4"  
        
        if nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_rights_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc
            
    elif cur_level == 5 :
        ">текст ивента прав 4-5"  
        
        if nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_rights_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 130

        call nsp_bonus_calc
        
        $ hermi.liking -= 2
            

    call nsp_hermione_goout

    $wtevent.Finalize() 

    return

label nsp_event_rights_5 :

    if cur_level == 1 :
        ">текст преивента прав 5-1"
    elif cur_level == 2 :
        ">текст преивента прав 5-2"
    elif cur_level == 3 :
        ">текст преивента прав 5-3"            
    elif cur_level == 4 :
        ">текст преивента прав 5-4"            
    elif cur_level == 5 :
        ">текст преивента прав 5-5" 
    elif cur_level == 6 :
        ">текст преивента прав 5-6"    
    elif cur_level == 7 :
        ">текст преивента прав 5-7"    
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_rights_5_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о правах "
    $ nsp_genie_sphere_req = nsp_germiona_rights_5_photo
    
    if nsp_germiona_rights_5_statimg == "New" :
        $ cur_level = nsp_event_rights_5 + 1
    else :
        $ cur_level = nsp_event_rights_5

    if cur_level == 1 :
        ">текст ивента прав 5-1"  
        
        if nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_rights_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 30

        call nsp_bonus_calc

    elif cur_level == 2 :
        ">текст ивента прав 5-2"  
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_rights_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 70

        call nsp_bonus_calc

    elif cur_level == 3 :
        ">текст ивента прав 5-3"   
        
        if nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_rights_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 80

        call nsp_bonus_calc
           
    elif cur_level == 4 :
        ">текст ивента прав 5-4"   
        
        if nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_rights_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 110

        call nsp_bonus_calc
           
    elif cur_level == 5 :
        ">текст ивента прав 5-5"   
        
        if nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_rights_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 140

        call nsp_bonus_calc
 
    elif cur_level == 6 :
        ">текст ивента прав 5-6"     
        
        if nsp_germiona_mediawhoring < 130 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 140 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_rights_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 170

        call nsp_bonus_calc
 
    elif cur_level == 7 :
        ">текст ивента прав 5-7"  
        
        if nsp_germiona_mediawhoring < 150 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 160 :
            $ nsp_germiona_mediawhoring += 1   
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_rights_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 190

        call nsp_bonus_calc


    call nsp_hermione_goout

    $wtevent.Finalize() 

    return

