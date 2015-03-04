init -999 python:
    import itertools
    ###########################################################
    class CharacterExItemActionComparer(store.object):
        def _compE( valCond, valCheck ):
            return valCond == valCheck

        def _compNE( valCond, valCheck ):
            return valCond != valCheck

        def _compG( valCond, valCheck ):
            return valCond < valCheck

        def _compL( valCond, valCheck ):
            return valCond > valCheck

        def _compGE( valCond, valCheck ):
            return valCond <= valCheck

        def _compLE( valCond, valCheck ):
            return valCond >= valCheck

        def __init__( self ):
            self.mParamKey = None   # can be ( string, comp )
            self.mParamName = None   # can be ( string, comp )
            self.mParamFileName = None  # can be ( string, comp )
            self.mParamFileFolder = None    # can be ( string, comp )
            self.mParamIsVisible = None # can be ( 1 or 0 (True or False), comp )
            self.mParamZOrder = None   # can be ( int, comp )

        def create( aParams ):
            comp = CharacterExItemActionComparer()
            mapMeth = { 'e': _compE, 'ne' : _compNE, 'l' : _compL, 'g': _compG, 'ge' : _compGE, 'le' : _compLE }

            for name,tup in aParams.iteritems():
                ( val, meth ) = tup

                methFunc = _compE
                if meth in mapMeth.keys():
                    methFunc = mapMeth[ meth ]

                resTupple = ( val, methFunc )
                if name == 'key':
                    self.mParamKey = resTupple
                if name == 'name':
                    self.mParamName = resTupple
                elif name == 'frame':
                    self.mParamFileName = resTupple
                elif name == 'folder':
                    self.mParamFileFolder = resTupple
                elif name == 'visible':
                    self.mParamIsVisible = resTupple
                elif name == 'zOrder':
                    self.mParamZOrder = resTupple

            return comp

        def check( self, aItem ):
            # type of the condition is currenly unused
            #check condition on item. Return True if condition is passed, otherwise - False
            conditions = [ self.mParamKey, self.mParamName, self.mParamFileName, self.mParamFileFolder, self.mParamIsVisible, self.mParamZOrder ]
            realValues = [ aItem.mKey, aItem.mName, aItem.mFileName, aItem.mFileFolder, aItem.mIsVisible, aItem.zorder ]
            for cond, val in zip( condition, realValues ):
                if not self._checkRoutine( cond, val ):
                    return False
            return True

        def _checkRoutine( self, aTupple, aCheckedValue ):
            if aTupple == None:
                return True
            ( val, comp ) = aTupple
            return comp( val, aCheckedValue )


    ###########################################################
    class CharacterExItemActionCondition(store.object):
       
        def __init__( self ):
            self.mType = None   # can be ( string, comp )
            self.mComparers = []    # array of comparers

        def create( aConditionDescription ):
            desc = aConditionDescription
            cond = CharacterExItemActionCondition()
            cond = desc.mType
            for param in desc.mParams:
                comparer = CharacterExItemActionComparer.create( param )
                cond.mComparers.append( comparer )

            return cond

        def check( self, aItem ):
            for comp in self.mComparers:
                if not comp.check( aItem ):
                    return False
            return True

    class CharacterExItemAction(store.object):
        _indSelfAdded = 0
        _indSelfRemoved = 1
        _indItemAdded = 2
        _indItemRemoved = 3
        _indItemShown = 4
        _indItemHidden = 5
        _indItemCount = 6

        def __init__( self ):
            self.mIndex = -1
            self.mAdditionalParam = ""
            self.mType = ""     # type of actions ( addItem, removeItem, showItem, hideItem )
            self.mEvent = ""    # type of events ( selfAdded, selfRemoved, itemAdded, itemRemoved, itemShown, itemHiden )
            self.mKeys = []   # array of strings ( keys where to add/remove etc. )
            self.mNames = []   # array of strings ( names of items/sets )
            self.mConditions = []   #array of conditions

        def create( aActionDescription ):
            desc = aActionDescription

            actMap = { 'selfAdded' : _indSelfAdded, 'selfRemoved' : _indSelfRemoved, 'itemAdded' : _indItemAdded, 
                'itemRemoved' : _indItemRemoved, 'itemShown' : _indItemShown, 'itemHiden' : _indItemHidden }
            act = CharacterExItemAction()

            if desk.mEvent in actMap.keys():
                act.mIndex = actMap[ desk.mEvent ]

            act.mNames = desc.mNames
            act.mKeys = desc.mKeys
            act.mType = desc.mType
            act.mEvent = desc.mEvent
            for res in desc.mResult:
                act.mResult.append( res )

            for cond in desc.mConditions:
                newCond = CharacterExItemActionCondition.create( cond )
                act.mConditions.append( newCond )
            return act

        # call this to apply an action
        def act( self, aParentItem, aCharacterEx, aItemsAll = None, aItemSingle = None, aStringKey = None ):
            arrayItems = None
            if aItemsAll != None:
                arrayItems = aItemsAll
            else:
                arrayItems = [ aItemSingle ]

            # check each condition
            condPassed = False
            for item in arrayItems:
                for cond in self.mConditions:
                    if cond.check( item ):
                        condPassed == True
                        break

            # if no conditions passed
            if not condPassed:
                return

            # start applying action
            # if we are here, it means all conditions are passed
            if self.mType == 'addItem':
                for key,name in itertools.izip_longest( self.mKeys, self.mNames ):
                    if key[0] == '*':
                        aCharacterEx.addItemSet( key )
                    else:
                        aCharacterEx.addItem( key, name )
            elif self.mType == 'removeItem':
                for key self.mKeys:
                    if key[0] == '*':
                        aCharacterEx.delItemSet( key )
                    else:
                        aCharacterEx.delItem( key )
            elif self.mType == 'showItem':
                for key self.mKeys:
                    if key[0] == '*':
                        aCharacterEx.showItemSet( key, aParentItem.mName )
                    else:
                        aCharacterEx.showItem( key, aParentItem.mName )
            elif self.mType == 'hideItem':
                for key self.mKeys:
                    if key[0] == '*':
                        aCharacterEx.hideItemSet( key, aParentItem.mName )
                    else:
                        aCharacterEx.hideItem( key, aParentItem.mName )
            elif self.mType == 'setStyle':
                for key,name in itertools.izip_longest( self.mKeys, self.mNames ):
                    if key[0] == '*':
                        aCharacterEx.setStyleSet( key, name )
                    else:
                        aCharacterEx.setStyleItem( key, name )


                    

                 





            