label main_ex_CharacterExItem_constants:
    # main zOrders
    define G_Z_UNDERLEGS = 0
    define G_Z_LEGS = 20
    define G_Z_PANTIES = 40
    define G_Z_SKIRT = 60
    define G_Z_HANDS = 80
    define G_Z_BODY = 100
    define G_Z_TITS = 120
    define G_Z_DRESS = 140
    define G_Z_FACE = 300
    
    # additional zOrders
    define G_Z_HEADWEAR = 160
    define G_Z_POSE = 180

    # here is the keys for additional items
    define G_N_SKIRT = 'skirt'
    define G_N_BADGE = 'badge'
    define G_N_NETS = 'nets'
    
    return

init -999 python:

    class CharacterExItem(store.object):
        # some kind of enumerator
        _indSelfAdded = CharacterExItemAction._indSelfAdded
        _indSelfRemoved = CharacterExItemAction._indSelfRemoved
        _indItemAdded = CharacterExItemAction._indItemAdded
        _indItemRemoved = CharacterExItemAction._indItemRemoved
        _indItemShown = CharacterExItemAction._indItemShown
        _indItemHidden = CharacterExItemAction._indItemHidden
        _indItemCount = CharacterExItemAction._indItemCount

        # creates variables
        def _create_vars( self ):
            self.mKey = ""
            self.mName = ""
            self.mIsVisible = True
            self.mFileName = ""
            self.mFileFolder = ""
            self.mStyles = {}
            self.mActiveStyle = None  # name of current active style
            self.mOwner = None # pointer to CharacterExData - container where item is currently assigned

            # public
            self.image = None
            self.zorder = 0
            self.position = Transform( pos = ( 0, 0 ) )            
            # parent of item, should be string key or None. When parent item is hiden, this item also hide, and the same with showing parent
            self.parent = None

            # here is the list of keys to hide with this item
            self.mHideList = []
            
            # stuff for actions
            # self.mActions is an array of arrays
            self.mActions = []
            for num in range( _indItemCount ):
                self._mActions.append( [] )

            # map with transforms
            self.mTransforms = {}

            # here we'll store all items, which affects visibility of this item
            # items, stored here, change the visibility to FALSE
            self.mDirectors = set()

        # old constructor
        def __init__( self, aFolder, aName, aOrder, aParent = None, aPos = None ):
            self._create_vars()

            self.mName = aName
            self.mFileFolder = aFolder
            self.mImage = aFolder + aName
            self.mZOrder = aOrder
            self.mItemPos = Transform( pos = ( 0, 0 ) ) 
            if aPos is not None:
                self.mItemPos = aPos
            # parent of item, should be string key or None. When parent item is hiden, this item also hide, and the same with showing parent
            self.mParent = aParent

            # here is the list of keys to hide with this item
            self.mHideList = []
            self._fillHideList()

        # new constructor
        def __init__( self, aName, aStylesMap ):
            self._create_vars()

            self.mName = aName
            self.mStyles = aStylesMap   # map of styleDescriptions

            # set current style to 'default'
            self.setStyle( 'default' )
            self._fillHideList()

        # static constructor to create from description
        def create( aDescription ):
            item = CharacterExItem( aDescription.mName, aDescription.mStyles )
            return item


        ##########################################################
        # change style method
        ##########################################################        

        def setStyle( self, aStyleName ):
            if aStyleName in self.mStyles.keys():
                if self.mActiveStyle != None:
                    self._discardCurrentStyle()
                self.mActiveStyle = aStyleName
                self._applyStyle( aStyleName )

        def getStyle( self ):
            return self.mActiveStyle

        ##########################################################
        # modify image methods
        ##########################################################
        
        def updateImage( self, aImage ):
            # here we can change image ( for example, make im.Flip action to the image, and save it here )
            self.mImage = aImage
        
        def getImage( self ):
            return self.mImage
            
        ##########################################################
        # show/hide methods
        ##########################################################

        def hide( self, aSource, aKey ):
            prevVis = self.mIsVisible
            self._hideInner( aSource )
            if prevVis != self.mIsVisible:
                self.mOwner._onItemHiden( aKey, self )
                for inKey in self.mHideList:
                    self.mOwner.showItem( inKey, self.mName )
                
        def show( self, aSource, aKey ):
            prevVis = self.mIsVisible            
            self._showInner( aSource )
            if prevVis != self.mIsVisible:
                self.mOwner._onItemShown( aKey, self )
                for inKey in self.mHideList:
                    self.mOwner.hideItem( inKey, self.mName )    

        ##########################################################
        # methods for proper transform work
        ##########################################################

        def addTransform( self, aName, aTransform ):
            if aName in self.mTransforms.keys():
                tr = self.mTransforms[ aName ]
                tr.discard( self.image )
                del self.mTransforms[ aName ]
            self.mTransforms[ aName ] = aTransform
            aTransform.apply( self.image )
                
        def delTransform( self, aName ):
            if aName in self.mTransforms.keys():
                tr = self.mTransforms[ aName ]
                tr.discard( self.image )
                del self.mTransforms[ aName ]

        def clearTransforms( self ):
            keys = self.mTransforms.keys()
            for key in keys:
                self.delTransform( key )

        def getTransform( self, aName ):
            if aName in self.mTransforms.keys():
                return self.mTransforms[ aName ]
            else:
                return None
            
        ##########################################################
        # inner callbacks, do not use them directly
        ##########################################################            

        def onSelfAdded( self, aKey, aItems, aCharacterEx ):
            self.mOwner = aCharacterEx
            self.mKey = aKey
            if self.mParent in aItems:
                if not aItems[ self.mParent ].mIsVisible:
                    self._hideInner( 'parent' )
            self.innerOnSelfAdded( aItems )

        def onSelfRemoved( self, aItems, aCharacterEx ):
            self.innerOnSelfRemoved( aItems )
            self.mOwner = None
        
        def onItemAdded( self, aItem ):
            self.innerOnItemAdded( aItem )
            
        def onItemRemoved( self, aItem ):
            if aItem.mKey == self.mParent:
                self._showInner( 'parent' )
            self.innerOnItemRemoved( aItem )
            
        def onItemHidden( self, aItem ):
            if aItem.mKey == self.mParent:
                self._hideInner( 'parent' )
            self.innerOnItemHidden( aItem )
            
        def onItemShown( self, aItem ):
            if aItem.mKey == self.mParent:
                self._showInner( 'parent' )
            self.innerOnItemShown( aItem )

        ##########################################################
        # methods to forget about them :D
        ##########################################################
        def _hideInner( self, aSource ):
            self.mIsVisible = False
            self.mDirectors.add( aSource )
                
        def _showInner( self, aSource ):
            self.mDirectors.discard( aSource )
            if not self.mDirectors:
                self.mIsVisible = True

        def _applyAction( self, aIndex, aCharacterEx, aItemsAll = None, aItemSingle = None ):
            for action in self.mActions[ aIndex ]:
                action.act( self, aCharacterEx, aItemsAll, aItemSingle )

        def _applyStyle( self, aStyleName ):
            desc = self.mStyles[ aStyleName ]
            self.mFileName = desc.mFrame
            self.mFileFolder = desc.mFileFolder

            self.image = self.mFileFolder + self.mFileName
            self.zorder = desc.mZOrder
            self.position = desc.mShift
            self.parent = desc.mParent
            self.mIsVisible = desc.mIsVisible

            del self.mHideList[:]
            for elem in desc.mHideList:
                self.mHideList.append( elem )
            
            # map with transforms
            self.mTransforms.clear()

            # clear actions
            for elem in self._mActions:
                del elem[:]
            # create new
            for actDesc in desc.mActions:
                actNew = CharacterExItemAction.create( actDesc )
                self._mActions[ actNew.mIndex ] = actNew

            # hide need-to-hide items
            if self.mOwner != None:
                for key in self.mHideList:
                    self.mOwner.hideItem( key, self.mName )

            # here we somehow should check newly added actions
            # ???

        def _discardCurrentStyle( self ):
            self.clearTransforms()
            # show need-to-hide items
            if self.mOwner != None:
                for key in self.mHideList:
                    self.mOwner.showItem( key, self.mName )

        ##########################################################
        # methods to override
        ##########################################################

        def _fillHideList( self ):
            # the easiest way to hide other items by this one - add their keys to the self.mHideList in a way:
            # self.mHideList.append( 'name' )
            None
        
        def innerOnSelfAdded( self, aItems ):
            # this called when THIS item is added to Hermione
            # we can add additional items, needed for this item, to HermioneView
            for key in self.mHideList:
                self.mOwner.hideItem( key, self.mName )
            self._applyAction( _indSelfAdded, self.mOwner, aItems )
            
        def innerOnSelfRemoved( self, aItems ):
            # this called just after deleting SELF from Hermione
            for key in self.mHideList:
                self.mOwner.showItem( key, self.mName )
            self._applyAction( _indSelfRemoved, self.mOwner, aItems )
        
        def innerOnItemAdded( self, aItem ):
            # this called when other new item added to Hermione, and THIS item is existed before it
            # we can add additional items, needed for this item, to HermioneView
            if aItemKey in self.mHideList:
                self.mOwner.hideItem( aItemKey, self.mName )
            self._applyAction( _indItemAdded, self.mOwner, None, aItem )
            
        def innerOnItemRemoved( self, aItem ):
            # this called when other new item added to Hermione, and THIS item is existed before it
            # we can add additional items, needed for this item, to HermioneView
            # item is removed... fuck all!
            #if aItemKey in self.mHideList:
            #    aCharacterEx.showItem( aItemKey, self.mName )
            self._applyAction( _indItemRemoved self.mOwner, None, aItem )

        def innerOnItemHidden( self, aItem ):
            # this called when other item is hidden
            self._applyAction( _indItemHidden, self.mOwner, None, aItem )
            
        def innerOnItemShown( self, aItem ):
            # this called when other item is shown
            self._applyAction( _indItemShown, self.mOwner, None, aItem )
           