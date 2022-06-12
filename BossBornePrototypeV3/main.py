# Version 1.17.0.15
#         ^ indicates semester
#           ^ indicates school week
#              ^ indicates update (0 for prototype, 1 for initial, 2 for next, 3 etc)
#                ^ each time i open this file change this number

import commands.help
import commands.look
import commands.examine
import commands.grab 
import commands.inventory 
import commands.unlock 
import commands.drop 
import commands.open 
import commands.movement 
import commands.lick
import commands.punch
import commands.breakObject
import commands.up

playerInventory = []

def cmds(currentRoom):
    currentRoom.print_description()

    # where all the commands happen
    while True:
        playerCommand = input(">")
        if playerCommand.lower() in ['look', 'l']:
            commands.look.cmd_look(currentRoom)
        elif playerCommand.startswith('examine'): # important to use startswith as it allows us to access passed objects, kinda like function arguments
            commands.examine.cmd_examine(currentRoom, playerCommand)
        elif playerCommand.startswith('grab'): # similar method to examine, but removes the object from the room and adds to player inventory
            commands.grab.cmd_grab(currentRoom, playerCommand, playerInventory)
        elif playerCommand.lower() in ['inventory', 'i']:
            commands.inventory.cmd_inventory(playerInventory)
        elif playerCommand.startswith('unlock'):
            commands.unlock.cmd_unlock(currentRoom, playerCommand, playerInventory)
        elif playerCommand.startswith('drop'): # similar method to grab, but removes from inventory and adds to room
            commands.drop.cmd_drop(currentRoom, playerCommand, playerInventory)
        elif playerCommand.lower() in ['n', 'north']:
            try:
                currentRoom = commands.movement.cmd_north(currentRoom)
            except AttributeError:
                continue
        elif playerCommand.lower() in ['e', 'east']:
            try:
                currentRoom = commands.movement.cmd_east(currentRoom)
            except AttributeError:
                continue
        elif playerCommand.lower() in ['s', 'south']:
            try:
                currentRoom = commands.movement.cmd_south(currentRoom)
            except AttributeError:
                continue
        elif playerCommand.lower() in ['w', 'west']:
            try:
                currentRoom = commands.movement.cmd_west(currentRoom)
            except AttributeError:
                continue
        elif playerCommand.lower() in ['help', 'h', 'cmds', 'cmd', 'commands', 'command']:
            commands.help.cmd_help()
        elif playerCommand.startswith('open'):
            commands.open.cmd_open(currentRoom, playerCommand)
        elif playerCommand.startswith('lick'):
            commands.lick.cmd_lick(currentRoom, playerCommand)
        elif playerCommand.startswith('punch'):
            commands.punch.cmd_punch(currentRoom, playerCommand)   
        elif playerCommand.startswith('break'):
            commands.breakObject.cmd_break(currentRoom, playerCommand, playerInventory)
        elif playerCommand.lower() in ['up', 'u']:
            commands.up.cmd_up()
