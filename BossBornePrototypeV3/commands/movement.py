from classDefinitions import Door

def cmd_north(currentRoom):
    if not currentRoom._n: 
        print("You can't move in that direction")
        raise AttributeError("dummy error to continue loop")
    if isinstance(currentRoom._n, Door):
        currentRoom = currentRoom._n.enterDoor(currentRoom)
        return currentRoom
    else:
        currentRoom = currentRoom._n
        currentRoom.print_description()
        return currentRoom

def cmd_east(currentRoom):
    if not currentRoom._e: 
        print("You can't move in that direction")
        raise AttributeError("dummy error to continue loop")
    if isinstance(currentRoom._e, Door):
        currentRoom = currentRoom._e.enterDoor(currentRoom)
        return currentRoom
    else:
        currentRoom = currentRoom._e
        currentRoom.print_description()
        return currentRoom

def cmd_south(currentRoom):
    if not currentRoom._s: 
        print("You can't move in that direction")
        raise AttributeError("dummy error to continue loop")
    if isinstance(currentRoom._s, Door):
        currentRoom = currentRoom._s.enterDoor(currentRoom)
        return currentRoom
    else:
        currentRoom = currentRoom._s
        currentRoom.print_description()
        return currentRoom

def cmd_west(currentRoom):
    if not currentRoom._w: 
        print("You can't move in that direction")
        raise AttributeError("dummy error to continue loop")
    if isinstance(currentRoom._w, Door):
        currentRoom = currentRoom._w.enterDoor(currentRoom)
        return currentRoom
    else:
        currentRoom = currentRoom._w
        currentRoom.print_description()
        return currentRoom