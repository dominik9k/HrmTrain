
#===TG MODS START===

init -2 python:

# NOTE: To change the data within the following list structures, you need to do it here. Not via code in the game,
# since the changes won't stick. It's safe that these are here in the init, since I don't expect any of these to
# change during normal play.

    # Month info, based on the school year of 1995/96. Harry and Hermione's fifth year.
    #
    # List of tuples, each pertaining to a month: use [0/1/2/3/4/5] to access them.
    #
    # ( # days in month,
    #   day of week the 1st falls on: 1=Sun & 7=Sat,
    #   date of new moon,
    #   date of full moon
    #   short name of month
    #   full name of month )
    #
    # You shouldn't need to touch this, unless expanding the range to accommodate new years or something.
    #
    # Also, I don't use month_info[0]. January = month_info[1].
    #
    # To get "Jan", you would need use: "month = month_info[1][4]".
    month_info = [(0,0,0,0,"",""),
        (31,2,20,5,"Jan","January"),
        (29,5,18,4,"Feb","February"),
        (31,6,19,5,"Mar","March"),
        (30,2,17,4,"Apr","April"),
        (31,4,17,3,"May","May"),
        (30,7,16,1,"Jun","June"),
        (31,2,15,1,"Jul","July"),
        (31,5,14,28,"Aug","August"),
        (30,6,24,9,"Sep","September"),
        (31,1,24,8,"Oct","October"),
        (30,4,22,7,"Nov","November"),
        (31,6,22,7,"Dec","December")]

    # Week info, giving short and long names for days. More importantly, attaching a unique number to each day of the
    # week.
    #
    # Again, a list of tuples: use [0/1] to access them.
    #
    # ( short name of day: 1=Sun & 7=Sat,
    #   long name of day )
    #
    # To get "Tuesday", you would need use: "weekday = week_info[3][1]".
    week_info = [("",""),
        ("Sun","Sunday"),
        ("Mon","Monday"),
        ("Tue","Tuesday"),
        ("Wed","Wednesday"),
        ("Thu","Thursday"),
        ("Fri","Friday"),
        ("Sat","Saturday")]

    # Weekend dates. I could have rolled these into holidays...
    # But it might be handy to have these separate (for some reason).
    weekends = [[0],
        [6,7,13,14,20,21,27,28],
        [3,4,10,11,17,18,24,25],
        [2,3,9,10,16,17,23,24,30,31],
        [6,7,13,14,20,21,27,28],
        [4,5,11,12,18,19,25,26],
        [1,2,8,9,15,16,22,23,29,30],
        [6,7,13,14,20,21,27,28],
        [3,4,10,11,17,18,24,25],
        [2,3,9,10,16,17,23,24,30],
        [1,7,8,14,15,21,22,28,29],
        [4,5,11,12,18,19,25,26],
        [2,3,9,10,16,17,23,24,30,31]]

    # UK school dates, 2014/15
#    holidays = [[0],
#        [1,2,3,4],
#        [14,15,16,17,18,19,20,21,22],
#        [],
#        [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
#        [4,23,24,25,26,27,28,29,30,31],
#        [],
#        [22,23,24,25,26,27,28,29,30,31],
#        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
#        [],
#        [24,25,26,27,28,29,30,31],
#        [1,2],
#        [20,21,22,23,24,25,26,27,28,29,30,31]]
    # 103 days, total

    # Hogwarts (fantasy) holiday dates, 1995/96
    #
    # 9-week Summer holiday, with shorter Christmas and Easter holidays Based off wiki information.
    #
    # I made this up, but it's pretty accurate. Works out to be about the same as regular schools have (in 2015).
    # Not quite the 9 weeks in summer, but 8.5 is pretty close...
    holidays = [[0],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14],
        [],
        [],
        [3,4,5,6,7,8,9,10,11,12,13,14],
        [],
        [27,28,29,30],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
        [],
        [],
        [],
        [20,21,22,23,24,25,26,27,28,29,30,31]]
    # 104 days, total

