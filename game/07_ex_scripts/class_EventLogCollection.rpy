
init -998 python:
  
# Класс - обертка для словаря логов ивентов
    class EventLogCollection(store.object):
        def __init__( self):
            self.Dict=dict() # Словарь логов
            
# Можно вызвать elog("Name") и получить лог ивента "Name",
# Если вызвать с параметром None - получим саму коллекцию (полезно, если обращаться через лямбду)
        def __call__( self, sName):
            if sName==None:
                return self
            if not sName in self.Dict:
                self.Dict.update({sName : EventLog(sName)})
            return self.Dict[sName]

# Был ли завершен ивент? Как параметр можно подать имя или альтернативное имя
        def IsFinished(self, sNameOrAlter):
            for o in self.Dict:
                if self.Dict[o].alter==sNameOrAlter:
                    return self.Dict[o].Finished
            if sNameOrAlter in self.Dict:
                return self.Dict[sNameOrAlter].Finished
            return False










