init -800 python:
    import ntpath
    # xml assistant functions
    
    def _getFileNameFromPath( aPath ):
        filename = ntpath.basename( aPath ).encode( "utf-8" )
        splitted = filename.rsplit( '.', 1 )
        return splitted[0]

    def __xmlUpdateItems( aCharacterEx ):
        linkKey = aCharacterEx.mLinkerKey
        keys = aCharacterEx.mItems.keys()
        for key in keys:
            item = aCharacterEx.mItems[ key ]
            if item != None:
                if item.mName != None:
                    if item.mName != "":
                        aCharacterEx.delItem( key )
                        aCharacterEx.addItem( key, item.mName )

        