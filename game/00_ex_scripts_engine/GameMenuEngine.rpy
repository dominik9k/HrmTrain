init -500 python:
    class GameMenuEngine( store.object ):
        def __init__( self ):
            self.mStorage = {}
            # for tests
            men = GameMenu()
            menItem = GameMenuItem( 'test', 'test_label' )
            men.addItem( menItem )
            self.regMenu( 'bird_text', men )

        def pushMenu( self, aKey, aMenu ):
            curPlace = None
            if aKey in self.mStorage.keys():
                curPlace = self.mStorage[ aKey ]
            else:
                curPlace = []
                self.mStorage[ aKey ] = curPlace
            curPlace.insert( 0, aMenu )

        def popMenu( self, aKey ):
            curPlace = None
            if aKey in self.mStorage.keys():
                curPlace = self.mStorage[ aKey ]
                del curPlace[0]

        def get( self, aKey ):
            if aKey in self.mStorage.keys():
                return self.mStorage[ aKey ]
            return None

        def show( self, aKey ):
            menu = self.get( aKey )
            if menu:
                menu.show( aKey )
