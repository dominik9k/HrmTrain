
init -993 python:
  
# Обертка точки исполнения ивентов
    class EventPoint(store.object):
        # constructor - Event initializing
        def __init__( self, Name, HSC):
            self.Name=Name
            self.HSC=HSC

# Добавить шаг в сценарий для этой точки
        def AddStep( self, sStep, sScenario="", ready=None, done=None, IsJump=False):
            return self.HSC(sScenario).AddStep(sStep, self.Name, ready, done, IsJump)

# Добавить вызов процедуры в сценарий для этой точки
        def AddCall( self, sStep, sScenario="", ready=None, done=None):
            self.AddStep(sStep, sScenario, ready, done, False)

# Добавить безусловный переход в сценарий для этой точки
        def AddJump( self, sStep, sScenario="", ready=None, done=None):
            self.AddStep(sStep, sScenario, ready, done, True)

# Есть готовый для исполнения шаг?
# Если сценариев будет несколько, переписать или перекрыть!
        def IsStep(self):
            return self.HSC().GetStep(self.Name)!=None    

# Исполнить шаг (если есть готовый для исполнения)
# Если сценариев будет несколько, переписать или перекрыть!
        def RunStep(self):
            self.Step = self.HSC().GetStep(self.Name)
            if self.Step!=None:
                renpy.call("Run",self.Step["Name"], self.Step["IsJump"])
            return None  

