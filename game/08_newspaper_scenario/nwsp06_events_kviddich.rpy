label nsp_event_kviddich_1 :

    if cur_level == 1 :
        ">текст преивента квиддича 1-1"
    elif cur_level == 2 :
        ">текст преивента квиддича 1-2"
    elif cur_level == 3 :
        ">текст преивента квиддича 1-3"            
    elif cur_level == 4 :
        ">текст преивента квиддича 1-4"            
    elif cur_level == 5 :
        ">текст преивента квиддича 1-5"        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_kviddich_1_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о квиддиче "
    $ nsp_genie_sphere_diamond_req = 3
    
    if nsp_germiona_kviddich_1_statimg == "New" :
        $ cur_level = nsp_event_kviddich_1 + 1
    else :
        $ cur_level = nsp_event_kviddich_1

    if cur_level == 1 :
        ">текст ивента квиддича 1-1"
        
        if nsp_germiona_mediawhoring < 10 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 10

        call nsp_bonus_calc
            
    elif cur_level == 2 :
        ">текст ивента квиддича 1-2"
        
        if nsp_germiona_mediawhoring < 25 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 35 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 35

        call nsp_bonus_calc
            
    elif cur_level == 3 :
        ">текст ивента квиддича 1-3" 
        
        if nsp_germiona_mediawhoring < 35 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 45 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 45

        call nsp_bonus_calc
            
    elif cur_level == 4 :
        ">текст ивента квиддича 1-4"  
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 80

        call nsp_bonus_calc
        
    elif cur_level == 5 :
        ">текст ивента квиддича 1-5"
        
        if nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 110

        call nsp_bonus_calc
        

    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_kviddich_2 :

    if cur_level == 1 :
        ">текст преивента квиддича 2-1"        
        
    elif cur_level == 2 :
        ">текст преивента квиддича 2-2"
        
    elif cur_level == 3 :
        ">текст преивента квиддича 2-3"
        
    elif cur_level == 4 :
        ">текст преивента квиддича 2-4" 
        
    elif cur_level == 5 :
        ">текст преивента квиддича 2-5" 
        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_kviddich_2_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о квиддиче "
    $ nsp_genie_sphere_diamond_req = 3
    
    if nsp_germiona_kviddich_2_statimg == "New" :
        $ cur_level = nsp_event_kviddich_2 + 1
    else :
        $ cur_level = nsp_event_kviddich_2

    if cur_level == 1 :
        ">текст ивента квиддича 2-1"  
        
        if nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_2 = cur_level 
        
        $ nsp_newspaper_bonus_base = 40

        call nsp_bonus_calc       

    elif cur_level == 2 :
        ">текст ивента квиддича 2-2"
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_2 = cur_level 
        
        $ nsp_newspaper_bonus_base = 80

        call nsp_bonus_calc
            
    elif cur_level == 3 :
        ">текст ивента квиддича 2-3"   
        
        if nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_2 = cur_level
        
        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc
            
    elif cur_level == 4 :
        ">текст ивента квиддича 2-4"            
        
        if nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_2 = cur_level
        
        $ nsp_newspaper_bonus_base = 130

        call nsp_bonus_calc
            
    elif cur_level == 5 :
        ">текст ивента квиддича 2-5" 
        
        if nsp_germiona_mediawhoring < 130 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 140 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_2 = cur_level 
        
        $ nsp_newspaper_bonus_base = 170

        call nsp_bonus_calc

    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_kviddich_3 :

    if cur_level == 1 :
        ">текст преивента квиддича 3-1"
    elif cur_level == 2 :
        ">текст преивента квиддича 3-2"
    elif cur_level == 3 :
        ">текст преивента квиддича 3-3"            
    elif cur_level == 4 :
        ">текст преивента квиддича 3-4"            
    elif cur_level == 5 :
        ">текст преивента квиддича 3-5"        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_kviddich_3_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о квиддиче "
    $ nsp_genie_sphere_diamond_req = 3
    
    if nsp_germiona_kviddich_3_statimg == "New" :
        $ cur_level = nsp_event_kviddich_3 + 1
    else :
        $ cur_level = nsp_event_kviddich_3

    if cur_level == 1 :
        ">текст ивента квиддича 3-1"
        
        if nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 80

        call nsp_bonus_calc
        
    elif cur_level == 2 :
        ">текст ивента квиддича 3-2"
        
        if nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc
        
    elif cur_level == 3 :
        ">текст ивента квиддича 3-3" 
        
        if nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1 
            
        $ nsp_event_kviddich_3 = cur_level 
        
        $ nsp_newspaper_bonus_base = 120

        call nsp_bonus_calc
        
        $ hermi.liking -= 2
        
    elif cur_level == 4 :
        ">текст ивента квиддича 3-4" 
        
        if nsp_germiona_mediawhoring < 130 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 140 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 170

        call nsp_bonus_calc
        
        $ hermi.liking -= 3
            
    elif cur_level == 5 :
        ">текст ивента квиддича 3-5"  
        
        if nsp_germiona_mediawhoring < 160 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 170 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_3 = cur_level
        
        $ nsp_newspaper_bonus_base = 210

        call nsp_bonus_calc
            

    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_kviddich_4 :

    if cur_level == 1 :
        ">текст преивента квиддича 4-1"
    elif cur_level == 2 :
        ">текст преивента квиддича 4-2"
    elif cur_level == 3 :
        ">текст преивента квиддича 4-3"            
    elif cur_level == 4 :
        ">текст преивента квиддича 4-4"            
    elif cur_level == 5 :
        ">текст преивента квиддича 4-5"        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_kviddich_4_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о квиддиче "
    $ nsp_genie_sphere_diamond_req = 3
    
    if nsp_germiona_kviddich_4_statimg == "New" :
        $ cur_level = nsp_event_kviddich_4 + 1
    else :
        $ cur_level = nsp_event_kviddich_4
        
    if cur_level == 1 :
        ">текст ивента квиддича 4-1"
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 70

        call nsp_bonus_calc
        
    elif cur_level == 2 :
        ">текст ивента квиддича 4-2"
        
        if nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 100

        call nsp_bonus_calc
            
    elif cur_level == 3 :
        ">текст ивента квиддича 4-3" 
        
        if nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 140

        call nsp_bonus_calc
            
    elif cur_level == 4 :
        ">текст ивента квиддича 4-4"  
        
        if nsp_germiona_mediawhoring < 150 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 160 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 190

        call nsp_bonus_calc
        
        $ hermi.liking -= 4
            
    elif cur_level == 5 :
        ">текст ивента квиддича 4-5"  
        
        if nsp_germiona_mediawhoring < 170 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 180 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_4 = cur_level
        
        $ nsp_newspaper_bonus_base = 220

        call nsp_bonus_calc
        
        $ hermi.liking -= 6
            

    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_kviddich_5 :

    if cur_level == 1 :
        ">текст преивента квиддича 5-1"
    elif cur_level == 2 :
        ">текст преивента квиддича 5-2"
    elif cur_level == 3 :
        ">текст преивента квиддича 5-3"            
    elif cur_level == 4 :
        ">текст преивента квиддича 5-4"            
    elif cur_level == 5 :
        ">текст преивента квиддича 5-5"   
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_kviddich_5_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о квиддиче "
    $ nsp_genie_sphere_diamond_req = 3
    
    if nsp_germiona_kviddich_5_statimg == "New" :
        $ cur_level = nsp_event_kviddich_5 + 1
    else :
        $ cur_level = nsp_event_kviddich_5

    if cur_level == 1 :
        ">текст ивента квиддича 5-1"  
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 80

        call nsp_bonus_calc

    elif cur_level == 2 :
        ">текст ивента квиддича 5-2"  
        
        if nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc

    elif cur_level == 3 :
        ">текст ивента квиддича 5-3"   
        
        if nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 140

        call nsp_bonus_calc
        
        $ hermi.liking -= 2
           
    elif cur_level == 4 :
        ">текст ивента квиддича 5-4"   
        
        if nsp_germiona_mediawhoring < 140 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 150 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 180

        call nsp_bonus_calc
        
        $ hermi.liking -= 4
           
    elif cur_level == 5 :
        ">текст ивента квиддича 5-5"   
        
        if nsp_germiona_mediawhoring < 170 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 180 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_5 = cur_level
        
        $ nsp_newspaper_bonus_base = 220

        call nsp_bonus_calc
        
        $ hermi.liking -= 6
        

    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_kviddich_6 :

    if cur_level == 1 :
        ">текст преивента квиддича 6-1"
    elif cur_level == 2 :
        ">текст преивента квиддича 6-2"
    elif cur_level == 3 :
        ">текст преивента квиддича 6-3"            
    elif cur_level == 4 :
        ">текст преивента квиддича 6-4"            
    elif cur_level == 5 :
        ">текст преивента квиддича 6-5"   
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_kviddich_6_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о квиддиче "
    $ nsp_genie_sphere_diamond_req = 3
    
    if nsp_germiona_kviddich_6_statimg == "New" :
        $ cur_level = nsp_event_kviddich_6 + 1
    else :
        $ cur_level = nsp_event_kviddich_6

    if cur_level == 1 :
        ">текст ивента квиддича 6-1"  
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_6 = cur_level
        
        $ nsp_newspaper_bonus_base = 90

        call nsp_bonus_calc

    elif cur_level == 2 :
        ">текст ивента квиддича 6-2"  
        
        if nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_6 = cur_level
        
        $ nsp_newspaper_bonus_base = 130

        call nsp_bonus_calc

    elif cur_level == 3 :
        ">текст ивента квиддича 6-3"   
        
        if nsp_germiona_mediawhoring < 130 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 140 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_6 = cur_level
        
        $ nsp_newspaper_bonus_base = 180

        call nsp_bonus_calc
           
    elif cur_level == 4 :
        ">текст ивента квиддича 6-4"   
        
        if nsp_germiona_mediawhoring < 160 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 170 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 70 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_6 = cur_level
        
        $ nsp_newspaper_bonus_base = 220

        call nsp_bonus_calc
           
    elif cur_level == 5 :
        ">текст ивента квиддича 6-5"   
        
        if nsp_germiona_mediawhoring < 190 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 200 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 80 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_kviddich_6 = cur_level
        
        $ nsp_newspaper_bonus_base = 260

        call nsp_bonus_calc
        

    call nsp_hermione_goout

    $event.Finalize() 

    return
