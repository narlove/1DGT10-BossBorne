def cmd_inventory(playerInventory):
    if len(playerInventory) > 0:
        print("You are currently holding: ")
        c = 0
        for eachObject in playerInventory:
            c += 1
            print(f"{c}. {eachObject._name.title()}")
    else:
        print("You are not currently holding anything")