init -800 python:
    # xml assistant functions
     
    def __xmlUpdateItems( aCharacterEx ):
        linkKey = aCharacterEx.mLinkerKey
        keys = aCharacterEx.mStuff.keys()
        for key in keys:
            item = aCharacterEx.mStuff[ key ]
            if item != None:
                if item.mName != None:
                    if item.mName != "":
                        aCharacterEx.delItem( key )
                        aCharacterEx.addItem( key, item.mName )

        