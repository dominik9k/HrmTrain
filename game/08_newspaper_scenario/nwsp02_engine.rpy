################
### Основные обработчики ###                
################

label newsp_letter:

    call bigletter(["{size=-7}От: Министерства Магии\nКому: Профессору Альбусу Дамблдору\n\n{/size}"
    "{size=-4}Дорогой профессор Дамблдор.\n\nМы хотим сообщить Вам, что Комитет по Прессе изучил "
    "реакцию ваших читателей в школе и постановил следующее:\n\n"
    "В соответствии с популярностью последнего выпуска газеты выплатить редакции "
    "[nsp_newspaper_cur_money] галлеонов.\n\n"
    "Спасибо за сотрудничество !\n\n"
    "{size=-3}С уважением,\nМинистерство Магии.{/size}"])
    
    $ gold += nsp_newspaper_cur_money
    
    if (hermi._incomePercent>0):
        $nsp_newspaper_cur_money=nsp_newspaper_cur_money*hermi._incomePercent//100
        $gold-=nsp_newspaper_cur_money
        "> Согласно вашему соглашению с Гермионой [dgold] галеонов ([hermi._incomePercent]%%) перечисляются на ее счет"
    
    $ nsp_newspaper_published = False
    $ nsp_newspaper_last_money = nsp_newspaper_cur_money
    
    if nsp_newspaper_menu == 2:
        $hero(m,"{size=+1}АРГХ ! Тысяча песчаных змей и один питон!..{/size}")
        $hero("{size=+1}Проклятые разработчики модов ! Да вы издеваетесь !{/size}")
        dr "Одну минутку..."
        $hero("{size=+1}Столько стараний ради [nsp_newspaper_cur_money] галлеонов ? Сейчас здесь будет убийство !{/size}")
        dr "Да погоди, не кипятись. Дело в том, что..."
        $hero("{size=-1}Да пошел ты ! Больше никаких модов, только классика !{/size}")
        dr "О не-е-е-е-е-е-ет... Джинни, я обещаю, что ты не зря учился газетному делу ! Спроси Снейпа, и он подскажет, как заработать больше !"
        $hero("{size=-4}Хммм. Ладно, только ради тебя, дам моду еще один шанс.{/size}")
        $ nsp_newspaper_menu = 3

    $event.Finalize()
    call screen main_menu_01

