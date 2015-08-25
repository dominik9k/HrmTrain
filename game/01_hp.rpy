label hp:
    stop music fadeout 1
#    $ select = renpy.imagemap("screens/s2pot04.png", "screens/s2pot04b.png", [                                            
#                                            (492, 400, 637, 600, "no"),
#                                            (647, 400, 799, 600, "yes"),
#                                                ])     
#    if select == "no":
#        jump fromcsoon
#    if select == "yes":
#        pass
    
    show screen blkfade
    
    show image "03_hp/01_bg/00.png"
    pause.1
    scene blkfade
    show image "03_hp/01_bg/00.png"
    hide blkfade with Dissolve(.3)
    $ renpy.play('sounds/magic4.ogg')
    scene white
    pause.02
    hide screen blkfade
    show magic5
    pause.05
    scene white
    pause.05
    pause.05
    scene white
    pause.05
    show image "03_hp/01_bg/00.png"
    show whitefade at basicfade, center
    #show magic at basicfade, center
    #show magic2 at basicfade2, center
    show magic3 at basicfade3, center 
    #show magic4 at basicfade4, center # OVAL
    hide magic
    hide magic2
    hide magic3
    hide magic4
    #hide whitefade
    show heal
    stop music fadeout 1
    pause 1
    hide whitefade
    with d3
    pause 1



  

  
###THE GAME STARTS###

$ day = 0 

#===TG MODS START===

# These set the game to start on September 14. The game usually forwards past the first day when starting a new game,
# so cal_day needs to be set a day prior to when you want things to begin.
$ cal_new_year = False
$ cal_month = 9
$ cal_day = 13

# Circled days. This structure holds all the dates that show up circled.
#
# So, if you want to add a date, you can just put the date in here directly, or you can add them dynamically later.
# It doesn't make much sense to add them now, so I recommend adding them as events take place within the scene.
#
# jan-dec, going down. Actually, it's jan-aug,1996, and sep-dec,1995.
#
# (eg: 4,24,29 in the March list would make those days circled.)
$ circled_days = [[0],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []]

# Starred days. This structure holds all the dates that show up starred.
#
# So, if you want to add a date, you can just put the date in here directly, or you can add them dynamically later.
# It doesn't make much sense to add them now, so I recommend adding them as events take place within the scene.
#
# jan-dec, going down. Actually, it's jan-aug,1996, and sep-dec,1995.
#
# (eg: 4,24,29 in the March list would make those days starred.)
$ starred_days = [[0],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []]

# Calendar notes. These relate to the hand-written notes that can be posted on the calendar. You need to photoshop
# them yourself if you want more. Check the archive for fonts, etc.
#
# ( day,
#   filename of the png that has the message (without .png extension) )
#
# NOTE: you can have several notes on the same day. They will just overlap.
#
# So, if you want to add a note, you can just put the entry here directly, or you can add them dynamically later.
# It doesn't make much sense to add them now, so I recommend adding them as events take place within the scene.
#
# Each element is a tuple, so: (date, "filename"), (date, "filename"), etc.
#
# eg: (13, "cal_note_hermione_tutoring"), (27, "cal_note_hogsmeade_weekends").
#
# If you do make new notes, put them in with the others: 03_hp/11_misc/
$ cal_notes = [[(0,"")],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []]

# Dictionary of unrelated items, grouped by key and giving a list of dates.
#
# 'key' : ( month, day, "desc" ), ( month, day, "desc" ), etc
#
# This is an open dictionary. So, if you want to add an important date to it, go ahead. Just make sure the key is
# unique if the stuff you're entering is separate from what's already present. If in doubt, put some kind of unique
# prefix before any meaningful name. Remember, other mods might make use of this too.
#
# These additional dates can either be entered directly here with all the or later, using coding to add to the
# dictionary. Makes no real difference.
#
# four_seasons = start dates of: (autumn) -> (winter) -> (spring) -> (summer)
# term_dates = the 3 school terms: (start_term1,'name'), (end_term1), (start_term2, 'name'), etc.
# holiday_dates = same as above, but different.
# OWL_dates = fifth-years take their Ordinary Wizarding Levels. 2 weeks.
# hogsmeade_weekends = dates are every 3 weeks, alternating between Sat & Sun.
# ball_dates = possible seasonal ball dates. Dunno about this yet.
$ important_dates = {
    'four_seasons':[(9,22,"Autumn"),(12,21,"Winter"),(3,20,"Spring"),(6,21,"Summer")],
    'term_dates':[(9,1,"Autumn term"),(12,19),(1,15,"Winter term"),(4,2),(4,15,"Spring term"),(6,26)],
    'holiday_dates':[(12,20,"Christmas holidays"),(1,14),(4,3,"Easter holidays"),(4,14),(6,27,"Summer holidays"),(8,31)],
    'OWL_dates':[(6,10),(6,21)],
    'hogsmeade_weekends':[(9,23),(10,15),(11,4),(11,26),(12,16),(2,4),(2,24),(3,17),(5,4),(5,26),(6,15)],
    'dumblegenies_arrival':[(9,14)],
    'hermiones_periods':[(9,18),(10,16),(11,13),(12,11),(1,8),(2,5),(3,4),(4,1),(4,29),(5,27),(6,24),(7,22),(8,19)],
    'ball_dates':[(9,30,"Autumn Ball"),(12,16,"Yule Ball"),(3,30,"Spring Fling"),(6,22,"Prom")] }

# Dictionary of flags for (date) knowledge for a bunch of things.
# Pretty crude, but this might be built on as this mod is further developed.
$ known_dates = {
    'OWL_dates':False,
    'hogsmeade_weekends':False,
    'hermiones_periods':False,
    'ball_dates':False }

### FLOO POWDER TRAVEL STUFF ###

$ travel_fire = False

# temp variables for floo powder travel mod
$ floo_travel_known = True
$ hogsmeade_known = True
$ inv_floo_powder = 1
$ Hermione_here = False

