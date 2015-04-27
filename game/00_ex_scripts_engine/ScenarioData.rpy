init -500 python:
    import xml.etree.ElementTree as ET

    class ScenarioData:
        def __init__( self ):
            self.mName = None
            #
            self.mStage = None
            self.mLabelInit = None
            self.mLabelCondition = None
            self.mLabelExecute = None
            self.mLabelActions = None
            # flags
            self.mIsFinished = False
            self.mIsInited = False

        def read( self, aElementRoot ):
            for child in aElementRoot:
                if child.tag == 'stage':
                    self.mStage = child.text
                elif child.tag == 'init':
                    self.mLabelInit = child.text
                elif child.tag == 'condition':
                    self.mLabelCondition = child.text
                elif child.tag == 'execute':
                    self.mLabelExecute = child.text
                elif child.tag == 'actions':
                    self.mLabelActions = child.text
                elif child.tag == 'name':
                    self.mName = child.text

        def isStage( self, aStage ):
            return self.mStage == aStage

        def init( self ):
            if not self.mIsInited:
                self.mIsInited = True
                if self.mLabelInit:
                    renpy.call( self.mLabelInit )
                # do not write enything below - it will be ignored

        def check( self ):
            if self.mLabelCondition:
                renpy.call( self.mLabelCondition )
            # do not write enything below - it will be ignored

        def execute( self ):
            renpy.call( self.mLabelExecute )
            # do not write enything below - it will be ignored

        def action( self, aActionName ):
            renpy.call( self.mLabelActions, aActionName )
            # do not write enything below - it will be ignored

        def finish( self ):
            self.mIsFinished = True

        def isFinished( self ):
            return self.mIsFinished

        def name( self ):
            if self.mName:
                return self.mName
            else:
                return self.mLabelExecute