label nsp_newsp_themes:
    
    $ nsp_germiona_statimg_rights = "Block" # Гермиона: Доступность раздела "Права и дискриминация"
    $ nsp_germiona_statimg_magls = "Block" # Гермиона: Доступность раздела "О жизни маглов публично"
    $ nsp_germiona_statimg_kviddich = "Block"  # Гермиона: Доступность раздела "О квиддиче"
    $ nsp_germiona_statimg_sex = "Block"  # Гермиона: Доступность раздела "О Сексе"
    $ nsp_germiona_statimg_maniak = "Block"  # Гермиона: Доступность раздела "Маньяк"
    $ nsp_germiona_statimg_nude = "Block"  # Гермиона: Доступность раздела "Голый репортер в маске"
    $ nsp_germiona_statimg_forest = "Block"  # Гермиона: Доступность раздела "Запретный лес"
    $ nsp_germiona_statimg_studio = "Block"  # Гермиона: Доступность раздела "Студия у Джина"
    
    $ nsp_germiona_rights_1_statimg = "Block"
    $ nsp_germiona_rights_2_statimg = "Block"
    $ nsp_germiona_rights_3_statimg = "Block"
    $ nsp_germiona_rights_4_statimg = "Block"
    $ nsp_germiona_rights_5_statimg = "Block"
    
    $ nsp_germiona_magls_1_statimg = "Block"
    $ nsp_germiona_magls_2_statimg = "Block"
    $ nsp_germiona_magls_3_statimg = "Block"
    $ nsp_germiona_magls_4_statimg = "Block"
    $ nsp_germiona_magls_5_statimg = "Block"
    
    $ nsp_germiona_kviddich_1_statimg = "Block"
    $ nsp_germiona_kviddich_2_statimg = "Block"
    $ nsp_germiona_kviddich_3_statimg = "Block"
    $ nsp_germiona_kviddich_4_statimg = "Block"
    $ nsp_germiona_kviddich_5_statimg = "Block"
    $ nsp_germiona_kviddich_6_statimg = "Block"
    
    $ nsp_germiona_sex_1_statimg = "Block"
    $ nsp_germiona_sex_2_statimg = "Block"
    $ nsp_germiona_sex_3_statimg = "Block"
    $ nsp_germiona_sex_4_statimg = "Block"
    $ nsp_germiona_sex_5_statimg = "Block"
    
    $ nsp_germiona_maniak_1_statimg = "Block"
    $ nsp_germiona_maniak_2_statimg = "Block"
    $ nsp_germiona_maniak_3_statimg = "Block"
    
    $ nsp_germiona_nude_1_statimg = "Block"
    $ nsp_germiona_nude_2_statimg = "Block"
    $ nsp_germiona_nude_3_statimg = "Block"
    $ nsp_germiona_nude_4_statimg = "Block"
    $ nsp_germiona_nude_5_statimg = "Block"
    
    $ nsp_germiona_forest_1_statimg = "Block"
    $ nsp_germiona_forest_2_statimg = "Block"
    
    $ nsp_germiona_studio_1_statimg = "Block"
    $ nsp_germiona_studio_2_statimg = "Block"
    $ nsp_germiona_studio_3_statimg = "Block"
    $ nsp_germiona_studio_4_statimg = "Block"
    $ nsp_germiona_studio_5_statimg = "Block"
    $ nsp_germiona_studio_6_statimg = "Block"
    
    if nsp_germiona_menu_rights == 1:
        $ nsp_germiona_statimg_rights = "New"
    if nsp_germiona_menu_magls == 1:
        $ nsp_germiona_statimg_magls = "New"
    if nsp_germiona_menu_kviddich == 1:
        $ nsp_germiona_statimg_kviddich = "New"
    if nsp_germiona_menu_sex == 1:
        $ nsp_germiona_statimg_sex = "New"
    if nsp_germiona_menu_maniak == 1:
        $ nsp_germiona_statimg_maniak = "New"
    if nsp_germiona_menu_nude == 1:
        $ nsp_germiona_statimg_nude = "New"
    if nsp_germiona_menu_forest == 1:
        $ nsp_germiona_statimg_forest = "New"
    if nsp_germiona_menu_studio == 1:
        $ nsp_germiona_statimg_studio = "New"
        
    if nsp_germiona_menu_rights == 2:
        call nsp_init_flags_rights
    if nsp_germiona_menu_magls == 2:
        $ nsp_germiona_statimg_magls = "New"
    if nsp_germiona_menu_kviddich == 2:
        $ nsp_germiona_statimg_kviddich = "New"
    if nsp_germiona_menu_sex == 2:
        $ nsp_germiona_statimg_sex = "New"
    if nsp_germiona_menu_maniak == 2:
        $ nsp_germiona_statimg_maniak = "New"
    if nsp_germiona_menu_nude == 2:
        $ nsp_germiona_statimg_nude = "New"
    if nsp_germiona_menu_forest == 2:
        $ nsp_germiona_statimg_forest = "New"
    if nsp_germiona_menu_studio == 2:
        $ nsp_germiona_statimg_studio = "New"    
    
    menu:
    
        "- О правах и дискриминации {image=08_newspaper_scenario/flags/[nsp_germiona_statimg_rights].png} -" if nsp_newspaper_menu == 6:
    
            if nsp_germiona_menu_rights == 1 :
                ">Диалог тема 1"
                $ nsp_germiona_menu_rights = 2
                jump hermione_main_menu
        
            elif nsp_germiona_menu_rights == 2 :
                menu:
                    "- Сексуальные домогательства учеников -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_rights_1].png} {image=08_newspaper_scenario/flags/[nsp_germiona_rights_1_statimg].png}" :
                        jump nsp_event_rights_1
                    
                    "{color=#858585}--Не открытое действие-{/color}" if nsp_genie_writer < 1:
                        call nsp_vague_idea
                        jump nsp_newsp_themes                    
                        
                    "- Сексуальные домогательства учителей -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_rights_2].png} {image=08_newspaper_scenario/flags/[nsp_germiona_rights_2_statimg].png}" if nsp_genie_writer >= 1 :
                        jump nsp_event_rights_2

                    "{color=#858585}--Не открытое действие-{/color}" if nsp_genie_writer < 4 or (nsp_letter_7 == 0 and nsp_event_rights_3 == 0):
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Интервью с защитницей прав женщин -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_rights_3].png} {image=08_newspaper_scenario/flags/[nsp_germiona_rights_3_statimg].png}" if nsp_genie_writer >= 4 and (nsp_letter_7 > 0 or nsp_event_rights_3 > 0) :
                        jump nsp_event_rights_3

                    "{color=#858585}--Не открытое действие-{/color}" if nsp_genie_writer < 8:
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Заседание ООП с демонстрацией для девочек -\n{image=08_newspaper_scenario/hearts/heart_5[nsp_event_rights_4].png} {image=08_newspaper_scenario/flags/[nsp_germiona_rights_4_statimg].png}" if nsp_genie_writer >= 8 :
                        jump nsp_event_rights_4

                    "{color=#858585}--Не открытое действие-{/color}" if nsp_genie_writer < 10 or (nsp_event_rights_4 < 3):
                        call nsp_vague_idea
                        jump nsp_newsp_themes
                        
                    "- Заседание ООП с демонстрацией для смешанной группы -\n{image=08_newspaper_scenario/hearts/heart_7[nsp_event_rights_5].png} {image=08_newspaper_scenario/flags/[nsp_germiona_rights_5_statimg].png}" if nsp_genie_writer >= 10 and (nsp_event_rights_4 >= 3) :
                        jump nsp_event_rights_5
                
                    "- Ничего -" :
                        jump nsp_newsp_themes
            
        "- О жизни маглов {image=08_newspaper_scenario/flags/[nsp_germiona_statimg_magls].png} -" if nsp_newspaper_menu == 6:
    
            if nsp_germiona_menu_magls == 1 :
                $ nsp_germiona_menu_magls = 2
        
