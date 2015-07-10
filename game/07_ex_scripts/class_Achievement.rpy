label Achievement_constants:

    define const_ACH_WRD_HERMIONA_SHORTSKIRT = 0
    define const_ACH_WRD_HERMIONA_XSHORTSKIRT = 1
    define const_ACH_WRD_HERMIONA_XXSHORTSKIRT = 2
    define const_ACH_WRD_HERMIONA_XSMALLSKIRT = 3
    define const_ACH_WRD_HERMIONA_XXSMALLSKIRT = 4
    define const_ACH_WRD_HERMIONA_XXXSMALLSKIRT = 5
    define const_ACH_WRD_HERMIONA_SKIRT_CHEERLEADER = 6
    define const_ACH_WRD_HERMIONA_SKIRT_BUSINESS = 7
    define const_ACH_WRD_HERMIONA_STANDART02 = 8
    define const_ACH_WRD_HERMIONA_STANDART03 = 9
    define const_ACH_WRD_HERMIONA_STANDART04 = 10
    define const_ACH_WRD_HERMIONA_STANDART05 = 11
    define const_ACH_WRD_HERMIONA_SKIMPYSHIRT = 12
    define const_ACH_WRD_HERMIONA_SHIRT_CHEERLEADER = 13
    define const_ACH_WRD_HERMIONA_SHIRT_BUSINESS = 14
    define const_ACH_WRD_HERMIONA_NETS = 15
    define const_ACH_WRD_HERMIONA_TIGHTS = 16
    
    define const_ACH_EASTEREGGS_PHOENIX = 101
    define const_ACH_EASTEREGGS_PHOENIXSCENE = 102    
    
    return

init -999 python:
  
# Класс для удобного управления ачивками помимо концовок. При инициализации в игре создается объект $ achieve = Achievement()
    class Achievement(store.object):
        # constructor - Achievement initializing
        def __init__( self ):
            self.Values = { const_ACH_WRD_HERMIONA_SHORTSKIRT : False, const_ACH_WRD_HERMIONA_XSHORTSKIRT : False, const_ACH_WRD_HERMIONA_XXSHORTSKIRT : False,
                            const_ACH_WRD_HERMIONA_XSMALLSKIRT : False, const_ACH_WRD_HERMIONA_XXSMALLSKIRT : False, const_ACH_WRD_HERMIONA_XXXSMALLSKIRT : False,
                            const_ACH_WRD_HERMIONA_SKIRT_CHEERLEADER : False, const_ACH_WRD_HERMIONA_SKIRT_BUSINESS : False, const_ACH_WRD_HERMIONA_STANDARTFalse2 : False,
                            const_ACH_WRD_HERMIONA_STANDARTFalse3 : False, const_ACH_WRD_HERMIONA_STANDARTFalse4 : False, const_ACH_WRD_HERMIONA_STANDARTFalse5 = 11 : False,
                            const_ACH_WRD_HERMIONA_SKIMPYSHIRT : False, const_ACH_WRD_HERMIONA_SHIRT_CHEERLEADER : False, const_ACH_WRD_HERMIONA_SHIRT_BUSINESS : False,
                            const_ACH_WRD_HERMIONA_NETS : False, const_ACH_WRD_HERMIONA_TIGHTS : False,
                            
                            const_ACH_EASTEREGGS_PHOENIX : False, const_ACH_EASTEREGGS_PHOENIXSCENE = False,
                            } # Ачивменты текущей игры.
                
# Добавить ачивмент в список текущей игры для игрока (установить в True) : $ achieve.SetAchievement(const_ACH_WRD_HERMIONA_SHORTSKIRT)               
        def SetAchievement( self, iIndex ):
            self.Values[iIndex]=True

# Функция проверяет, заданно ли в текущем списке указанное достижение : if achieve.IsAchievement(const_ACH_WRD_HERMIONA_SHORTSKIRT): # дальше код, который выполняется если условие - истинно               
        def IsAchievement( self, iIndex ):
            if self.Values[iIndex]==True:
                return True
            else:
                return False