#===TG MODS STOP===

### PAPERWORK (MONEY-MAKING) RELATED FLAGS ###
$ day_of_week = 0 #Counts days of the week. Everyday +1. When day_of_week = 7 resets to zero.
$ report_chapters = 0 #Shows how many chapters of a current report has been completed so far. Resets to zero when report is finished.
$ finished_report = 0 #Shows amount of completed reports.
$ total_report = 0

$ got_mail = False #Turns true is you have WORK mail waiting. Owl will be displayed.
$ got_package = False #Turns TRUE when package from the "Muggle Oddities" catalog has arrived.
$ got_paycheck = False #When TRUE the paycheck is in the mail. Can't do paper work.
$ mail_from_her = False #Turns TRUE when there is a mail from Hermione. Basically the same as $ got_mail = True.
$ letter_text = []
$ letters = 0 #Shows how many letters are waiting to be read. +1 every new letter arrives. -1 Every time you read one letter.

### DR'S newspaper ooo ###

$ nsp_genie_typographic = 0 # Джин: Тип типографского набора, в начале - 0. Отсюда же Качество печати для Газеты
$ nsp_genie_typographic_exp = 0 # Растет при каждой публикации на 1, для покупки набора след уровня нужно не менее 2 публикаций с прошлым. При этом счетчик сбрасывается.
$ nsp_genie_writer = 0 # Джин: Навык писателя статей, в начале - 0. Отсюда же Мастерство написания для Газеты.
$ nsp_genie_photocamera = 0 # Джин: Тип используемого фотоаппарата, в начале - 0. Отсюда же украшения газеты.
$ nsp_genie_photocamera_exp = 3 # Растет при каждом ивенте на 1, для покупки фотоаппарата (кроме 1-го) след уровня нужно не менее 3 ивентов с прошлым. При этом счетчик сбрасывается. Для покупки первого аппарата опыт уже как бы есть.
$ nsp_genie_sphere = False # Джин: Наличие хрустального шара.
$ nsp_genie_sphere_level = 0 # Джин: Навык владения хрустальным шаром.
$ nsp_genie_sphere_level_exp = 0 # Джин: Опыт владения хрустальным шаром.
$ nsp_genie_sphere_ruby_level = 0 # Джин: Уровень рубина для шара
$ nsp_genie_sphere_diamond_level = 0 # Джин: Уровень алмаза для шара
$ nsp_genie_sphere_sapphire_level = 0 # Джин: Уровень сапфира для шара
$ nsp_genie_sphere_video = False # Джин: Наличие навыка переноса видео в газету

$ nsp_genie_sphere_diamond_req = 0

$ nsp_genie_sphere_ruby_level_eff = 0
$ nsp_genie_sphere_diamond_level_eff = 0
$ nsp_genie_sphere_sapphire_level_eff = 0

$ nsp_germiona_mediawhoring = 0 # Гермиона: Медиа-развращенность
$ nsp_germiona_impudence = 0 # Гермиона: Наглость
$ nsp_germiona_artistry = 0 # Гермиона: Артистичность

$ nsp_newspaper_bonus_text = "нет" # Газета: Текст, описание бонусного контента
$ nsp_newspaper_bonus_point = 0 # Газета: Баллы за бонусный контент
$ nsp_newspaper_bonus_base = 0 # Газета: Базовый бонус эвента
$ nsp_newspaper_bonus_text_base = 0 # Газета: Базовый текст эвента
$ nsp_newspaper_bonus_point_last = 0
$ nsp_newspaper_qual_last = 0
$ nsp_newspaper_last_money = 0 # Газета: Оценка публики, равна деньгам за предыдущий выпуск

$ nsp_newspaper_qual = 10 # Газета: Качество текущего выпуска
$ nsp_newspaper_cur_money = 10 # Газета: Оплата текущего выпуска
$ nsp_newspaper_published = False # Газета была опубликована
$ nsp_newspaper_published_mail = False # Письмо о награде за газету пришло

$ nsp_newspaper_articles = 0 # Газета: Количество написанных статей. Когда количество достигает 8, газету можно публиковать и счетчик сбрасывается.
$ nsp_newspaper_ready = False # Газета: Готовность.

$ nsp_pre_jobs_max = 0 # Подсчет максимального числа отчетов, которые были отосланы. Если число больше или равно 4, то приходит письмо о газете.

$ nsp_germiona_menu_rights = 1 # Гермиона: Доступность раздела "Права и дискриминация"
$ nsp_germiona_menu_magls = 1 # Гермиона: Доступность раздела "О жизни маглов публично"
$ nsp_germiona_menu_kviddich = 1  # Гермиона: Доступность раздела "О квиддиче"
$ nsp_germiona_menu_sex = 1  # Гермиона: Доступность раздела "О Сексе"
$ nsp_germiona_menu_maniac = 1  # Гермиона: Доступность раздела "Маньяк"
$ nsp_germiona_menu_nude = 1  # Гермиона: Доступность раздела "Голый репортер в маске"
$ nsp_germiona_menu_forest = 1  # Гермиона: Доступность раздела "Запретный лес"
$ nsp_germiona_menu_studio = 1  # Гермиона: Доступность раздела "Студия у Джина"

### Events flags
$ nsp_event_rights_1 = 0
$ nsp_event_rights_2 = 0
$ nsp_event_rights_3 = 0
$ nsp_event_rights_4 = 0
$ nsp_event_rights_5 = 0

$ nsp_event_magls_1 = 0
$ nsp_event_magls_2 = 0
$ nsp_event_magls_3 = 0
$ nsp_event_magls_4 = 0
$ nsp_event_magls_5 = 0

$ nsp_event_kviddich_1 = 0
$ nsp_event_kviddich_2 = 0
$ nsp_event_kviddich_3 = 0
$ nsp_event_kviddich_4 = 0
$ nsp_event_kviddich_5 = 0
$ nsp_event_kviddich_6 = 0

