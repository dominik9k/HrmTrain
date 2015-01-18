label EventLog_constants:
    # 
    define const_EVENT_FIRST_START = 0
    define const_EVENT_LAST_START = 1
    define const_EVENT_FIRST_FINISH = 2
    define const_EVENT_LAST_FINISH = 3


    return

# Если из python вызывать код  RenPy renpy.call("Название", параметр), то сразу после этого происходит вылет из кода python
# Unfortunately, renpy.call() always aborts the Python stack and returns to the Ren'py script. You should try to avoid using renpy.call(), which means only executing functions when you are sure you don't need to call a label inbetween.
# Поэтому функции обрачивающие логгированием вызов методов RenPy приходится писать тоже в RenPy
label Run(sName, bIsJump):
    if bIsJump:
        $ elog(sName).IncPassed()
        jump expression sName

    $ elog(sName).IncStarted()
    call expression sName
# Можно запустить постобработку ивента вернув лямбду. По умолчанию просто помечается, что ивент завершен
    if _return==None:
        $ elog(sName).IncFinished()
    else:
        $ _return(elog(sName))

return



init -999 python:
  
# Класс для логов ивентов, содержит сведения о том когда и сколько раз запускались ивенты и функции для работы с этой иформацией
    class EventLog(store.object):
        # constructor - Event initializing
        def __init__( self, sName, alter=None):
            self.StartCount=0
            self.FinishCount=0
            self.Name=sName     
            self.alter=alter    # Альтернативное имя ивента
            self.prev=None      # Предыдущий ивент (переустанавливается каждый раз)
            self.Days = {const_EVENT_FIRST_START : -1, const_EVENT_LAST_START : -1, const_EVENT_FIRST_FINISH : -1, const_EVENT_LAST_FINISH : -1}


# Произошло ли событие iStartFinishMode iDaysAgo дней назад или раньше?
        def IsExec( self, iDaysAgo, iStartFinishMode ):
            if self.Days[iStartFinishMode]==-1:
                return False
            else:
                return self.Days[iStartFinishMode] <= day-iDaysAgo

# Было ли завершено?
        def IsFinished( self ):
            return self.IsExec(0, const_EVENT_FIRST_FINISH)

# Логгировать запуск ивента
        def IncStarted( self ):
            if self.Days[const_EVENT_FIRST_START]==-1:
                self.Days[const_EVENT_FIRST_START]=day
            self.Days[const_EVENT_LAST_START]=day
            self.StartCount+=1

# Логгировать завершение ивента
        def IncFinished( self ):
            if self.Days[const_EVENT_FIRST_FINISH]==-1:
                self.Days[const_EVENT_FIRST_FINISH]=day
            self.Days[const_EVENT_LAST_FINISH]=day
            self.FinishCount+=1

# Логгировать запуск &  завершение ивента
        def IncPassed( self ):
            self.IncStarted()
            self.IncFinished()

# Завершено iDays назад или ранее?
        def IsAgo( self, iDays ):
            return self.IsExec(iDays,const_EVENT_LAST_FINISH)


        Finished = property(IsFinished)



