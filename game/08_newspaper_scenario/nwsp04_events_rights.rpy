label nsp_event_rights_1 :

    if cur_level == 1 :
        ">текст преивента прав 1-1"
    elif cur_level == 2 :
        ">текст преивента прав 1-2"
    elif cur_level == 3 :
        ">текст преивента прав 1-3"            
    elif cur_level == 4 :
        ">текст преивента прав 1-4"            
    elif cur_level == 5 :
        ">текст преивента прав 1-5"        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_rights_1_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о правах "
    $ nsp_genie_sphere_diamond_req = 1
    
    if nsp_germiona_rights_1_statimg == "New" :
        $ cur_level = nsp_event_rights_1 + 1
    else :
        $ cur_level = nsp_event_rights_1

    if cur_level == 1 :
        ">текст ивента прав 1-1"
        
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

    $event.Finalize() 

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
        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_rights_2_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о правах "
    $ nsp_genie_sphere_diamond_req = 1
    
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

    $event.Finalize() 

    return

label nsp_event_rights_3 :

    if cur_level == 1 :
        ">текст преивента прав 3-1"
    elif cur_level == 2 :
        ">текст преивента прав 3-2"
    elif cur_level == 3 :
        ">текст преивента прав 3-3"            
    elif cur_level == 4 :
        ">текст преивента прав 3-4"            
    elif cur_level == 5 :
        ">текст преивента прав 3-5"        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_rights_3_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о правах "
    $ nsp_genie_sphere_diamond_req = 4
    
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

    $event.Finalize() 

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
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_rights_4_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о правах "
    $ nsp_genie_sphere_diamond_req = 2
    
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

    $event.Finalize() 

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
    $ nsp_genie_sphere_diamond_req = 2
    
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

    $event.Finalize() 

    return

