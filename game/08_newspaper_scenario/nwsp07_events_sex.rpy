label nsp_event_sex_1 :

    if cur_level == 1 :
        ">текст преивента секса 1-1"
    elif cur_level == 2 :
        ">текст преивента секса 1-2"
    elif cur_level == 3 :
        ">текст преивента секса 1-3"            
    elif cur_level == 4 :
        ">текст преивента секса 1-4"            
    elif cur_level == 5 :
        ">текст преивента секса 1-5"        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_sex_1_complete :

    $ cur_level = 0
    
    if nsp_germiona_sex_1_statimg == "New" :
        $ cur_level = nsp_event_sex_1 + 1
    else :
        $ cur_level = nsp_event_sex_1

    if cur_level == 1 :
        ">текст ивента секса 1-1"
        
        if nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_sex_1 = cur_level
            
    elif cur_level == 2 :
        ">текст ивента секса 1-2"
        
        if nsp_germiona_mediawhoring < 35 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 45 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_1 = cur_level
            
    elif cur_level == 3 :
        ">текст ивента секса 1-3" 
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_1 = cur_level
            
    elif cur_level == 4 :
        ">текст ивента секса 1-4"  
        
        if nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_1 = cur_level
        
    elif cur_level == 5 :
        ">текст ивента секса 1-5"
        
        if nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_1 = cur_level
        

    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_sex_2 :

    if cur_level == 1 :
        ">текст преивента секса 2-1"        
        
    elif cur_level == 2 :
        ">текст преивента секса 2-2"
        
    elif cur_level == 3 :
        ">текст преивента секса 2-3"
        
    elif cur_level == 4 :
        ">текст преивента секса 2-4" 
        
    elif cur_level == 5 :
        ">текст преивента секса 2-5" 
        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_sex_2_complete :

    $ cur_level = 0
    
    if nsp_germiona_sex_2_statimg == "New" :
        $ cur_level = nsp_event_sex_2 + 1
    else :
        $ cur_level = nsp_event_sex_2

    if cur_level == 1 :
        ">текст ивента секса 2-1"  
        
        if nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_2 = cur_level        

    elif cur_level == 2 :
        ">текст ивента секса 2-2"
        
        if nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_2 = cur_level 
            
    elif cur_level == 3 :
        ">текст ивента секса 2-3"   
        
        if nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_2 = cur_level
            
    elif cur_level == 4 :
        ">текст ивента секса 2-4"            
        
        if nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_2 = cur_level
            
    elif cur_level == 5 :
        ">текст ивента секса 2-5" 
        
        if nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_2 = cur_level 

    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_sex_3 :

    if cur_level == 1 :
        ">текст преивента секса 3-1"
    elif cur_level == 2 :
        ">текст преивента секса 3-2"
    elif cur_level == 3 :
        ">текст преивента секса 3-3"            
    elif cur_level == 4 :
        ">текст преивента секса 3-4"            
    elif cur_level == 5 :
        ">текст преивента секса 3-5"        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_sex_3_complete :

    $ cur_level = 0
    
    if nsp_germiona_sex_3_statimg == "New" :
        $ cur_level = nsp_event_sex_3 + 1
    else :
        $ cur_level = nsp_event_sex_3

    if cur_level == 1 :
        ">текст ивента секса 3-1"
        
        if nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_sex_3 = cur_level
        
    elif cur_level == 2 :
        ">текст ивента секса 3-2"
        
        if nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_3 = cur_level
        
    elif cur_level == 3 :
        ">текст ивента секса 3-3" 
        
        if nsp_germiona_mediawhoring < 75 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 85 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1 
            
        $ nsp_event_sex_3 = cur_level  
        
    elif cur_level == 4 :
        ">текст ивента секса 3-4" 
        
        if nsp_germiona_mediawhoring < 95 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 105 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_3 = cur_level
            
    elif cur_level == 5 :
        ">текст ивента секса 3-5"  
        
        if nsp_germiona_mediawhoring < 115 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 125 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_3 = cur_level
            

    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_sex_4 :

    if cur_level == 1 :
        ">текст преивента секса 4-1"
    elif cur_level == 2 :
        ">текст преивента секса 4-2"
    elif cur_level == 3 :
        ">текст преивента секса 4-3"            
    elif cur_level == 4 :
        ">текст преивента секса 4-4"            
    elif cur_level == 5 :
        ">текст преивента секса 4-5"        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_sex_4_complete :

    $ cur_level = 0
    
    if nsp_germiona_sex_4_statimg == "New" :
        $ cur_level = nsp_event_sex_4 + 1
    else :
        $ cur_level = nsp_event_sex_4
        
    if cur_level == 1 :
        ">текст ивента секса 4-1"
        
        if nsp_germiona_mediawhoring < 45 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 55 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_4 = cur_level
        
    elif cur_level == 2 :
        ">текст ивента секса 4-2"
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_4 = cur_level
            
    elif cur_level == 3 :
        ">текст ивента секса 4-3" 
        
        if nsp_germiona_mediawhoring < 85 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 95 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_4 = cur_level
            
    elif cur_level == 4 :
        ">текст ивента секса 4-4"  
        
        if nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 130 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_4 = cur_level
            
    elif cur_level == 5 :
        ">текст ивента секса 4-5"  
        
        if nsp_germiona_mediawhoring < 140 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 150 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_4 = cur_level
            

    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_sex_5 :

    if cur_level == 1 :
        ">текст преивента секса 5-1"
    elif cur_level == 2 :
        ">текст преивента секса 5-2"
    elif cur_level == 3 :
        ">текст преивента секса 5-3"            
    elif cur_level == 4 :
        ">текст преивента секса 5-4"            
    elif cur_level == 5 :
        ">текст преивента секса 5-5"   
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_sex_5_complete :

    $ cur_level = 0
    
    if nsp_germiona_sex_5_statimg == "New" :
        $ cur_level = nsp_event_sex_5 + 1
    else :
        $ cur_level = nsp_event_sex_5

    if cur_level == 1 :
        ">текст ивента секса 5-1"  
        
        if nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_5 = cur_level

    elif cur_level == 2 :
        ">текст ивента секса 5-2"  
        
        if nsp_germiona_mediawhoring < 65 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 75 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_5 = cur_level

    elif cur_level == 3 :
        ">текст ивента секса 5-3"   
        
        if nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_5 = cur_level
           
    elif cur_level == 4 :
        ">текст ивента секса 5-4"   
        
        if nsp_germiona_mediawhoring < 115 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 125 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_5 = cur_level
           
    elif cur_level == 5 :
        ">текст ивента секса 5-5"   
        
        if nsp_germiona_mediawhoring < 160 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 170 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_sex_5 = cur_level
        

    call nsp_hermione_goout

    $event.Finalize() 

    return

