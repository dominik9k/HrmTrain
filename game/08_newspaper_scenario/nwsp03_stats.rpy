
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

label nsp_snape_dialog_stat :
    
    $ nsp_txt_add = ""
    
    $screens.Hide("snape_main")
    $snape.State("door").Visibility("body")
    
    if nsp_newspaper_qual_last >= 770 :
        $ nsp_txt_add = "великолепное глянцевое издание"
    elif nsp_newspaper_qual_last >= 240 :
        $ nsp_txt_add = "хорошо оформленное издание"
    elif nsp_newspaper_qual_last >= 60 :
        $ nsp_txt_add = "скромное издание"
    else :
        $ nsp_txt_add = "жалко выглядящее издание"

        
    if nsp_newspaper_bonus_point_last >= 15000 :
        if one_out_of_three == 1 :
            $snape ("~28//Сегодня я видел в главном зале огромную толпу учеников, которая разглядывала наше [nsp_txt_add].")
            $snape ("~21//Профессор Мак-Гонагалл с трудом навела порядок, а разглядев газету поближе густо покраснела.")
            $snape ("~02//Анонимность - это круто !")
        elif one_out_of_three == 2 :
            $snape ("~23//Ученики украдкой бегают с уроков посмотреть на наше [nsp_txt_add].")
            $snape ("~02//Я уже не говорю о переменах.")
            $snape ("~20//На сегодняшнем сдвоенном зельеварении было восемь случаев сексуальных домогательств между учениками прямо в классе.")
        else :
            $snape ("~03//Сегодня Филч и профессор Флитвик дежурили возле стенда, на котором висит наше [nsp_txt_add].")
            $snape ("~28//Но ученики освоили новую тактику, пока один отвлекает, остальные пользуются моментом.")
            $snape ("~20//А еще, по Хогвартсу тайно распространяются уменьшенные копии гезатных материалов.")
            $snape ("~22//Я и сам раздоб... то есть конфисковал парочку.")
    
    elif nsp_newspaper_bonus_point_last >= 5000 :
        if one_out_of_three == 1 :
            $snape ("~10//Многие ученики постоянно крутятся у стенда.")
            $snape ("~02//Думаю, они уже готовы на все, лишь бы перечитать наше [nsp_txt_add].")
            $snape ("~28//Похоже, профессора понемногу тоже привыкают.")
        elif one_out_of_three == 2 :
            $snape ("~23//Ученики, и особенно ученицы, стали заметно распутнее.")
            $snape ("~24//На них явно действует наше [nsp_txt_add].")
            $snape ("~28//Хорошо, что эту газету не видят их родители.")
        else :
            $snape ("~01//Сегодня Минерва пыталась удалить наше [nsp_txt_add].")
            $snape ("~28//Но листы надежно защищены заклинанием Альбуса.")
            $snape ("~23//Мне уже трудно вспомнить, почему издание газеты могло казаться скучным.")
    
    elif nsp_newspaper_bonus_point_last >= 1000 :
        if one_out_of_three == 1 :
            $snape ("~24//Некоторое количество учеников каждый день читает наше [nsp_txt_add].")
            $snape ("~09//Похоже моя идея про секс-материалы работает.")
            $snape ("~23//И это не удивляет.")
        elif one_out_of_three == 2 :
            $snape ("~02//Ученики на уроках выглядят более возбужденными.")
            $snape ("~13//Да и на моих \"личных\" ученицах это сказывается в лучшую сторону.")
        else :
            $snape ("~03//Наше [nsp_txt_add] пока что не очень интересно для мужской аудитории, но у него большой потенциал.")

    
    else :
            $snape ("~04//У нас [nsp_txt_add], да, именно [nsp_txt_add]. Формально.")
            $snape ("~06//А когда будут выполнятся мои советы относительно дополнительных материалов, его даже могут начать читать другие люди.")

    $screens.Hide("snape_02", "bld1", d3 )
    $snape.Visibility(transition=d3)
            
    show screen snape_main
    
    jump snape_ready