### GENERAL FUNCTIONS ###

    # User function to increment the date in a safe, predictable manner.
    def increment_cal_date():
        global cal_new_year
        global cal_month
        global cal_day

        cal_day += 1
        
        if cal_day > month_info[cal_month][0]:
            cal_month += 1
            cal_day = 1

        if cal_month > 12:
            cal_new_year = True
            cal_month = 1

        # in case of the year looping...
        if cal_month == 9 and cal_new_year:
            cal_new_year = False
            #reset_year() # to reset the year's old data??? Unimplemented.

    # User function to take care of adding notes to the calendar.
    #
    # Expects:
    # (1) a list of dates, [(m,d),(m,d),(m,d)].
    #     Make sure you are passing it dates within a LIST. The function requires this.
    # (2) a text string that relates to the filename of an actual image (a note image residing in 03_hp/11_misc/).
    #     So, something like "hogsmeade_weekends", which relates to the image: "cal_note_hogsmeade_weekends.png"
    #     that's currently in "03_hp/11_misc/".
    #
    # So, you can give it a list of dates, or just a list containing a single date. Don't try to give it more than one
    # note though. It won't like it.
    def add_cal_notes(dates, note):
        note = "cal_note_" + note

        for x in range(len(dates)):
            month = dates[x][0]
            day = dates[x][1]
            cal_notes[month].append((day, note))

    # User function to take care of adding circles to the calendar.
    #
    # Expects: a list of dates, [(m,d),(m,d),(m,d)].
    #          Make sure you are passing it dates within a LIST. The function requires this.
    def add_circled_days(dates):
        for x in range(len(dates)):
            month = dates[x][0]
            day = dates[x][1]
            circled_days[month].append(day)

    # User function to take care of adding stars to the calendar.
    #
    # Expects: a list of dates, [(m,d),(m,d),(m,d)].
    #          Make sure you are passing it dates within a LIST. The function requires this.
    def add_starred_days(dates):
        for x in range(len(dates)):
            month = dates[x][0]
            day = dates[x][1]
            starred_days[month].append(day)

    # User function to build a list of dates falling on a certain day within the month.
    #
    # Expects:
    # (1) any month of the year, 1-12.
    # (2) a day of the week, 1-7 (the numerical value of the day).
    #     Sunday=1, Saturday=7, just like how it looks in the game.
    def dates_of_day(month, day):
        list = []

        query_month = build_month(month)

        for x in range(len(query_month)):
            if (query_month[x][day-1] != 0):
                list.append((month, query_month[x][day-1]))

        return list

    # User function to return the day a date falls on.
    #
    # Expects: a properly formatted date (a tuple). Something like (m,d).
    #
    # Returns: a day in numerical value, 1-7.
    #
    # If you need to get English, use: day = week_info[value][1]. This is obviously AFTER you've gotten the value from
    # this function.
    def day_of_date(date):
        curr_month = date[0]
        curr_day = date[1]

        list = []

        query_month = build_month(curr_month)

        for x in range(len(query_month)):
            if curr_day in query_month[x]:
                for y in range(len(query_month[x])):
                    if query_month[x][y] == curr_day:
                        return (y + 1)

    # User function to return the new date, given a starting date and some number of days.
    #
    # This number can be negative, so you can use it to go backwards from a date as well as forwards.
    #
    # Expects: a properly formatted date (a tuple). Something like (m,d).
    #
    # Returns: a tuple, the new date.
    def date_finder(date, days):
        curr_month = date[0]
        curr_day = date[1]

        if days == 0:
            return date
        elif days < 0:
            for x in range(days*-1):
                curr_day -= 1
                if curr_day < 1:
                    curr_month -= 1
                    if curr_month < 1:
                        curr_month = 12
                    curr_day = month_info[curr_month][0]
            return (curr_month, curr_day)
        else:
            for x in range(days):
                curr_day += 1
                if curr_day > month_info[curr_month][0]:
                    curr_month += 1
                    if curr_month > 12:
                        curr_month = 1
                    curr_day = 1
            return (curr_month, curr_day)

    # User function to return the number of days between any two dates, going forward through the year.
    #
    # This is slightly different than just finding the number of days between any two dates, since going forwards may
    # lead to a different result than going backwards. If not 6 months apart, one will be shorter. And shorter doesn't
    # always make the most sense. Hence, complimentary functions.
    # 
    # Use this function for when you want to work out the days for something in the future. But always put the STARTING
    # DATE as the first calling value, and make sure you really want to go forwards through the year to this ENDING
    # DATE.
    #
    # There is a complimentary function for backwards. See below.
    #
    # Expects: a starting date and ending date, properly formatted.
    #
    # Returns: the number of days between them (going forward through the year).
    def day_count_forwards(start_date, end_date):
        start_month = start_date[0]
        start_day = start_date[1]
        end_month = end_date[0]
        end_day = end_date[1]

        count = 0

        if (start_month == end_month) and (start_day == end_day):
            return 0

        while (start_month != end_month) or (start_day != end_day):
            start_day += 1
            count += 1
            if start_day > month_info[start_month][0]:
                start_month +=1
                if start_month > 12:
                    start_month = 1
                start_day = 1

        return count

    # User function to return the number of days between any two dates, going backward through the year.
    #
    # This is slightly different than just finding the number of days between any two dates, since going forwards may
    # lead to a different result than going backwards. If not 6 months apart, one will be shorter. And shorter doesn't
    # always make the most sense. Hence, complimentary functions.
    # 
    # Use this function for when you want to work out the days from something in the past. But always put the STARTING
    # DATE as the first calling value, and make sure you really want to go backwards through the year to this ENDING
    # DATE.
    #
    # There is a complimentary function for forwards. See above.
    #
    # Expects: a starting date and ending date, properly formatted.
    #
    # Returns: the number of days between them (going backwards through the year).
    def day_count_backwards(start_date, end_date):
        start_month = start_date[0]
        start_day = start_date[1]
        end_month = end_date[0]
        end_day = end_date[1]

        count = 0

        if (start_month == end_month) and (start_day == end_day):
            return 0

        while (start_month != end_month) or (start_day != end_day):
            start_day -= 1
            count += 1
            if start_day < 1:
                start_month -=1
                if start_month < 1:
                    start_month = 12
                start_day = month_info[start_month][0]

        return count