#            if nsp_germiona_menu_rights == 1 :
#                menu:

            jump hermione_goout
            
        "- О квиддиче {image=08_newspaper_scenario/flags/[nsp_germiona_statimg_kviddich].png} -" if nsp_newspaper_menu == 6:
    
            if nsp_germiona_menu_kviddich == 1 :
                $ nsp_germiona_menu_kviddich = 2
        
#            if nsp_germiona_menu_rights == 1 :
#                menu:

            jump hermione_goout
            
        "- О сексе {image=08_newspaper_scenario/flags/[nsp_germiona_statimg_sex].png} -" if nsp_newspaper_menu == 6:
    
            if nsp_germiona_menu_sex == 1 :
                $ nsp_germiona_menu_sex = 2
        
#            if nsp_germiona_menu_rights == 1 :
#                menu:

            jump hermione_goout

        "{color=#858585}--Не открытое действие-{/color}" if nsp_newspaper_menu == 6 and nsp_germiona_menu_maniak == -1:
            jump nsp_newsp_themes
            
        "- Маньяк {image=08_newspaper_scenario/flags/[nsp_germiona_statimg_maniak].png} -" if nsp_newspaper_menu == 6 and nsp_germiona_menu_maniak >= 0:
    
            if nsp_germiona_menu_maniak == 1 :
                $ nsp_germiona_menu_maniak = 2
        
#            if nsp_germiona_menu_rights == 1 :
#                menu:

            jump hermione_goout
            
        "- Голый репортер в маске {image=08_newspaper_scenario/flags/[nsp_germiona_statimg_nude].png} -" if nsp_newspaper_menu == 6:
    
            if nsp_germiona_menu_nude == 1 :
                $ nsp_germiona_menu_nude = 2
        
#            if nsp_germiona_menu_rights == 1 :
#                menu:

            jump hermione_goout

        "{color=#858585}--Не открытое действие-{/color}" if nsp_newspaper_menu == 6 and nsp_germiona_menu_forest == -1:
            jump nsp_newsp_themes
            
        "- Запретный лес {image=08_newspaper_scenario/flags/[nsp_germiona_statimg_forest].png} -" if nsp_newspaper_menu == 6 and nsp_germiona_menu_forest >= 0:
    
            if nsp_germiona_menu_forest == 1 :
                $ nsp_germiona_menu_forest = 2
        
#            if nsp_germiona_menu_rights == 1 :
#                menu:

            jump hermione_goout
            
        "- Студия у Джина {image=08_newspaper_scenario/flags/[nsp_germiona_statimg_studio].png} -" if nsp_newspaper_menu == 6:
    
            if nsp_germiona_menu_studio == 1 :
                $ nsp_germiona_menu_studio = 2
        
#            if nsp_germiona_menu_rights == 1 :
#                menu:

            jump hermione_goout

        "- Ничего -" :
            jump hermione_main_menu

label nsp_init_flags_rights :

