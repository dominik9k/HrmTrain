init -500 python:
  
    class GameEngine( store.object ):
        def __init__( self, aScenarioBase ):
            self.mScenario = aScenarioBase

            # read this from file later
            self.mStages = [ 'DAY', 'NIGHT' ]
            self.mCurrentStageInd = 0
            self.mIsFinished = False
            
            self.mDay = 0

            # dictionary of objects
            self.mGlobalVariables = { 'global_test' : 0 }

            self.mCurrentEvent = None

            # dictionary of dictionary of objects
            self.mLocalVariablesBase = { 'event_test': { 'localVar': 0 } }
            # this is points to dictionary with local variables for current event
            self.mLocalVariables = None

        def fireAction( self, aActionKey ):
            if self.mCurrentEvent:
                self.mCurrentEvent.action( aActionKey )

        def fireStage( self, aCurrentScenario = None ):
            curStage = self.mStages[ self.mCurrentStageInd ]
            # check all items in scenario
            for sc in self.mScenario.mScenarios:
                # if we've passed scenario into this function - this means we are trying to continue choosing scenarios
                if aCurrentScenario != None:
                    if sc != aCurrentScenario:
                        continue
                    else:
                        aCurrentScenario = None
                        continue
                # if scenario is not finished
                if not sc.isFinished():
                    # and we are in appropriate state
                    if sc.isStage( curStage ):
                        # init scenario first time
                        self.mCurrentEvent = sc
                        self.setLocals( sc.name() )
                        return self.mCurrentEvent;
            self.mCurrentEvent = None
            return None

        def nextStage( self ):
            self.mCurrentStageInd += 1
            if self.mCurrentStageInd >= len( self.mStages ):
                self.mIsFinished = True
            return self.isFinished()

        def isFinished( self ):
            return self.mIsFinished

        def prepare( self ):
            self.mCurrentEvent = None
            self.mCurrentStageInd = 0
            self.mIsFinished = False

        # return current day
        def day( self ):
            return self.mDay

        def nextDay( self ):
            self.mDay += 1


        # for working with global variables
        def globals( self, aName ):
            if aName in self.mGlobalVariables.keys():
                return self.mGlobalVariables[ aName ]
            else:
                GameEngineDebugger.LogE( 'GameEngine.globals - no object for key ' + aName )
                return None

        def globalsWrite( self, aName, aValue ):
            if aName in self.mGlobalVariables.keys():
                self.mGlobalVariables[ aName ] = aValue
            else:
                GameEngineDebugger.LogE( 'GameEngine.globalsWrite - no object for key ' + aName )

        def globalsWriteNew( self, aName, aValue ):
            self.mGlobalVariables[ aName ] = aValue

        # for working with local variables
        def locals( self, aName ):
            if self.mLocalVariables != None:
                if aName in self.mLocalVariables.keys():
                    return self.mLocalVariables[ aName ]
                else:
                    GameEngineDebugger.LogE( 'GameEngine.locals - no object for key ' + aName )
            else:
                GameEngineDebugger.LogE( 'GameEngine.locals - unknown current event!' )
            return None

        def localsWrite( self, aName, aValue ):
            if self.mLocalVariables != None:
                if aName in self.mLocalVariables.keys():
                    self.mLocalVariables[ aName ] = aValue
                else:
                    GameEngineDebugger.LogE( 'GameEngine.localsWrite - no object for key ' + aName )
            else:
                GameEngineDebugger.LogE( 'GameEngine.localsWrite - unknown current event!' )

        def localsWriteNew( self, aName, aValue ):
            if self.mLocalVariables != None:
                self.mLocalVariables[ aName ] = aValue
            else:
                GameEngineDebugger.LogE( 'GameEngine.localsWriteNew - no object for key ' + aName )

        def setLocals( self, aEventName ):
            if aEventName == None:
                # clear settings
                self.mLocalVariables = None
            else:
                if aEventName not in self.mLocalVariablesBase.keys():
                    self.mLocalVariablesBase[ aEventName ] = {}
                self.mLocalVariables = self.mLocalVariablesBase[ aEventName ]


        # call this in the end of the event
        def finish( self ):
            if self.mCurrentEvent != None:
                self.mCurrentEvent.mIsFinished = True
                self.mCurrentEvent = None
                self.setLocals( None )
            else:
                GameEngineDebugger.LogE( 'GameEngine.finish - unknown current event!' )

# call this with 'call' method
label lblGameEngine_fireStage( aEngine, aPrevScenario = None ):
    $ matchedScenario = aEngine.fireStage( aPrevScenario )
    if matchedScenario:
        # start processing
        call lblGameEngine_init( aEngine, matchedScenario )
        call lblGameEngine_checkCondition( aEngine, matchedScenario )
        $ isPassed = _return
        if isPassed:
            # condition passed - should launch execution
            $ matchedScenario.execute()
        else:
            $ aEngine.setLocals( None )
            call lblGameEngine_fireStage( aEngine, matchedScenario )
    return

label lblGameEngine_init( aEngine, aScenario ):
    $ aScenario.init()
    return

label lblGameEngine_checkCondition( aEngine, aScenario ):
    $ aScenario.check()
    return _return


# call this when you need to end the event (with 'call' method)
label lblGameEngine_finishEvent( aEngine ):
    $ aEngine.finish()
    return


label lblGameEngine_action( aEngine, aActionName ):
    $ aEngine.fireAction( aActionName )
    return