$ nsp_event_sex_1 = 0
$ nsp_event_sex_2 = 0
$ nsp_event_sex_3 = 0
$ nsp_event_sex_4 = 0
$ nsp_event_sex_5 = 0

$ nsp_event_maniac_1 = 0
$ nsp_event_maniac_2 = 0
$ nsp_event_maniac_3 = 0

$ nsp_event_nude_1 = 0
$ nsp_event_nude_2 = 0
$ nsp_event_nude_3 = 0
$ nsp_event_nude_4 = 0
$ nsp_event_nude_5 = 0

$ nsp_event_forest_1 = 0
$ nsp_event_forest_2 = 0

$ nsp_event_studio_1 = 0
$ nsp_event_studio_2 = 0
$ nsp_event_studio_3 = 0
$ nsp_event_studio_4 = 0
$ nsp_event_studio_5 = 0
$ nsp_event_studio_6 = 0

### Letters flags

$ nsp_day = 0
$ nsp_day_letter7 = 0

$ nsp_letter_1 = 0
$ nsp_letter_2 = 0
$ nsp_letter_3 = 0
$ nsp_letter_4 = 0
$ nsp_letter_5 = 0
$ nsp_letter_6 = 0
$ nsp_letter_7 = 0
$ nsp_letter_8 = 0
$ nsp_letter_9 = 0
$ nsp_letter_10 = 0
$ nsp_letter_11 = 0
$ nsp_letter_12 = 0
$ nsp_letter_13 = 0

$ nsp_pre_letter = 0 # Газета: Письмо о газете. 0 - не было, 1 - есть, 2 - уже прочитано.
$ nsp_pre_snape = 0 # Газета: Разговоры со снейпом о газете, номер текущего этапа.
$ nsp_pre_dahre = 0 # Газета: Доступность учебных книг о газете в каталоге Дахры.
$ nsp_newspaper_menu = 0 # Газета: Уровень разблокировки газетных меню.

$ hermione_out_halfday = 0

###

### DR'S wardrobe ###

$ wrd_new_items = 0

$ wrd_tits = 0
$ wrd_tits_no = 1

# SKIRTS
$ wrd_skirt = 1
$ wrd_shortskirt = 0
$ wrd_xshortskirt = 0
$ wrd_xxshortskirt = 0
$ wrd_xsmallskirt = 0
$ wrd_xxsmallskirt = 0
$ wrd_xxxsmallskirt = 0
$ wrd_skirt_cheerleader = 0
$ wrd_skirt_business = 0

# SHIRTS
$ wrd_standart01 = 1
$ wrd_standart02 = 0
$ wrd_standart03 = 0
$ wrd_standart04 = 0
$ wrd_standart05 = 0
$ wrd_skimpyshirt = 0
$ wrd_shirt_cheerleader = 0
$ wrd_shirt_business = 0

# OTHER
$ wrd_badge_01 = 0

# STOCKINGS
$ wrd_nets = 0
$ wrd_tights = 0

# RENT

$ wrd_rent_happy_schoolgirl = 0
$ wrd_rent_playful_schoolgirl = 0
$ wrd_rent_cheerleader = 0
$ wrd_rent_business = 0

$ wrd_nopanties_dialog = False

### Phoenix

$ pnx_stage = 0
$ pnx_lock = False

### GETTING LETTERS ###
$ letter_from_hermione_02 = False #Turns true when you get second letter from Hermione.
$ letter_from_ficbook_fun = False

###SNAPE STATS###
$ snape_busy = False #When True, you can't summon Snape.
$ snape_friendship = 0 #Get's +1 after every evening spent is Snape's company.
$ snape_events = 0 #Get's +1 point every time a special event with Snape happens. 


#$ level = "00" #Hermione's whoring level.

$ hermione_takes_classes = False #Turns True when Hermione becomes unavailable for summon after performing personal request in the morning.
$ hermione_sleeping = False



$ tutoring_events = 0 #Get's +1 point every time a tutoring special event happens. 
$ knowledge = 0
#$ whoring = 0 #Default: 0
$ teachers_pet = 0
$ classmates_pet = 0
$ being_mean = 0 #+1 every time you are being mean to hermione.

$currentBook=None
$item=None


$ dates = 0 #Tracks how many times Hermione been tutored.



### CHITCHATS WITH SNAPE ###
$ chitchat_event_01_happened = False
$ chitchat_event_02_happened = False
$ chitchat_event_03_happened = False
$ chitchat_event_04_happened = False
$ chitchat_event_05_happened = False
$ chitchat_event_06_happened = False
$ chitchat_event_07_happened = False


### SPECIAL DATES WITH SNAPE ###

#$ date_with_snape_02_happened = False #Second date with Snape. They decide to de-throne Hermione.
                                      #Turns true after event_09

###Miscellaneous flags###
$ hold_all_the_events_please = False #When TRUE all the story events will be put on hold.
$ jerk_off_session = False #Turns True when you choose to jerk off while Hermione talks (Event_08)

$ tutoring_offer_made = False #If you offered her to tutor her (In event_12). Affects conversation in the next event.

#$ chitchated_with_snape = False #Prevents you from chitchating more then once a day. Turns back to False every night.


#$ snape_against_hermione = False #Turns True after event_01. Activates event_11 when hanging out with Snape next time.
#$ snape_against_hermione_02 = False #Turns True after event_09. Activates second event when hanging out with Snape.

#$ hermione_is_waiting_01 = False #Turns True at the end of first special event with Snape. Triggers next visit from Hermione (event_09)
#$ hermione_is_waiting_02 = False #Turns True at the end of second special event with Snape. Triggers next visit from Hermione 

$ phoenix_is_feed = False #When True the graphic of bird food being displayed on top of the phoenix food can.
$ fire_in_fireplace = False #When True there is a fire going in the fireplace.
$ hat_act = False

