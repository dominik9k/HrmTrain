label nsp_theme_rights :
    
    $herView.hideshowQQ( "body_01.png", pos )
    m "Итак, пришло направить твою стропт... настойчивость на новую цель."
    her "Сэр ?"
    m "Ты помнишь, зачем приходила в этот кабинет в первый раз ?"
    $herView.hideshowQQ( "body_15.png", pos )
    her "Э... Это когда вы попросили меня..."
    m "Нет, в самый первый раз."
    her "А, вы имеете ввиду, на первом курсе, когда мы с Гарри и Роном..."
    g4 "(Кактус мне в ухо.)"
    m "В первый раз с тех пор, как я здесь появ... Нет опять не то."
    m "Я говорю про твои обвинения в адрес преподавателей, проявляющих дискриминацию."
    $herView.hideshowQQ( "body_75.png", pos )
    her "Да, понимаю. Пришло время раскрыть правду общественности ?"
    her "Отлично, я готова !"
    $herView.hideshowQQ( "body_01.png", pos )
    g1 "Кхм-кха."
    m "На самом деле, я предлагаю сначала подготовить почву для этого."
    g9 "Есть пара идей, как это сделать."
    her "Хорошо, сэр."

    return

label nsp_event_rights_1 :

    if cur_level == 1 :
        $herView.hideshowQQ( "body_01.png", pos )
        
        if nsp_event_rights_1 == 0 :
            m "Сегодня тебе предстоит составить репортаж о том, как некоторые ученики пристают к девочкам. Возможно, это слизеринцы."
            m "Нам действительно нужен этот материал."
            $herView.hideshowQQ( "body_02.png", pos )
            her "Вы хотите, чтобы я провела расследование ?"
            m "Не ты ли жаловалась, что такое происходит ? Теперь есть возможность привлечь внимание читателей к проблеме."
            $herView.hideshowQQ( "body_24.png", pos )
            her "Да, но я..."
            her "Возможно, я немного преувеличила."
            her "То есть некоторые ученики действительно ведут себя неподобающе, но это происходит не так часто."
            m "Это не важно, от тебя требуется только придумать сюжет и убедительно пересказать его мне."
            $herView.hideshowQQ( "body_13.png", pos )
            her "Ну, если вы так считаете... Хорошо."
            $herView.hideshowQQ( "body_01.png", pos )
        else :
            m "Сегодня тебе снова предстоит придумать рассказ о домогательствах."
            m "Есть вдохновение ?"
            $herView.hideshowQQ( "body_06.png", pos )
            her "Наверное да, сэр."
            
        $herView.hideshowQQ( "body_01.png", pos )
        
    elif cur_level == 2 :
        $herView.hideshowQQ( "body_01.png", pos )
        
        if nsp_event_rights_1 == 1 :
            m "Сегодня тебе предстоит придумать новый текст репортажа."
            her "Опять про приставание на улице ?"
            m "Эм... Прояви фантазию ! На этот раз можно написать про..."
            g1 "Про..."
            her "Похоже, не только у меня плохо с фантазией."
            her "Сэр."
            g4 "Ах так ? Вечером принеси мне рассказ про пенную вечиринку !"
            her "Ох."
            her "Профессор, но я ни разу не была на пенных... Да я и на обычных вечиринках бываю редко."
            g9 "Что поделать, жизнь журналиста состоит не только из славы и доступных девчо... то есть почестей."
            m "Жду тебя вечером."
            her "Да, сэр."
          
        else :
            g9 "Сегодня вечером мы должны снова проработать тему вечеринок для читателей."
            $herView.hideshowQQ( "body_06.png", pos )
            her "Так точно, сэр."
            
        $herView.hideshowQQ( "body_01.png", pos )
        
    elif cur_level == 3 :
        ">текст преивента прав 1-3"            
    elif cur_level == 4 :
        ">текст преивента прав 1-4"            
    elif cur_level == 5 :
        ">текст преивента прав 1-5"        
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_rights_1_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о правах "
    $ nsp_genie_sphere_req = nsp_germiona_rights_1_photo
    
    if nsp_germiona_rights_1_statimg == "New" :
        $ cur_level = nsp_event_rights_1 + 1
    else :
        $ cur_level = nsp_event_rights_1

    if cur_level == 1 :
    
        show screen hermione_02
        $herView.hideshowQQ( "body_01.png", pos )
        g9 "Ты пришла ? Отлично, я готов записывать."
        $herView.hideshowQQ( "body_06.png", pos )
        her "Хорошо, сэр"
        her "Сегодня я шла по улице в сторону оранжереи."
        her "Вот."
        g9 "Отлично, продолжай."
        $herView.hideshowQQ( "body_09.png", pos )
        her "И у двери стояла группа слизеринцев. Один из них позвал меня и я..."
        m "И ты пошла с ним в укромное место ?"
        $herView.hideshowQQ( "body_13.png", pos )
        her "Э... Нет, сэр. Я попыталась пройти мимо. Но один из них загородил мне дорогу."
        her "Пока я пыталась его обойти, подошли остальные."
        $herView.hideshowQQ( "body_24.png", pos )
        her "И они... Они трогали меня..."
        m "Трогали ? Как именно трогали ?"
        $herView.hideshowQQ( "body_31.png", pos )
        her "Я ..."
        $herView.hideshowQQ( "body_33.png", pos )
        ">Гермиона покраснела и замолчала."
        $herView.hideshowQQ( "body_30.png", pos )
        her "Сэр, напоминаю вам, что это выдуманная история !"
        m "Да, но у любой истории должно быть окончание."
        $herView.hideshowQQ( "body_45.png", pos )
        her "Ммм. Хорошо."
        her "Один из них схватил меня за локоть и начал поглаживать плечо."
        her "Другой погладил по щеке."
        $herView.hideshowQQ( "body_54.png", pos )
        her "Третий... Третий..."
        m "И что же третий ?"
        her "Третий подошел сзади и положил руку мне на живот."
        $herView.hideshowQQ( "body_85.png", pos )
        her "Сэр, я больше не могу."
        m "Ну же, еще пару фраз для завершения."
        her "Мне очень стыдно такое представлять."
        g4 "Сосредоточься !"
        $herView.hideshowQQ( "body_81.png", pos )
        her "Ладно. Четвертый парень усмехнулся и посмотрел мне в глаза. Маленькая шлюха, сказал он."
        her "И..."
        m "И ?"
        $herView.hideshowQQ( "body_59.png", pos )
        her "И приподняв край моей юбки провел рукой по обнаженному бедру."
        her "А потом я вырвалась и убежала."
        her "Вот и вся история, сэр."
        g9 "Ну что же, совсем неплохо."
        $herView.hideshowQQ( "body_02.png", pos )
        her "Правда, сэр ?"
        m "Да. До следующего раза."
        $herView.hideshowQQ( "body_14.png", pos )
        her "Следующего ра... Да, профессор, как скажете."
        $herView.hideshowQQ( "body_01.png", pos )
        
        if nsp_germiona_mediawhoring < 10 :
            $ nsp_germiona_mediawhoring += 2
        elif nsp_germiona_mediawhoring < 20 :
            $ nsp_germiona_mediawhoring += 1
            
        $ nsp_event_rights_1 = cur_level
        
        $ nsp_newspaper_bonus_base = 10
        
        call nsp_bonus_calc
            
    elif cur_level == 2 :
        show screen hermione_02
        $herView.hideshowQQ( "body_01.png", pos )
        
        her "Здравствуйте, сэр."
        m "Здравствуй, Гермиона. Давай сразу к делу. Что ты можешь рассказать мне о недавней вечеринке на факультете Слизерин ?"
        her "(Я так и знала, что этот старый извращенец упомянет Слизерин.)"
        m "Ты что-то сказала ?"
        her "Я говорю, прекрасный выбор, сэр. Вы как всегда в ударе."
        m "Итак ?"
        her "Нуууу. На прошлой неделе в гостиной подземелья Слизерина устроили просто нечто."
        g5 "Слизеринцы живут в подземелье ??? Впрочем не важно, продолжай."
        her "Сок лился рекой, друзья шутили друг над другом, всем было весело, а какие там были викторины ..."
        m "И розовые пони какали радугой на брудершафт..."
        g4 "Ты издеваешься ? Может быть мне лучше было доверить спасение школы кому-то вроде этой Гринграсс ?"
        her "Простите, сэр, я исправлюсь !"
        her "Пиво лилось рекой, небольшие компании распивали напитки покрепче, раскрасневшиеся девчонки постепенно позволяли себе все больше..."
        g9 "О да, я в тебе не сомневался. Продолжай !"
        her "Чем больше меня накачивали, тем приятнее становилось..."
        g5 ".............."
        her "Пивом, сэр ! Я про пиво !"
        her "И вот кульминация вечиринки. Все девчонки собрались в круг. Парни приготовились. И началась..."
        g9 "Оргия ! О да, я знал это. Давай же, главное не упускай подробности !"
        her "..............."
        her "Сэр."
        her "Я..."
        her "Прошу вас, не говорите таких вещей."
        g6 "Но ты же не оставишь меня... в смысле рассказ в таком состоянии ?"
        m "Нам нужно что-то действительно интересное. Неужели у тебя нет никаких идей ?"
        her "Эм, да. Если подумать..."
        her "Итак, все собрались и начался конкурс. Все девушки пытались пройти под шестом изогнувшись, не задев его грудью."
        her "Побеждает та, которой громче будет кричать толпа."
        her "В какой-то момент выпивка начала ударять в голову..."
        g1 "И тебе тоже !"
        her "Да, мне тоже... И мы начали проходить под шестом задрав рубашку, с голой грудью..."
        g9 "Превосходно ! Продолжай !"
        her "И вот настала моя очередь. Все уставились только на меня."
        m "О да, детка"
        her "Мои освобожденные буфера весело подпрыгнули, разгоряченное тело изогнулось..."
        g1 "аааааргх"
        her "И я начала проходить, стараясь удержать равновесие."
        her "Но алкоголь сделал свое дело."
        her "Меня начало вести в бок. Какой-то хитрый парень воспользовался ситуацией и подошел меня поддержать."
        her "И он схватил..."
        her "Нет, я не могу это сказать."
        m "Давай, сделай это !"
        her "Вы помните, что это всего лишь придуманный рассказ ?"
        m "Ты сейчас все испортишь ! Нужно немедленно кончить ! То есть закончить !"
        her "Хорошо, хорошо. И он схватил мои буфера, как бы поддерживая и начал их мять."
        her "В этот момент я опомнилась, и начала вырываться. От неожиданности он отступил, и я, покраснев, убежала."
        her "Вот такие вечиринки и проходят на факультете Слизерин."
        her "Это непримелимо и с ними нужно бороться."
        her "Хороший финал, сэр ?"
        g7 "Всхлюп. Да да, все отлично. Ты можешь идти. У меня тут небольшая авария."
        her "Эх, профессор."
        
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

    $wtevent.Finalize() 

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
        
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_rights_2_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о правах "
    $ nsp_genie_sphere_req = nsp_germiona_rights_2_photo
    
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

    $wtevent.Finalize() 

    return

