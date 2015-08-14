label menu_dahr_book:
    $ choose = RunMenu()
    python:
        for e in this.List:
            if e.GetValue("block")==_block: # Нужно ставить GetValue("block")  а не _block - у ивента такого объекта может не быть
                choose.AddItem("- Книга: "+e._caption+" - "+("{image=check_08.png}" if e._status>-2 else "{image=check_07.png}"), 
                    "menu_dahre_book_2", e.Name)

    $ choose.Show("the_oddities")

    label menu_dahre_book_2:
        $ the_gift = wtevent._img     # "03_hp/18_store/08.png" # Copper book of spirit.
        show screen gift
        with d3
        dahr "\"[wtevent._caption]\". [wtevent._description]\n"
        if wtevent._status>-2: 
            call do_have_book
            jump the_oddities
        menu:
            "- Купить книгу за [wtevent._price] галлеонов -":
                if gold >= wtevent._price:
                    hide screen points
                    $ gold -= wtevent._price
                    show screen points
                    $ order_placed = True
                    $ wtevent.IncValue("status",1)
#                            $ bought_book_01 = True
                    call thx_4_shoping #Massage that says "Thank you for shopping here!".
                    jump desk
                else:
                    call no_gold #Massage: m "I don't have enough gold".
                    jump expression _label
            "- Ничего -":
                hide screen gift
                jump expression _label #education_menu


label menu_dahr_gifts_and_gears:
    $ choose = RunMenu()
    python:
        for o in itsDAHR():
            if not (o.Name in {"scroll","dress","panties","dress","skirt","standart2","standart3","standart4","standart5"} or o.GetValue("block") in {"gears_hair", "gears_panties"}): 
                _temp={"candy": fn0, "chocolate": fn0, "owl": fn0, "beer": fn3, "mag1": fn0, "mag2": fn0, "mag3": fn0, "mag4": fn3,
                     "condoms": fn3, "perfume": fn0,"vibrator": fn3, "lubricant": fn0,"ballgag": fn0, "plug": fn3, "strapon": fn3,
                     "ball_dress": lambda e: this.Has("sorry_about_hesterics"), "badge": fn0, "nets": fn0, 
                            "shortskirt": lambda e: hermi.whoring >= 3 and (hero.Items.Count("shortskirt")+hermi.Items.Count("shortskirt")+itsOWL.Count("shortskirt")==0),
                            "xshortskirt": lambda e: hermi.whoring >= 3 and (hero.Items.Count("xshortskirt")+hermi.Items.Count("xshortskirt")+itsOWL.Count("xshortskirt")==0),
                            "xxshortskirt": lambda e: hermi.whoring >= 3 and (hero.Items.Count("xxshortskirt")+hermi.Items.Count("xxshortskirt")+itsOWL.Count("xxshortskirt")==0),
                            "xsmallskirt": lambda e: hermi.whoring >= 3 and (hero.Items.Count("xsmallskirt")+hermi.Items.Count("xsmallskirt")+itsOWL.Count("xsmallskirt")==0),
                            "xxsmallskirt": lambda e: hermi.whoring >= 3 and (hero.Items.Count("xxsmallskirt")+hermi.Items.Count("xxsmallskirt")+itsOWL.Count("xxsmallskirt")==0),
                            "xxxsmallskirt": lambda e: hermi.whoring >= 3 and (hero.Items.Count("xxxsmallskirt")+hermi.Items.Count("xxxsmallskirt")+itsOWL.Count("xxxsmallskirt")==0),
                            "skimpyshirt": lambda e: hermi.whoring >= 3 and (hero.Items.Count("skimpyshirt")+hermi.Items.Count("skimpyshirt")+itsOWL.Count("skimpyshirt")==0),
                            "tights": lambda e: hermi.whoring >= 3 and (hero.Items.Count("tights")+hermi.Items.Count("tights")+itsOWL.Count("tights")==0),
                            "shirt_business": lambda e: hermi.whoring >= 3 and (hero.Items.Count("shirt_business")+hermi.Items.Count("shirt_business")+itsOWL.Count("shirt_business")==0),
                            "skirt_business": lambda e: hermi.whoring >= 3 and (hero.Items.Count("skirt_business")+hermi.Items.Count("skirt_business")+itsOWL.Count("skirt_business")==0),
                            "shirt_cheerleader": lambda e: hermi.whoring >= 3 and (hero.Items.Count("shirt_cheerleader")+hermi.Items.Count("shirt_cheerleader")+itsOWL.Count("shirt_cheerleader")==0),
                            "skirt_cheerleader": lambda e: hermi.whoring >= 3 and (hero.Items.Count("skirt_cheerleader")+hermi.Items.Count("skirt_cheerleader")+itsOWL.Count("skirt_cheerleader")==0),
                            "hair_set": lambda e: hermi.whoring >= 3 and (hero.Items.Count("hair_set")+hermi.Items.Count("hair_set")+itsOWL.Count("hair_set")==0)}[o.Name](o)

