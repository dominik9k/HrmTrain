init -997 python:


  
# Класс - персона
    class Person(Entry):
    
        current = None
        wrd_menu_screen = "person_wrd_menu"
        wrd_menu_main_screen = "person_wrd_menu_main"
    
        # constructor 
        def __init__( self, Name, caption, charData=None, defVals=None, constVals=None):
        
            if constVals==None:
                constVals={"caption": caption}
            else:
                constVals.update({"caption": caption})                

            if defVals==None:
                defVals={"liking":0, "whoring":0, "talkTime":0, "giftTime":0, "wrd_choice":None, "wrd_block":None, "wrd_new_len":0, "wrd_set_upshirt":False,
                        "wrd_set_upskirt":False, "wrd_set_downpanties":False, "wrd_set_noshirt":False, "wrd_upshirt":False, "wrd_upskirt":False, 
                        "wrd_downpanties":False, "wrd_noshirt":False, "wrd_sperm_dried":False, "wrd_hair_set":False, "wrd_spermpanties":False }
            else:
                defVals.update({"liking":0, "whoring":0, "talkTime":0, "wrd_choice":None, "wrd_block":None, "wrd_new_len":0, "wrd_set_upshirt":False,
                        "wrd_set_upskirt":False, "wrd_set_downpanties":False, "wrd_set_noshirt":False, "wrd_upshirt":False, "wrd_upskirt":False, 
                        "wrd_downpanties":False, "wrd_noshirt":False, "wrd_sperm_dried":False, "wrd_hair_set":False, "wrd_spermpanties":False })

