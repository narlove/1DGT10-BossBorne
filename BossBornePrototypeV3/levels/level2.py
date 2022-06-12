from classDefinitions import *
from levels.levelDescriptions import level2D
import main

def run_level2():
    global ventFanBlock
    global vents
    # instanciating all objects in each room so these can be appended to the list of objects in the room
    # CUBICLE 1
    electricalBoxKey = Items("Small key", True, False, "", "", True) # will only be found in a storage object so doesnt need big description
    computerCase = Storage("Computer", level2D.computerCaseLongDescription, level2D.computerCaseShortDescription, False, [electricalBoxKey])
    stickyNote = Items("Sticky note", False, False, level2D.stickyNoteLongDescription, level2D.stickyNoteShortDescription, True)
    # KITCHEN
    coffee = Items("Coffee", True, True, level2D.coffeeLongDescription, level2D.coffeeShortDescription, True)
    # CUBICLE 2
    screwdriver = Items("Screwdriver", True, True, level2D.screwdriverLongDescription, level2D.screwdriverShortDescription, True)
    # maybe we add throwables in here like desk drawers complete with a pencil?
    # CUBICLE 4
    wires = BreakableItems("Wires", False, False, "", "", False, level2D.wiresBreakMessage, "", "", coffee)
    electricalBox = Storage("Box", level2D.electricalBoxLongDescription, level2D.electricalBoxShortDescription, True, [wires], electricalBoxKey)
    # CUBICLE 5
    ventScreen = Items("Vent", False, False, level2D.ventScreenLongDescription, level2D.ventScreenShortDescription, True)
    
    # instanciating all the rooms
    #elevator = Room('Elevator', [], None, None, None, None, level2D.elevatorDescription)
    cubicle1 = Room("Cubicle 1", [computerCase, stickyNote], None, None, None, None, level2D.cubicle1Description)
    cubicle2 = Room("Cubicle 2", [screwdriver], None, None, None, None, level2D.cubicle2Description)
    cubicle3 = Room("Cubicle 3", [], None, None, None, None, level2D.cubicle3Description)
    cubicle4 = Room("Cubicle 4", [electricalBox], None, None, None, None, level2D.cubicle4Description)
    cubicle5 = Room("Cubicle 5", [ventScreen], None, None, None, None, level2D.cubicle5Description)
    cubicle6 = Room("Cubicle 6", [], None, None, None, None, level2D.cubicle6Description)
    vents = Room("Vents", [], None, None, None, None, level2D.ventsOnDescription)
    stairwell = Room("Stairwell", [], None, None, None, None, level2D.stairwellDescription)
    kitchen = Room("Kitchen", [coffee], None, None, None, None, level2D.kitchenDescription)

    # connecting all the rooms
    
    cubicle1._e = cubicle6
    cubicle1._w = kitchen

    kitchen._e = cubicle1
    kitchen._s = cubicle2

    cubicle2._n = kitchen
    cubicle2._s = cubicle3

    cubicle3._n = cubicle2
    cubicle3._e = cubicle4

    # there should be a locked door here
    cub4ToStairwellDoor = Door(cubicle4, stairwell, True, None)
    stairwellToCub4Door = Door(stairwell, cubicle4, True, cub4ToStairwellDoor, None) # this door is merely a workaround to not return an error
                                                                                     # the user will not be aware this door exists, nor will they have any
                                                                                     # possbility of opening it
    cubicle4._e = cub4ToStairwellDoor
    cubicle4._w = cubicle3
    cub4ToStairwellDoor._correspondingDoor = stairwellToCub4Door
    
    cub5ToVentsDoor = Door(cubicle5, vents, True, None, screwdriver)
    ventsToCub5Door = Door(vents, cubicle5, True, cub5ToVentsDoor, screwdriver)
    cub5ToVentsDoor._correspondingDoor = ventsToCub5Door
    
    ventFanBlock = Door(vents, stairwell, True, None, None)
    blockCircumvent = Door(stairwell, vents, True, ventFanBlock, None) # another circumvention of my own code
    ventFanBlock._correspondingDoor = blockCircumvent
    vents._s = ventFanBlock # this part is confusing - you cannot go back to the stairwell from the vents, and there isnt actually a vent fan room so going south in the vents just 
                         # takes you to the stairwell
    vents._w = ventsToCub5Door
    
    cubicle5._e = cub5ToVentsDoor
    cubicle5._n = cubicle6
    
    cubicle6._s = cubicle5
    cubicle6._w = cubicle1

    currentRoom = cubicle1
    print(level2D.elevatorDescription)
    main.cmds(currentRoom)