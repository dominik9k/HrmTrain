init -999 python:
    import xml.etree.ElementTree as ET
    import re

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

    ###########################################################
    class CharacterExDescriptionTransform(store.object):
        #
        def __init__( self, aElementRoot, aId ):
            self.mId = aId
            self.mName = ""
            self.mParams = {}
            self._read( aElementRoot )

        #
        def _read( self, aElementRoot ):
            for child in aElementRoot:
                if child.tag == 'name':
                    self.mName = child.text
                elif child.tag == 'params':
                    for param in child:
                        self.mParams[ param.tag ] = param.text

    ###########################################################
    class CharacterExDescriptionActionCondition(store.object):
        #
        def __init__( self, aElementRoot, aFolderBase, aOrderBase ):
            self.mType = ""
            self.mParams = {}   # map (string-tupple(value,compare_method))
            # compare methods:
            # e - equal (default)
            # ne - not equal
            # le - lower or equal
            # ge - greater or equal
            # l - lower
            # g - greater
            # ne - not equal
            self._read( aElementRoot, aFolderBase, aOrderBase )

        #
        def _read( self, aElementRoot, aFolderBase, aOrderBase ):
            self.mType = aElementRoot.get('type')
            compPossible = [ 'e', 'ne', 'ge', 'le', 'g', 'l' ]
            for param in aElementRoot:
                compareMeth = param.get('c')
                if compareMeth == None or ( compareMeth not in compPossible ):
                    compareMeth = 'e'
                # we need additional checking for folder and zorder params
                val = param.text
                if param.tag == 'folder':
                    val = aFolderBase.get( val )
                elif param.tag == 'zorder':
                    val = _assistantReadZOrder( val, aOrderBase )
                self.mParams[ param.tag ] = ( val, compareMeth )

    ###########################################################
    class CharacterExDescriptionActionBlock(store.object):
        #
        def __init__( self, aElementRoot, aFolderBase, aOrderBase ):
            self.mConditions = []   # array of condition descriptions
            self._read( aElementRoot, aFolderBase, aOrderBase )

        #
        def _read( self, aElementRoot, aFolderBase, aOrderBase ):
            for child in aElementRoot:
                if child.tag == 'condition':
                    newCond = CharacterExDescriptionActionCondition( child, aFolderBase, aOrderBase )
                    self.mConditions.append( newCond )

    ###########################################################
    class CharacterExDescriptionActionResult(store.object):
        def __init__( self, aElementRoot ):
            self.mType = ""     # type of actions ( addItem, removeItem, showItem, hideItem )
            self.mKeys = []   # array of strings ( keys where to add/remove etc. )
            self.mNames = []   # array of strings ( names of items/styles )
            self.mSets = []    # array of strings ( names of sets )
            self.mItems = []   # array of strings ( names of items )
            self._read( aElementRoot )

        #
        def _read( self, aElementRoot ):
            self.mType = aElementRoot.get('type')
            for child in aElementRoot:
                if child.tag == 'key':
                    if child.text:
                        for key in child.text.split(','):
                            self.mKeys.append( key )
                elif child.tag == 'name':
                    if child.text:
                        for name in child.text.split(','):
                            self.mNames.append( name )
                elif child.tag == 'set':
                    if child.text:
                        for name in child.text.split(','):
                            self.mSets.append( name )
                elif child.tag == 'item':
                    if child.text:
                        for name in child.text.split(','):
                            self.mItems.append( name )

    ###########################################################
    class CharacterExDescriptionAction(store.object):
        #
        def __init__( self, aElementRoot, aFolderBase, aOrderBase ):
            self.mEvent = ""    # type of events ( selfAdded, selfRemoved, itemAdded, itemRemoved, itemShown, itemHidden )
            self.mBlocks = []   # array of block descriptions
            self.mResults = []  # array of result descriptions
            self._read( aElementRoot, aFolderBase, aOrderBase )

        #
        def _read( self, aElementRoot, aFolderBase, aOrderBase ):
            self.mEvent = aElementRoot.get('event')
            for child in aElementRoot:
                if child.tag == 'body':
                    for block in child:
                        self.mBlocks.append( CharacterExDescriptionActionBlock( block, aFolderBase, aOrderBase ) )
                if child.tag == 'result':
                    self.mResults.append( CharacterExDescriptionActionResult( child ) )

    ###########################################################
    class CharacterExDescriptionStyle(store.object):
        #
        def _fillValuesForDefault( self ):
            self.mFrame = ""
            self.mFileFolder = ""
            self.mZOrder = 0
            self.mParent = ""
            self.mIsVisible = True
            self.mShift = Transform( pos = ( 0, 0 ) )
            self.mTransforms = {} # map of transform descriptions
            self.mHideList = [] # array of strings
            self.mActions = []  # array of actions descriptions

        def __init__( self, aElementRoot, aStyleName, aItemName, aIsSubitem, aFolderBase, aOrderBase ):
            self.mName = aItemName
            self.mFrame = None
            self.mFileFolder = None
            self.mZOrder = None
            self.mParent = None
            self.mIsVisible = True
            self.mShift = None
            self.mTransforms = None # map of transform descriptions
            self.mHideList = None # array of strings
            self.mActions = None  # array of actions descriptions
            
            if aStyleName == 'default':
                self._fillValuesForDefault()

            self._read( aElementRoot, aIsSubitem, aFolderBase, aOrderBase )

        # read self from xml
        def _read( self, aElementRoot, aIsSubitem, aFolderBase, aOrderBase ):
            for child in aElementRoot:
                if child.tag == 'frame':
                    self.mFrame = child.text
                elif child.tag == 'folder':
                    self.mFileFolder = aFolderBase.get( child.text )
                elif child.tag == 'zorder':
                    self._readOrder( child, aOrderBase )
                elif child.tag == 'visible':
                    self.mIsVisible = _parseBool( child.text )  #from WTXmlAssitantFunctions
                elif child.tag == 'parent':
                    if not aIsSubitem:
                        self.mParent = child.text
                elif child.tag == 'shift':
                    self._readShift( child )
                elif child.tag == 'transforms':
                    if self.mTransforms == None:
                        self.mTransforms = {}
                    for trSingle in child:
                        trId = trSingle.get('id')
                        self.mTransforms[ trId ] = CharacterExDescriptionTransform( trSingle, trId )

                elif child.tag == 'hidelist':
                    if not aIsSubitem:
                        self._readHideList( child )

                elif child.tag == 'actions':
                    if not aIsSubitem:
                        if self.mActions == None:
                                self.mActions = []
                        for actSingle in child:
                            self.mActions.append( CharacterExDescriptionAction( actSingle, aFolderBase, aOrderBase ) )

        def _readHideList( self, child ):
            if self.mHideList == None:
                self.mHideList = []
            _assistantReadList( child, self.mHideList )

        def _readShift( self, child ):
            if child.text != '':
                posText = child.text
                if posText != None:
                    positions = []
                    for pos in child.text.split( ',' ):
                        positions.append( int( pos ) )
                    self.mShift = Transform( pos = ( positions[0], positions[1] ) )

        def _readOrder( self, child, aOrderBase ):
            self.mZOrder = _assistantReadZOrder( child.text, aOrderBase )

    ###########################################################
    class CharacterExDescriptionItem(store.object):
        #
        def __init__( self, aXmlRoot, aFolderBase, aOrderBase ):
            self.mKey = ""
            self.mName = ""
            self.mIsSubitem = False
            self.mSubitems = []
            self.mStyles = {}
            self._read( aXmlRoot, aFolderBase, aOrderBase )


        # read self from xml
        def _read( self, aXmlRoot, aFolderBase, aOrderBase ):
            # first of all we should read this two items
            for child in aXmlRoot:
                if child.tag == 'key':
                    self.mKey = child.text
                elif child.tag == 'name':
                    self.mName = child.text
                elif child.tag == 'isSubitem':
                    self.mIsSubitem = _parseBool( child.text )  #from WTXmlAssitantFunctions
                elif child.tag == 'subitems':
                    _assistantReadList( child, self.mSubitems )

            # and only then - styles
            for child in aXmlRoot:
                if child.tag == 'style':
                    styleKey = child.get('name')
                    self.mStyles[ styleKey ] = CharacterExDescriptionStyle( child, styleKey, self.mName,
                        self.mIsSubitem, aFolderBase, aOrderBase )
