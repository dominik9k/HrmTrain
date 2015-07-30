label after_load:

#===TG MODS START===

    if not hasattr(renpy.store,'day'): #important! [needed in case of new game!]
        $ day = 0
    if not hasattr(renpy.store,'desk_examined'): #important! [needed in case of new game!]
        $ desk_examined = False
    if not hasattr(renpy.store,'cal_new_year'): #important!
        $ cal_new_year = False
    if not hasattr(renpy.store,'cal_month'): #important!
        $ cal_month = 9
    if not hasattr(renpy.store,'cal_day'): #important!
        $ cal_day = 13
        if day > 0:
            $ day_to_date()
    if not hasattr(renpy.store,'important_dates'): #important!
        $ important_dates = {
            'four_seasons':[(9,22,"Autumn"),(12,21,"Winter"),(3,20,"Spring"),(6,21,"Summer")],
            'term_dates':[(9,1,"Autumn term"),(12,19),(1,15,"Winter term"),(4,2),(4,15,"Spring term"),(6,26)],
            'holiday_dates':[(12,20,"Christmas holidays"),(1,14),(4,3,"Easter holidays"),(4,14),(6,27,"Summer holidays"),(8,31)],
            'OWL_dates':[(6,10),(6,21)],
            'hogsmeade_weekends':[(9,23),(10,15),(11,4),(11,26),(12,16),(2,4),(2,24),(3,17),(5,4),(5,26),(6,15)],
            'dumblegenies_arrival':[(9,14)],
            'hermiones_periods':[(9,18),(10,16),(11,13),(12,11),(1,8),(2,5),(3,4),(4,1),(4,29),(5,27),(6,24),(7,22),(8,19)],
            'ball_dates':[(9,30,"Autumn Ball"),(12,16,"Yule Ball"),(3,30,"Spring Fling"),(6,22,"Prom")] }
    if not hasattr(renpy.store,'known_dates'): #important!
        $ known_dates = {
            'OWL_dates':False,
            'hogsmeade_weekends':False,
            'hermiones_periods':False,
            'ball_dates':False }
        if desk_examined:
            $ known_dates['hogsmeade_weekends'] = True
    if not hasattr(renpy.store,'circled_days'): #important!
        $ circled_days = [[0],[],[],[],[],[],[],[],[],[],[],[],[]]
    if not hasattr(renpy.store,'starred_days'): #important!
        $ starred_days = [[0],[],[],[],[],[],[],[],[],[],[],[],[]]
    if not hasattr(renpy.store,'cal_notes'): #important!
        $ cal_notes = [[(0,"")],[],[],[],[],[],[],[],[],[],[],[],[]]
        if desk_examined:
            $ dates_list = important_dates['hogsmeade_weekends']
            $ add_cal_notes(dates_list, 'hogsmeade_weekends')

#===TG MODS STOP===

# Метка - зерезервированная RenPy. На нее программа переходит после загрузки.
# Код ниже инициализирует переменные хранилища, если они не были инициализированы (например, написан новый шаг сценария)
# Этот же код вызываем из блока start для начальной инициализации переменных
    python:
        InitEntriesFields()
    return

label start_elog:    
    # Elog class initialization
    # Инициализация словаря параметров, которые необходимо записывать при сохранении и списка, содержащего историю перехода по меткам
    python:
        global elog
        global labelHistory
        global jumpHistory
        
    $elog=dict()
    $labelHistory=[]
    $jumpHistory=[]
#    $entries=[]
    return

init -999 python:

    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')


# Функции для работы со словарем elog - сохранятеся
    def IsStoreKey(key):
        return key in elog

    def IsStoreSubKey(key, subkey):
        if IsStoreKey(key):
            return subkey in elog[key]
        return False

    def SetStoreValue(key, subkey, value):
#        debug.SaveString("SetStoreValue("+str(key)+", "+str(subkey)+", "+str(value), 3)
        if not IsStoreKey(key):
            elog.update({key: dict()})

        __SetStoreValue_oldvalue=GetStoreValue(key, subkey)

        if not IsStoreSubKey(key, subkey):
            elog[key].update({subkey: value})
        else:
            elog[key][subkey]=value
        OnChangeStoreValue(key, subkey, __SetStoreValue_oldvalue, value) # Перехватываем все изменения

# Намеренно не ставлю здесь проверок на наличие соответствующего поля. Разработчик должен проверять перед вызовом с помощью функций  IsStoreKey IsStoreSubKey
    def GetStoreValue(key, subkey):
        if IsStoreKey(key):
