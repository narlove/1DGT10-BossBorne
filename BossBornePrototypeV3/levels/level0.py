from classDefinitions import *
import main

def run_level0(): # set up all the level information here
    rock = Items("Rock", True, True, "A simple rock with a few jagged edges. It looks rather harmless, and rather boring.", "There is a rock on the floor in front of you.", True)
    key = Items("Key", True, False, "A standard, medieval key. Complete with a little rust around the edges, it looks like it could be big enough to open a slightly-larger than normal padlock.",
                  "A key sits on a podium in the middle of the room.", True)
    
    barrel = Storage("Barrel", "A broken down old barrel", "A broken down old barrel sits in the corner of the room.", True, [rock], key)
    
    # creates the rooms with objects in an array and a description
    chamber = Room("Chamber", [key, barrel], None, None, None, None, "A circular chamber, with no windows and a dome on top as a roof.")
    testRoom = Room("Test Room", [rock], None, None, None, None, "You're in a test room. An exit into what looks to be a little chamber sits on the east wall.")
    testRoomEastDoor = Door(testRoom, chamber, True, None, key)
    chamberWestDoor = Door(chamber, testRoom, True, testRoomEastDoor, key)
    testRoomEastDoor._correspondingDoor = chamberWestDoor
    chamber._w = chamberWestDoor # this is to "link" up the rooms, so we can tell what connects to what
    testRoom._e = testRoomEastDoor
    currentRoom = chamber # really important, think of this as the character. constantly needs to be updated whenever something is changed.
    main.cmds(currentRoom)