#$ summoning_hermione_unlocked = False #Unlocks after event_14. Adds "Summon Hermione" button to the door.
#$ tutoring_hermione_unlocked = False #Unlocks after event_14.
#$ buying_favors_from_hermione_unlocked = False 


#$ hanging_with_snape = False #Turns true when "hanging with Snape during the night time" becomes available. (Snape becomes available for summons).
$ have_catalogue = False #Turns True when you obtain "The muggle oddities" catalog. (The button shows).


#$ books = [] 
$ gifts12 = []



### GENIE STATS ###============================
$ imagination = 1 #+1 for every completed book. Unlocks new sexual favors to buy. 1 point of imagination = 1 level of whoring.
$ concentration = 0 #+1 for every completed book on concentration. Pops up during paperwork.
$ speedwriting = 0 #+1 for every completed book on speedwriting. Pops up during paperwork.
$ job_lvl = 1 #Show how many reports you are allowed to complete per week.
### ===========================================

### BOOKS ###

$ book_07_units = 0 #Monitors progress with this book.
$ book_07_complete = False #Turns True when you finish reading book #7.
$ book07 = "\"Моя дорогая вайфу\""
$ shea = 0 #Shows how many times you went on a date with your stepsister Shea.
$ shea_waifu = False #Turns True if you finish the book with Shea.
$ complited_shea_already = False #Turns TRUE when you finish with Shea once. Need so that when you finish with Shea again you don get +1 Imagination.

$ victoria = 0
$ victoria_waifu = False #Turns True if you finish the book with ms.Victoria.
$ complited_stevens_already = False #Turns TRUE when you finish with Ms.Stevens once. Need so that when you finish with Shea again you don get +1 Imagination.

$ leena = 0
$ leena_waifu = False #Completed the book with Leena.
$ complited_leena_already = False #Turns TRUE when you finish with Leena once. Need so that when you finish with Shea again you don get +1 Imagination.
$ waifu_book_completed = False #Turns TRUE when you unlock the harem ending.



### NON-FICTION BOOKS ###========================================================================================
#BOOK 08
#$ book_08_units = 0 #Monitors progress with this book.
#$ book_08_complete = False #Turns True when you finish reading book #4.
#$ book08 = "\"Скорочтение для чайников\"" #1/6 chance to complete an extra chapter during reading.
$ s_reading_lvl = 0 #+1 When complete first book on speed reading. +1 again when complete the second book.



### MUGGLE ODDITIES ### =========================================================================
$ order_placed = False #TRUE when and order has been placed on an item.
#$ days_in_delivery = 0 # +1 day, every day since the orer has been made (when order_placed = True).
$ days_in_delivery2 = 0 # +1 day, every day since the orer has been made (when order_placed = True).
$ package_is_here = False # Turns true when days_in_delivery >= 5. Package is displayed.



### LEVELING UP PERSONAL REQUESTS ###
$ request_01 = 0 #Genie touches himself.
#$ request_02 = 0 #"Lift your skirt".
$ request_02_b_points = 0 #"Flirt with 3 classmates".
$ request_02_c_points = 0 #"Flirt with a teacher".
#$ request_03_points = 0 #"Give me your panties."
#$ request_04_points = 0 #"Molest tits."
#$ request_05_points = 0 #"Molest butt."
$ request_06_points = 0 #"Flash panties to a classmate."
$ request_07_points = 0 #"Flash panties to a teacher."
#$ request_08_points = 0 #"Show me your tits."
$ request_09_points = 0 #"Show me your pussy."
$ request_10_points = 0 #"Flash nipple to a classmate."
$ request_11_points = 0 #"Get naked."
#$ request_12_points = 0 #"Let me play with your tits."
$ request_15_points = 0 #(Flash a nipple to a teacher)
$ request_16_points = 0 #(Finger her pussy)
$ request_17_points = 0 #(Stick a finger up her butthole.)
#$ request_18_points = 0 #(Handjob).
$ request_19_points = 0 #(Rub dick against her cheeks.)
$ request_20_points = 0 #(Grab a classmate's cock)
$ request_21_points = 0 #(Cum on tits). 
#$ request_22_points = 0 #(Blowjob). 
$ request_23_points = 0 #(Give handjob to a classmate)
$ request_24_points = 0 #(Flash your tits to a teacher)
$ request_25_points = 0 #(Cum on face and with enough whoring send to class with face covered in cum.)
$ request_26_points = 0 #(Go to class with mouth full of cum).
$ request_27_points = 0 #(Blow two classamates).
$ request_28_points = 0 #(Give handjob to a teacher). 
#$ request_29_points = 0 #(Sex). 
$ request_30_points = 0 #(Blow a teacher)
#$ request_31_points = 0 #(Anal sex)
$ request_32_points = 0 #(Wear a very revealing outfit to class)


###PERSONAL REQUESTS#####
$ request_02_b = False #Flirt with 3 classmates.
$ request_02_c = False #Flirt with a teacher.
$ request_03 = False #Turns True when Hermione is sent on request No.3. (Goes to class without panties).
$ request_05 = False #Turns True when Hermione is sent on request No.5. (Flash panties to a classmate).
$ request_06 = False #Turns True when Hermione is sent on request No.6. (Flash panties to a teacher).
$ request_10 = False #Turns True when Hermione is sent on request No.10. (Flash a nipple to a classmate).
$ request_13 = False #Turns True when Hermione is sent on request No.13. (Wear a see-through shirt to class).
$ request_15 = False #Turns True when Hermione is sent on request No.15. (Flash a nipple to a teacher).
$ request_20 = False #Turns True when Hermione is sent on request No.20. (Grab a classmate's cock).
$ request_21 = False #Turns True when Hermione is sent on request No.21. (Jerk off on tits and put the clothes back on).
$ request_23 = False #Turns True when Hermione is sent on request No.23. (Give handjob to a classmate).
$ request_24 = False #Turns True when Hermione is sent on request No.24. (Flash your tits to a teacher).
$ request_25 = False #Turns True when Hermione is sent on request No.25. (Cum on face and send to class).
$ request_26 = False #Turns True when Hermione is sent on request No.26. (Go to class with mouth full of cum).
$ request_27 = False #Turns True when Hermione is sent on request No.27. (Blow two classamates).
$ request_28 = False #Turns True when Hermione is sent on request No.28. (Handjob to a teacher).
$ request_30 = False #Turns True when Hermione is sent on request No.30. (Blowjob to a teacher).
$ request_32 = False #Turns True when Hermione is sent on request No.32. (Put on a slutty dress and go to classes).
$ request_33 = False #Turns True when Hermione is sent on request No.33. (Go to classes with cum covered face).

