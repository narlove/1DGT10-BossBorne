class Room: # this is the room class
    def __init__(self, name: str, objects: list, n, e, s, w, description: str):
        self._name = name
        self._objects = objects # get a list  of the objects in the room
        self._n = n # all of these are the directions that can be accessed from this room
        self._e = e
        self._s = s
        self._w = w
        self._description = description # keep a description

    def get_description(self): # function works by getting the short description of each object in the room and appending it to the description
        # this helps if a user picks up an object and it is no longer in the room
        self._tempDes = ""
        self._tempDes = self._description
        toAppend = self._objects[:]
        try:
            self._tempDes = self._tempDes + "\n" + toAppend[0]._shortDes
            toAppend.pop(0)
            for eachObject in toAppend:
                self._tempDes = self._tempDes + " " + eachObject._shortDes
        except:
            pass
        return self._tempDes
    
    def print_description(self): # same method as above but prints rather than returns, just for simplicity and QoL
        self._tempDes = ""
        self._tempDes = self._description
        toAppend = self._objects[:]
        try:
            self._tempDes = self._tempDes + "\n" + toAppend[0]._shortDes
            toAppend.pop(0)
            for eachObject in toAppend:
                self._tempDes = self._tempDes + " " + eachObject._shortDes
        except:
            pass
        print(self._tempDes)
 
    def print_objects(self): # iterates through the objects list and prints them out
        c = 0 
        for item in self._objects:
            c += 1
            print(f'{c}. {item._name}')
            
    description = property(get_description) # for easy access of the description, and so devs dont have to edit the self._description.
    # this needs to be implemented more, but for this example code, it will be left as is
 
class Items: # all objects stem from here
    def __init__(self, name: str, canPickup: bool, canDrop: bool, description: str, shortDes: str, canLick: bool):
        self._name = name
        self._canPickup = canPickup
        self._canDrop = canDrop
        self._description = description
        self._shortDes = shortDes # this is for appending to the room description if the object is in the room
        self._canLick = canLick
 
    def get_description(self): # similar two functions to the room class
        return self._description
    
    def print_description(self):
        print(self._description)
        
class BreakableItems(Items): # inherits from the items class because they will a lot of similar stuff
    def __init__(self, name: str, canPickup: bool, canDrop: bool, description: str, shortDes: str, isBroken: bool, breakMessage: str, bDes: str, bSDes: str, reqItem: Items = None):
        super().__init__(name, canPickup, canDrop, description, shortDes, False)
        self._isBroken = isBroken # check if its broken so it cant be twice in a row
        self._breakMessage = breakMessage # the message to display when its broken
        self._brokenDescription = bDes # the description to set to when its broken
        self._brokenShortDescription = bSDes # the short des to set to when its broken
        self._reqItem = reqItem
        
    def breakObject(self, item):
        if self._isBroken == True:
            print("That object is already broken!")
            return
        if not item or item != self._reqItem:
            print("You cant break this object with that item")
            return
        self._isBroken = True
        print(self._breakMessage)
        self._description = self._brokenDescription
        self._shortDes = self._brokenShortDescription

class Door:
    def __init__(self, startingRoom: Room, endingRoom: Room, isLocked: bool, correspondingDoor, reqKey: Items = None):
        self._startingRoom = startingRoom
        self._endingRoom = endingRoom
        self._isLocked = isLocked
        self._reqKey = reqKey
        self._correspondingDoor = correspondingDoor
        
    def enterDoor(self, currentRoom):
        if self._isLocked == True:
            print("This door is locked")
            return currentRoom
        newRoom = self._endingRoom
        newRoom.print_description()
        return newRoom
    
    def unlockDoor(self, key):
        if self._isLocked == False:
            print("This door is not locked")
            return
        if not key or key != self._reqKey:
            print("This is the wrong key")
            return
        self._isLocked = False
        self._correspondingDoor._isLocked = False
        print("The door is unlocked")

class Storage:
    def __init__(self, name: str, description: str, shortDes: str, isLocked: bool, storedItems: list, reqItem: Items = None):
        self._name = name 
        self._description = description
        self._shortDes = shortDes
        self._isLocked = isLocked 
        self._reqItem = reqItem
        self._storedItems = storedItems 
        self._isOpened = False 
        
    def get_description(self) -> str:
        return self._description
    
    def print_description(self):
        print(self._description)
    
    def unlockContainer(self, key):
        if self._isLocked == False:
            print(f"This {self._name.lower()} is not locked")
            return
        if not key or key != self._reqItem:
            print("This is the wrong key")
            return
        self._isLocked = False
        print(f"The {self._name.lower()} is unlocked")
        
    def openContainer(self):
        if self._isLocked == True:
            print(f"The {self._name.lower()} is locked!")
            return
        self._isOpened = True
        print(f"Sitting inside the {self._name.lower()} is: ")
        if not self._storedItems:
            print("Nothing!")
        else:
            c = 0
            for item in self._storedItems:
                c += 1
                print(f"{c}. {item._name}")