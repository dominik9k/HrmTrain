
init -995 python:
  
# Класс - обертка для словаря сценариев с специфическими функциями по игре
    class ScenarioCollection(store.object):
        def __init__( self, ELog):
            self.Scenarios=dict() # Словарь сценариев
            self.ELog=ELog

        def __call__( self, sName="" ):
            return self.Scenarios[sName]

        def Init( self): # Код специфический для игры, не стал делать отдельного класса просто ради инициализации переменных
            self.DAY=EventPoint("DAY", self)
            self.NIGHT=EventPoint("NIGHT", self)
            self.SNAPE=EventPoint("SNAPE", self)
            self.CHITCHAT=EventPoint("CHITCHAT", self)
            self.IsDaysAfter2=lambda e: e.prev.IsDaysAfter(2)
            self.AddScenario("")
            self.RET_NoFinished = lambda e: None  # Возвращается, как результат функции, если ивент не завершен (например, Гермиона говорит, что придет завтра event_09) 

# Добавить сценарий
        def AddScenario(self, sName):
            if not sName in self.Scenarios:
                self.Scenarios.update({sName : Scenario(self.ELog, Name=sName )})