# EVENTS #==============================================================================================================================================
### EVENT 01 ####
$ desk_examined = False #Turns True when you did examine you desk on day one.
$ cupboard_examined = False
$ bird_examined = False
$ door_examined = False
$ fireplace_examined = False
$ hat_examined = False

if this.event_05._finish2==4: 
    $ day = 4 # Если в начале новой игры выбрано перепрыгнуть на утро после дуэли т.е. event_05._finish2=4, установить день = 4
    $ desk_examined = True #Turns True when you did examine you desk on day one.
    $ cupboard_examined = True
    $ bird_examined = True
    $ door_examined = True
    $ fireplace_examined = True
    $ hat_examined = True
    $ rum_times = 4
$ report_talk = False    

# QUESTS #==============================================================================================================================================
$ zyablik_switch = 0
### TUTORING QUEST ####
$ teacher_jinn_quest = 0
$ study_book_quest_counter = 0
###SCREENS### NO NEED FOR THIS ONE ANYMORE. (SHOWS WHORING THOUGH).
screen statistics: #более подробно см. здесь http://www.renpy.org/doc/html/screens.html
    hbox: #горизонтальный «контейнер», где будет изображение золота и его количество
        spacing 10 xpos 630 ypos 20#отступ для текста, если надо прямо в левом углу — убираем его        
        text "{size=-3}День: [day]\nРаспутство: [whoring]\nУровень: [level]\nЗнания: [knowledge]\nСлизерин: [slytherin]\nГриффиндор: [gryffindor]\nДружба со Снейпом: [snape_friendship]\nДень недели: [day_of_week]\nКонцентрация: [concentration]\nСкорописание: [speedwriting]{/size}" #сумма текстом



###DAY STARTS HERE###<<<<<<<<<<<<<<<<<<<-----------------------------------------------------------------------------------###
###========================================================================================================================###
label day_start: 
    
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY THEME
        
        
$ chitchated_with_her = False #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
$ chitchated_with_snape = False #Prevents you from chitchating more then once a day. Turns back to False every night and every day.

$ hermione_main_zorder = 5 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
$ gifted = False #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
$ searched = False #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.


### MENU PLACEMENT ###
$ menu_x = 0.5 #Just to make sure that menu is displayed in the center of the screen by default.

### RESETING STUFF ###
$ only_upper = False #When true, legs are not displayed in the hermione_main screen.
$ autograph = False #Displays professor Lockhart's autograph on Hermione's leg.
$ no_blinking = False #When True - blinking animation is not displayed. 
$ sperm_on_tits = False #Sperm on tits when Hermione pulls her shirt up.
$ aftersperm = False #Shows cum stains on Hermione's uniform.
    
$ phoenix_is_feed = False #At the beginning of every new day Phoenix is not fed.
$ only_upper = False #When False legs are displayed in the hermione_main acreen.
$ hat_act = False

stop bg_sounds #Stops playing the fire SFX.
stop weather #Stops playing the rain SFX.

hide screen blkfade
hide screen notes #A bunch of notes poping out with a "win" sound effect.
hide screen phoenix_food
hide screen done_reading
hide screen done_reading_02
hide screen candlefire_01 #CANDLE FIRE.
hide screen candlefire_02 #CANDLE FIRE.
hide screen lightening #Hide lighting so it won't get stuck during clear sky weather and such.
hide screen cloud_night_01 #NIGHT CLOUDS.
hide screen cloud_night_02 #NIGHT CLOUDS.
hide screen cloud_night_03 #NIGHT CLOUDS.
hide screen bld1 #You know what this is. Just making sure it doesn't get stuck.
 
#if whoring >= 0 and whoring <= 2:
#    $ level = "01"
#if whoring >= 3 and whoring <= 5:
#    $ level = "02"
#if whoring >= 6 and whoring <= 8:
#    $ level = "03"
#if whoring >= 9 and whoring <= 11:
#    $ level = "04"
#if whoring >= 12 and whoring <= 14:
#    $ level = "05"
    
#if whoring >= 15 and whoring <= 17:
#    $ level = "06"
    
#if whoring >= 18 and whoring <= 20:
#    $ level = "07"
    
#if whoring >= 21 and whoring <= 23:
#    $ level = "08"
    
#if whoring >= 24 and whoring <= 26:
#    $ level = "09"
    
#if whoring >= 27 and whoring <= 29:
#    $ level = "10"

if hermi.whoring >= 12 and not touched_by_boy: #Turns true if sent Hermione to get touched by a boy at least once.
    $ lock_public_favors = True #Turns True if reached whoring level 05 while public event "Touched by boy" never attempted. Locks public events.



$ generating_snape_bonus = renpy.random.randint(1, 2) #Determines whether ot not Snape bonus will be added to the Slytherin house.   
$ generating_points = renpy.random.randint(1, 2) #Determines whether or not point will be awarded to Slytherin on this day. # MAKE NO CHANGES HERE. BEING USED AS "ONE_OUT_OF_TWO".
$ generating_points_gryffindor = renpy.random.randint(1, 10) #Addying point to Gryffindor (07_points_gry.rpy)  
$ generating_points_hufflepuff = renpy.random.randint(1, 10) #Addying point to Hufflepuff (07_points_gry.rpy)  
$ generating_points_ravenclaw = renpy.random.randint(1, 10) #Addying point to Ravenclaw (07_points_gry.rpy)  

