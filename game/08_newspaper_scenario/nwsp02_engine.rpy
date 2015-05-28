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
        dr "{size=-4}Одну минутку..."
        $hero("{size=+1}Столько стараний ради [nsp_newspaper_cur_money] галлеонов ? Сейчас здесь будет убийство !{/size}")
        dr "{size=-4}Да погоди, не кипятись. Дело в том, что..."
        $hero("{size=-1}Да пошел ты ! Больше никаких модов, только классика !{/size}")
        dr "{size=-4}О не-е-е-е-е-е-ет... Джинни, я обещаю, что ты не зря учился газетному делу ! Спроси Снейпа, и он подскажет, как заработать больше !"
        $hero("{size=-4}Хммм. Ладно, только ради тебя, дам моду еще один шанс.{/size}")
        $ nsp_newspaper_menu = 3

    $event.Finalize()
    call screen main_menu_01
