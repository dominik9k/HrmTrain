
label newsp_stats_00:

    $nsp_newspaper_qual_text=""
    $nsp_genie_typographic_text=""
    $nsp_genie_writer_text=""
    $nsp_genie_photocamera_text=""
    
    $ nsp_newspaper_qual = (10 * (1 + nsp_genie_writer) * (1 + nsp_genie_typographic)) + (5 * nsp_genie_photocamera)

    if nsp_newspaper_qual >= 0:
        $ nsp_newspaper_qual_text = "никакое"        
    if nsp_newspaper_qual >= 20:
        $ nsp_newspaper_qual_text = "плохое"
    if nsp_newspaper_qual >= 60:
        $ nsp_newspaper_qual_text = "ниже среднего"
    if nsp_newspaper_qual >= 150:
        $ nsp_newspaper_qual_text = "среднее" 
    if nsp_newspaper_qual >= 240:
        $ nsp_newspaper_qual_text = "выше среднего"        
    if nsp_newspaper_qual >= 400:
        $ nsp_newspaper_qual_text = "хорошее"        
    if nsp_newspaper_qual >= 540:
        $ nsp_newspaper_qual_text = "отличное"        
    if nsp_newspaper_qual >= 770:
        $ nsp_newspaper_qual_text = "шедевр"
        
    if nsp_genie_typographic == 0:
        $ nsp_genie_typographic_text = "рукописный листок"
    if nsp_genie_typographic == 1:
        $ nsp_genie_typographic_text = "плохо напечатано"
    if nsp_genie_typographic == 2:
        $ nsp_genie_typographic_text = "напечатано"
    if nsp_genie_typographic == 3:
        $ nsp_genie_typographic_text = "хорошо напечатано"
    if nsp_genie_typographic == 4:
        $ nsp_genie_typographic_text = "глянец"
    if nsp_genie_typographic == 5:
        $ nsp_genie_typographic_text = "яркий глянец"
    if nsp_genie_typographic == 6:
        $ nsp_genie_typographic_text = "сияющий глянец"
        
    if nsp_genie_writer == 0:
        $ nsp_genie_writer_text = "никакое"
    if nsp_genie_writer == 1:
        $ nsp_genie_writer_text = "начинающий"
    if nsp_genie_writer == 2:
        $ nsp_genie_writer_text = "слабый любитель"
    if nsp_genie_writer == 3:
        $ nsp_genie_writer_text = "любитель"
    if nsp_genie_writer == 4:
        $ nsp_genie_writer_text = "хороший любитель"
    if nsp_genie_writer == 5:
        $ nsp_genie_writer_text = "продвинутый любитель"
    if nsp_genie_writer == 6:
        $ nsp_genie_writer_text = "начинающий профессионал"
    if nsp_genie_writer == 7:
        $ nsp_genie_writer_text = "слабый профессионал"
    if nsp_genie_writer == 8:
        $ nsp_genie_writer_text = "профессионал"
    if nsp_genie_writer == 9:
        $ nsp_genie_writer_text = "сильный профессионал"
    if nsp_genie_writer == 10:
        $ nsp_genie_writer_text = "шедевр пера"
        
    if nsp_genie_photocamera == 0:
        $ nsp_genie_photocamera_text = "нет"
    if nsp_genie_photocamera == 1:
        $ nsp_genie_photocamera_text = "ч/б орнаменты"
    if nsp_genie_photocamera == 2:
        $ nsp_genie_photocamera_text = "цветные орнаменты"
    if nsp_genie_photocamera == 3:
        $ nsp_genie_photocamera_text = "псевдо-3д орнаменты"
    if nsp_genie_photocamera == 4:
        $ nsp_genie_photocamera_text = "движущиеся орнаменты"


    $screens.ShowD3("newsp_stats_00", 
    par1="{size=-3}ИНФОРМАЦИЯ о ГАЗЕТЕ{/size}\n\n"
    "{size=-4} Итоговое качество газеты :\n[nsp_newspaper_qual] ([nsp_newspaper_qual_text]) {/size}\n"
    "{size=-4} Качество печати газеты:\n[nsp_genie_typographic] ([nsp_genie_typographic_text]){/size}\n"
    "{size=-4} Качество статей газеты:\n[nsp_genie_writer] ([nsp_genie_writer_text]){/size}\n"
    "{size=-4} Качество украшений газеты:\n[nsp_genie_photocamera] ([nsp_genie_photocamera_text]){/size}\n"
    "{size=-4} Бонусный контент:\n[nsp_newspaper_bonus_text]{/size}\n"
    "{size=-4} Качество бонусного контента:\n[nsp_newspaper_bonus_point]{/size}\n"
    "{size=-4} Прошлая награда:\n[nsp_newspaper_last_money] {/size}\n",
        )
# Если этого не делать, то при включенной ускоренной прокрутке окно появляется и тут же исчезает. 
# Если ставить, то при ускоренной прокрутке чтобы окно исчезло нужно щелкать дважды. 
# Пока непонятно почему так, но это намного предпочтительнее мелькания
    $config.allow_skipping = False 
    pause
    $config.allow_skipping = True # 
    $screens.HideD3("newsp_stats_00")


    call screen main_menu_01



screen newsp_stats_00(par1):
    zorder 4

    add "03_hp/11_misc/lrm_stats.png" at Position(xpos=200, ypos=30)

    hbox:
        spacing 40 xpos 260 ypos 100 xmaximum 350  #       
        text par1 #lrm_stats_text_01



