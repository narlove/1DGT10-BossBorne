def cmd_drop(currentRoom, playerCommand, playerInventory):
    dObject = playerCommand[5:].lower()     
    completed = False       
    for eachObject in playerInventory:
        if dObject == eachObject._name.lower():
            if eachObject._canDrop == False:
                print(f"The {eachObject._name.lower()} is unable to be dropped")
                completed = True
                break
            currentRoom._objects.append(eachObject)
            playerInventory.remove(eachObject)
            print(f"You dropped a {eachObject._name.lower()}")
            completed = True
            break
    if completed != True:
        print(f"There is no such object with name {dObject}")