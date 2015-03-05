init -998 python:
    from copy import deepcopy 
    class CharacterExData(store.object):
        # constructor - memorizing Character object
        def __init__( self, aItemCreator ):
            # currenlty dressed things
            self.mStuff = {}
            # dictionary with transforms
            self.mTransforms = {}
            # here we'll save all items and global transforms on character
            self.mSavedItems = {}
            self.mSavedTransforms = {}
            # list of all attached views
            self.mViews = []
            # object to create items from description in xml files
            self.mCreator = aItemCreator
           
        ##########################################################
        # methods to save/delete attached views
        ##########################################################

        def getView( self, aIndex = 0 ):
            if aIndex < len( self.mViews ):
                return self.mViews[ aIndex ]
            else:
                return None

        def attachedToView( self, aView ):
            self.mViews.append( aView )

        def detachedFromView( self, aView ):
            if aView in self.mViews:
                self.mViews.remove( aView )

        ##########################################################
        # methods to work with global character transforms
        ##########################################################

        def addTransform( self, aTransform, aKey = 'default' ):
            self.delTransform( aKey )
            self.mTransforms[ aKey ] = aTransform
            #apply transform for all items (even hiden)
            for val in self.mStuff.values():
                val.addTransform( aKey, aTransform )
            
        def delTransform( self, aKey = 'default' ):
            # discard transform for all items
            if aKey in self.mTransforms.keys():
                for val in self.mStuff.values():
                    val.delTransform( aKey )
                del self.mTransforms[ aKey ]
        
        # remove all transforms
        def clearTransforms( self ):
            keyset = self.mTransforms.keys()
            for key in keyest:
                self.delTransform( key )
            self.mTransforms.clear()


        ##########################################################
        # methods to manipulate items of character
        ##########################################################            
        
        # return Item if Hermione get the item with given key, otherwise - None
        def getItem( self, aKey ):
            if aKey in self.mStuff.keys():
                return self.mStuff[ aKey ]
            else:
                return None
                
        # add additional stuff on hermione ( permanent )
        def addItemDirect( self, aKey, aCharacterExItem ):
            self._addItem( aKey, aCharacterExItem )

        # add additional stuff on hermione ( permanent )
        def addItem( self, aKey, aName ):
            newItem = self.mCreator.create( aName )
            if newItem[0] != None:
                self.addItemDirect( aKey, newItem[0] )

        def addItemSet( self, aSetName ):
            self._applyToSet( aSetName, 0 )
        
        # del additional stuff on hermione ( permanent )
        def delItem( self, aKey ):
            self._delItem( aKey )

        def delItemSet( self, aSetName ):
            self._applyToSet( aSetName, 1 )

        # show item on hermione ( make it visible )
        def showItem( self, aKey, aSource = 'game' ):
            if aKey in self.mStuff.keys():
                item = self.mStuff[ aKey ]
                item.show( aSource, aKey )

        # show item set on character
        def showItemSet( self, aSetName, aSource = 'game' ):
            self._applyToSet( aSetName, 2, aSource )

        # hide item on character ( make it invisible )
        def hideItem( self, aKey, aSource = 'game' ):
            if aKey in self.mStuff.keys():
                item = self.mStuff[ aKey ]
                item.hide( aSource, aKey )

        # hide item set on character
        def hideItemSet( self, aSetName, aSource = 'game' ):
            self._applyToSet( aSetName, 3, aSource )

        # set style to item
        def setStyleItem( self, aKey, aStyleName ):
            curItem = self.getItem( aKey )
            if curItem != None:
                curItem.setStyle( aStyleName )

        # set style to all items in set
        def setStyleSet( self, aSetName, aStyleName ):
            self._applyToSet( aSetName, 4, aStyleName )

        # return True, if the item with suck name exists in items on passed position
        def checkItem( self, aKey, aName ):
            if aKey in self.mStuff.keys():
                item = self.mStuff[ aKey ]
                if item.mName == aName:
                    return True
            return False

        # call this to remove all items from character mStuff
        def clear( self ):
            self.mStuff = {}
            
        ##########################################################
        # save/load/clear/copy current item sets
        ##########################################################        
        
        # save current state to variable
        def saveState( self ):
            self.mSavedItems = {}# deepcopy( self.mStuff )
            for key in self.mStuff.keys():
                self.mSavedItems[ key ] = deepcopy( self.mStuff[ key ] )
            self.mSavedTransforms = {}
            for key in self.mTransforms.keys():
                self.mSavedTransforms[ key ] = deepcopy( self.mTransforms[ key ] )

    
        # load saved statet
        def loadState( self ):
            self.mStuff.clear()
            for key in self.mSavedItems.keys():
                self.mStuff[ key ] = deepcopy( self.mSavedItems[ key ] )
            self.mTransforms.clear()
            for key in self.mSavedTransforms.keys():
                self.mTransforms[ key ] = deepcopy( self.mSavedTransforms[ key ] )              

        # clears the state
        def clearState( self ):
            self.mSavedItems = {}
            self.mSavedTransforms = {}

        # call this to copy all items from the other CharacteEx object
        def copyState( self, aCharacterEx ):
            self.mStuff.clear()
            for key in aCharacterEx.mStuff.keys():
                self.mStuff[ key ] = deepcopy( aCharacterEx.mStuff[ key ] )
            self.mTransforms.clear()
            for key in aCharacterEx.mTransforms.keys():
                self.mTransforms[ key ] = deepcopy( aCharacterEx.mTransforms[ key ] )                
            
        ##########################################################
        # methods to add/del important parts of clothes, but you still can use addItem/delItem methods
        ##########################################################
        
        def addLegs( self, aData ):
            self._addItem( 'legs', aData )
        def delLegs( self ):
            self._delItem( 'legs' )
            
        def addHands( self, aData ):
            self._addItem( 'hands', aData )
        def delHands( self ):
            self._delItem( 'hands' )
            
        def addPanties( self, aData ):
            self._addItem( 'panties', aData )
        def delPanties( self ):
            self._delItem( 'panties' )

        def addSkirt( self, aData ):
            self._addItem( 'skirt', aData )
        def delSkirt( self ):
            self._delItem( 'skirt' )
            
        def addBody( self, aData ):
            self._addItem( 'body', aData )
        def delBody( self ):
            self._delItem( 'body' )
            
        def addDress( self, aData ):
            self._addItem( 'dress', aData )
        def delDress( self ):
            self._delItem( 'dress' )
            
        def addTits( self, aData ):
            self._addItem( 'tits', aData )
        def delTits( self ):
            self._delItem( 'tits' )
            
        def addPose( self, aData ):
            self._addItem( 'pose', aData )
        def delPose( self ):
            self._delItem( 'pose' )
        
        def addFace( self, aData ):
            self._addItem( 'face', aData )
        def delFace( self ):
            self._delItem( 'face' )
        
        ##########################################################
        # DO NOT CALL CALL THESE METHODS FROM THE OUTER CODE! ONLY FROM THE CLASS, THEY'RE INNER!
        ##########################################################        

        def _addItem( self, aName, aData ):
            self._delItem( aName )
            aData.onSelfAdded( aName, self.mStuff, self )
            self.mStuff[ aName ] = aData
            for item in self.mStuff.values():
                if item != aData:
                    item.onItemAdded( aData )
            # apply current transforms
            for key,val in self.mTransforms.iteritems():
                aData.addTransform( key, val )

        def _delItem( self, aName ):
            if aName in self.mStuff.keys():
                data = self.mStuff[ aName ]
                del self.mStuff[ aName ]
                data.onSelfRemoved( self.mStuff, self )
                for item in self.mStuff.values():
                    item.onItemRemoved( data )
                
        def _onItemHiden( self, aItem ):
            for item in self.mStuff.values():
                item.onItemHidden( aItem )  
            
        def _onItemShown( self, aItem ):
            for item in self.mStuff.values():
                item.onItemShown( aItem )  

        # aWhatToDo == 0 - add, 1 - remove, 2 - show, 3 - hide, 4 - style
        def _applyToSet( self, aSetName, aWhatToDo, aStringParam = None ):
            if aSetName[0] != '*':
                aSetName = '*' + aSetName
            setDesc = self.mCreator.mSetBase.getInfo( aSetName )
            if setDesc == None:
                return
            if aWhatToDo == 0:
                setItems = self.mCreator.create( aSetName )
                for item in setItems:
                    if item != None:
                        self.addItemDirect( item.mKey, item )
            elif aWhatToDo == 1:
                for key,name in zip( setDesc.mKeys, setDesc.mNames ):
                    if key != None:
                        curItem = self.getItem( key )
                        if curItem != None:
                            if curItem.mName == name:
                                self.delItem( key )
            elif aWhatToDo == 2:
                for key,name in zip( setDesc.mKeys, setDesc.mNames ):
                    if key != None:
                        curItem = self.getItem( key )
                        if curItem != None:
                            if curItem.mName == name:
                                self.showItem( key, aStringParam )
            elif aWhatToDo == 3:
                for key,name in zip( setDesc.mKeys, setDesc.mNames ):
                    if key != None:
                        curItem = self.getItem( key )
                        if curItem != None:
                            if curItem.mName == name:
                                self.hideItem( key, aStringParam )
            elif aWhatToDo == 4:
                for key,name in zip( setDesc.mKeys, setDesc.mNames ):
                    if key != None:
                        curItem = self.getItem( key )
                        if curItem != None:
                            if curItem.mName == name:
                                curItem.setStyle( aStringParam )

