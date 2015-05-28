################
### Товары из спецкаталогов для газеты и хрустального шара. ###                
################

label menu_dahre_newsp:
    $ choose = RunMenu()
    python:
        for e in this.List:
            if e.GetValue("block")==_block: # Нужно ставить GetValue("block")  а не _block - у ивента такого объекта может не быть
                choose.AddItem("- Для газет: "+e._caption+" - "+("{image=check_08.png}" if e._status>-2 else "{image=check_07.png}"), 
                    "menu_dahre_newsp_2", e.Name)

    $ choose.Show("the_oddities")

    label menu_dahre_newsp_2:
        $ the_gift = event._img     # "03_hp/18_store/08.png" # Copper book of spirit.
        show screen gift
        with d3
        dahr "\"[event._caption]\". [event._description]\n"
        if event._status>-2: 
            call do_have_book
            jump the_oddities
        if nsp_newspaper_menu < 4 and event.Name <> "nsp_newsp_book_pre":
            "> Эта книга вас не интересует."
            hide screen gift
            jump expression _label #education_menu
        menu:
            "- Купить книгу за [event._price] галлеонов -":
                if gold >= event._price:
                    $ gold -= event._price
                    $ order_placed = True
                    $ event.IncValue("status",1)
#                            $ bought_book_01 = True
                    call thx_4_shoping #Massage that says "Thank you for shopping here!".
                    jump desk
                else:
                    call no_gold #Massage: m "I don't have enough gold".
                    jump expression _label
            "- Ничего -":
                hide screen gift
                jump expression _label #education_menu

label menu_dahre_upd:
    $ choose = RunMenu()
    python:
        for e in this.List:
            if e.GetValue("block")==_block: # Нужно ставить GetValue("block")  а не _block - у ивента такого объекта может не быть
                choose.AddItem("- Для газет: "+e._caption+" - "+("{image=check_08.png}" if e._status>-2 else "{image=check_07.png}"), 
                    "menu_dahre_upd_2", e.Name)

    $ choose.Show("the_oddities")

    label menu_dahre_upd_2:
        $ the_gift = event._img     # "03_hp/18_store/08.png" # Copper book of spirit.
        show screen gift
        with d3
        dahr "\"[event._caption]\". [event._description]\n"
        if event._status>-2: 
            call do_have_book
            jump the_oddities
        menu:
            "- Купить за [event._price] галлеонов -":
                if gold >= event._price:
                    $ gold -= event._price
                    $ order_placed = True
                    $ event.IncValue("status",1)
#                            $ bought_book_01 = True
                    call thx_4_shoping #Massage that says "Thank you for shopping here!".
                    jump desk
                else:
                    call no_gold #Massage: m "I don't have enough gold".
                    jump expression _label
            "- Ничего -":
                hide screen gift
                jump expression _label #education_menu