#            elif _block=="gears" and o._block=="gears": 
                if o._block==_block:
                    choose.AddItem("- "+o._caption+" - ("+str(o._price)+" гал.) -" if _temp and itsDAHR.Count(o.Name)>0 else "{color=#858585}- Товар временно отсутствует -{/color}", 
                        "menu_dahr_gift_order" if _temp else "out", o.Name)

    $ choose.Show("the_oddities") 



label menu_dahr_gift_order:
    if _block=="scroll":
        $item=itsDAHR("scroll")
    else:
        $item=itsDAHR(choose.choice)
    label menu_dahr_scroll_order:
    $ the_gift = item._img # CANDY.
    show screen gift
    with d3
    $itemCount=0
    if item.Name=="xxxsmallskirt":
        menu:
            "- Купить супер-короткую мини-юбку (---) -":
                if vouchers >= 1: #Shows the amount of DAHR's vouchers in your possession.
                    $ vouchers -= 1 #Shows the amount of DAHR's vouchers in your possession.
                    $ order_placed = True
                    $itsOWL.AddItem(item.Name)
                    $itsDAHR.AddItem(item.Name,-1)
                    call thx_4_shoping #Massage that says "Thank you for shopping here!".
                    jump desk
                else:
                    dahr "Эту вещь можно купить только за \"Ваучер Дахра\"."
                    dahr "Что-то не так..."
                    dahr "Чертовы переводчики..."
                    dahr "Я..."
                    translators "Так-то лучше. Этот момент показался всем достаточно сложным. Я о юбке. Дальше будет подсказка, как ее получить."
                    menu:
                        "- Глянуть подсказку -":
                            translators "{size=14}Подсказка от переводчика:\nНайти его можно {b}правильно{/b} прочитав книгу {b}[book07]{/b}{/size}."
                            translators "{size=14}Более подробно {a=http://skazgames.com/forum/viewtopic.php?f=2&t=30#p4}здесь{/a}{/size}."
                        
                        "- Не нужно -":
                            translators "Как угодно."
                    hide screen gift
                    with d3
                    jump menu_dahr_gifts_and_gears
            "- Ничего -":
                hide screen gift
                with d3
                jump menu_dahr_gifts_and_gears

    if itsDAHR.Count(item.Name)>0:
        if _block in {"gears", "gears_shirt", "gears_skirt", "gears_stockings", "gears_other", "gears_dress", "gears_panties"} :
            menu:
                dahr "[item._description]"
                "- Купить ([item._price] галеонов) -":
                    $itemCount=1
                "- Ничего -":
                    hide screen gift
                    jump menu_dahr_gifts_and_gears

        else:
            $_price2=item._price*2
            $_price3=item._price*3
            $i_count=itsDAHR.Count(item.Name)
            $_price_all=item._price*i_count
            
            if itsDAHR.Count(item.Name)>0:
                menu:
                    dahr "[item._description]"
                    "- Купить 1 ([item._price] галеонов) -":
                        $itemCount=1
                    "- Купить 2 ([_price2] галеонов) -" if itsDAHR.Count(item.Name)>1:
                        $itemCount=2
                    "- Купить 3 ([_price3] галеонов) -" if itsDAHR.Count(item.Name)>2:
                        $itemCount=3
                    "- Купить оставшиеся - [i_count] ([_price_all] галеонов) -" if i_count>3 and _block == "scroll" :
                        $itemCount=i_count
                    "- Ничего -":
                        hide screen gift
                        jump the_oddities


        if gold >= item._price*itemCount:
            hide screen points
            $ gold -=item._price*itemCount
            show screen points
            $ order_placed = True
            $itsOWL.AddItem(item.Name,itemCount)
            if item.Name in {"scroll", "ball_dress"}:
                $itsDAHR.AddItem(item.Name,-itemCount)
    #        $ bought_candy = True #Affects 15_mail.rpy
            call thx_4_shoping #Massage that says "Thank you for shopping here!".
            jump desk
        else:
            call no_gold #Massage: m "I don't have enough gold".
            jump the_oddities

    else:
        ">Извините, товар закончился"
        hide screen gift




