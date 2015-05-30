init -500 python:
  
    class GlobalVariableStorage( store.object ):
        def __init__( self, aScenarioBase ):
            # dictionary of objects
            self.mGlobalVariables = {}
            # for testing
            self.mGlobalVariables = { 'global_test' : 0 }

        # for working with global variables
        def get( self, aName ):
            if aName in self.mGlobalVariables.keys():
                return self.mGlobalVariables[ aName ]
            else:
                GameEngineDebugger.LogE( 'GlobalVariableStorage.get - no object for key ' + aName )
                return None

        def set( self, aName, aValue ):
            if aName in self.mGlobalVariables.keys():
                self.mGlobalVariables[ aName ] = aValue
            else:
                GameEngineDebugger.LogE( 'GlobalVariableStorage.set - no object for key ' + aName )

        def setNew( self, aName, aValue ):
            self.mGlobalVariables[ aName ] = aValue

        def clean( self ):
            self.mGlobalVariables = {}