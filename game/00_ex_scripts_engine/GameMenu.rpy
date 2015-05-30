init -500 python:
    class GameMenu( store.object ):
        def __init__( self ):
            self.mChoises = []

        def addItem( self, aMenuItem ):
            self.mChoises.append( aMenuItem )

        def show( self, aCode ):
            self._showMenuInner( aCode )


        def _showMenuInner( self, aCode ):
            # here we conver from this menu class to class_RunMenu
            convertor = RunMenu()
            for choise in self.mChoises:
                convertor.AddItem( choise.mText, choise.mLabel, choise.mIsActive, 'stub' )
            $ choose.Show( "after_cam")


label GameMenu_ExitLabel():
    return