# Получить название ачивмента : achieve.Name(const_ACH_WRD_HERMIONA_SHORTSKIRT)
        def Name ( self, iIndex ):
            if iIndex == const_ACH_WRD_HERMIONA_SHORTSKIRT :
                return "Гермиона ходит в укороченной школьной юбке."
            elif iIndex == const_ACH_WRD_HERMIONA_XSHORTSKIRT :
                return "Гермиона ходит в сильно укороченной школьной юбке."
            elif iIndex == const_ACH_WRD_HERMIONA_XXSHORTSKIRT :
                return "Гермиона ходит в короткой школьной юбке."
            elif iIndex == const_ACH_WRD_HERMIONA_XSMALLSKIRT :
                return "Гермиона ходит в школьной миниюбке."
            elif iIndex == const_ACH_WRD_HERMIONA_XXSMALLSKIRT :
                return "Гермиона ходит в укороченной школьной миниюбке."
            elif iIndex == const_ACH_WRD_HERMIONA_XXXSMALLSKIRT :
                return "Гермиона ходит в суперкороткой школьной миниюбке."
            elif iIndex == const_ACH_WRD_HERMIONA_SKIRT_CHEERLEADER :
                return "Гермиона ходит в юбке болельщицы Гриффиндора."
            elif iIndex == const_ACH_WRD_HERMIONA_SKIRT_BUSINESS :
                return "Гермиона ходит в юбке бизнес-леди."
            elif iIndex == const_ACH_WRD_HERMIONA_STANDART02 :
                return "Гермиона ходит без жилетки."
            elif iIndex == const_ACH_WRD_HERMIONA_STANDART03 :
                return "Гермиона ходит без жилетки и галстука."
            elif iIndex == const_ACH_WRD_HERMIONA_STANDART04 :
                return "Гермиона ходит в рубашке с расстегнутым воротом."
            elif iIndex == const_ACH_WRD_HERMIONA_STANDART05 :
                return "Гермиона ходит в полурасстегнутой рубашке."
            elif iIndex == const_ACH_WRD_HERMIONA_SKIMPYSHIRT :
                return "Гермиона ходит в рубашке мини-топике."
            elif iIndex == const_ACH_WRD_HERMIONA_SHIRT_CHEERLEADER :
                return "Гермиона ходит в кофте болельщицы Гриффиндора."
            elif iIndex == const_ACH_WRD_HERMIONA_SHIRT_BUSINESS :
                return "Гермиона ходит в белой рубашке в деловом стиле."
            elif iIndex == const_ACH_WRD_HERMIONA_NETS :
                return "Гермиона ходит в ажурных чулках."
            elif iIndex == const_ACH_WRD_HERMIONA_TIGHTS :
                return "Гермиона ходит в колготках."
            elif iIndex == const_ACH_EASTEREGGS_PHOENIX :
                return "Вам удалось обнаружить пасхалку Феникса."
            elif iIndex == const_ACH_EASTEREGGS_PHOENIXSCENE :
                return "Вам удалось обнаружить второй уровень пасхалки Феникса."
            return "Ошибка: незаданный ачивмент."
            