label nsp_hermione_dialog_status :

    if nsp_newspaper_qual_last >= 770 :
        $ nsp_txt_add = "Сэр, газета прекрасно оформлена и может служить образцом для других !"
    elif nsp_newspaper_qual_last >= 240 :
        $ nsp_txt_add = "Сэр, газета хорошо оформлена и смотрится просто здорово."
    elif nsp_newspaper_qual_last >= 60 :
        $ nsp_txt_add = "Сэр, газета оформлена более-менее нормально, но могла бы быть и лучше."
    else :
        $ nsp_txt_add = "Сэр, газета выглядит просто ужасно, если вы хотите мое мнение. Я утешаю себя тем, что это просто разминка."

        
    if nsp_newspaper_bonus_point_last >= 15000 :
        if one_out_of_three == 1 :
            $herView.hideshowQQ( "body_33.png", pos )
            her "Сэр, по всей школе обсуждают нашу газету. Может это и хорошо для соревнования, но нормально ли ?"
            $herView.hideshowQQ( "body_34.png", pos )
            her "Я хочу сказать, неужели и во всех остальных школах происходит то же самое ? Трудно поверить."
        elif one_out_of_three == 2 :
            $herView.hideshowQQ( "body_50.png", pos )
            her "Если хотите знать мое мнение, логичнее было открыть борд... в смысле класс сексуального образования, чем выставлять меня напоказ перед всей школой."
            $herView.hideshowQQ( "body_57.png", pos )
            her "А как же моя гордость ?"
            her "Так, крепись, Гермиона, все ради победы школы."
        else :
            $herView.hideshowQQ( "body_02.png", pos )
            her "Сэр, в школе появился фан-клуб {size=+4}газеты{/size}!"
            $herView.hideshowQQ( "body_33.png", pos )
            her "Многие считают авторов героями за то, что вы их не можете найти."
            her "Если бы они только знали... Нет, хорошо, что они не знают, а то я бы сошла с ума."
    
    elif nsp_newspaper_bonus_point_last >= 5000 :
        if one_out_of_three == 1 :
            $herView.hideshowQQ( "body_34.png", pos )
            her "Профессор, скажите, неужели газета с самого начала задумывалась именно в таком виде ?"
            $herView.hideshowQQ( "body_50.png", pos )
            her "Теперь я целый день чувствую смущение после каждой публикации."
        elif one_out_of_three == 2 :
            $herView.hideshowQQ( "body_01.png", pos )
            her "[nsp_txt_add]"
            $herView.hideshowQQ( "body_04.png", pos )
            her "Многие ученики пытаются вычислить, кто работает в редакции. Надеюсь, этого не произойдет."
            $herView.hideshowQQ( "body_08.png", pos )
            her "Иначе моя жизнь уже никогда не станет прежней."
        else :
            $herView.hideshowQQ( "body_01.png", pos )
            her "[nsp_txt_add]"
            $herView.hideshowQQ( "body_12.png", pos )
            her "Я не понимаю, кем нужно быть, чтобы постоянно изучать наши материалы. А ведь многие это делают."
            $herView.hideshowQQ( "body_34.png", pos )
            her "А самое ужасное, что после публикации и я не могу удержаться. Уф."
    
    elif nsp_newspaper_bonus_point_last >= 1000 :
        if one_out_of_three == 1 :
            $herView.hideshowQQ( "body_01.png", pos )
            her "[nsp_txt_add]"
            $herView.hideshowQQ( "body_12.png", pos )
            her "И еще, меня смущают особые материалы, которые вы разместили в центре."
            $herView.hideshowQQ( "body_24.png", pos )
            her "Я не думала, что это будет так... так... так откровенно !"
        elif one_out_of_three == 2 :
            $herView.hideshowQQ( "body_01.png", pos )
            her "[nsp_txt_add]"
            $herView.hideshowQQ( "body_28.png", pos )
            her "Но я хотела бы спросить, вы уверены, что публикация таких материалов допустимо ?"
            m "Неужели ты стыдишься своей же журналистской деятельности ?"
            $herView.hideshowQQ( "body_33.png", pos )
            her "Вовсе нет !"
            her "Я просто... просто переживаю за результат межшкольного соревнования !"
            m "Какого еще межшко... А, ну да ! Ты об {size=+3}этом{/size} соревновании."
        else :
            $herView.hideshowQQ( "body_01.png", pos )
            her "[nsp_txt_add]"
            $herView.hideshowQQ( "body_50.png", pos )
            her "Но, среди учеников теперь ходят разные сплетни по поводу редакции. Наверное, я не буду их пересказывать."
            $herView.hideshowQQ( "body_13.png", pos )
            her "Хорошо, никто не знает, что я работаю на вас."

    
    else :
            $herView.hideshowQQ( "body_01.png", pos )
            her "[nsp_txt_add]\nА еще не хватает чего-нибудь интересного, что могло бы издалека заинтересовать читателя."

    $herView.hideshowQQ( "body_01.png", pos )
    jump hermione_main_menu