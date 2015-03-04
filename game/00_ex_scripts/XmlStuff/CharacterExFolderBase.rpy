init -998 python:
    import xml.etree.ElementTree as ET

    class CharacterExFolderBase:
        # constructor
        def __init__( self ):
           self.mSynonyms = {}

        # this should be called at the beginning of the game, path is the location of folders.xml file
        def read( aFolderFilePath ):
            opened = ET.parse( renpy.loader.transfn( aFolderFilePath ) )
            root = opened.getroot()
            
            for child in root:
                key = child.get('name')
                path = child.text
                if not path.endswith( '/' ):
                    path += '/'
                self.mSynonyms[ key ] = path

        # aValue should be string
        def get( aValue ):
            if aValue in self.mSynonyms.keys():
                return self.mSynonyms[ aValue ]
            else:
                return aValue
