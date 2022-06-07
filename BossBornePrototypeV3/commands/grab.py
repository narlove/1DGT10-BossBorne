from classDefinitions import Storage

def cmd_grab(currentRoom, playerCommand, playerInventory):
    gObject = playerCommand[5:].lower()
    completed = False
    for eachObject in currentRoom._objects:
        if gObject == eachObject._name.lower():
            if isinstance(eachObject, Storage):
                print("You can't pickup storage objects!")
                completed = True
                break
            if eachObject._canPickup == False:
                print(f"The {eachObject._name.lower()} is unable to be picked up")
                completed = True
                break
            currentRoom._objects.remove(eachObject)
            playerInventory.append(eachObject)
            print(f"You picked up a {eachObject._name.lower()}")
            completed = True
            break
    if completed != True:
        for eachStorage in currentRoom._objects:
            if not isinstance(eachStorage, Storage):
                continue
            containerReference = currentRoom._objects[currentRoom._objects.index(eachStorage)]
            if containerReference._isLocked == True:
                completed = False   
                break
            if containerReference._isOpened == False:
                completed = False
                break
            for eachCObject in containerReference._storedItems:
                if gObject == eachCObject._name.lower():
                    containerReference._storedItems.remove(eachCObject)
                    playerInventory.append(eachCObject)  
                    print(f"You picked up a {eachCObject._name.lower()}")
                    completed = True
        if completed != True:
            print(f"There is no such object with name {gObject}")             
                
        #print(f"There is no such object with name {gObject}")
        # what im thinking is that if we cant find the object in a scene, check the scene for storage containers and then check for the object in there.