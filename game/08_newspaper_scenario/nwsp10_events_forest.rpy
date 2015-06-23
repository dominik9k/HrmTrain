label nsp_theme_forest :
    
    $herView.hideshowQQ( "body_01.png", pos )
    m "Скажи, что тебе известно о Запретном лесе ?"
    $herView.hideshowQQ( "body_13.png", pos )
    her "Дайте подумать, сэр."
    her "Это лес вокруг Хогвартса, считающийся частью его территории."
    her "И там живут разные волшебные существа. И мистер Хагрид следит за порядком в нем."
    m "А еще ?"
    her "В нем опасно, сэр. Некоторые из существ агрессивны."
    m "И ?"
    $herView.hideshowQQ( "body_15.png", pos )
    her "И ученикам запрещено ходить туда в одиночку, сэр !"
    m "Вот как ? А если у тебя... ну то есть у ученика будет разрешение директора ?"
    $herView.hideshowQQ( "body_14.png", pos )
    her "Вы решили проверить меня, сэр ? Да, директор имеет право дать доступ в Запретный лес."
    her "Но вы же не..."
    $herView.hideshowQQ( "body_11.png", pos )
    her "О, нет. Вы хотите отправить туда {size=+4}меня{/size} ?"
    g9 "Не волнуйся, я не предложу тебе ничего опасного."
    $herView.hideshowQQ( "body_12.png", pos )
    her "Да, сэр."
    $herView.hideshowQQ( "body_01.png", pos )

    return

label nsp_event_forest_1 :

    if cur_level == 1 :
        ">текст преивента леса 1-1"
    elif cur_level == 2 :
        ">текст преивента леса 1-2"
    elif cur_level == 3 :
        ">текст преивента леса 1-3"            
    elif cur_level == 4 :
        ">текст преивента леса 1-4"            
    elif cur_level == 5 :
        ">текст преивента леса 1-5"        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_forest_1_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о Запретном лесе "
    $ nsp_genie_sphere_req = nsp_germiona_forest_1_photo
    
    if nsp_germiona_forest_1_statimg == "New" :
        $ cur_level = nsp_event_forest_1 + 1
    else :
        $ cur_level = nsp_event_forest_1

    if cur_level == 1 :
        ">текст ивента леса 1-1"
        
        if nsp_germiona_mediawhoring < 10 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_forest_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 10

        call nsp_bonus_calc
            
    elif cur_level == 2 :
        ">текст ивента леса 1-2"
        
        if nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_forest_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 30

        call nsp_bonus_calc
            
    elif cur_level == 3 :
        ">текст ивента леса 1-3" 
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_forest_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 70

        call nsp_bonus_calc
            
    elif cur_level == 4 :
        ">текст ивента леса 1-4"  
        
        if nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_forest_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 140

        call nsp_bonus_calc
        
    elif cur_level == 5 :
        ">текст ивента леса 1-5"
        
        if nsp_germiona_mediawhoring < 150 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 160 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_forest_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 200

        call nsp_bonus_calc
        

    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_forest_2 :

    if cur_level == 1 :
        ">текст преивента леса 2-1"        
        
    elif cur_level == 2 :
        ">текст преивента леса 2-2"
        
    elif cur_level == 3 :
        ">текст преивента леса 2-3"
        
    elif cur_level == 4 :
        ">текст преивента леса 2-4" 
        
    elif cur_level == 5 :
        ">текст преивента леса 2-5" 
        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_forest_2_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о Запретном лесе "
    $ nsp_genie_sphere_req = nsp_germiona_forest_2_photo
    
    if nsp_germiona_forest_2_statimg == "New" :
        $ cur_level = nsp_event_forest_2 + 1
    else :
        $ cur_level = nsp_event_forest_2

    if cur_level == 1 :
        ">текст ивента леса 2-1"  
        
        if nsp_germiona_mediawhoring < 10 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_forest_2 = cur_level 
        
        $ nsp_newspaper_bonus_base = 30

        call nsp_bonus_calc       

    elif cur_level == 2 :
        ">текст ивента леса 2-2"
        
        if nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_forest_2 = cur_level 
        
        $ nsp_newspaper_bonus_base = 50

        call nsp_bonus_calc
            
    elif cur_level == 3 :
        ">текст ивента леса 2-3"   
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_forest_2 = cur_level
        
        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc
            
    elif cur_level == 4 :
        ">текст ивента леса 2-4"            
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_forest_2 = cur_level
        
        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc
        
        $ hermi.liking -= 10
            
    elif cur_level == 5 :
        ">текст ивента леса 2-5" 
        
        if nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_forest_2 = cur_level 
        
        $ nsp_newspaper_bonus_base = 130

        call nsp_bonus_calc

    call nsp_hermione_goout

    $event.Finalize() 

    return



