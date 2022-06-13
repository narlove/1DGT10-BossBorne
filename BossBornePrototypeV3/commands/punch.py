from classDefinitions import *

def cmd_punch(currentRoom, playerCommand):
    pObject = playerCommand[6:].lower()
    for eachObject in currentRoom._objects:
        if pObject == eachObject._name.lower():
            if not isinstance(eachObject, Items):
                print("You can't punch this item... idiot")
                break
            if eachObject._canPunch == False:
                print(f"The {eachObject._name.lower()} is unable to be punched... dumbass")
                break
            print(f"You PUNCHED the {eachObject._name.lower()}")
