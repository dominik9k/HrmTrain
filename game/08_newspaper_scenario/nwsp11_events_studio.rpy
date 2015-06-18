label nsp_theme_studio :
    ">Диалог тема 8"
    return

label nsp_event_studio_1 :

    if cur_level == 1 :
        ">текст преивента студии 1-1"
    elif cur_level == 2 :
        ">текст преивента студии 1-2"
    elif cur_level == 3 :
        ">текст преивента студии 1-3"            
    elif cur_level == 4 :
        ">текст преивента студии 1-4"            
    elif cur_level == 5 :
        ">текст преивента студии 1-5"        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_studio_1_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о фотостудии "
    
    if nsp_germiona_studio_1_statimg == "New" :
        $ cur_level = nsp_event_studio_1 + 1
    else :
        $ cur_level = nsp_event_studio_1

    if cur_level == 1 :
        ">текст ивента студии 1-1"
        
        if nsp_germiona_mediawhoring < 10 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 10

        call nsp_bonus_calc_photo
            
    elif cur_level == 2 :
        ">текст ивента студии 1-2"
        
        if nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 20

        call nsp_bonus_calc_photo
            
    elif cur_level == 3 :
        ">текст ивента студии 1-3" 
        
        if nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 40

        call nsp_bonus_calc_photo
            
    elif cur_level == 4 :
        ">текст ивента студии 1-4"  
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc_photo
        
    elif cur_level == 5 :
        ">текст ивента студии 1-5"
        
        if nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc_photo
        
    if nsp_germiona_artistry < 25 :
        $ nsp_germiona_artistry += 1
        
    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_studio_2 :

    if cur_level == 1 :
        ">текст преивента студии 2-1"        
        
    elif cur_level == 2 :
        ">текст преивента студии 2-2"
        
    elif cur_level == 3 :
        ">текст преивента студии 2-3"
        
    elif cur_level == 4 :
        ">текст преивента студии 2-4" 
        
    elif cur_level == 5 :
        ">текст преивента студии 2-5" 
        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_studio_2_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о фотостудии "
    
    if nsp_germiona_studio_2_statimg == "New" :
        $ cur_level = nsp_event_studio_2 + 1
    else :
        $ cur_level = nsp_event_studio_2

    if cur_level == 1 :
        ">текст ивента студии 2-1"  
        
        if nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_2 = cur_level
        
        $ nsp_newspaper_bonus_base = 30

        call nsp_bonus_calc_video        

    elif cur_level == 2 :
        ">текст ивента студии 2-2"
        
        if nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_2 = cur_level 
        
        $ nsp_newspaper_bonus_base = 50

        call nsp_bonus_calc_video
            
    elif cur_level == 3 :
        ">текст ивента студии 2-3"   
        
        if nsp_germiona_mediawhoring < 65 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 75 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_2 = cur_level
        
        $ nsp_newspaper_bonus_base = 65

        call nsp_bonus_calc_video
            
    elif cur_level == 4 :
        ">текст ивента студии 2-4"            
        
        if nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_2 = cur_level
        
        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc_video
            
    elif cur_level == 5 :
        ">текст ивента студии 2-5" 
        
        if nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_2 = cur_level 
        
        $ nsp_newspaper_bonus_base = 110

        call nsp_bonus_calc_video

    if nsp_germiona_artistry < 25 :
        $ nsp_germiona_artistry += 1
        
    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_studio_3 :

    if cur_level == 1 :
        ">текст преивента студии 3-1"
    elif cur_level == 2 :
        ">текст преивента студии 3-2"
    elif cur_level == 3 :
        ">текст преивента студии 3-3"            
    elif cur_level == 4 :
        ">текст преивента студии 3-4"            
    elif cur_level == 5 :
        ">текст преивента студии 3-5"        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_studio_3_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о фотостудии "
    
    if nsp_germiona_studio_3_statimg == "New" :
        $ cur_level = nsp_event_studio_3 + 1
    else :
        $ cur_level = nsp_event_studio_3

    if cur_level == 1 :
        ">текст ивента студии 3-1"
        
        if nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 20

        call nsp_bonus_calc_photo
        
    elif cur_level == 2 :
        ">текст ивента студии 3-2"
        
        if nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 40

        call nsp_bonus_calc_photo
        
    elif cur_level == 3 :
        ">текст ивента студии 3-3" 
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_3 = cur_level  
        
        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc_photo
        
    elif cur_level == 4 :
        ">текст ивента студии 3-4" 
        
        if nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc_photo
            
    elif cur_level == 5 :
        ">текст ивента студии 3-5"  
        
        if nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 130 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 120

        call nsp_bonus_calc_photo
            
    if nsp_germiona_artistry < 25 :
        $ nsp_germiona_artistry += 1

    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_studio_4 :

    if cur_level == 1 :
        ">текст преивента студии 4-1"
    elif cur_level == 2 :
        ">текст преивента студии 4-2"
    elif cur_level == 3 :
        ">текст преивента студии 4-3"            
    elif cur_level == 4 :
        ">текст преивента студии 4-4"            
    elif cur_level == 5 :
        ">текст преивента студии 4-5"        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_studio_4_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о фотостудии "
    
    if nsp_germiona_studio_4_statimg == "New" :
        $ cur_level = nsp_event_studio_4 + 1
    else :
        $ cur_level = nsp_event_studio_4
        
    if cur_level == 1 :
        ">текст ивента студии 4-1"
        
        if nsp_germiona_mediawhoring < 25 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 35 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 25

        call nsp_bonus_calc_video
        
    elif cur_level == 2 :
        ">текст ивента студии 4-2"
        
        if nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 40

        call nsp_bonus_calc_video
            
    elif cur_level == 3 :
        ">текст ивента студии 4-3" 
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc_video
            
    elif cur_level == 4 :
        ">текст ивента студии 4-4"  
        
        if nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc_video
            
    elif cur_level == 5 :
        ">текст ивента студии 4-5"  
        
        if nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 130 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 120

        call nsp_bonus_calc_video
            
    if nsp_germiona_artistry < 25 :
        $ nsp_germiona_artistry += 1
        
    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_studio_5 :

    if cur_level == 1 :
        ">текст преивента студии 5-1"
    elif cur_level == 2 :
        ">текст преивента студии 5-2"
    elif cur_level == 3 :
        ">текст преивента студии 5-3"            
    elif cur_level == 4 :
        ">текст преивента студии 5-4"            
    elif cur_level == 5 :
        ">текст преивента студии 5-5"   
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_studio_5_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о фотостудии "
    
    if nsp_germiona_studio_5_statimg == "New" :
        $ cur_level = nsp_event_studio_5 + 1
    else :
        $ cur_level = nsp_event_studio_5

    if cur_level == 1 :
        ">текст ивента студии 5-1"  
        
        if nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 50

        call nsp_bonus_calc_photo

    elif cur_level == 2 :
        ">текст ивента студии 5-2"  
        
        if nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 70

        call nsp_bonus_calc_photo

    elif cur_level == 3 :
        ">текст ивента студии 5-3"   
        
        if nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc_photo
           
    elif cur_level == 4 :
        ">текст ивента студии 5-4"   
        
        if nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 110

        call nsp_bonus_calc_photo
           
    elif cur_level == 5 :
        ">текст ивента студии 5-5"   
        
        if nsp_germiona_mediawhoring < 130 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 140 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 130

        call nsp_bonus_calc_photo
        
    if nsp_germiona_artistry < 25 :
        $ nsp_germiona_artistry += 1

    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_studio_5 :

    if cur_level == 1 :
        ">текст преивента студии 5-1"
    elif cur_level == 2 :
        ">текст преивента студии 5-2"
    elif cur_level == 3 :
        ">текст преивента студии 5-3"            
    elif cur_level == 4 :
        ">текст преивента студии 5-4"            
    elif cur_level == 5 :
        ">текст преивента студии 5-5"   
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_studio_6_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о фотостудии "
    
    if nsp_germiona_studio_6_statimg == "New" :
        $ cur_level = nsp_event_studio_6 + 1
    else :
        $ cur_level = nsp_event_studio_6

    if cur_level == 1 :
        ">текст ивента студии 6-1"  
        
        if nsp_germiona_mediawhoring < 45 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 55 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_6 = cur_level
        
        $ nsp_newspaper_bonus_base = 45

        call nsp_bonus_calc_video

    elif cur_level == 2 :
        ">текст ивента студии 6-2"  
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_6 = cur_level
        
        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc_video

    elif cur_level == 3 :
        ">текст ивента студии 6-3"   
        
        if nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_6 = cur_level
        
        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc_video
           
    elif cur_level == 4 :
        ">текст ивента студии 6-4"   
        
        if nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 130 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_6 = cur_level
        
        $ nsp_newspaper_bonus_base = 120

        call nsp_bonus_calc_video
           
    elif cur_level == 5 :
        ">текст ивента студии 6-5"   
        
        if nsp_germiona_mediawhoring < 140 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 150 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_studio_6 = cur_level
        
        $ nsp_newspaper_bonus_base = 140

        call nsp_bonus_calc_video
        
    if nsp_germiona_artistry < 25 :
        $ nsp_germiona_artistry += 1

    call nsp_hermione_goout

    $event.Finalize() 

    return
