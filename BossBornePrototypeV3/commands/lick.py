from classDefinitions import Items

lickTotal = 0

def cmd_lick(currentRoom, playerCommand):
    global lickTotal
    lObject = playerCommand[5:].lower()
    for eachObject in currentRoom._objects:
        if lObject == eachObject._name.lower():
            if not isinstance(eachObject, Items):
                print("You can't lick this item.")
                break
            if eachObject._canLick == False:
                print(f"The {eachObject._name.lower()} is unable to be licked... weirdo")
                break
            print(f"You licked a {eachObject._name.lower()}...that's nasty")
            lickTotal += 1
            if lickTotal >= 5:
                print("From licking too much things you have contracted CHOLERA")
            break