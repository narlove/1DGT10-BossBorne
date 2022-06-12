from classDefinitions import BreakableItems, Storage
import levels.level2 # specifically for this file because i need a chain reaction to occur after wires are burnt

def cmd_break(currentRoom, playerCommand, playerInventory):
    bObject = playerCommand[6:] # splice off the examine part of the command and just get the object
    completed = False
    for eachObject in currentRoom._objects: # compare the object and see if something similar to that name is in the scene
        if not isinstance(eachObject, BreakableItems):
            continue
        if bObject.lower() == eachObject._name.lower():
            inputKey = str(input("What item will you use to break this object? "))
            for eachIObject in playerInventory:
                if inputKey == eachIObject._name.lower():
                    eachObject.breakObject(eachIObject)
                    completed = True
                    break   
    if completed != True:
        for eachStorage in currentRoom._objects:
            if not isinstance(eachStorage, Storage):
                continue
            containerReference = currentRoom._objects[currentRoom._objects.index(eachStorage)]
            for eachCObject in containerReference._storedItems:
                if not isinstance(eachCObject, BreakableItems):
                    continue
                if bObject == eachCObject._name.lower():
                    inputKey = str(input("What item will you use to break this object? "))
                    for eachIObject in playerInventory:
                        if inputKey == eachIObject._name.lower():
                            eachCObject.breakObject(eachIObject)
                            completed = True
                            break
        if completed != True:
            print(f"There is no such object with name {bObject}") 
    if completed == True and eachObject._name.lower() == "wires" or completed == True and eachCObject._name.lower() == "wires":
        levels.level2.ventFanBlock._isLocked = False
        levels.level2.ventFanBlock._correspondingDoor._isLocked = False
        levels.level2.vents._description = levels.level2.level2D.ventsOffDescription