#            debug.SaveString("GetStoreValue("+str(key)+", "+str(subkey)+")="+str(elog[key].get(subkey)), 3)
            pass
        else:
            debug.SaveString("GetStoreValue("+str(key)+", "+str(subkey)+")=НЕТ КЛЮЧА!", 3)

        return elog[key].get(subkey)

    def GetStoreAllSubKeys(key):
        res=[]
        for s in elog:
            if s==key:
                for subkey in elog[s]:
                    res.append(subkey)
                return res
        return res



# Полная копия по функционалу верхнего блока процедур, но работает с объектом arr, который объявляется в блоке Init и не сохранятется и каждый раз инициализируется

    def IsArrayKey(key):
        return key in arr

    def IsArraySubKey(key, subkey):
        if IsArrayKey(key):
            return subkey in arr[key]
        return False

    def SetArrayValue(key, subkey, value):
#        debug.SaveString("SetArrayValue("+str(key)+", "+str(subkey)+", "+str(value), 3)
        if not IsArrayKey(key):
            arr.update({key: dict()})
        if not IsArraySubKey(key, subkey):
            arr[key].update({subkey: value})
        else:
            arr[key][subkey]=value

# Намеренно не ставлю здесь проверок на наличие соответствующего поля. Разработчик должен проверять перед вызовом с помощью функций  IsStoreKey IsStoreSubKey
    def GetArrayValue(key, subkey):
#        debug.SaveString("GetArrayValue("+str(key)+", "+str(subkey)+")="+str(arr[key].get(subkey)), 3)
        return arr[key].get(subkey)

    def GetArrayAllSubKeys(key):
        res=[]
        for s in arr:
            if s==key:
                for subkey in arr[s]:
#                    renpy.say(her,str(key)+" "+str(s)+" "+subkey)
                    res.append(subkey)
                return res
        return res

#    def GetLabelCount(s):
#        return labelHistory.count(s)

#    def IsLabelCountEq(s1, s2):
#        return labelHistory.count(s1)==labelHistory.count(s2)



    def RegEntry(entry):
        entry.handle=len(entries)
        entries.append(entry)
        return entry

    def GetEntry(Name):
        for o in entries:
            if o.Name==Name:
                return o
        return None


    def GetEntriesByType(typeName):
        __set=set()
        for o in entries:
            if o.Type==typeName:
                __set.update({o})
        return __set

    def InitEntryField(entry, subkey):
        exec "entries["+str(entry.handle)+"]._"+subkey+"=entries["+str(entry.handle)+"].GetValue('"+subkey+"')"
        return            

    def InitEntriesFields():
        if hasattr(renpy.store,"elog"): # Если уже инициализирован elog
#            this.InitStart()
            if hasattr(renpy.store,"wtevent"):
                if renpy.store.wtevent!=None: # Состояние переменной объекта wtevent после чтения сохранения может отличаться от полей объекта this.GetCall(wtevent.Name). 
                    for e in this.List: # Нужно сопоставить их, иначе присвоение полей одного из объектов непредсказуемо влияет на поля другого
                        if e.Name==renpy.store.wtevent.Name:
                            renpy.store.wtevent=this.GetCall(renpy.store.wtevent.Name)
                            break

            for o in entries:   # Если значение не заполнено (т.е. разрабдотчик ввел новое или новый объект появился) - заполнить значениями по умолчанию
                for subkey in o.defVals:
                    if not IsStoreSubKey(o.Name, subkey):
                        SetStoreValue(o.Name, subkey,  o.defVals[subkey])
#        else:
        for o in entries: # для всех объектов типа наследников Entry создать поля типа  объект._имяпеременной
            __list=GetStoreAllSubKeys(o.Name)
            for subkey in __list:
                InitEntryField(o, subkey)
            __list=GetArrayAllSubKeys(o.Name)
            for subkey in __list:
# Нельзя создавать переменные для лямбда- RenPy их пытается записать при сохранении и возвращает ошибку               
                if not subkey in ["ready", "done"]:
                    InitEntryField(o, subkey)
        storeInitialized=True


    def OnChangeStoreValue(key, subkey, oldvalue, newvalue):
        __entry=GetEntry(key)        
        if __entry.Type=="Event":
# Если заключено соглашение с Гермионой, то после каждой встречи с Дафной Гриффиндор получает 10 очков
            if (__entry.GetValue("members")!=None):
                if ("daphne" in __entry.GetValue("members")) and (subkey=="finishCount") and (newvalue>(0 if oldvalue==None else oldvalue)):
                    if hermi._pointsPerDaphneVisit>0:
                        Say("По вашему соглашению с Гермионой Гриффиндор получает 10 очков")
                        renpy.store.gryffindor+=10

