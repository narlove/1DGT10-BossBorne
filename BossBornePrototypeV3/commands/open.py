from classDefinitions import Storage

def cmd_open(currentRoom, playerCommand):
    oObject = playerCommand[5:].lower()
    completed = False
    for eachObject in currentRoom._objects:
        if not isinstance(eachObject, Storage):
            continue
        if oObject == eachObject._name.lower():
            eachObject.openContainer()
            completed = True
            break
    if completed != True:
        print("You cannot open that object")