label the_oddities:
    $choose=None
    menu:
        dahr "Добро пожаловать в \"каталог Приблуд Дахра\". Ваши предпочтения не покажутся нам странными!"
### DR'S NEWSPAPER ooo ###
        "- Для редакций: Образовательные книги -" if nsp_pre_dahre >= 1:
            label newspaper_menu:
                $_label="newspaper_menu"
                $_block="books_newsp"
                jump menu_dahre_newsp

        "- Для редакций: Инструменты -" if nsp_newspaper_menu >= 5:
            label newspaper_menu2:
                $_label="newspaper_menu2"
                $_block="books_newsp2"
                jump menu_dahre_upd
                
        "- Для Вашего Хрустального шара -" if nsp_genie_sphere :
            jump nsp_sphere_dahre
            
###
        "- Образовательные книги -":
            label education_menu:
                $_label="education_menu"
                $_block="books_edu"
                jump menu_dahr_book
        "- Фантастика -":
            label fiction_menu:
                $_label="fiction_menu"
                $_block="books_fict"
                jump menu_dahr_book



        "- Подарки -":
            label gifts_menu:
                $_block="gifts"
                jump menu_dahr_gifts_and_gears
                
                            
                            
        #"- Одежда -":
        #    label app:
        #        $_block="gears"
        #        jump menu_dahr_gifts_and_gears
                
                
        "- Одежда -":
            label app:
                jump wrd_dahr_gears



        "- Священные свитки -":
            label sscrolls:
                $_block="scroll"
                jump menu_dahr_gift_order

        "- Ничего -":
            jump desk
        
        
### ALREADY HAVE THIS BOOK
label do_have_book:
    show screen bld1
    m "Я уже это покупал и мне больше не нужно."
    hide screen bld1
    hide screen gift
    with d3
    return
### THANK YOU FOR shopping here.
label thx_4_shoping:
# Пока не было объекта Item книги были сделаны через объект Event. Вероятно, надо переделать, через Item, но из-за спешки при подготовке к релизу пока пусть будет костыль
    if "books_" in _block:
        $_caption=wtevent._caption
        $_price=wtevent._price
        $itemCount=1
    else:
        $item=itsOWL()[0]
        $itemCount=itsOWL.Count(item.Name)
        $_caption=item._caption
        $_price=item._price
    $ days_in_delivery2 = one_of_five  #Generating one number out of three for various porpoises.
    if days_in_delivery2==1:
        $days_in_delivery2+=1 # Назавтра только экспресс
#        $days_in_delivery2+=itemCount-1  # Удлинняется, если несколько предметов

    if gold >= _price*itemCount//2:
        menu:
            dahr "Вы заказали [itemCount] шт. предметов \"[_caption]\". Вы оплатите экспресс-доставку?"
            "Экспресс-доставка (+50%% за срочность)":
                $days_in_delivery2=1
                hide screen points
                $gold -= _price*itemCount//2
                show screen points
                dahr "Спасибо за покупку в \"Приблудах Дахра\". Ваш заказ будет доставлен завтра."
            "Обычная доставка":
                dahr "Спасибо за покупку в \"Приблудах Дахра\". Доставка вашего заказа займет около [days_in_delivery2] дней."

        hide screen gift
        with d3
        return
    
### THANK YOU FOR shopping here. IMMEDIATE DELIVERY.
label thx_4_shoping2:
    dahr "Спасибо за покупку в \"Приблудах Дахра\"."
    hide screen gift
    with d3
    return
### NOT ENOUGH GOLD ###
label no_gold:
    m "У меня нет столько золота... Это удручает..."
    hide screen gift
    with d3
    return
    
### Этот товар закончился на складе ###

label out:
    dahr "Этот товар закончился на складе"
    jump the_oddities
#    return

label wrd_dahr_gears:

    menu:
        "- Юбки -":
            $_block="gears_skirt"
            jump menu_dahr_gifts_and_gears
        
        "- Верх -":
            $_block="gears_shirt"
            jump menu_dahr_gifts_and_gears
        
        "- Чулки/Колготки -":
            $_block="gears_stockings"
            jump menu_dahr_gifts_and_gears
        
        "- Платья-":
            $_block="gears_dress"
            jump menu_dahr_gifts_and_gears
        
        "- Прочее -":
            $_block="gears_other"
            jump menu_dahr_gifts_and_gears
            
        "- Прокат на день -":
            jump wrd_dahr_rent_menu
    
        "- Ничего -":
             jump the_oddities

