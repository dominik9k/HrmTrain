init -999 python:
    import xml.etree.ElementTree as ET

    class CharacterExItemBase:
        # constructor
        def __init__( self ):
           self.mItems = {} # map of ( name, item_description )

        # this should be called at the beginning of the game, path is the location of zorders.xml file
        def read( self, aStartPath, aFolderBase, aZOrderBase ):
            fileList = renpy.list_files()
            for item in fileList:
                if item.endswith( '.hxml' ):
                    if item.startswith( aStartPath ):
                        # we found needed item!
                        self._readFile( item, aFolderBase, aZOrderBase )

        def _readFile( self, aFilePath, aFolderBase, aZOrderBase ):
            opened = ET.parse( renpy.loader.transfn( aFilePath ) )
            root = opened.getroot()
            itemDesc = CharacterExDescriptionItem( root, aFolderBase, aZOrderBase )
            self.mItems[ itemDesc.mName ] = itemDesc

        # return ItemDesctiption or None
        # remember to NOT CHANGE the obtained descriptions
        def get( self, aItemName ):
            if aItemName in self.mItems.keys():
                return self.mItems[ aItemName ]
            else:
                return None
