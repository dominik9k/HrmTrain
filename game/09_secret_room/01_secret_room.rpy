label sroom_main:
    
    scene title2
    with flashbb

    python :
        achieve = Achievement()
    
    dr "Добро пожаловать Тайную Комнату. Здесь вы можете изучить список своих игровых достижений и насладиться некоторыми бонусами."
    
    
    label sroom_main2:
    menu:
    
#        "- Пригласить девушку -":
        
        "- Посмотреть список достижений -":
            python :
                achieve.ShowList("sroom_main2")
            
    
        "- Отмена -":
            return 
    
    return