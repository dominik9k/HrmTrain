init -998 python:
    import xml.etree.ElementTree as ET

    class CharacterExOrderBase:
        # constructor
        def __init__( self ):
           self.mSynonyms = {}

        # this should be called at the beginning of the game, path is the location of zorders.xml file
        def read( self, aOrderFilePath ):
            opened = ET.parse( renpy.loader.transfn( aOrderFilePath ) )
            root = opened.getroot()
            
            for child in root:
                key = child.get('name')
                self.mSynonyms[ key ] = int( child.text )

        # aValue should be string-key or int-value
        def get( self, aValue ):
            if aValue in self.mSynonyms.keys():
                return self.mSynonyms[ aValue ]
            else:
                return int( aValue )
