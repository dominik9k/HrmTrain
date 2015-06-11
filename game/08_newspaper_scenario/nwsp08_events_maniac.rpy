label nsp_event_maniac_1 :

    if cur_level == 1 :
        ">текст преивента маньяка 1-1"
    elif cur_level == 2 :
        ">текст преивента маньяка 1-2"
    elif cur_level == 3 :
        ">текст преивента маньяка 1-3"            
    elif cur_level == 4 :
        ">текст преивента маньяка 1-4"                  
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_maniac_1_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о маньяке "
    $ nsp_genie_sphere_diamond_req = 3
    
    if nsp_germiona_maniac_1_statimg == "New" :
        $ cur_level = nsp_event_maniac_1 + 1
    else :
        $ cur_level = nsp_event_maniac_1

    if cur_level == 1 :
        ">текст ивента маньяка 1-1"
        
        if nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_maniac_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 60

        call nsp_bonus_calc
            
    elif cur_level == 2 :
        ">текст ивента маньяка 1-2"
        
        if nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_maniac_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 70

        call nsp_bonus_calc
            
    elif cur_level == 3 :
        ">текст ивента маньяка 1-3" 
        
        if nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_maniac_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc
            
    elif cur_level == 4 :
        ">текст ивента маньяка 1-4"  
        
        if nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_maniac_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc
        

    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_maniac_2 :

    if cur_level == 1 :
        ">текст преивента маньяка 2-1"        
        
    elif cur_level == 2 :
        ">текст преивента маньяка 2-2"
        
    elif cur_level == 3 :
        ">текст преивента маньяка 2-3"
        
    elif cur_level == 4 :
        ">текст преивента маньяка 2-4" 
        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_maniac_2_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о маньяке "
    $ nsp_genie_sphere_diamond_req = 3
    
    if nsp_germiona_maniac_2_statimg == "New" :
        $ cur_level = nsp_event_maniac_2 + 1
    else :
        $ cur_level = nsp_event_maniac_2

    if cur_level == 1 :
        ">текст ивента маньяка 2-1"  
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_maniac_2 = cur_level  
        
        $ nsp_newspaper_bonus_base = 110

        call nsp_bonus_calc      

    elif cur_level == 2 :
        ">текст ивента маньяка 2-2"
        
        if nsp_germiona_mediawhoring < 65 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 75 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_maniac_2 = cur_level 
        
        $ nsp_newspaper_bonus_base = 115

        call nsp_bonus_calc
            
    elif cur_level == 3 :
        ">текст ивента маньяка 2-3"   
        
        if nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_maniac_2 = cur_level
        
        $ nsp_newspaper_bonus_base = 120

        call nsp_bonus_calc
            
    elif cur_level == 4 :
        ">текст ивента маньяка 2-4"            
        
        if nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 70 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_maniac_2 = cur_level
        
        $ nsp_newspaper_bonus_base = 140

        call nsp_bonus_calc
 

    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_maniac_3 :

    if cur_level == 1 :
        ">текст преивента маньяка 3-1"
    elif cur_level == 2 :
        ">текст преивента маньяка 3-2"
    elif cur_level == 3 :
        ">текст преивента маньяка 3-3"            
    elif cur_level == 4 :
        ">текст преивента маньяка 3-4"            
    elif cur_level == 5 :
        ">текст преивента маньяка 3-5"        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_maniac_3_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о маньяке "
    $ nsp_genie_sphere_diamond_req = 3
    
    if nsp_germiona_maniac_3_statimg == "New" :
        $ cur_level = nsp_event_maniac_3 + 1
    else :
        $ cur_level = nsp_event_maniac_3

    if cur_level == 1 :
        ">текст ивента маньяка 3-1"
        
        if nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_maniac_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 130

        call nsp_bonus_calc
        
    elif cur_level == 2 :
        ">текст ивента маньяка 3-2"
        
        if nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_maniac_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 160

        call nsp_bonus_calc
        
        $ hermi.liking -= 4
        
    elif cur_level == 3 :
        ">текст ивента маньяка 3-3" 
        
        if nsp_germiona_mediawhoring < 135 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 145 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 70 :
            $ nsp_germiona_impudence += 1 
            
        $ nsp_event_maniac_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 195

        call nsp_bonus_calc
        
        $ hermi.liking -= 6
        
    elif cur_level == 4 :
        ">текст ивента маньяка 3-4" 
        
        if nsp_germiona_mediawhoring < 150 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 160 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 80 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_maniac_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 220

        call nsp_bonus_calc
            
    elif cur_level == 5 :
        ">текст ивента маньяка 3-5"  
        
        if nsp_germiona_mediawhoring < 160 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 170 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 80 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_maniac_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 230

        call nsp_bonus_calc
            

    call nsp_hermione_goout

    $event.Finalize() 

    return
