label sroom_main:
    
    scene title2
    with flashbb

    call Achievement_constants
    
    python :
    
        global achieve
    
        achieve = Achievement()
    
    dr "Добро пожаловать Тайную Комнату. Здесь вы можете изучить список своих игровых достижений и насладиться некоторыми бонусами."
    
    
    label sroom_main2:
    menu:
    
#        "- Пригласить девушку -":
        
        "- Посмотреть список достижений -":
            label sroom_achlist :

                python :
                    achieve.ShowList("sroom_main2",None)

                    renpy.say( ach, achieve.DispDescription())
                    
                call sroom_achlist
            
    
        "- Отмена -":
            return 
    
    return