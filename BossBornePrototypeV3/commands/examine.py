def cmd_examine(currentRoom, playerCommand):
    eObject = playerCommand[8:] # splice off the examine part of the command and just get the object
    completed = False
    for eachObject in currentRoom._objects: # compare the object and see if something similar to that name is in the scene
        if eObject.lower() == eachObject._name.lower():
            print(f"{eachObject._description}")
            completed = True
            break
    if completed != True:
        print("You can't examine that object")