$ one_out_of_three = renpy.random.randint(1, 3) #Generating one number out of three for various porpoises.
$ i_of_iv = renpy.random.randint(1, 4) #Generating one number out of three for various porpoises.
$ one_of_five = renpy.random.randint(1, 5) #Generating one number out of three for various porpoises.
$ i_of_vii = renpy.random.randint(1, 7)
$ one_of_ten = renpy.random.randint(1, 10) #Generating one number out of three for various porpoises.
$ one_of_tw = renpy.random.randint(1, 20) #Generating one number out of three for various porpoises.

### CUPBOARD MONEY GENERATOR ###

$ gold1 = renpy.random.randint(1, 10) # Money you find in the cupboard when Whoring Level: 1-2.
$ gold2 = renpy.random.randint(10, 40) # Money you find in the cupboard when Whoring Level: 3-4.
$ gold3 = renpy.random.randint(20, 50) # Money you find in the cupboard when Whoring Level: 5-6.
$ gold4 = renpy.random.randint(30, 90) # Money you find in the cupboard when Whoring Level: 7+.



$ daytime = True #True when it is daytime. Turns False during nighttime. 
$ hermione_sleeping = False
$ hermione_takes_classes = False
$ snape_busy = False
$ fire_in_fireplace = False
$ hat_act = False
hide screen fireplace_fire

### EVENTS RELATED FLAGS ###
$ days_without_an_event +=1

if letters < 0 : # На случай всяких неожиданностей
    $ letters = 0

### PAPERWORK (MONEY-MAKING) RELATED FLAGS ###
if day_of_week >= 7: #Counts days of the week. Everyday +1. When day_of_week = 7 resets to zero.
    $ day_of_week = 0
    if finished_report >= 1:
        $ got_paycheck = True #When TRUE the paycheck is in the mail. Can't do paper work.
        $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
        #$ got_mail = True comented out because being replaced with $ letters += 1
$ day_of_week += 1

### HERMIONE ###
# Ежеденевные изменения для всех персонажей
$hermi.liking+=1
$daphne.liking+=1

### DR'S newspaper ooo ###
#">>>[nsp_newspaper_articles] [nsp_newspaper_ready] [nsp_newspaper_published] [nsp_newspaper_published_mail]"

if nsp_pre_jobs_max < finished_report:
    $ nsp_pre_jobs_max = finished_report
    
if nsp_newspaper_menu >= 6 :
    $ nsp_day += 1
    $ nsp_day_letter7 += 1
    
if nsp_letter_7 == 3:
    $ nsp_letter_7 = 0

# На случай бага-пересечения с другим письмом.
if nsp_letter_7 == 2:
    $ nsp_letter_7 = 0
    
if nsp_letter_7 == 1:
    $ nsp_letter_7 = 2

### MUGGLE ODDITIES RELATED FLAGS ### VERSION TWO. This one randomizes delivery waiting days.
if order_placed: #TRUE when and order has been placed on an item.
    $ days_in_delivery2 -=1
    if days_in_delivery2 <= 0: 
        $ package_is_here = True
        $ order_placed = False



scene black

$ raining = False #No rain before the weather has been chosen at the beginning of every day.
hide screen new_window #Hiding clear sky bg.
hide screen cloud #THE CLOUD.


$ wather_generator = renpy.random.randint(1, 100) 
#$ wather_generator = 99 #THIS LINE IS FOR TESTING. 99 = Rain.
if wather_generator >= 81 and wather_generator <= 90: # RAIN
    #play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    $ raining = True
    show image "03_hp/07_weather/cloudy.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Cloudy background
    show rain at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Rain animation
elif wather_generator >= 1 and wather_generator <= 40: # CLEAR WEATHER.
    show screen new_window # показываем заглушку за окном #<<<XALJIO------------------------------------------XALJIO!!!!!!!!!!!
    #show image "03_hp/01_bg/03_weather.png" 
elif wather_generator >= 41 and wather_generator <= 60: #Floating cloud
    show screen new_window # показываем заглушку за окном #<<<XALJIO------------------------------------------XALJIO!!!!!!!!!!!
    show screen cloud #THE CLOUD.
    #show image "03_hp/01_bg/03_weather.png" 
    #show cloud_01 at Position(xpos=280, ypos=215, xanchor="center", yanchor="center") 
elif wather_generator >= 61 and wather_generator <= 80: # CLOUDY WEATHER
    show image "03_hp/07_weather/cloudy.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Cloudy background
    $ lighting_generator = renpy.random.randint(1, 2)
    if lighting_generator == 1:
        show lightening at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Rain animation
elif wather_generator >= 91 and wather_generator <= 100: # RAIN WITH LIGHTENING.
    #play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    $ raining = True
    show image "03_hp/07_weather/cloudy.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Cloudy background
    show lightening at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Rain animation
    show rain at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Rain animation


#show image im.Alpha("03_hp/01_bg/01_main_room.png", 0.5) #Transparent Background.




hide screen room_night #Hiding NIGHT BG from last night.
show screen room #Showing main room BG. 

hide screen door   
hide screen cupboard
hide screen chair
hide screen fireplace
hide screen phoenix
hide screen candle_01    
hide screen candle_02
hide screen genie
hide screen owl
hide screen owl_02
hide screen with_snape #Genie hangs out with Snape in front of the fireplace.
hide screen with_snape_animated #Genie hangs out with Snape in front of the fireplace.
if package_is_here:
    hide screen package


