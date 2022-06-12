helpCommand = ['look | l: Prints the room description again',
               'examine [object]: Gives a more detailed description of the object',
               'grab [object]: Grab an object and put it in your inventory',
               'drop [object]: Remove an object from your inventory',
               'inventory | i: Print a list of everything in your inventory',
               'unlock [direction] door: Unlock the door of this room in that direction, but it will prompt you for the correct key!',
               'help | h | commands | cmds: Bring up this description of commands',
               'n | north: Move north (if avaliable)',
               'e | east: Move east (if avaliable)',
               's | south: Move south (if avaliable)',
               'w | west: Move west (if avaliable)',
               'open [container]: Opens the specified container so you can grab items out of it.',
               'lick [object] | Lick an object... don\'t try it too many times though...',
               'break [object] | Break an object, but it will prompt you for a device to break it with.']

def cmd_help():
    for command in helpCommand:
        print(command)