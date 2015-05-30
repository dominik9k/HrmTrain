init -500 python:
  
    class LocalVariableStorage( store.object ):
        def __init__( self ):
            self.mLocalVariablesBase = {}
            # this is points to dictionary with local variables for current event
            self.mLocalVariables = None
            # for testing
            self.mLocalVariablesBase = { 'event_test': { 'localVar': 0 } }

        # for working with local variables
        def get( self, aName ):
            if self.mLocalVariables != None:
                if aName in self.mLocalVariables.keys():
                    return self.mLocalVariables[ aName ]
                else:
                    GameEngineDebugger.LogE( 'LocalVariableStorage.get - no object for key ' + aName )
            else:
                GameEngineDebugger.LogE( 'LocalVariableStorage.get - local base is not chosen!' )
            return None

        def set( self, aName, aValue ):
            if self.mLocalVariables != None:
                if aName in self.mLocalVariables.keys():
                    self.mLocalVariables[ aName ] = aValue
                else:
                    GameEngineDebugger.LogE( 'LocalVariableStorage.set - no object for key ' + aName )
            else:
                GameEngineDebugger.LogE( 'LocalVariableStorage.set - local base is not chosen!' )

        def setNew( self, aName, aValue ):
            if self.mLocalVariables != None:
                self.mLocalVariables[ aName ] = aValue
            else:
                GameEngineDebugger.LogE( 'LocalVariableStorage.setNew - no object for key ' + aName )

        def choose( self, aEventName ):
            if aEventName == None:
                # clear settings
                self.mLocalVariables = None
            else:
                if aEventName not in self.mLocalVariablesBase.keys():
                    self.mLocalVariablesBase[ aEventName ] = {}
                self.mLocalVariables = self.mLocalVariablesBase[ aEventName ]

        def clean( self ):
            self.mLocalVariables = None
            self.mLocalVariablesBase = {}