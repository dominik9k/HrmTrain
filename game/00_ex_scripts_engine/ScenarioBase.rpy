init -500 python:
    import xml.etree.ElementTree as ET

    class ScenarioBase:
        def __init__( self, aScenarioFilePath ):
            self.mScenarioFilePath = aScenarioFilePath
            self.mScenarios = []
            self._read()

        def _read( self ):
            f = renpy.file( self.mScenarioFilePath )
            opened = ET.parse( f )
            root = opened.getroot()
            for child in root:
                if child.tag == 'act':
                    newSc = ScenarioData()
                    newSc.read( child )
                    self.mScenarios.append( newSc )