from classDefinitions import *
from levels.levelDescriptions import level2D
import main

def run_level2():
    # instanciating all objects in each room so these can be appended to the list of objects in the room
    # CUBICLE 1
    electricalBoxKey = Items("Small key", True, False, "", "", True) # will only be found in a storage object so doesnt need big description
    computerCase = Storage("Computer case", level2D.computerCaseLongDescription, level2D.computerCaseShortDescription, False, [electricalBoxKey])
    stickyNote = Items("Sticky note", False, False, level2D.stickyNoteLongDescription, level2D.stickyNoteShortDescription, True)
    # KITCHEN
    coffee = Items("Hot cup of coffee", True, True, level2D.coffeeLongDescription, level2D.coffeeShortDescription, True)
    # CUBICLE 2
    screwdriver = Items("Screwdriver", True, True, level2D.screwdriverLongDescription, level2D.screwdriverShortDescription, True)
    # maybe we add throwables in here like desk drawers complete with a pencil?
    # CUBICLE 4
    electricalBox = Storage("Electrical box", level2D.electricalBoxLongDescription, level2D.electricalBoxShortDescription, True, [], electricalBoxKey)
    # CUBICLE 5
    ventScreen = Items("Vent cover", False, False, level2D.ventScreenLongDescription, level2D.ventScreenShortDescription, True)
    
    # instanciating all the rooms
    elevator = Room('Elevator', [], None, None, None, None, level2D.elevatorDescription)
    cubicle1 = Room("Cubicle 1", [computerCase, stickyNote], None, None, None, None, level2D.cubicle1Description)
    cubicle2 = Room("Cubicle 2", [screwdriver], None, None, None, None, level2D.cubicle2Description)
    cubicle3 = Room("Cubicle 3", [], None, None, None, None, level2D.cubicle3Description)
    cubicle4 = Room("Cubicle 4", [electricalBox], None, None, None, None, level2D.cubicle4Description)
    cubicle5 = Room("Cubicle 5", [ventScreen], None, None, None, None, level2D.cubicle5Description)
    cubicle6 = Room("Cubicle 6", [], None, None, None, None, level2D.cubicle6Description)
    vents = Room("Vents", [], None, None, None, None, level2D.ventsDescription)
    stairwell = Room("Stairwell", [], None, None, None, None, level2D.stairwellDescription)
    kitchen = Room("Kitchen", [coffee], None, None, None, None, level2D.kitchenDescription)
    
    currentRoom = elevator
    main.cmds(currentRoom)