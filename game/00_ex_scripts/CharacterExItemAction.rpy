init -999 python:
    import itertools

    ###########################################################
    class CharacterExItemActionBlock(store.object):
       
        def __init__( self ):
            self.mConditions = []    # array of ICharacterExItemActionCondition

        @classmethod
        def create( cls, aBlockDescription ):
            desc = aBlockDescription
            block = cls()
            for cond in desc.mConditions:
                condition = CharacterExItemActionConditionFactory.create( cond )
                block.mConditions.append( condition )
            return block

        def check( self, aItems, aEventSenderItem, isNeedPassedItems ):
            passedItems = []
            for cond in self.mConditions:
                ( res, passed ) = cond.check( aItems, aEventSenderItem, isNeedPassedItems )
                if not res:
                    return ( False, passedItems )
                elif passed != None:
                    passedItems.extend( passed )

            if not passedItems:
                passedItems = None
            return ( True, passedItems )

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
            self.mBadResults = []   #array of bad results. Bad results are applied if NO blocks passed

        # checking all conditions
        def _checkBlocks( self, aArrayItems, aEventSenderItem, isNeedPassedItems ):
            for block in self.mBlocks:
                ( res, passed ) = block.check( aArrayItems, aEventSenderItem, isNeedPassedItems )
                if res:
                    return ( True, passed )
            return ( False, None )

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
                newRes = CharacterExItemActionResultFactory.create( res )
                act.mResults.append( newRes )

            for badRes in desc.mBadResults:
                newBadRes = CharacterExItemActionResultFactory.create( badRes )
                act.mBadResults.append( newBadRes )

            return act

        # call this to apply an action
        def act( self, aParentItem, aEventSenderItem, aCharacterEx, aItemsAllDictionary ):

            # copy references
            arrayItems = list(aItemsAllDictionary.values())
            #add parent item to list only in case of 'selfRemoved' event
            if self.mEvent == 'selfRemoved':
                arrayItems.append( aParentItem )

            isNeedPassedItems = False
            for res in self.mResults:
                isNeedPassedItems = isNeedPassedItems or res.isNeedPassedItems()
            for res in self.mBadResults:
                isNeedPassedItems = isNeedPassedItems or res.isNeedPassedItems()

            # check conditions
            ( actionActive, arrPassedItems ) = self._checkBlocks( arrayItems, aEventSenderItem, isNeedPassedItems )

            if actionActive:
                # start applying results of action
                # if we are here, it means all conditions are passed
                for res in self.mResults:
                    res.apply( aCharacterEx, aParentItem, arrPassedItems )
            else:
                for badRes in self.mBadResults:
                    badRes.apply( aCharacterEx, aParentItem, arrayItems )
