label event_01_init():
    python:
        GE.localsWriteNew( "bird_examined", False );
        GE.localsWriteNew( "desk_examined", False );
        GE.localsWriteNew( "cupboard_examined", False );
        GE.localsWriteNew( "door_examined", False );
        GE.localsWriteNew( "fireplace_examined", False );
    return

label event_01_cond():
    python:
        result = False
        if( GE.day() == 1 and not GE.locals( "bird_examined" ) and 
            not GE.locals( "desk_examined" ) and not GE.locals( "cupboard_examined" ) and 
            not GE.locals( "door_examined" ) and not GE.locals( "fireplace_examined" ) ):
            result = True
    return result

label event_011(): #First event in the game. Gennie finds himself at the desk.
    $screens.ShowD3("bld1")
    $hero(  m,  "......1............?// Ваше высочество?// .......................................................",
            g4, "Я сделал это снова?// Телепортировал себя непонятно куда...",
            m,  "Что с этими ингредиентами?// Похоже, они мощнее, чем я думал.// Ну, не важно что это за место, дел у меня тут нет...// Лучше обернуть заклинание вспять, иначе принцесса будет снова злиться на меня...//"
                ".....................// Хотя...// Есть в этом месте что-то странное... это...// Оно наполненно.... // МАГИЕЙ?!//"
                " Да... магия, я чувствую. Такая мощная и в то же время...// ...чужая.// Интересно...// Думаю, нужно здесь осмотреться...")

    $screens.HideD3("bld1")
    #$this.event_01.Finalize()
    return

label event_01_actions( aActionName ):
    $hero(  m,  "......1....23123123123........?// Ваше высочество?// .......................................................")    
    return