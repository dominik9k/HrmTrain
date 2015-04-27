init -500 python:
    class MenuEngine( store.object ):
        def __init__( self ):
            self.mMenus = {}
            self.mStack = []

        def regMenu( self, aKey, aMenuLabel ):
            self.