#### Event Rights_1
    if nsp_event_rights_1 == 0 and nsp_genie_writer >=0 :
        if hermi.whoring >= 0 and nsp_germiona_mediawhoring >= 0 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_1_statimg = "New"
    elif nsp_event_rights_1 == 1 :            
        if hermi.whoring >= 3 and nsp_germiona_mediawhoring >= 10 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_1_statimg = "New"
        else :
            $ nsp_germiona_rights_1_statimg = "Explored"
    elif nsp_event_rights_1 == 2 :
        if hermi.whoring >= 6 and nsp_germiona_mediawhoring >= 20 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_1_statimg = "New"
        else :
            $ nsp_germiona_rights_1_statimg = "Explored"
    elif nsp_event_rights_1 == 3 :
        if hermi.whoring >= 9 and nsp_germiona_mediawhoring >= 30 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_1_statimg = "New"
        else :
            $ nsp_germiona_rights_1_statimg = "Explored"
    elif nsp_event_rights_1 == 4 :
        if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 40 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_rights_1_statimg = "New"
        else :
            $ nsp_germiona_rights_1_statimg = "Explored"
    elif nsp_event_rights_1 == 5 :
        $ nsp_germiona_rights_1_statimg = "Full"

### Event Rights_2
    if nsp_event_rights_2 == 0 and nsp_genie_writer >= 1 :
        if hermi.whoring >= 3 and nsp_germiona_mediawhoring >= 10 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_2_statimg = "New"
    elif nsp_event_rights_2 == 1 :            
        if hermi.whoring >= 6 and nsp_germiona_mediawhoring >= 20 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_2_statimg = "New"
        else :
            $ nsp_germiona_rights_2_statimg = "Explored"
    elif nsp_event_rights_2 == 2 :
        if hermi.whoring >= 9 and nsp_germiona_mediawhoring >= 30 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_2_statimg = "New"
        else :
            $ nsp_germiona_rights_2_statimg = "Explored"
    elif nsp_event_rights_2 == 3 :
        if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 40 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_rights_2_statimg = "New"
        else :
            $ nsp_germiona_rights_2_statimg = "Explored"
    elif nsp_event_rights_2 == 4 :
        if hermi.whoring >= 15 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_rights_2_statimg = "New"
        else :
            $ nsp_germiona_rights_2_statimg = "Explored"
    elif nsp_event_rights_2 == 5 :
        $ nsp_germiona_rights_2_statimg = "Full"
        
### Event Rights_3
    if nsp_letter_7 == 0:
        $ nsp_germiona_rights_3_statimg = "Denied"
    else :
        if nsp_event_rights_3 == 0 and nsp_genie_writer >= 4 :
            if hermi.whoring >= 0 and nsp_germiona_mediawhoring >= 0 and nsp_germiona_impudence >= 0 :
                $ nsp_germiona_rights_3_statimg = "New"
        elif nsp_event_rights_3 == 1 :            
            if hermi.whoring >= 6 and nsp_germiona_mediawhoring >= 20 and nsp_germiona_impudence >= 0 :
                $ nsp_germiona_rights_3_statimg = "New"
            else :
                $ nsp_germiona_rights_3_statimg = "Explored"
        elif nsp_event_rights_3 == 2 :
            if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 40 and nsp_germiona_impudence >= 10 :
                $ nsp_germiona_rights_3_statimg = "New"
            else :
                $ nsp_germiona_rights_3_statimg = "Explored"
        elif nsp_event_rights_3 == 3 :
            if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 20 :
                $ nsp_germiona_rights_3_statimg = "New"
            else :
                $ nsp_germiona_rights_3_statimg = "Explored"
        elif nsp_event_rights_3 == 4 :
            if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 60 and nsp_germiona_impudence >= 30 :
                $ nsp_germiona_rights_3_statimg = "New"
            else :
                $ nsp_germiona_rights_3_statimg = "Explored"
        elif nsp_event_rights_3 == 5 :
            $ nsp_germiona_rights_3_statimg = "Full"
        
### Event Rights_4
    if nsp_event_rights_4 == 0 and nsp_genie_writer >= 8 :
        if hermi.whoring >= 9 and nsp_germiona_mediawhoring >= 30 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_4_statimg = "New"
    elif nsp_event_rights_4 == 1 :            
        if hermi.whoring >= 12 and nsp_germiona_mediawhoring >= 40 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_4_statimg = "New"
        else :
            $ nsp_germiona_rights_4_statimg = "Explored"
    elif nsp_event_rights_4 == 2 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 60 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_4_statimg = "New"
        else :
            $ nsp_germiona_rights_4_statimg = "Explored"
    elif nsp_event_rights_4 == 3 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 80 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_rights_4_statimg = "New"
        else :
            $ nsp_germiona_rights_4_statimg = "Explored"
    elif nsp_event_rights_4 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 100 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_rights_4_statimg = "New"
        else :
            $ nsp_germiona_rights_4_statimg = "Explored"
    elif nsp_event_rights_4 == 5 :
        $ nsp_germiona_rights_4_statimg = "Full"
        