# Инициализация объектов тела и головы
            if charData!=None:
                charData.clearState()
                defVals.update({"vData": charData, 
                    "body": CharacterExView( 5, 
                        Character(caption, color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed"), "body"+Name ), 
                    "head": CharacterExView( 8, 
                        Character(caption, color="#402313", window_right_padding=220, show_two_window=True, ctc="ctc3", ctc_position="fixed"), "head"+Name )
                    })

                defVals["body"].attach( charData )
                defVals["head"].pushScreenTag( 'head' )
                defVals["head"].attach( charData )
                defVals["body"].data().addItemSet( Name+'_body' )
                defVals["body"].data().addItemSet( Name+'_start_clothes' )

            defVals.update({"curchar": None, "talkingView": "body", "Visible": False})

            super(Person, self).__init__(Name=Name, Type="Person", defVals=defVals, constVals=constVals )

            self.Items=RegEntry(ItemCollection("items"+Name))        # Коллекция ивентов
            self.chibi=RegEntry(Chibi("chibi"+Name))                # Чибик
            
            self.Wrd_new=RegEntry(ItemCollection("wrd_new"+Name))
            self.Wrd_adm=RegEntry(ItemCollection("wrd_adm"+Name))
            self.Wrd_wear=RegEntry(ItemCollection("wrd_wear"+Name))
            self.Wrd_set=RegEntry(ItemCollection("wrd_set"+Name))
            self.Wrd_adm_tmp=RegEntry(ItemCollection("wrd_adm_tmp"+Name))

            return


        def __call__( self, arg1, arg2=None, arg3=None, arg4=None, arg5=None, arg6=None, arg7=None, arg8=None, arg9=None, arg10=None, 
                        arg11=None, arg12=None, arg13=None, arg14=None, arg15=None, arg16=None, arg17=None, arg18=None, arg19=None, 
                        arg20=None, arg21=None, arg22=None, arg23=None, arg24=None):
            self.__args=[]
# Разбираем исходный массив на элементы. На вход могут подаваться строки или Character             
            for o in [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23, arg24]:
                if o==None:
                    break
                if isinstance( o, ADVCharacter ): # Если ADVCharacter, то добавляем в массив
                    self.__args.append(o)
                else: # Иначе - разбираем на подстроки
                    debug.SaveString("o: "+str(o), 3)
                    for p in o.split("//"):
                        debug.SaveString("p: "+str(p), 3)
                        if p!=None:
                            if p.strip()!=None:
                                self.__args.append(p.strip(" "))
                                debug.SaveString("p.strip: "+str(p.strip(" ")), 3)

# Разобрано, начинаем отображать

# Если было не видимо - показать
            self.__trans=None #d3
            if not self.GetValue("Visible"):
                self.Visibility(self._talkingView, True, self.__trans)
# Если аргументы закончились - прервать                
            for o in self.__args:
                if (o==None) or (o==""):
                    break
                if not isinstance( o, basestring ): # если не строка, значит Character
                    self.curchar=o
                else: # теперь столько строки
                    if o[0]=="~": # если это фейс, то показать его
                        self.Face(o.replace("~",""))    
                    else:
# Если это герой, то скрыть всех персонажей, для которых не указано отбражаться при реплике героя                        
                        if self.Name=="hero": 
                            for p in GetEntriesByType("Person"):
                                if p.Name not in {"hero"}:
                                    if p.GetValue("Visible"):
                                        p.Visibility(p._talkingView, False, None)
#                                    if "body+" not in p._talkingView:
#                                        p.body.hideQ()
#                                        p.SetValue("Visible", False)
#                                    if "head+" not in p._talkingView:
#                                        p.head.hideQ()
#                                        p.SetValue("Visible", False)
                        renpy.say(self.curchar, StringFormat(o))
            return self

# Смена лица персонажа
        def Face(self, s):
# Если есть пробелы - значит это набор стилей бровей, глаз, щек и рта через пробел
# Если нет пробелов - значит название стиля лица
# Если есть точка - значит это имя файла
            if not " " in s:
                if "." in s:
                    self.body.addFaceName( s )
                else:
                    self.body.data().setStyleKey( "face", "face_"+s )
            else:

                self.__temp=s.split(" ")
                for i in range(4):
                    self.body.data().setStyleKey( ['brows', 'eyes', 'blush', 'mouth'][i], ['brows', 'eyes', 'blush', 'mouth'][i]+"_"+self.__temp[i] )

            return

        def Answer(self, pers): # Для конструкций типа   $hero("...").Answer(hermi("...")) - не факт, что будет удобно
            return self


        def ItemSetsCustomize(self, sets, isClear=True): 
            if isClear:
                self.data.mItems.clear() # Удалить все итемы
            for o in sets:
                self.body.data().addItemSet( self.Name+'_'+o )
            return self

        def ItemsCustomize(self, update=None, delete=None): # chibi=None): 
            if delete!=None:
                for o in delete:
                    self.data.delItem( 'item_'+o )

            if update!=None:
                for o in update:
                    oo=o.split(":")
                    self.data.addItem('item_'+oo[0], "default" if len(oo)==1 else oo[0]+"_"+oo[1])

#            if chibi!=None:
#                self.chibi.appearance=chibi

            return self


        def LoadDefItemSets(self): # Пригодилось только один раз - когда изначально подгрузился неправильный набор сетов, перегрузить его в процесс игры
            self.ItemSetsCustomize({"body", "start_clothes"}, True)
#            self.body.data().addItemSet( self.Name+'_body' )
#            self.body.data().addItemSet( self.Name+'_start_clothes' )
            return
                
        def WrdAdd (self, Name = None, Block = None, Type = "new") :
        
            if Name != None and Block in ["gears_shirt","gears_skirt","gears_other","gears_stockings","gears_hair","gears_panties"] :
                if Type == "new" and self.Wrd_new.Count(Name) <= 0 :
                    self.Wrd_new.AddItem(Name)
                    self.Wrd_new.SetBlock(Name,Block)
                elif Type == "adm" and self.Wrd_adm.Count(Name) <= 0 :
                    self.Wrd_adm.AddItem(Name)
                    self.Wrd_adm.SetBlock(Name,Block)
                elif Type == "wear" and self.Wrd_wear.Count(Name) <= 0 :
                    self.Wrd_wear.AddItem(Name)
                    self.Wrd_wear.SetBlock(Name,Block)
                elif Type == "set" and self.Wrd_set.Count(Name) <= 0 :
                    self.Wrd_set.AddItem(Name)
                    self.Wrd_set.SetBlock(Name,Block)
                    
                if self.Items.Count(Name) < 1:
                    self.Items.AddItem (Name,1)
                    self.Items.SetBlock (Name,Block)
                    
        def WrdRem (self, Name = None, Type = "new") :
            block = self.Items.GetBlock(Name)

            if Name != None and block in ["gears_shirt","gears_skirt","gears_other","gears_stockings","gears_hair","gears_panties"] :
 
                if Type == "new" :
                    self.Wrd_new.AddItem(Name,-1)

                elif Type == "adm" :
                    self.Wrd_adm.AddItem(Name,-1)
                    
                elif Type == "wear" :
                    self.Wrd_wear.AddItem(Name,-1)
                    
                elif Type == "set" :
                    self.Wrd_set.AddItem(Name,-1)
                
        def WrdInit (self) :
            self.WrdAdd("dress","gears_shirt","adm")
            self.WrdAdd("dress","gears_shirt","wear")
            self.WrdAdd("dress","gears_shirt","set")
            self.WrdAdd("skirt","gears_skirt","adm")
            self.WrdAdd("skirt","gears_skirt","wear")
            self.WrdAdd("skirt","gears_skirt","set")
            self.WrdAdd("hair_basic","gears_hair","adm")
            self.WrdAdd("hair_basic","gears_hair","wear")
            self.WrdAdd("hair_basic","gears_hair","set")
            self.WrdAdd("panties","gears_panties","adm")
            self.WrdAdd("panties","gears_panties","wear")
            self.WrdAdd("panties","gears_panties","set")            
            
            if self.Name == "hermione" :
                self.WrdAdd("standart2","gears_shirt","new")
            
#                self.WrdAdd("hair_ponytail_brown","gears_hair","adm")
#                self.WrdAdd("hair_updo_black","gears_hair","adm")
#                self.WrdAdd("hair_updo_brown","gears_hair","adm")
#                self.WrdAdd("hair_wacky_black","gears_hair","adm")
#                self.WrdAdd("hair_wacky_blonde","gears_hair","adm")
#                self.WrdAdd("hair_wacky_red","gears_hair","adm")
                self.WrdAdd("hair_wavy_black","gears_hair","adm")
                self.WrdAdd("hair_wavy_blonde","gears_hair","adm")
#                self.WrdAdd("hair_wavy_combed_brown","gears_hair","adm")
                self.WrdAdd("hair_wavy_red","gears_hair","adm")

            
            self.wrd_set_upshirt = False
            self.wrd_set_upskirt = False
            self.wrd_set_downpanties = False
            self.wrd_set_noshirt = False
            
            self.WrdSetMain()
                
        def WrdDelShirt (self) :   
            for o in self.Wrd_wear() :
                if self.Items.GetBlock(o.Name) == "gears_shirt" :
                    self.Wrd_wear.AddItem(o.Name,-1)

            self.wrd_upshirt = False
        
        def WrdDelSkirt (self) :   
            for o in self.Wrd_wear() :
                if self.Items.GetBlock(o.Name) == "gears_skirt" :
                    self.Wrd_wear.AddItem(o.Name,-1)
                    
            self.wrd_upskirt = False
        
        def WrdDelOther (self) :   
            for o in self.Wrd_wear() :
                if self.Items.GetBlock(o.Name) == "gears_other" :
                    self.Wrd_wear.AddItem(o.Name,-1)                
        
        def WrdDelStockings (self) :   
            for o in self.Wrd_wear() :
                if self.Items.GetBlock(o.Name) == "gears_stockings" :
                    self.Wrd_wear.AddItem(o.Name,-1)              
        
        def WrdDelHair (self) :   
            for o in self.Wrd_wear() :
                if self.Items.GetBlock(o.Name) == "gears_hair" :
                    self.Wrd_wear.AddItem(o.Name,-1)   
                    
        def WrdDelPanties (self) :   
            for o in self.Wrd_wear() :
                if self.Items.GetBlock(o.Name) == "gears_panties" :
                    self.Wrd_wear.AddItem(o.Name,-1)  
                    
        def WrdDelBlock (self, Block = None) :
            if Block == "gears_shirt" :
                self.WrdDelShirt()
            elif Block == "gears_skirt" :
                self.WrdDelSkirt()
            elif Block == "gears_other" :
                self.WrdDelOther()
            elif Block == "gears_stockings" :
                self.WrdDelStockings()
            elif Block == "gears_hair" :
                self.WrdDelHair()
            elif Block == "gears_panties" :
                self.WrdDelHair()
                
        def WrdSetDelShirt (self) :   
            for o in self.Wrd_set() :
                if self.Items.GetBlock(o.Name) == "gears_shirt" :
                    self.Wrd_set.AddItem(o.Name,-1)

            self.wrd_set_upshirt = False
        
        def WrdSetDelSkirt (self) :   
            for o in self.Wrd_set() :
                if self.Items.GetBlock(o.Name) == "gears_skirt" :
                    self.Wrd_set.AddItem(o.Name,-1)
                    
            self.wrd_set_upskirt = False
        
        def WrdSetDelOther (self) :   
            for o in self.Wrd_set() :
                if self.Items.GetBlock(o.Name) == "gears_other" :
                    self.Wrd_set.AddItem(o.Name,-1)                
        
        def WrdSetDelStockings (self) :   
            for o in self.Wrd_set() :
                if self.Items.GetBlock(o.Name) == "gears_stockings" :
                    self.Wrd_set.AddItem(o.Name,-1)                
        
        def WrdSetDelHair (self) :   
            for o in self.Wrd_set() :
                if self.Items.GetBlock(o.Name) == "gears_hair" :
                    self.Wrd_set.AddItem(o.Name,-1)                 
        
        def WrdSetDelPanties (self) :   
            for o in self.Wrd_set() :
                if self.Items.GetBlock(o.Name) == "gears_panties" :
                    self.Wrd_set.AddItem(o.Name,-1)                        
                    
        def WrdSetDelBlock (self, Block = None) :
            if Block == "gears_shirt" :
                self.WrdSetDelShirt()
            elif Block == "gears_skirt" :
                self.WrdSetDelSkirt()
            elif Block == "gears_other" :
                self.WrdSetDelOther()
            elif Block == "gears_stockings" :
                self.WrdSetDelStockings()
            elif Block == "gears_hair" :
                self.WrdSetDelHair()
            elif Block == "gears_panties" :
                self.WrdSetDelPanties()

                
        def WrdIsAdm (self, Name = None) :
            if Name != None and self.Wrd_adm.Count(Name) > 0 :
                return True
            
            return False
            
        def WrdIsWear (self, Name = None) :
            if Name != None and self.Wrd_wear.Count(Name) > 0 :
                return True
            
            return False
                
        def WrdMain (self) :
            self.data.mItems.clear() # Удалить все итемы
            self.body.data().addItemSet( self.Name+'_body' )
            self.body.data().addItem( 'item_tits' )
            self.body.data().addItem( 'item_tits_no' )
 
            for o in self.Wrd_wear():
                if self.Items.GetBlock(o.Name) == "gears_other" :
                    if self.wrd_upshirt == False and self.wrd_noshirt == False :
                        self.body.data().addItem("item_" + o.Name)
                elif self.Items.GetBlock(o.Name) == "gears_shirt" :
                    if self.wrd_upshirt == True :
                        self.body.data().addItem("item_pose_up_" + o.Name)
                    else :
                        self.body.data().addItem("item_" + o.Name)
                elif self.Items.GetBlock(o.Name) == "gears_skirt" :
                    if self.wrd_upskirt == True :
                        self.body.data().addItem("item_pose_lifted_" + o.Name)
                    else :
                        self.body.data().addItem("item_" + o.Name)
                elif self.Items.GetBlock(o.Name) == "gears_stockings" :
                    self.body.data().addItem("item_" + o.Name)
                elif self.Items.GetBlock(o.Name) == "gears_hair" :
                    self.body.data().addItem("item_" + o.Name)
                elif self.Items.GetBlock(o.Name) == "gears_panties" and self.whoring < 12 and not self.wrd_spermpanties :
                    self.body.data().addItem("item_" + o.Name)

            if self.wrd_sperm_dried :
                self.body.data().setStyleAll('sperm_dried')
                
            if self.wrd_upskirt :
                self.body.data().setStyleAll('with_lifted_skirt')
   
            if self.wrd_spermpanties :
                self.body.data().addItem("item_panties")
                self.body.data().addItem("item_panties_sperm")

            
            return self
            
        def WrdSetMain (self) :
            
            self.wrd_upshirt = self.wrd_set_upshirt
            self.wrd_upskirt = self.wrd_set_upskirt
            self.wrd_downpanties = self.wrd_set_downpanties
            self.wrd_noshirt = self.wrd_set_noshirt
            self.wrd_sperm_dried = False
            self.wrd_spermpanties = False
            
            self.Wrd_wear.Clear()
            for i in self.Wrd_set() :
                self.Wrd_wear.AddItem(i.Name,1)
                self.Wrd_wear.SetBlock(i.Name,self.Items.GetBlock(i.Name))

            self.WrdMain()
            return self
            
        def WrdSetMainBL (self, Face="body_01.png") :
    
            screens.Show(Dissolve(1), "blkfade") #Completely black screen.

            self.WrdSetMain()
            
            self.body.hideshowQQ( Face, pos )
    
            renpy.pause (0.5)
            screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
            screens.Show("ctc").Pause().Hide("ctc")

            return self
            
        def WrdMainBL (self, Face="body_01.png") :

            screens.Show(Dissolve(1), "blkfade") #Completely black screen.
    
            self.WrdMain()

            self.body.hideshowQQ( Face, pos )
    
            renpy.pause (0.5)
            screens.Hide(Dissolve(1), "blkfade") #Completely black screen.
            screens.Show("ctc").Pause().Hide("ctc")

            return self
                
        def WrdSetAddNew (self, Item = None) :
            block = self.Items.GetBlock(Item)
            if Item != None and block in ["gears_shirt","gears_skirt","gears_stockings","gears_other","gears_hair","gears_panties"] :             
                self.WrdAdd(Item,block,"new")   
                
        def WrdSetUnlock (self, Item = None) :
                            
            if self.Items.Count(Item) < 1:
                self.Items.AddItem (Item,1)
                    
            block = self.Items.GetBlock(Item)
            if Item != None and block in ["gears_shirt","gears_skirt","gears_stockings","gears_other","gears_hair","gears_panties"] :   
                self.WrdRem(Item,"new")
                self.WrdAdd(Item,block,"adm")
            
        def WrdDress (self, Item = None) :
            block = self.Items.GetBlock(Item)
            if Item != None and block in ["gears_shirt","gears_skirt","gears_stockings","gears_other","gears_hair","gears_panties"] :             
                self.WrdDelBlock (block)
                self.WrdAdd(Item, block, "wear")
                if block == "shirt" :
                    self.wrd_noshirt = False
                    self.wrd_upshirt = False
                elif block == "skirt" :
                    self.wrd_upskirt = False  
                self.WrdMain()
                
        def WrdSetDress (self, Item = None) :
        
            if Item == "delstockings" :
                self.WrdSetDelStockings ()
            
            elif Item == "delother" :
                self.WrdSetDelOther ()
                
            else :
        
                block = self.Items.GetBlock(Item)

                if Item != None and block in ["gears_shirt","gears_skirt","gears_stockings","gears_other","gears_hair","gears_panties"] and self.Wrd_adm.Count(Item) > 0 : 
                    self.WrdSetDelBlock (block)
                    self.WrdAdd(Item, block, "set")
                    if block == "gears_shirt" :
                        self.wrd_set_noshirt = False
                        self.wrd_set_upshirt = False
                    elif block == "gears_skirt" :
                        self.wrd_set_upskirt = False  
                    elif block == "gears_panties" :
                        self.wrd_set_downpanties = False

            self.WrdSetMain()
        
        def WrdUpSkirt (self) :
            self.wrd_upskirt = True
            self.WrdDownShirt() 
            self.WrdMain()
            
        def WrdDownSkirt (self) :
            self.wrd_upskirt = False
            self.WrdMain()
            
        def WrdUpShirt (self) :
            self.wrd_upshirt = True
            self.WrdDownSkirt() 
            self.WrdMain()
            
        def WrdDownShirt (self) :
            self.wrd_upshirt = False
            self.WrdMain()
            
        def WrdNoShirt (self) :
            self.wrd_noshirt = True
            self.WrdDelShirt()
            self.WrdMain()
            
        def WrdNoSkirt (self) :
            self.WrdDelSkirt()
            self.WrdMain()
            
        def WrdNoOther (self) :
            self.WrdDelOther()
            self.WrdMain()
        
        def WrdNoStockings (self) :
            self.WrdDelStockings()
            self.WrdMain()
            
        def WrdNoHair (self) :
            self.WrdDelHair()
            self.WrdMain()
            
        def WrdSetUpSkirt (self) :
            self.set_upskirt = True
            self.WrdSetDownShirt() 
            self.WrdSetMain()
            
        def WrdSetDownSkirt (self) :
            self.set_upskirt = False
            self.WrdSetMain()
            
        def WrdSetUpShirt (self) :
            self.set_upshirt = True
            self.WrdSetDownSkirt() 
            self.WrdSetMain()
            
        def WrdSetDownShirt (self) :
            self.set_upshirt = False
            self.WrdSetMain()
            
        def WrdSetNoShirt (self) :
            self.set_noshirt = True
            self.WrdSetDelShirt()
            self.WrdSetMain()
            
        def WrdSetNoSkirt (self) :
            self.WrdSetDelSkirt()
            self.WrdSetMain()
            
        def WrdSetNoOther (self) :
            self.WrdSetDelOther()
            self.WrdSetMain()
        
        def WrdSetNoStockings (self) :
            self.WrdSetDelStockings()
            self.WrdSetMain()
            
        def WrdSpermDried (self) :
            self.wrd_sperm_dried = True
            self.wrd_upshirt = False
            self.wrd_upskirt = False
            self.WrdMain()
            
        def WrdNoSpermDried (self) :
            self.wrd_sperm_dried = False
            self.WrdMain()
            
        def WrdSpermPanties (self) :
            self.wrd_spermpanties = True
            self.WrdMain()
            
        def WrdNoSpermPanties (self) :
            self.wrd_spermpanties = False
            self.WrdMain()
       
            
        def WrdMenuRun ( self , block = "new"):
        
            Person.current = self
            self.wrd_block = block

            self.Wrd_adm_tmp.Clear()
            for i in self.Wrd_adm() :
                if self.Items.GetBlock(i.Name) == self.wrd_block :
                    self.Wrd_adm_tmp.AddItem(i.Name)
            
            renpy.call_screen(Person.wrd_menu_screen)
            
            return
            
        def WrdMenuMainRun ( self ):
        
            Person.current = self
            self.wrd_new_len = 0
            for i in self.Wrd_new() :
                self.wrd_new_len += 1
            self.wrd_block = "main"
            
            while self.wrd_block != "out" :
                if self.wrd_block == "main" :
                    renpy.call_screen(Person.wrd_menu_main_screen)
                elif self.wrd_block != "out" :
                    self.WrdMenuRun (self.wrd_block)
                    if self.wrd_choice != None and self.wrd_block == "new" :
                        renpy.call("wrd_first_" + self.wrd_choice)
                    elif self.wrd_block != "main" :
                        self.WrdSetDress(self.wrd_choice)
                        self.WrdSetMainBL ()
            
            return
            
        def WrdSetChoice (self, iName) :
            self.wrd_choice = iName
            
        def WrdSetBlock (self, iBlock) :
            self.wrd_block = iBlock
            
        def WrdHairUnlock (self) :
            self.wrd_hair_set = True
        
# Задает видимость персоны. 
# body+ - показывать тело всегда, без плюса только во время реплики, 
# head+ - показывать голову всегда, без плюса только во время реплики
# Например, строка: bodyhead  означает, что во время реплики необходимо показать и голову и тело. а когда говорит герой все скрывать
# isTalking - если истина, то сразу показывать в режиме реплики
        def Visibility(self, talkingView=" ", isTalking=True, transition=None):
            debug.SaveString(self.Name+" "+talkingView+" "+str(isTalking))
            self.SetValue("talkingView", talkingView)
            if self.Name!="hero":
                if (isTalking and ('head' in self._talkingView)) or ('head+' in self._talkingView):
                    self.head.showQ(None, self.pos2, transition)
                else:
                    self.head.hideQ(transition)
                    self.curchar=self.char
                if (isTalking and ('body' in self._talkingView)) or ('body+' in self._talkingView):  
                    self.body.showQ(None, self.pos, transition)
#                    self.SetValue("Visible", True)
                else:
                    self.body.hideQ(transition)
#                    self.SetValue("Visible", False)
                    self.curchar=self.char2

                if isTalking:
                    if len(talkingView)>1: # Если длина строки больше 1 значит она - не пробел и значит что-то теперь отображается
                        self.SetValue("Visible", True)    
                else:
                    if not "+" in talkingView: # Если в строке нет плюса, значит сейчас все спрятано
                        self.SetValue("Visible", False)
            return self

        def State(self, pos=None, pos2=None):
            if pos!=None:
                if isinstance( pos, basestring ):
                    self.pos=self.GetValue("pos_"+pos)
                else:
                    self.pos=pos
            if pos2!=None:
                if isinstance( pos2, basestring ):
                    self.pos2=self.GetValue("pos2_"+pos)
                else:
                    self.pos2=pos2

            return self

        def IsTalk(self):
            return self.GetValue("talkTime")==time.stamp

        def CommitTalk(self):
            return self.SetValue("talkTime", time.stamp) 

        def IsGift(self):
            return self.GetValue("giftTime")==time.stamp 

        def CommitGift(self):
            return self.SetValue("giftTime", time.stamp) 

        @property
        def pos(self):
            return self.GetValue("pos")
        @pos.setter
        def pos(self, value):
            self.SetValue("pos", value)
#            self.body.showQ(None, self.GetValue(value))

        @property
        def pos2(self):
            return self.GetValue("pos2")
        @pos2.setter
        def pos2(self, value):
            self.SetValue("pos2", value)
#            self.head.showQ(None, self.GetValue(value))


        @property
        def data(self):
            return self.body.data()

        @property
        def char(self):
            return self.body.mCh

        @property
        def char2(self):
            return self.head.mCh

        @property
        def curchar(self):
            return self.GetValue("curchar")
        @curchar.setter
        def curchar(self, value):
            self.SetValue("curchar", value)



        @property
        def liking(self):
            return self.GetValue("liking")
        @liking.setter
        def liking(self, value):
            self.SetValue("liking", value, minim=-100, maxim=0)

        @property
        def whoring(self):
            return self.GetValue("whoring")
        @whoring.setter
        def whoring(self, value):
            self.SetValue("whoring", value, minim=0)

        @property
        def body(self):
            return self.GetValue("body")

        @property
        def head(self):
            return self.GetValue("head")
          
        @property
        def wrd_choice(self):
            return self.GetValue("wrd_choice")
        @wrd_choice.setter
        def wrd_choice(self, value):
            self.SetValue("wrd_choice", value)
            
        @property
        def wrd_block(self):
            return self.GetValue("wrd_block")
        @wrd_block.setter
        def wrd_block(self, value):
            self.SetValue("wrd_block", value)
            
        @property
        def wrd_new_len(self):
            return self.GetValue("wrd_new_len")
        @wrd_new_len.setter
        def wrd_new_len(self, value):
            self.SetValue("wrd_new_len", value)
            
        @property
        def wrd_set_upshirt(self):
            return self.GetValue("wrd_set_upshirt")
        @wrd_set_upshirt.setter
        def wrd_set_upshirt(self, value):
            self.SetValue("wrd_set_upshirt", value)
            
        @property
        def wrd_set_upskirt(self):
            return self.GetValue("wrd_set_upskirt")
        @wrd_set_upskirt.setter
        def wrd_set_upskirt(self, value):
            self.SetValue("wrd_set_upskirt", value)
            
        @property
        def wrd_set_downpanties(self):
            return self.GetValue("wrd_set_downpanties")
        @wrd_set_downpanties.setter
        def wrd_set_downpanties(self, value):
            self.SetValue("wrd_set_downpanties", value)
            
        @property
        def wrd_set_noshirt(self):
            return self.GetValue("wrd_set_noshirt")
        @wrd_set_noshirt.setter
        def wrd_set_noshirt(self, value):
            self.SetValue("wrd_set_noshirt", value)
            
        @property
        def wrd_upshirt(self):
            return self.GetValue("wrd_upshirt")
        @wrd_upshirt.setter
        def wrd_upshirt(self, value):
            self.SetValue("wrd_upshirt", value)
            
        @property
        def wrd_upskirt(self):
            return self.GetValue("wrd_upskirt")
        @wrd_upskirt.setter
        def wrd_upskirt(self, value):
            self.SetValue("wrd_upskirt", value)
            
        @property
        def wrd_downpanties(self):
            return self.GetValue("wrd_downpanties")
        @wrd_downpanties.setter
        def wrd_downpanties(self, value):
            self.SetValue("wrd_downpanties", value)
            
        @property
        def wrd_noshirt(self):
            return self.GetValue("wrd_noshirt")
        @wrd_noshirt.setter
        def wrd_noshirt(self, value):
            self.SetValue("wrd_noshirt", value)
            
        @property
        def wrd_sperm_dried(self):
            return self.GetValue("wrd_sperm_dried")
        @wrd_sperm_dried.setter
        def wrd_sperm_dried(self, value):
            self.SetValue("wrd_sperm_dried", value)
            
        @property
        def wrd_hair_set(self):
            return self.GetValue("wrd_hair_set")
        @wrd_hair_set.setter
        def wrd_hair_set(self, value):
            self.SetValue("wrd_hair_set", value)
            
        @property
        def wrd_spermpanties(self):
            return self.GetValue("wrd_spermpanties")
        @wrd_spermpanties.setter
        def wrd_spermpanties(self, value):
            self.SetValue("wrd_spermpanties", value)
            
            
screen person_wrd_menu_main:
    add "03_hp/11_misc/bld.png"
    window:
        style "menu_window"
        xalign menu_x
        yalign 0.5

        vbox:
            style "menu"
            spacing 2
            
            if Person.current.wrd_new_len > 0 :
                button :
                    action [Function (Person.current.WrdSetBlock, iBlock = "new"), Return ()] 
                    style "menu_choice_button"

                    text "Новые вещи" style "menu_choice"    
                    
            button :
                action [Function (Person.current.WrdSetBlock, iBlock = "gears_shirt"), Return ()] 
                style "menu_choice_button"

                text "Одежда: Верх" style "menu_choice"  
                    
            button :
                action [Function (Person.current.WrdSetBlock, iBlock = "gears_skirt"), Return ()] 
                style "menu_choice_button"

                text "Одежда: Низ" style "menu_choice"  
                    
            button :
                action [Function (Person.current.WrdSetBlock, iBlock = "gears_stockings"), Return ()] 
                style "menu_choice_button"

                text "Чулки/колготки" style "menu_choice"  
                    
            button :
                action [Function (Person.current.WrdSetBlock, iBlock = "gears_other"), Return ()] 
                style "menu_choice_button"

                text "Прочее" style "menu_choice"
                
            if Person.current.wrd_hair_set :    
                button :
                    action [Function (Person.current.WrdSetBlock, iBlock = "gears_hair"), Return ()] 
                    style "menu_choice_button"

                    text "Прически" style "menu_choice"
                    
            button:
                action [Function (Person.current.WrdSetBlock, iBlock = "out"), Return ()] 
                style "menu_choice_button"

                text "Назад" style "menu_choice"              
            
            
    zorder 7
            
screen person_wrd_menu:
    add "03_hp/11_misc/bld.png"
    window:
        style "menu_window"
        xalign menu_x
        yalign 0.5

        vbox:
            style "menu"
            spacing 2
            
            if Person.current.wrd_block == "new" :
            
                for i in Person.current.Wrd_new() :
                    button:
                        action [Function(Person.current.WrdSetChoice, iName=i.Name), Return()] 
                        style "menu_choice_button"

                        text Person.current.Items.GetCaption(i.Name) style "menu_choice"
                        
            else :
            
                if Person.current.wrd_block == "gears_stockings" :
                    button:
                        action [Function(Person.current.WrdSetChoice, iName="delstockings"), Return()] 
                        style "menu_choice_button"
                            
                        text "Снять чулки/колготки" style "menu_choice"
                
                elif Person.current.wrd_block == "gears_other" :
                    button:
                        action [Function(Person.current.WrdSetChoice, iName="delother"), Return()] 
                        style "menu_choice_button"
                            
                        text "Снять значек" style "menu_choice"
                        
                for i in Person.current.Wrd_adm_tmp() :
                    button:
                        action [Function(Person.current.WrdSetChoice, iName=i.Name), Return()] 
                        style "menu_choice_button"
                            
                        if i in Person.current.Wrd_wear() :
                            text "{color=222277}" + Person.current.Items.GetCaption(i.Name) + "{/color}" style "menu_choice"
                        else :
                            text Person.current.Items.GetCaption(i.Name) style "menu_choice"
                        
            button:
                action [Function (Person.current.WrdSetBlock, iBlock = "main"), Return ()] 
                style "menu_choice_button"

                text "Назад" style "menu_choice"                



    zorder 7

