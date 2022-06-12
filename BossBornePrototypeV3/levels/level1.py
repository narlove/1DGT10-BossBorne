from classDefinitions import *
from levels.levelDescriptions import peterdinklin
import main

#LEVELS IS CALLED PETERDINKLIN BECAUSE IT BROKE SO WE STUCK WITH PETERDINKLIN <----Note for myself


def run_level1():
    #ENTRANCE
    gun = Items("Gun", True, False, peterdinklin.gunLongDescription, peterdinklin.gunShortDescription, True, True)
    #RECEPTION
    pen = Items("Pen", True, True, peterdinklin.penLongDescription, peterdinklin.penShortDescription, True, True)
    levelMap = Items("Map", False, False, peterdinklin.levelMapLongDescription, peterdinklin.levelMapShortDescription, True, True)
    #KITCHEN
    apple = Items("Apple", True, True, peterdinklin.appleLongDescription, peterdinklin.appleShortDescription, True, True)
    banana = Items("Banana", True, True, peterdinklin.bananaLongDescription, peterdinklin.bananaShortDescription, True, True)
    fridge = Storage("Fridge", peterdinklin.fridgeLongDescription, peterdinklin.fridgeShortDescription, False, [apple, banana]) 
    #BATHROOM STALL
    accessKey = Items("Access Key", True, False,  peterdinklin.accessKeyLongDescription, peterdinklin.accessKeyShortDescription, True, True)


    #ROOMS~~~~
    lounge = Room("Lounge", [], None, None, None, None, peterdinklin.loungeDescription)
    elevator = Room("Elevator", [], None, None, None, None, peterdinklin.elevatorDescription)
    bathroom = Room("Bathroom", [], None, None, None, None, peterdinklin.bathroomDescription)
    bathroomStall = Room("Bathroom Stall", [accessKey], None, None, None, None,  peterdinklin.stallDescription)
    reception = Room("Reception", [pen, levelMap], None, None, None, None, peterdinklin.receptionDescription)
    kitchen = Room("Kitchen", [fridge], None, None, None, None, peterdinklin.kitchenDescription)
    entrance = Room("Entrance", [gun], None, None, None, None, peterdinklin.entranceDescription)
    lobby = Room("Lobby", [], None, None, None, None, peterdinklin.lobbyDescription)
    elevatorInside = Room("Elevator Inside", [], None, None, None, None, peterdinklin.elevatorInsideDescription)

  # Locked Doors
    elevatorToElevatorInside = Door(elevator, elevatorInside, True, None, accessKey)
    elevatorInsideToElevator = Door(elevatorInside, elevator, True, elevatorToElevatorInside, accessKey)
    elevatorToElevatorInside._correspondingDoor = elevatorInsideToElevator

    bathroomToBathroomStall = Door(bathroom, bathroomStall, True, None, pen)
    bathroomStallToBathroom = Door(bathroomStall, bathroom, True, bathroomToBathroomStall, None)
    bathroomToBathroomStall._correspondingDoor = bathroomStallToBathroom

    #Connecting all the rooms
    reception._s = lobby

    entrance._n = lobby

    lobby._n = reception
    lobby._e = elevator
    lobby._w = lounge
    lobby._s = entrance

    elevator._w = lobby

    lounge._e = lobby
    lounge._n = bathroom
    lounge._w = kitchen

    bathroom._s = lounge
    bathroom._n = bathroomToBathroomStall

    bathroomStall._s = bathroomStallToBathroom

    kitchen._e = lounge

    elevator._w = lobby
    elevator._e = elevatorToElevatorInside

    elevatorInside.w = elevatorInsideToElevator

    currentRoom = entrance
    main.cmds(currentRoom)