show screen door   
show screen cupboard
show screen chair
show screen fireplace
show screen phoenix
show screen candle_01    
show screen candle_02



### DAY MAIL ###

if day == 2:
    $ letter_from_hermione_02 = True #Turns true when you get second letter from Hermione.
    $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.

if day == 12: # LETTER THAT UNLOCKS PAPERWORK BUTTON.
    $ work_unlock = True # Send a letter that will unlock an ability to write reports.
    $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.

### DR'S NEWSPAPER ooo ###

if day > 20 and nsp_pre_jobs_max >= 4 and nsp_pre_letter < 1:
    $ nsp_pre_letter = 1
    $ letters += 1

if nsp_newspaper_published_mail == False and nsp_newspaper_published == True :
    $ nsp_newspaper_published_mail = True
    $ letters += 1
    
if nsp_day == 10:
    $ nsp_letter_1 = 1
    $ letters += 1
    
# DR'S PUB DISABLE    
#if nsp_day == 40:
#    $ nsp_letter_2 = 1
#    $ letters += 1
    
#if nsp_day >= 20 and nsp_letter_9 == 0 and nsp_event_forest_1 >= 1:
#    $ nsp_letter_9 = 1
#    $ letters += 1

#if nsp_day_letter7 == 7 and nsp_letter_7 == 0 and nsp_event_rights_3 < 5 :
#    if one_of_ten <= 7:
#        $ nsp_letter_7 = 1
#        $ letters += 1 
#    $ nsp_day_letter7 = 0
    
if letters <= 0 : # Чинит отчеты и публикации газеты в случае потери писем.
    $ nsp_newspaper_published = False
    $ nsp_newspaper_published_mail = False 
    $ got_paycheck = False
    

###

if package_is_here:
    play sound "sounds/owl.mp3"  #Quiet...
    show screen package
show screen genie

if total_report >= 10 and letter_from_ficbook_fun == False:
    $letters+=1
    
if this.IsStep("MAIL"):
    $letters+=1
if got_mail or mail_from_her or letters >= 1:
    play sound "sounds/owl.mp3"  #Quiet...
    show screen owl




#hide screen statistics 
#show screen statistics 

hide screen points
show screen points

with fade

$ day +=1

#===TG MODS START===

$ increment_cal_date()

#===TG MODS STOP===
    
# RENT RESET
    
if wrd_rent_happy_schoolgirl == 1 :
    ">С мягким шелестом форма веселой школьницы рассыпалась в пыль."
    
if wrd_rent_playful_schoolgirl == 1 :
    ">С мягким шелестом форма игривой школьницы рассыпалась в пыль."
    
if wrd_rent_cheerleader == 1 :
    ">С мягким шелестом форма болельщицы Гриффиндора рассыпалась в пыль."
    
if wrd_rent_business == 1 :
    ">С мягким шелестом одежда бизнес-леди рассыпалась в пыль."    
    
$ wrd_rent_happy_schoolgirl = 0
$ wrd_rent_playful_schoolgirl = 0
$ wrd_rent_cheerleader = 0
$ wrd_rent_business = 0

###

### DAY EVENTS ###<============================================================================================================================================================

### DR'S Newspaper ooo ###
if nsp_newspaper_menu == 8 :
    jump nsp_snape_dialog3

$ hermione_out_halfday -= 1

if hermione_out_halfday <= 0 :
    $ hermione_out_halfday = 0
    $ this.RunStep("DAY")
    
    
###
    
    

label day_main_menu:
    
  
if phoenix_is_feed:
    show screen phoenix_food
    
    

if day == 1 and daytime and bird_examined and desk_examined and cupboard_examined and door_examined and fireplace_examined and hat_examined:
    show screen bld1
    with d3
    m "Уже темнеет..."
    m "Я просто проведу остаток дня в этой комнате?"
    hide screen bld1
    with d3
    jump night_start



show screen animation_feather
call screen main_menu_01




####NIGHT STARTS HERE###<<<<<<<<<<<-----------------------------------------------------------------------------------------------------###
###=====================================================================================================================================###
label night_start:
    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    


    
    
$ daytime = False  
$ snape_busy = False
$ hermione_takes_classes = False
$ chitchated_with_snape = False #Prevents you from chitchating more then once a day. Turns back to False every night and every day.
$ chitchated_with_her = False #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
$ gifted = False #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
$ hat_act = False

stop bg_sounds #Stops playing the fire SFX.
stop weather #Stops playing the rain SFX.

scene black

hide screen blkfade
hide screen notes #A bunch of notes poping out with a "win" sound effect.
hide screen done_reading #Hiding genie sitting with closed book in his hands.
hide screen done_reading_02 #Done reading by the fire
hide screen new_window #Hiding clear sky bg.
hide screen cloud #THE CLOUD.

hide screen lightening #Hide lighting so it wouldn't get stuck during clear sky weather and such.
###WEATHER
if wather_generator >= 81 and wather_generator <= 90: # RAIN WITH LIGHTENING.
    show image "03_hp/07_weather/night_sky_04.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Cloudy background
    show lightening at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Rain animation
    show rain at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Rain animation
elif wather_generator >= 1 and wather_generator <= 30: #Clear sky with stars.
    show image "03_hp/07_weather/night_sky.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")# CLEAR WEATHER.
    
elif wather_generator >= 41 and wather_generator <= 50: #Clear sky with stars 02. (floating cloud during the day).
    show image "03_hp/07_weather/night_sky.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")# CLEAR WEATHER.

elif wather_generator >= 31 and wather_generator <= 40: #CLEAR FULL MOON.
    show image "03_hp/07_weather/night_sky_02.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")# CLEAR WEATHER.

elif wather_generator >= 51 and wather_generator <= 60: #FULL MOON WITH CLOUDS
    show screen cloud_night_01
    show screen cloud_night_02
    show screen cloud_night_03
    show image "03_hp/07_weather/night_sky_02.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")
    
