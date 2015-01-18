
init -996 python:
  
# Работа с сценариями - заданными последовательностями ивентов (шагов)
# При описании сценария (добавлении его шагов) можно задать условия, при которых возможно выполнение шага (т.е. переход переход на метку ивента)
# Кроме того, при вызове сценария на выполнение действует правило - шаг может быть выполнен, только если выполнены все предыдущие шаги
# Т.о. сохраняется логика событий

    class Scenario(store.object):
        def __init__( self, ELog, Name="", ):
            self.List=[]        # Список строк - названий шагов в заданной последовательности
            self.Dict=dict()    # Словарь шагов
            self.Name=Name      # Название словаря
            self.ELog=ELog      # Лямбда выражение для доступа к коллекции логов ивентов

# Добавление шага.  
        def AddStep( self, sName, block, ready, done, IsJump):
            alter=None
            sp =sName.split(":") 
            if len(sp)>1:
                sName=sp[0]
                alter=sp[1]
            if not sName in self.List:
                self.List.append(sName)
                self.Dict.update({sName: {"Name":sName, "alter": alter, "block":block, "ready":ready,  "done":done, "IsJump":IsJump}})
            return self.Dict[sName]

# Получение текущего шага в точке доступа (если условия не выполнены, то None)
        def GetStep( self, block):
            prev=None
            for o in self.List:
# prev используется при вызове e.prev в лямбда. Поскольку EventLog не знает, какой ивент предыдущий, каждый раз при вызове ему это явно указывается
# здесь же для ивентлога устанавливается альтернативное имя.
#Красивее установить альтернативное имя в AddStep, но AddStep запускается в блоке init, a elog инициализируется только в start (связано с необходимостью сохранять данные) 
                evn=self.ELog(o)
                evn.prev=prev
                evn.alter=self.Dict[o]["alter"]


                # Условие старта обязательное, без него не запустится
                readyDef=lambda e:True
                if prev!=None:
                    readyDef=lambda e:e.prev.Finished
                # Условие старта дополнительное (написанное пользователем) соединяются через И
                ready=lambda e:True
                if self.Dict[o]["ready"]!=None:
                    ready=self.Dict[o]["ready"]

                # Условие выполнения по умолчанию
                done=lambda e:e.Finished
                # Условие выполнения дополнительное (написанное пользователем). Перекрывает условие по умолчанию
                if self.Dict[o]["done"]!=None:
                    done=self.Dict[o]["done"]

                if self.Dict[o]["block"]==block and readyDef(evn) and ready(evn) and not done(evn) :
                    return self.Dict[o]
                        
                prev=evn
            return None






