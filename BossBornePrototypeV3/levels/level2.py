from classDefinitions import *
from levels.levelDescriptions import level2D
import main

def run_level2():
    # instanciating all objects in each room so these can be appended to the list of objects in the room
    # CUBICLE 1
    computerCase = Storage("Computer case")
    stickyNote = Items("Sticky Note", False, False, level2D.stickyNoteLongDescription, level2D.stickyNoteShortDescription)
    
    # instanciating all the rooms
    elevator = Room('Elevator', [], None, None, None, None, level2D.elevatorDescription)
    cubicle1 = Room("Cubicle 1", [computerCase, stickyNote], None, None, None, None, level2D.cubicle1Description)
    cubicle2
    cubicle3
    cubicle4
    cubicle5
    cubicle6
    vents
    ventsfan
    stairwell
    kitchen
    
    currentRoom = elevator
    main.cmds(currentRoom)