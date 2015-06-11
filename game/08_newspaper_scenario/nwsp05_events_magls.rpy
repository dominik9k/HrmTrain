label nsp_event_magls_1 :

    if cur_level == 1 :
        ">текст преивента маглов 1-1"
    elif cur_level == 2 :
        ">текст преивента маглов 1-2"
    elif cur_level == 3 :
        ">текст преивента маглов 1-3"            
    elif cur_level == 4 :
        ">текст преивента маглов 1-4"            
    elif cur_level == 5 :
        ">текст преивента маглов 1-5"        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_magls_1_complete :

    $ cur_level = 0
    
    if nsp_germiona_magls_1_statimg == "New" :
        $ cur_level = nsp_event_magls_1 + 1
    else :
        $ cur_level = nsp_event_magls_1

    if cur_level == 1 :
        ">текст ивента маглов 1-1"
        
        if nsp_germiona_mediawhoring < 10 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_magls_1 = cur_level
            
    elif cur_level == 2 :
        ">текст ивента маглов 1-2"
        
        if nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_magls_1 = cur_level
            
    elif cur_level == 3 :
        ">текст ивента маглов 1-3" 
        
        if nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_1 = cur_level
            
    elif cur_level == 4 :
        ">текст ивента маглов 1-4"  
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_1 = cur_level
        
    elif cur_level == 5 :
        ">текст ивента маглов 1-5"
        
        if nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_1 = cur_level
        

    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_magls_2 :

    if cur_level == 1 :
        ">текст преивента маглов 2-1"        
        
    elif cur_level == 2 :
        ">текст преивента маглов 2-2"
        
    elif cur_level == 3 :
        ">текст преивента маглов 2-3"
        
    elif cur_level == 4 :
        ">текст преивента маглов 2-4" 
        
    elif cur_level == 5 :
        ">текст преивента маглов 2-5" 
        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_magls_2_complete :

    $ cur_level = 0
    
    if nsp_germiona_magls_2_statimg == "New" :
        $ cur_level = nsp_event_magls_2 + 1
    else :
        $ cur_level = nsp_event_magls_2

    if cur_level == 1 :
        ">текст ивента маглов 2-1"  
        
        if nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_magls_2 = cur_level        

    elif cur_level == 2 :
        ">текст ивента маглов 2-2"
        
        if nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_2 = cur_level 
            
    elif cur_level == 3 :
        ">текст ивента маглов 2-3"   
        
        if nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_2 = cur_level
            
    elif cur_level == 4 :
        ">текст ивента маглов 2-4"            
        
        if nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_2 = cur_level
            
    elif cur_level == 5 :
        ">текст ивента маглов 2-5" 
        
        if nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_2 = cur_level 

    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_magls_3 :

    if cur_level == 1 :
        ">текст преивента маглов 3-1"
    elif cur_level == 2 :
        ">текст преивента маглов 3-2"
    elif cur_level == 3 :
        ">текст преивента маглов 3-3"            
    elif cur_level == 4 :
        ">текст преивента маглов 3-4"            
    elif cur_level == 5 :
        ">текст преивента маглов 3-5"        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_magls_3_complete :

    $ cur_level = 0
    
    if nsp_germiona_magls_3_statimg == "New" :
        $ cur_level = nsp_event_magls_3 + 1
    else :
        $ cur_level = nsp_event_magls_3

    if cur_level == 1 :
        ">текст ивента маглов 3-1"
        
        if nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_magls_3 = cur_level
        
    elif cur_level == 2 :
        ">текст ивента маглов 3-2"
        
        if nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_3 = cur_level
        
    elif cur_level == 3 :
        ">текст ивента маглов 3-3" 
        
        if nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1 
            
        $ nsp_event_magls_3 = cur_level  
        
    elif cur_level == 4 :
        ">текст ивента маглов 3-4" 
        
        if nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_3 = cur_level
            
    elif cur_level == 5 :
        ">текст ивента маглов 3-5"  
        
        if nsp_germiona_mediawhoring < 130 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 140 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_3 = cur_level
            

    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_magls_4 :

    if cur_level == 1 :
        ">текст преивента маглов 4-1"
    elif cur_level == 2 :
        ">текст преивента маглов 4-2"
    elif cur_level == 3 :
        ">текст преивента маглов 4-3"            
    elif cur_level == 4 :
        ">текст преивента маглов 4-4"            
    elif cur_level == 5 :
        ">текст преивента маглов 4-5"        
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_magls_4_complete :

    $ cur_level = 0
    
    if nsp_germiona_magls_4_statimg == "New" :
        $ cur_level = nsp_event_magls_4 + 1
    else :
        $ cur_level = nsp_event_magls_4
        
    if cur_level == 1 :
        ">текст ивента маглов 4-1"
        
        if nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 30 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 10 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_4 = cur_level
        
    elif cur_level == 2 :
        ">текст ивента маглов 4-2"
        
        if nsp_germiona_mediawhoring < 45 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 55 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_4 = cur_level
            
    elif cur_level == 3 :
        ">текст ивента маглов 4-3" 
        
        if nsp_germiona_mediawhoring < 60 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 30 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_4 = cur_level
            
    elif cur_level == 4 :
        ">текст ивента маглов 4-4"  
        
        if nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_4 = cur_level
            
    elif cur_level == 5 :
        ">текст ивента маглов 4-5"  
        
        if nsp_germiona_mediawhoring < 110 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_4 = cur_level
            

    call nsp_hermione_goout

    $event.Finalize() 

    return

label nsp_event_magls_5 :

    if cur_level == 1 :
        ">текст преивента маглов 5-1"
    elif cur_level == 2 :
        ">текст преивента маглов 5-2"
    elif cur_level == 3 :
        ">текст преивента маглов 5-3"            
    elif cur_level == 4 :
        ">текст преивента маглов 5-4"            
    elif cur_level == 5 :
        ">текст преивента маглов 5-5"   
            
    $event.Finalize()    
    
    jump hermione_goout
    
label nsp_event_magls_5_complete :

    $ cur_level = 0
    
    if nsp_germiona_magls_5_statimg == "New" :
        $ cur_level = nsp_event_magls_5 + 1
    else :
        $ cur_level = nsp_event_magls_5

    if cur_level == 1 :
        ">текст ивента маглов 5-1"  
        
        if nsp_germiona_mediawhoring < 40 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 50 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 20 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_5 = cur_level

    elif cur_level == 2 :
        ">текст ивента маглов 5-2"  
        
        if nsp_germiona_mediawhoring < 70 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 80 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 40 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_5 = cur_level

    elif cur_level == 3 :
        ">текст ивента маглов 5-3"   
        
        if nsp_germiona_mediawhoring < 90 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 100 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 50 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_5 = cur_level
           
    elif cur_level == 4 :
        ">текст ивента маглов 5-4"   
        
        if nsp_germiona_mediawhoring < 120 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 130 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_5 = cur_level
           
    elif cur_level == 5 :
        ">текст ивента маглов 5-5"   
        
        if nsp_germiona_mediawhoring < 160 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 170 :
            $ nsp_germiona_mediawhoring += 1
            
        if nsp_germiona_impudence < 60 :
            $ nsp_germiona_impudence += 1
            
        $ nsp_event_magls_5 = cur_level
        

    call nsp_hermione_goout

    $event.Finalize() 

    return