label wrd_dahr_rent_menu :

    $ add = ""

    menu:
        "- Форма веселой школьницы (100 галлеонов) -" if wrd_rent_happy_schoolgirl == 0 :
            if hermi.whoring < 3 :
                $add = "Интуиция подсказывает вам, что Гермиона откажется это надевать."
            if gold >= 100 :
                menu :
                    ">Вы уверены, что хотите взять напрокат на один день форму веселой школьницы за 100 галлеонов ? [add]"
                
                    "Да" :
                        hide screen points
                        $ gold -= 100
                        show screen points
                        ">В шкафу раздался шорох и материализовался комплект веселой школьницы. Вы не уверены, но похоже в кабинете стало меньше пыли."
                        $ wrd_rent_happy_schoolgirl = 1
                        jump wrd_dahr_gears
                
                    "Нет" :
                        jump wrd_dahr_rent_menu
                    
            else :
                ">К сожалению, у вас недостаточно денег."
                jump wrd_dahr_rent_menu
        
        "{color=#858585}- Форма веселой школьницы. -{/color}" if wrd_rent_happy_schoolgirl == 1 :
            ">Данный комплект уже взят напрокат на сегодня."
            jump wrd_dahr_rent_menu
        
        "- Форма игривой школьницы (250 галлеонов) -" if wrd_rent_playful_schoolgirl == 0:
            if hermi.whoring < 12 :
                $add = "Интуиция подсказывает вам, что Гермиона откажется это надевать."
            if gold >= 250 :
                menu :
                    "Вы уверены, что хотите взять напрокат на один день форму игривой школьницы за 250 галлеонов ? [add]"
                
                    "Да" :
                        hide screen points
                        $ gold -= 250
                        show screen points
                        ">В шкафу раздался шорох и материализовался комплект игривой школьницы. Вы не уверены, но похоже в кабинете стало меньше пыли."
                        $ wrd_rent_playful_schoolgirl = 1
                        jump wrd_dahr_gears
                
                    "Нет" :
                        jump wrd_dahr_rent_menu
                    
            else :
                ">К сожалению, у вас недостаточно денег."
                jump wrd_dahr_rent_menu
        
        "{color=#858585}- Форма игривой школьницы. -{/color}" if wrd_rent_playful_schoolgirl == 1:
            ">Данный комплект уже взят напрокат на сегодня."
            jump wrd_dahr_rent_menu
        
        "- Форма болельщицы Гриффиндора (125 галлеонов) -" if wrd_rent_cheerleader == 0 :
            if hermi.whoring < 6 :
                $add = "Интуиция подсказывает вам, что Гермиона откажется это надевать."
            if gold >= 125 :
                menu :
                    "Вы уверены, что хотите взять напрокат на один день форму болельщицы Гриффиндора за 125 галлеонов ? [add]"
                
                    "Да" :
                        hide screen points
                        $ gold -= 125
                        show screen points
                        ">В шкафу раздался шорох и материализовался комплект болельщицы Гриффиндора. Вы не уверены, но похоже в кабинете стало меньше пыли."
                        $ wrd_rent_cheerleader = 1
                        jump wrd_dahr_gears
                
                    "Нет" :
                        jump wrd_dahr_rent_menu
                    
            else :
                ">К сожалению, у вас недостаточно денег."
                jump wrd_dahr_rent_menu
        
        "{color=#858585}- Форма болельщицы Гриффиндора -{/color}" if wrd_rent_cheerleader == 1 :
            ">Данный комплект уже взят напрокат на сегодня."
            jump wrd_dahr_rent_menu
        
        "- Одежда бизнес-леди (200 галлеонов) -" if wrd_rent_business == 0 :
            if hermi.whoring < 9 :
                $add = "Интуиция подсказывает вам, что Гермиона откажется это надевать."
            if gold >= 200 :
                menu :
                    "Вы уверены, что хотите взять напрокат на один день одежду бизнес-леди за 200 галлеонов ? [add]"
                
                    "Да" :
                        hide screen points
                        $ gold -= 200
                        show screen points
                        ">В шкафу раздался шорох и материализовался комплект бизнес-леди. Вы не уверены, но похоже в кабинете стало меньше пыли."
                        $ wrd_rent_business = 1
                        jump wrd_dahr_gears
                
                    "Нет" :
                        jump wrd_dahr_rent_menu
                    
            else :
                ">К сожалению, у вас недостаточно денег."
                jump wrd_dahr_rent_menu
        
        "{color=#858585}- Форма бизнес-леди -{/color}" if wrd_rent_business == 1 :
            ">Данный комплект уже взят напрокат на сегодня."
            jump wrd_dahr_rent_menu
        
        "- Ничего -" :
            jump wrd_dahr_gears