elif wather_generator >= 61 and wather_generator <= 80: #HEAVY CLOUDS.
    show image "03_hp/07_weather/night_sky_04.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")
    $ lighting_generator = renpy.random.randint(1, 2)
    if lighting_generator == 1:
        show lightening at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Lighting

elif wather_generator >= 91 and wather_generator <= 100: #RAIN.
    show image "03_hp/07_weather/night_sky_04.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Cloudy background
    show rain at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Rain animation
    




if package_is_here:
    hide screen package
hide screen room #Hiding main room BG. 
show screen room_night #Showing main room NIGHT BG. 
hide screen door   
hide screen cupboard
hide screen chair
hide screen fireplace
hide screen phoenix
hide screen candle_01    
hide screen candle_02
hide screen genie
hide screen owl
hide screen owl_02

show screen door   
show screen cupboard
show screen chair
show screen fireplace
show screen phoenix
show screen candle_01  
show screen candlefire_01 #CANDLE FIRE.
show screen candle_02
show screen candlefire_02 #CANDLE FIRE.
if package_is_here:
    show screen package
show screen genie

#hide screen statistics 
#show screen statistics 

hide screen points
show screen points

if got_mail or mail_from_her or letters >= 1:
    show screen owl
with fade





call points_changes #Makes changes in the Slytherin house points.
call points_changes_gryffindor #Makes changes in the Gryffindor (And the rest of the houses) house points. (07_points_gry.rpy)
# call snape_bonus # Not in use anymore.

###QUEST SHIT###
if teacher_jinn_quest == 5:
    $ study_book_quest_counter += 1
    
if study_book_quest_counter == 3 and teacher_jinn_quest == 5:
    jump event_16

if total_report == 5 and report_talk == False:
    $ report_talk = True
    jump bad_reports



### NIGHT REQUESTS ###

### DR'S Newspaper ooo ###

$ hermione_out_halfday -= 1

if hermione_out_halfday <= 0 :
    $ hermione_out_halfday = 0
    $ this.RunStep("NIGHT")

###




label night_main_menu:
    
    
if phoenix_is_feed:
    show screen phoenix_food
    
show screen animation_feather
call screen main_menu_01    
    

pause
show ch_hem 01 at Position(xpos=732, ypos=350, xanchor="center", yanchor="center")
pause 


show ch_hem walk_01 at Move((732, 350), (300, 350), 5.0,
                  xanchor="center", yanchor="center") with Dissolve(.1)
pause 5.0

show ch_hem blink at Position(xpos=300, ypos=350, xanchor="center", yanchor="center") with Dissolve(.1)
pause 

show ch_hem run_f at Move((300, 350), (732, 350), 2.0,
                  xanchor="center", yanchor="center") with Dissolve(.1)

pause 2.0

show ch_hem blink at Position(xpos=300, ypos=350, xanchor="center", yanchor="center") with Dissolve(.1)
pause 
  
  
  
  
  

    

    
    
### INIT ###

init -2: 
    
    $ l_blush = False # Turns on blushing in the l_head screen. (Lola).
    $ l_things = False # Turns on cheerful emotion symbol in l_screen. (Lola).
    $ l_question = False # Turns on question mark emotion symbol in l_screen. (Lola).
    $ l_drop = False # Turns on drop emotion symbol in l_screen. (Lola).
    $ l_hearts = False # Turns on hearts emotion symbol in l_screen. (Lola).
    $ l_exclamation = False # Turns on hearts emotion symbol in l_screen. (Lola).
    $ l_tears = False # Turns on tears in l_screen. (Lola).
    
    $ config.autoreload = False
    

    
    
    
    
    
    
    

#методы движения через ATL надо объявлять в этом блоке
    transform cloud_move: #Метод ATL для задания движения облаков. Более продвинутый и современный, чем move. Про его возможности читать здесь: http://www.renpy.org/wiki/atl 
        xpos 408 #координата X, из которой облако начинает движение
        choice: #Функция, для выбора случайного значение из (в данном случае) пяти заданных для высоты облака. Можно хоть 20 выборов задать.
            ypos 150 #высота, на котором плывет облако
        choice:
            ypos 160
        choice:
            ypos 170
        choice:
            ypos 190
        choice:
            ypos 200

        linear 15.0 xpos 50 # linear — скорость движения. Чем больше значение , тем медленнее. xpos — координата x, куда облако движется
        pause 7
        repeat # повтор движения
        

    transform cloud_night_move_01: #CLOUD NIGHT 01. http://www.renpy.org/wiki/atl 
        xpos 408 #координата X, из которой облако начинает движение
        choice:
            ypos 130
        choice:
            ypos 150 #высота, на котором плывет облако
        choice:
            ypos 150 #высота, на котором плывет облако
        linear 30.0 xpos 50 # linear — скорость движения. Чем больше значение , тем медленнее. xpos — координата x, куда облако движется
        pause 2
        repeat # повтор движения
        
    transform cloud_night_move_02: #CLOUD NIGHT 01. http://www.renpy.org/wiki/atl 
        xpos 408 #координата X, из которой облако начинает движение
        choice:
            ypos 150 #высота, на котором плывет облако
        choice:
            ypos 170 #высота, на котором плывет облако
        linear 70.0 xpos 50 # linear — скорость движения. Чем больше значение , тем медленнее. xpos — координата x, куда облако движется
        pause 2
        repeat # повтор движения    
        
    transform cloud_night_move_03: #CLOUD NIGHT 01. http://www.renpy.org/wiki/atl 
        xpos 408 #координата X, из которой облако начинает движение
        ypos 160 #высота, на котором плывет облако
        linear 50.0 xpos 50 # linear — скорость движения. Чем больше значение , тем медленнее. xpos — координата x, куда облако движется
        pause 2
        repeat # повтор движения   

    label assmenu: # Sent here from "EXTRAS" menu. Basically just jumps to the title screen. 
        return