### Event Rights_5
    if nsp_event_rights_5 == 0 and nsp_genie_writer >= 10 and nsp_event_rights_4 >= 3 :
        if hermi.whoring >= 9 and nsp_germiona_mediawhoring >= 20 and nsp_germiona_impudence >= 0 :
            $ nsp_germiona_rights_5_statimg = "New"
    elif nsp_event_rights_5 == 1 :            
        if hermi.whoring >= 15 and nsp_germiona_mediawhoring >= 50 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_rights_5_statimg = "New"
        else :
            $ nsp_germiona_rights_5_statimg = "Explored"
    elif nsp_event_rights_5 == 2 :
        if hermi.whoring >= 18 and nsp_germiona_mediawhoring >= 60 and nsp_germiona_impudence >= 10 :
            $ nsp_germiona_rights_5_statimg = "New"
        else :
            $ nsp_germiona_rights_5_statimg = "Explored"
    elif nsp_event_rights_5 == 3 :
        if hermi.whoring >= 21 and nsp_germiona_mediawhoring >= 80 and nsp_germiona_impudence >= 20 :
            $ nsp_germiona_rights_5_statimg = "New"
        else :
            $ nsp_germiona_rights_5_statimg = "Explored"
    elif nsp_event_rights_5 == 4 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 100 and nsp_germiona_impudence >= 30 :
            $ nsp_germiona_rights_5_statimg = "New"
        else :
            $ nsp_germiona_rights_5_statimg = "Explored"
    elif nsp_event_rights_5 == 5 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 120 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_rights_5_statimg = "New"
        else :
            $ nsp_germiona_rights_5_statimg = "Explored"
    elif nsp_event_rights_5 == 6 :
        if hermi.whoring >= 24 and nsp_germiona_mediawhoring >= 140 and nsp_germiona_impudence >= 40 :
            $ nsp_germiona_rights_5_statimg = "New"
        else :
            $ nsp_germiona_rights_5_statimg = "Explored"
    elif nsp_event_rights_5 == 7 :
        $ nsp_germiona_rights_5_statimg = "Full"
        
### Theme Rights
    $ nsp_germiona_statimg_rights = "Full"
    
    if nsp_germiona_rights_1_statimg != "Full" and nsp_germiona_rights_1_statimg != "Full_block":
        $ nsp_germiona_statimg_rights = "Explored"
    elif  nsp_germiona_rights_2_statimg != "Full" and nsp_germiona_rights_2_statimg != "Full_block":
        $ nsp_germiona_statimg_rights = "Explored"
    elif  nsp_germiona_rights_3_statimg != "Full" and nsp_germiona_rights_3_statimg != "Full_block":
        $ nsp_germiona_statimg_rights = "Explored"
    elif  nsp_germiona_rights_4_statimg != "Full" and nsp_germiona_rights_4_statimg != "Full_block":
        $ nsp_germiona_statimg_rights = "Explored"
    elif  nsp_germiona_rights_5_statimg != "Full" and nsp_germiona_rights_5_statimg != "Full_block":
        $ nsp_germiona_statimg_rights = "Explored"
        
    if nsp_germiona_rights_1_statimg == "New":
        $ nsp_germiona_statimg_rights = "New"
    elif  nsp_germiona_rights_2_statimg == "New":
        $ nsp_germiona_statimg_rights = "New"
    elif  nsp_germiona_rights_3_statimg == "New":
        $ nsp_germiona_statimg_rights = "New"
    elif  nsp_germiona_rights_4_statimg == "New":
        $ nsp_germiona_statimg_rights = "New"
    elif  nsp_germiona_rights_5_statimg == "New":
        $ nsp_germiona_statimg_rights = "New"

    return
    
    
label nsp_vague_idea:
    show screen blktone8
    ">Вы не можете точно сформулировать новую идею. Возможно повышение писательского мастерства или какие-то особые условия могли бы помочь."
    hide screen blktone8
    return
    
label nsp_hermione_goout:

hide screen bld1
$herView.hideQ()
hide screen bld1
$herView.hideQ() 
hide screen blktone 
hide screen hermione_02
hide screen ctc
with d3

if daytime:
    $ hermione_takes_classes = True
else:
    $ hermione_sleeping = True
        
    return