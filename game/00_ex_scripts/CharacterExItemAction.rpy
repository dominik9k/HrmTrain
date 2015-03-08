init -999 python:
    import itertools
    ###########################################################
    class CharacterExItemActionCondition(store.object):
        def _compE( self, valCond, valCheck ):
            return valCond == valCheck

        def _compNE( self, valCond, valCheck ):
            return valCond != valCheck

        def _compG( self, valCond, valCheck ):
            return valCond < valCheck

        def _compL( self, valCond, valCheck ):
            return valCond > valCheck

        def _compGE( self, valCond, valCheck ):
            return valCond <= valCheck

        def _compLE( self, valCond, valCheck ):
            return valCond >= valCheck

        def _missItemFunc( self, aResult ):
            return not aResult

        def _hasItemFunc( self, aResult ):
            return aResult

        def __init__( self ):
            self.mType = ""     # type of condition. Can be 'hasItem' or 'missItem'
            self.mParamKey = None   # can be ( string, comp )
            self.mParamName = None   # can be ( string, comp )
            self.mParamFileName = None  # can be ( string, comp )
            self.mParamFileFolder = None    # can be ( string, comp )
            self.mParamIsVisible = None # can be ( 1 or 0 (True or False), comp )
            self.mParamZOrder = None   # can be ( int, comp )
            self.mParamStyle = None     # can be ( string, comp )
            # boolean - is this item is the sender of action or not, can be ( 1 or 0 (True or False), comp )
            self.mParamActionItem = None 

        @classmethod
        def create( cls, aConditionDescription ):
            desc = aConditionDescription
            cond = cls()
            mapMeth = { 'e': cond._compE, 'ne' : cond._compNE, 'l' : cond._compL, 'g': cond._compG,
                 'ge' : cond._compGE, 'le' : cond._compLE }

            cond.mType = desc.mType
            for name,tup in desc.mParams.iteritems():
                ( val, meth ) = tup

                methFunc = cond._compE
                if meth in mapMeth.keys():
                    methFunc = mapMeth[ meth ]

                resTupple = ( val, methFunc )
                if name == 'key':
                    cond.mParamKey = resTupple
                if name == 'name':
                    cond.mParamName = resTupple
                elif name == 'frame':
                    cond.mParamFileName = resTupple
                elif name == 'folder':
                    cond.mParamFileFolder = resTupple
                elif name == 'visible':
                    cond.mParamIsVisible = resTupple
                elif name == 'zorder':
                    cond.mParamZOrder = resTupple
                elif name == 'style':
                    cond.mParamStyle = resTupple
                elif name == 'actionItem':
                    cond.mParamActionItem = resTupple

            return cond

        def check( self, aItems, aEventSenderItem ):
            # select result function
            resFunc = None
            if self.mType == 'hasItem':
                resFunc = self._hasItemFunc
            elif self.mType == 'missItem':
                resFunc = self._missItemFunc

            # fail condition if the type is incorrect
            if resFunc == None:
                return False

            for item in aItems:
                if self._checkOne( item, aEventSenderItem ):
                    return resFunc( True )
            return resFunc( False )

        def _checkOne( self, aItem, aEventSenderItem ):
            #check action item - ignore all compare methods
            if self.mParamActionItem != None:
                ( val, comp ) = self.mParamActionItem
                compareRes = ( aItem.mName == aEventSenderItem.mName )
                if compareRes != bool(val):
                    return False

            desired = [ self.mParamKey, self.mParamName, self.mParamFileName,
                         self.mParamFileFolder, self.mParamIsVisible, self.mParamZOrder, self.mParamStyle ]
            real = [ aItem.mKey, aItem.mName, aItem.mFileName,
                         aItem.mFileFolder, aItem.mIsVisible, aItem.zorder, aItem.mActiveStyle ]
            for cond,val in zip( desired, real ):
                if not self._checkRoutine( cond, val ):
                    return False
            return True

        def _checkRoutine( self, aTupple, aCheckedValue ):
            if aTupple == None:
                return True
            ( val, comp ) = aTupple
            return comp( val, aCheckedValue )


    # ###########################################################
    # class CharacterExItemActionCondition(store.object):
       
    #     def __init__( self ):
    #         self.mType = None   # can be ( string, comp )
    #         self.mComparers = []    # array of comparers

    #     @classmethod
    #     def create( cls, aConditionDescription ):
    #         desc = aConditionDescription
    #         cond = cls()
    #         cond.mType = desc.mType
    #         for param in desc.mParams:
    #             comparer = CharacterExItemActionComparer.create( param )
    #             cond.mComparers.append( comparer )
    #         return cond

    #     def check( self, aItems, aEventSenderItem ):
    #         for comp in self.mComparers:
    #             for item in aItems:
    #                 if self.mType == 'hasItem':
    #             for comp in self.mComparers:
    #                 if not comp.check( aItem, aEventSenderItem ):
    #                     return False
    #             return True
    #         elif self.mType == 'missItem':
    #             for comp in self.mComparers:
    #                 if comp.check( aItem, aEventSenderItem ):
    #                     return False
    #             return True

    ###########################################################
    class CharacterExItemActionBlock(store.object):
       
        def __init__( self ):
            self.mConditions = []    # array of blocks

        @classmethod
        def create( cls, aBlockDescription ):
            desc = aBlockDescription
            block = cls()
            for cond in desc.mConditions:
                condition = CharacterExItemActionCondition.create( cond )
                block.mConditions.append( condition )
            return block

        def check( self, aItems, aEventSenderItem ):
            for cond in self.mConditions:
                if not cond.check( aItems, aEventSenderItem ):
                    return False
            return True

    ###########################################################
    class CharacterExItemActionResult(store.object):
        def __init__( self ):
            self.mType = ""     # type of result ( addItem, removeItem, showItem, hideItem )
            self.mKeys = []   # array of strings ( keys where to add/remove etc. )
            self.mNames = []   # array of strings ( names of items/styles )
            self.mSets = []    # array of strings ( names of sets )
            self.mItems = []   # array of strings ( names of items )

        @classmethod
        def create( cls, aResultDescription ):
            desc = aResultDescription
            res = cls()
            res.mType = desc.mType
            for key in desc.mKeys:
                res.mKeys.append( key )
            for name in desc.mNames:
                res.mNames.append( name )
            for theSet in desc.mSets:
                res.mSets.append( theSet )
            for item in desc.mItems:
                res.mItems.append( item )
            return res

        @staticmethod
        def getItemKeyByName( aParentItem, aSearchedItemName ):
            if aParentItem.mOwner != None:
                itemBase = WTXmlLinker.i( aParentItem.mOwner.mLinkerKey )
                return itemBase.getItemKey( aSearchedItemName )
            else:
                return ""

        def apply( self, aCharacterEx, aParentItem ):
            if self.mKeys and self.mNames:
                for key,name in itertools.izip_longest( self.mKeys, self.mNames ):   
                    if key != "":
                        self._applyKeyResults( aParentItem, aCharacterEx, key, name )
                    else:
                        key = CharacterExItemActionResult.getItemKeyByName( aParentItem, name )
                        if key == "":
                            continue
                        self._applyKeyResults( aParentItem, aCharacterEx, key, name )
            elif self.mSets:
                for theSet,name in itertools.izip_longest( self.mSets, self.mNames ):   
                    theSet = "*" + theSet
                    self._applySetResults( aParentItem, aCharacterEx, theSet, name )
            elif self.mItems:
                for item,name in itertools.izip_longest( self.mItems, self.mNames ):   
                    self._applyItemResults( aParentItem, aCharacterEx, item, name )

        def _applySetResults( self, aParentItem, aCharacterEx, aSetName, aName ):
            if self.mType == 'addItem':
                aCharacterEx.addItemSet( aSetName )
            elif self.mType == 'removeItem':
                aCharacterEx.delItemSet( aSetName )
            elif self.mType == 'showItem':
                aCharacterEx.showItemSet( aSetName, aParentItem.mName )
            elif self.mType == 'hideItem':
                aCharacterEx.hideItemSet( aSetName, aParentItem.mName )
            elif self.mType == 'setStyle':
                aCharacterEx.setStyleSet( aSetName, aName )

        def _applyItemResults( self, aParentItem, aCharacterEx, aItemName, aName ):
            if self.mType == 'addItem':
                aCharacterEx.addItem( aItemName )
            elif self.mType == 'removeItem':
                aCharacterEx.delItem( aItemName )
            elif self.mType == 'showItem':
                aCharacterEx.showItem( aItemName, aParentItem.mName )
            elif self.mType == 'hideItem':
                aCharacterEx.hideItem( aItemName, aParentItem.mName )
            elif self.mType == 'setStyle':
                aCharacterEx.setStyleItem( aItemName, aName )

        def _applyKeyResults( self, aParentItem, aCharacterEx, aKey, aName ):
            if self.mType == 'addItem':
                aCharacterEx.addItemKey( aKey, aName )
            elif self.mType == 'removeItem':
                aCharacterEx.delItemKey( aKey )
            elif self.mType == 'showItem':
                aCharacterEx.showItemKey( aKey, aParentItem.mName )
            elif self.mType == 'hideItem':
                aCharacterEx.hideItemKey( aKey, aParentItem.mName )
            elif self.mType == 'setStyle':
                aCharacterEx.setStyleKey( aKey, aName )

    ###########################################################
    class CharacterExItemAction(store.object):
        _indSelfAdded = 0
        _indSelfRemoved = 1
        _indItemAdded = 2
        _indItemRemoved = 3
        _indItemShown = 4
        _indItemHidden = 5
        _indStyleBeforeChange = 6
        _indStyleAfterChange = 7
        _indItemCount = 8

        def __init__( self ):
            self.mIndex = -1
            self.mEvent = ""    # type of events ( selfAdded, selfRemoved, itemAdded, itemRemoved, itemShown, itemHidden )
            self.mBlocks = []   #array of blocks
            self.mResults = []  #array of results

        # checking all conditions
        def _checkBlocks( self, aArrayItems, aEventSenderItem ):
            for block in self.mBlocks:
                if block.check( aArrayItems, aEventSenderItem ):
                    return True
            return False

        @classmethod
        def create( cls, aActionDescription ):
            desc = aActionDescription

            actMap = { 'selfAdded' : CharacterExItemAction._indSelfAdded, 'selfRemoved' : CharacterExItemAction._indSelfRemoved, 
                'itemAdded' : CharacterExItemAction._indItemAdded, 'itemRemoved' : CharacterExItemAction._indItemRemoved,
                'itemShown' : CharacterExItemAction._indItemShown, 'itemHidden' : CharacterExItemAction._indItemHidden,
                'beforeStyleChange' : CharacterExItemAction._indStyleBeforeChange, 'afterStyleChange' : CharacterExItemAction._indStyleAfterChange }
            act = cls()

            if desc.mEvent in actMap.keys():
                act.mIndex = actMap[ desc.mEvent ]

            act.mEvent = desc.mEvent

            for block in desc.mBlocks:
                newBlock = CharacterExItemActionBlock.create( block )
                act.mBlocks.append( newBlock )

            for res in desc.mResults:
                newRes = CharacterExItemActionResult.create( res )
                act.mResults.append( newRes )

            return act

        # call this to apply an action
        def act( self, aParentItem, aEventSenderItem, aCharacterEx, aItemsAllDictionary ):

            # copy references
            arrayItems = list(aItemsAllDictionary.values())
            #add parent item to list only in case of 'selfRemoved' event
            if self.mEvent == 'selfRemoved':
                arrayItems.append( aParentItem )

            # check conditions
            actionActive = self._checkBlocks( arrayItems, aEventSenderItem )

            # if no conditions passed
            if not actionActive:
                return

            # start applying results of action
            # if we are here, it means all conditions are passed
            for res in self.mResults:
                res.apply( aCharacterEx, aParentItem )

            # for key,name in itertools.izip_longest( self.mKeys, self.mNames ):
            #     if key != "":
            #         if key[0] == '*':
            #             self._checkSetActions( aParentItem, aCharacterEx, key, name )
            #         else:
            #             self._checkItemActions( aParentItem, aCharacterEx, key, name )
            #     else:
            #         key = self._getItemKeyByName( self, aParentItem, name )
            #         if key == "":
            #             continue
            #         self._checkItemActions( aParentItem, aCharacterEx, key, name )
                        