init -500 python:
    class GameMenuItem( store.object ):
        def __init__( self, aText, aLabel, aIsActive = True ):
            self.mText = aText
            self.mLabel = aLabel
            self.mIsActive = aIsActive