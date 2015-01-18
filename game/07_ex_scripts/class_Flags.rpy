
init -993 python:
  
# Обертка для работы с флажками
# Проверку завершения любого ивента можно привести так: flag("EventName"), здесь EventName может быть именем или альтернативным именем ивента
    class Flags(store.object):
        def __init__( self, ELog):
            self.ELog=ELog


        def __call__( self, sNameOrAlter):
            return self.ELog(None).IsFinished(sNameOrAlter)



    global flag
    flag=Flags(lambda s: elog(s))