label nsp_event_rights_3 :

    if cur_level == 1 :
    
        $herView.hideshowQQ( "body_01.png", pos )
        ">текст преивента прав 3-1"
        $herView.hideshowQQ( "body_01.png", pos )
        
    elif cur_level == 2 :
        ">текст преивента прав 3-2"
    elif cur_level == 3 :
        ">текст преивента прав 3-3"            
    elif cur_level == 4 :
        ">текст преивента прав 3-4"            
    elif cur_level == 5 :
        ">текст преивента прав 3-5"        
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_rights_3_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о правах "
    $ nsp_genie_sphere_req = nsp_germiona_rights_3_photo
    
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
        
        $ nsp_event_rights_3_unpub = True
        
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
        
        $ nsp_event_rights_3_unpub = True
        
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
        
        $ nsp_event_rights_3_unpub = True
        
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
        
        $ nsp_event_rights_3_unpub = True
            
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

    $wtevent.Finalize() 

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
            
    $wtevent.Finalize()    
    
    jump hermione_goout
    
label nsp_event_rights_4_complete :

    $ cur_level = 0
    
    $ nsp_newspaper_bonus_text_base = " о правах "
    $ nsp_genie_sphere_req = nsp_germiona_rights_4_photo
    
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

    $wtevent.Finalize() 

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
    $ nsp_genie_sphere_req = nsp_germiona_rights_5_photo
    
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

    $wtevent.Finalize() 

    return

