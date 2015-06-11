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
            
    elif cur_level == 2 :
        ">текст ивента леса 1-2"
        
        if nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_forest_1 = cur_level
            
    elif cur_level == 3 :
        ">текст ивента леса 1-3" 
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_forest_1 = cur_level
            
    elif cur_level == 4 :
        ">текст ивента леса 1-4"  
        
        if nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_forest_1 = cur_level
        
    elif cur_level == 5 :
        ">текст ивента леса 1-5"
        
        if nsp_germiona_mediawhoring < 150 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 160 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_forest_1 = cur_level
        

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

    elif cur_level == 2 :
        ">текст ивента леса 2-2"
        
        if nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_forest_2 = cur_level 
            
    elif cur_level == 3 :
        ">текст ивента леса 2-3"   
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_forest_2 = cur_level
            
    elif cur_level == 4 :
        ">текст ивента леса 2-4"            
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_forest_2 = cur_level
            
    elif cur_level == 5 :
        ">текст ивента леса 2-5" 
        
        if nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_forest_2 = cur_level 

    call nsp_hermione_goout

    $event.Finalize() 

    return



