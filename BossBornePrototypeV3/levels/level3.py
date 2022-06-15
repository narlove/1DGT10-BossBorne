from classDefinitions import * 
import main

currentRoom = None

def run_level3():
    # instanciating all objects in each room so these can be appended to the list of objects in the room
    # CUBICLE 1    
    # instanciating all the rooms
    stairwell = Room("Stairwell", [], None, None, None, None, level3D.stairwellDescription)
    mainOffice = Room("Office", [], None, None, None, None, level3D.officeDescription)
    desk = Room("Desk", [stickyNote], None, None, None, None, level3D.deskDescription)
    hiddenCompartment = Room("Compartment", [], None, None, None, None, level3D.compartmentDescription)
    
    currentRoom = mainOffice
    main.cmds(currentRoom)