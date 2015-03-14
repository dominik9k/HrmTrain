init -800 python:
    import ntpath
    # xml assistant functions
    
    def _parseBool( aString ):
        # only this 3 values is equal to True, all other - False
        return aString in [ '1', 'true', 'True' ]

    def _getFileNameFromPath( aPath ):
        filename = ntpath.basename( aPath ).encode( "utf-8" )
        splitted = filename.rsplit( '.', 1 )
        return splitted[0]

    def _assistantReadZOrder( aOrderString, aOrderBase ):
        txt = aOrderString
        tokens = []
        operators = []
        prevPos = 0
        for ind in range( len( txt ) ):
            if txt[ind] == '+' or txt[ind] == '-' or txt[ind] == '*' or txt[ind] == '/':
                param = txt[prevPos:ind]
                prevPos = ind + 1
                tokens.append( param )
                operators.append( txt[ind] )
        if prevPos != 0 and prevPos < len( txt ):
            param = txt[prevPos:len(txt)]
            tokens.append( param )
        if not tokens:
            return aOrderBase.get( txt )
        else:
            # this will change type to int
            for ind in range( len( tokens ) ):
                tokens[ind] = aOrderBase.get( tokens[ind] )
            res = tokens[0]
            tokInd = 1
            # very simple calculator, without prioritising multiplication over addition and so on
            # just do operations one after another
            for op in operators:
                nextVal = tokens[tokInd]
                if op == '+':
                    res += nextVal
                elif op == '-':
                    res -= nextVal
                elif op == '*':
                    res *= nextVal
                elif op == '/':
                    res //= nextVal
                tokInd += 1
            return res

    def _assistantReadList( aChild, aListToRead ):
            itemList = list( aChild )
            if not itemList:
                aListToRead.append( aChild.text )
            else:    
                for hideItem in itemList:
                    aListToRead.append( hideItem.text )

    def __xmlUpdateItems( aCharacterEx ):
        linkKey = aCharacterEx.mLinkerKey
        keys = aCharacterEx.mItems.keys()
        for key in keys:
            item = aCharacterEx.mItems[ key ]
            if item != None:
                if item.mName:
                    aCharacterEx.delItemKey( key )
                    aCharacterEx.addItemKey( key, item.mName )
        