# Получить описание ачивмента : achieve.Description(const_ACH_WRD_HERMIONA_SHORTSKIRT)
        def Description ( self, iIndex ):
            if iIndex == const_ACH_WRD_HERMIONA_SHORTSKIRT :
                return "Вы купили Гермионе в подарок укороченную школьную юбку. Затем удалось уговорить ее носить эту юбку в школе на занятиях."
            elif iIndex == const_ACH_WRD_HERMIONA_XSHORTSKIRT :
                return "Вы купили Гермионе в подарок сильно укороченную школьную юбку. Затем удалось уговорить ее носить эту юбку в школе на занятиях."
            elif iIndex == const_ACH_WRD_HERMIONA_XXSHORTSKIRT :
                return "Вы купили Гермионе в подарок короткую школьную юбку. Затем удалось уговорить ее носить эту юбку в школе на занятиях. Куда только смотрят учителя ?"
            elif iIndex == const_ACH_WRD_HERMIONA_XSMALLSKIRT :
                return "Вы купили Гермионе в подарок школьную миниюбку и уговорили носить на занятиях. Спасайся кто может, секс-бомба покинула люк."
            elif iIndex == const_ACH_WRD_HERMIONA_XXSMALLSKIRT :
                return "Вы купили Гермионе в подарок укороченную школьную миниюбку и уговорили носить на занятиях. Месть Снейпу сладка."
            elif iIndex == const_ACH_WRD_HERMIONA_XXXSMALLSKIRT :
                return "Вы купили Гермионе в подарок суперкороткую школьную миниюбку и уговорили носить на занятиях. Нет слов, чтобы это описать."
            elif iIndex == const_ACH_WRD_HERMIONA_SKIRT_CHEERLEADER :
                return "Вы купили Гермионе в подарок юбку болельщицы Гриффиндора и уговорили носить на занятиях. Раз-два, три-четыре. Юбки выше, колени шире. Или там было по-другому ?"
            elif iIndex == const_ACH_WRD_HERMIONA_SKIRT_BUSINESS :
                return "Вы купили Гермионе в подарок юбку бизнес-леди и уговорили носить на занятиях. Страшно представить, в чем заключается этот бизнес."
            elif iIndex == const_ACH_WRD_HERMIONA_STANDART02 :
                return "Вы уговорили Гермиону ходить на занятия без жилетки. Только не думайте, что теперь вас ждет карьера дипломата."
            elif iIndex == const_ACH_WRD_HERMIONA_STANDART03 :
                return "Вы уговорили Гермиону ходить на занятия без жилетки и галстука. Пока что ничего выдающегося."
            elif iIndex == const_ACH_WRD_HERMIONA_STANDART04 :
                return "Вы уговорили Гермиону ходить на занятия без жилетки и галстука, да еще и расстегнуть верхнюю пуговичку. Совсем неплохо !"
            elif iIndex == const_ACH_WRD_HERMIONA_STANDART05 :
                return "Вы уговорили Гермиону расстегнуть все пуговицы на рубашке, кроме самых важных. Пора подумать о публичных ораторских выступлениях."
            elif iIndex == const_ACH_WRD_HERMIONA_SKIMPYSHIRT :
                return "Вы уговорили Гермиону ходить на занятия в маленьком клочке ткани, называемом рубашка минитопик. Но не нужно гордиться... Ладно ! Вы {size=+2}можете{/size} гордиться !"
            elif iIndex == const_ACH_WRD_HERMIONA_SHIRT_CHEERLEADER :
                return "Вы подарили Гермионе кофту болельщицы Гриффиндора и уговорили ходить в ней на занятия. Дафна Гринграсс была в ярости."
            elif iIndex == const_ACH_WRD_HERMIONA_SHIRT_BUSINESS :
                return "Вы подарили Гермионе рубашку бизнесс-леди. Осталось придумать соответствующий бизнес."
            elif iIndex == const_ACH_WRD_HERMIONA_NETS :
                return "Вы убедили Гермиону носить сетчатые чулки. И немало рыбки попадется в эти сети..."
            elif iIndex == const_ACH_WRD_HERMIONA_TIGHTS :
                return "Вы убедили Гермиону носить колготки. Зачем ?"
            elif iIndex == const_ACH_EASTEREGGS_PHOENIX :
                return "Ваша природная любовь и сострадание к животным дали неожиданный результат. Потому что добро должно размнож... побеждать."
            elif iIndex == const_ACH_EASTEREGGS_PHOENIXSCENE :
                return "Вам удалось увидеть старую сцену времен Акабура под новым углом. С очередной найденной пасхалкой вас!"
            return "Ошибка: незаданный ачивмент."
            
# Получить название ачивмента с учетом его доступности : achieve.DispName(const_ACH_WRD_HERMIONA_SHORTSKIRT)
        def DispName ( self, iIndex ):
            if self.Values[iIndex]==True:
                return self.Name ( iIndex )
            else :
                return "{color=#858585}- Скрыто -{/color}"
                
# Получить описание ачивмента с учетом его доступности : achieve.DispDescription(const_ACH_WRD_HERMIONA_SHORTSKIRT)
        def DispDescription ( self, iIndex ):
            if self.Values[iIndex]==True:
                return self.Description ( iIndex )
            else :
                return "Данное достижение еще не достигнуто. А ведь оно доступно где-то в игре... Терпеливо ждет своего часа..."

# Сохранить в объекте persistent текущие достижения (старые тоже не удаляются), например : $ achieve.UpdatePersistent() 
        def UpdatePersistent ( self ):
            if persistent.achieve is None:
                persistent.achieve = set()
            persistent.achieve.update({self.Values});

# Является ли концовка iIndex запомненной (т.е.) проходили ли ее раньше, например : if not end.IsPersistent(1): # дальше код, который выполняется, если условие истинно
        def IsPersistent ( self, iIndex ):
            return iIndex in persistent.endings