### SERVICE FUNCTIONS ###

    # Service function to convert the (on-going) days count to an equivalent date.
    #
    # This is most useful in the situation of a user wanting to integrate the calendar into an already running game,
    # via loading a save file.
    #
    # So, what this does is take that file's day and converts it (hopefully)
    def day_to_date():
        for x in range(day):
            increment_cal_date()

    # Service function for printing calendar dates.
    # Only used by the screen calendar: module.
    def cal_pos(col, row):
        origin_xpos, origin_ypos = 192, 208
        spacing_x, spacing_y = 60, 50
        return origin_xpos + spacing_x*(col-1), origin_ypos + spacing_y*(row-1)

    # Service function to build accurate rows and columns composing a (any) month.
    #
    # Expects: any month, 1-12.
    #
    # Returns: completed, usable array (list of lists).
    def build_month(month):
        matrix = [[],
                  [],
                  [],
                  [],
                  [],
                  []]

        curr_row = 0
        curr_col = 0
        curr_day = 1
        spaces_filled = 0

        # fill up the front empty spaces with 0's
        for x in range(month_info[month][1] - 1):
            matrix[curr_row].append(0)
            curr_col += 1
            spaces_filled += 1

        # fill in the days
        for y in range(month_info[month][0]):
            if curr_col == 7:
                curr_row += 1
                curr_col = 0

            matrix[curr_row].append(curr_day)
            curr_col += 1
            curr_day += 1
            spaces_filled += 1

        # 42 spaces in total in the matrix grid.
        # It's best if we fill the trailing empty ones with 0's too, to make
        # the matrix completely safe to query.
        for z in range(42-spaces_filled):
            if curr_col == 7:
                curr_row += 1
                curr_col = 0

            matrix[curr_row].append(0)
            curr_col += 1

        return matrix

label calendar:
    $ cal_browsing_month = cal_month
    $ cal_browsing_new_year = cal_new_year

    show screen bld1
    with Dissolve(.3)
    call screen calendar

label calendar_cleanup:
    hide screen bld1
    with Dissolve(.3)
    jump day_main_menu

label calendar_decrement:
    if cal_browsing_month == 1:
        $ cal_browsing_month = 12
        $ cal_browsing_new_year = False
    else:
        $ cal_browsing_month -= 1
    call screen calendar

label calendar_increment:
    if cal_browsing_month == 12:
        $ cal_browsing_month = 1
        $ cal_browsing_new_year = True
    else:
        $ cal_browsing_month += 1
    call screen calendar

#===TG MODS STOP===
