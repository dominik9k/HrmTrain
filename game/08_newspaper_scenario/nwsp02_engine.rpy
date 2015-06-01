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
    

#    call nsp_events_init
    
    menu:
    
        "- О правах и дискриминации {image=08_newspaper_scenario/flags/[nsp_germiona_statimg_rights].png} -" if nsp_newspaper_menu == 6:
    
            if nsp_germiona_menu_rights == 1 :
                $ nsp_germiona_menu_rights = 2
        
#            if nsp_germiona_menu_rights == 1 :
#                menu:

            jump hermione_goout
            
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

        "{color=#858585}- ?????? -{/color}" if nsp_newspaper_menu == 6 and nsp_germiona_menu_maniak == -1:
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

        "{color=#858585}- ????????? ??? -{/color}" if nsp_newspaper_menu == 6 and nsp_germiona_menu_forest == -1:
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

#label nsp_events_init:
    

            