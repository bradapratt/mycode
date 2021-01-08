#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  use [item]
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


def printMapDefault():
    print("""\
           N                             +--------+
           ^                             | PANTRY |
           |                             |        |
           |        X = YOU ARE HERE     |        |
           +                             |        |
                                         |        |
        +---------------+--------+-------+--| |---+
        |               |        |                |
        |  LIVING ROOM  ⊥  HALL  ⊥  DINING ROOM   |
        |               _        _                |
        |               |        |                |
        |               |        |                |
        |               |        |                |
        +-----| |----------------+---------| |----+
        |   BEDROOM 1   |                         |
        |               |                         |
        |               |        GARDEN           |
        +-----| |-------+                         |
        |   BEDROOM 2   |                         ⊥
        |               |                         _
        |               |                         |
        +-----| |-------+                         |
        |               ⊥                         |
        |   KITCHEN     _                         |
        |               +-------------------------+
        |               ⊥       BASEMENT          |
        |               _                         |
        |               |                         |
        +---------------+-------------------------+
        """)


def printMapPantry():
    print("""\
           N                             +--------+
           ^                             | PANTRY |
           |                             |        |
           |        X = YOU ARE HERE     |   X    |
           +                             |        |
                                         |        |
        +---------------+--------+-------+--| |---+
        |               |        |                |
        |  LIVING ROOM  ⊥  HALL  ⊥  DINING ROOM   |
        |               _        _                |
        |               |        |                |
        |               |        |                |
        |               |        |                |
        +-----| |----------------+---------| |----+
        |   BEDROOM 1   |                         |
        |               |                         |
        |               |        GARDEN           |
        +-----| |-------+                         |
        |   BEDROOM 2   |                         ⊥
        |               |                         _
        |               |                         |
        +-----| |-------+                         |
        |               ⊥                         |
        |   KITCHEN     _                         |
        |               +-------------------------+
        |               ⊥       BASEMENT          |
        |               _                         |
        |               |                         |
        +---------------+-------------------------+
    """)


def printMapDiningRoom():
    print("""\
           N                             +--------+
           ^                             | PANTRY |
           |                             |        |
           |        X = YOU ARE HERE     |        |
           +                             |        |
                                         |        |
        +---------------+--------+-------+--| |---+
        |               |        |                |
        |  LIVING ROOM  ⊥  HALL  ⊥  DINING ROOM   |
        |               _        _                |
        |               |        |        X       |
        |               |        |                |
        |               |        |                |
        +-----| |----------------+---------| |----+
        |   BEDROOM 1   |                         |
        |               |                         |
        |               |        GARDEN           |
        +-----| |-------+                         |
        |   BEDROOM 2   |                         ⊥
        |               |                         _
        |               |                         |
        +-----| |-------+                         |
        |               ⊥                         |
        |   KITCHEN     _                         |
        |               +-------------------------+
        |               ⊥       BASEMENT          |
        |               _                         |
        |               |                         |
        +---------------+-------------------------+
    """)


def printMapHall():
    print("""\
           N                             +--------+
           ^                             | PANTRY |
           |                             |        |
           |        X = YOU ARE HERE     |        |
           +                             |        |
                                         |        |
        +---------------+--------+-------+--| |---+
        |               |        |                |
        |  LIVING ROOM  ⊥  HALL  ⊥  DINING ROOM   |
        |               _        _                |
        |               |    X   |                |
        |               |        |                |
        |               |        |                |
        +-----| |----------------+---------| |----+
        |   BEDROOM 1   |                         |
        |               |                         |
        |               |        GARDEN           |
        +-----| |-------+                         |
        |   BEDROOM 2   |                         ⊥
        |               |                         _
        |               |                         |
        +-----| |-------+                         |
        |               ⊥                         |
        |   KITCHEN     _                         |
        |               +-------------------------+
        |               ⊥       BASEMENT          |
        |               _                         |
        |               |                         |
        +---------------+-------------------------+
    """)


def printMapLivingRoom():
    print("""\
           N                             +--------+
           ^                             | PANTRY |
           |                             |        |
           |        X = YOU ARE HERE     |        |
           +                             |        |
                                         |        |
        +---------------+--------+-------+--| |---+
        |               |        |                |
        |  LIVING ROOM  ⊥  HALL  ⊥  DINING ROOM   |
        |               _        _                |
        |       X       |        |                |
        |               |        |                |
        |               |        |                |
        +-----| |----------------+---------| |----+
        |   BEDROOM 1   |                         |
        |               |                         |
        |               |        GARDEN           |
        +-----| |-------+                         |
        |   BEDROOM 2   |                         ⊥
        |               |                         _
        |               |                         |
        +-----| |-------+                         |
        |               ⊥                         |
        |   KITCHEN     _                         |
        |               +-------------------------+
        |               ⊥       BASEMENT          |
        |               _                         |
        |               |                         |
        +---------------+-------------------------+
    """)


def printMapBedroom1():
    print("""\
           N                             +--------+
           ^                             | PANTRY |
           |                             |        |
           |        X = YOU ARE HERE     |        |
           +                             |        |
                                         |        |
        +---------------+--------+-------+--| |---+
        |               |        |                |
        |  LIVING ROOM  ⊥  HALL  ⊥  DINING ROOM   |
        |               _        _                |
        |               |        |                |
        |               |        |                |
        |               |        |                |
        +-----| |----------------+---------| |----+
        |   BEDROOM 1   |                         |
        |       X       |                         |
        |               |        GARDEN           |
        +-----| |-------+                         |
        |   BEDROOM 2   |                         ⊥
        |               |                         _
        |               |                         |
        +-----| |-------+                         |
        |               ⊥                         |
        |   KITCHEN     _                         |
        |               +-------------------------+
        |               ⊥       BASEMENT          |
        |               _                         |
        |               |                         |
        +---------------+-------------------------+
    """)


def printMapBedroom2():
    print("""\
           N                             +--------+
           ^                             | PANTRY |
           |                             |        |
           |        X = YOU ARE HERE     |        |
           +                             |        |
                                         |        |
        +---------------+--------+-------+--| |---+
        |               |        |                |
        |  LIVING ROOM  ⊥  HALL  ⊥  DINING ROOM   |
        |               _        _                |
        |               |        |                |
        |               |        |                |
        |               |        |                |
        +-----| |----------------+---------| |----+
        |   BEDROOM 1   |                         |
        |               |                         |
        |               |        GARDEN           |
        +-----| |-------+                         |
        |   BEDROOM 2   |                         ⊥
        |      X        |                         _
        |               |                         |
        +-----| |-------+                         |
        |               ⊥                         |
        |   KITCHEN     _                         |
        |               +-------------------------+
        |               ⊥       BASEMENT          |
        |               _                         |
        |               |                         |
        +---------------+-------------------------+
    """)


def printMapKitchen():
    print("""\
           N                             +--------+
           ^                             | PANTRY |
           |                             |        |
           |        X = YOU ARE HERE     |        |
           +                             |        |
                                         |        |
        +---------------+--------+-------+--| |---+
        |               |        |                |
        |  LIVING ROOM  ⊥  HALL  ⊥  DINING ROOM   |
        |               _        _                |
        |               |        |                |
        |               |        |                |
        |               |        |                |
        +-----| |----------------+---------| |----+
        |   BEDROOM 1   |                         |
        |               |                         |
        |               |        GARDEN           |
        +-----| |-------+                         |
        |   BEDROOM 2   |                         ⊥
        |               |                         _
        |               |                         |
        +-----| |-------+                         |
        |               ⊥                         |
        |   KITCHEN     _                         |
        |               +-------------------------+
        |       X       ⊥       BASEMENT          |
        |               _                         |
        |               |                         |
        +---------------+-------------------------+
    """)


def printMapBasement():
    print("""\
           N                             +--------+
           ^                             | PANTRY |
           |                             |        |
           |        X = YOU ARE HERE     |        |
           +                             |        |
                                         |        |
        +---------------+--------+-------+--| |---+
        |               |        |                |
        |  LIVING ROOM  ⊥  HALL  ⊥  DINING ROOM   |
        |               _        _                |
        |               |        |                |
        |               |        |                |
        |               |        |                |
        +-----| |----------------+---------| |----+
        |   BEDROOM 1   |                         |
        |               |                         |
        |               |        GARDEN           |
        +-----| |-------+                         |
        |   BEDROOM 2   |                         ⊥
        |               |                         _
        |               |                         |
        +-----| |-------+                         |
        |               ⊥                         |
        |   KITCHEN     _                         |
        |               +-------------------------+
        |               ⊥       BASEMENT          |
        |               _           X             |
        |               |                         |
        +---------------+-------------------------+
    """)


def printMapGarden():
    print("""\
           N                             +--------+
           ^                             | PANTRY |
           |                             |        |
           |        X = YOU ARE HERE     |        |
           +                             |        |
                                         |        |
        +---------------+--------+-------+--| |---+
        |               |        |                |
        |  LIVING ROOM  ⊥  HALL  ⊥  DINING ROOM   |
        |               _        _                |
        |               |        |                |
        |               |        |                |
        |               |        |                |
        +-----| |----------------+---------| |----+
        |   BEDROOM 1   |                         |
        |               |                         |
        |               |        GARDEN           |
        +-----| |-------+                         |
        |   BEDROOM 2   |                         ⊥
        |               |           X             _
        |               |                         |
        +-----| |-------+                         |
        |               ⊥                         |
        |   KITCHEN     _                         |
        |               +-------------------------+
        |               ⊥       BASEMENT          |
        |               _                         |
        |               |                         |
        +---------------+-------------------------+
    """)


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'west': 'Living Room',
        'east': 'Dining Room'
    },

    'Kitchen': {
        'north': 'Bedroom 2',
        'northeast': 'Garden',
        'southeast': 'Basement',
        'item': 'monster'
    },

    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'north': 'Pantry',
        'item': 'potion'
    },

    'Garden': {
        'north': 'Dining Room',
        'west': 'Bedroom 2'
    },

    'Pantry': {
        'south': 'Dining Room',
        'item': 'cookie'
    },

    'Living Room': {
        'east': 'Hall',
        'south': 'Bedroom 1'
    },

    'Bedroom 1': {
        'north': 'Living Room',
        'south': 'Bedroom 2'
    },

    'Bedroom 2': {
        'north': 'Bedroom 1',
        'east': 'Garden',
        'south': 'Kitchen',
        'item': 'map'
    },

    'Basement': {
        'west': 'Kitchen',
        'item': 'key'
    }
}

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # if they type 'use' first
    if move[0] == 'use':
        if move[1] in inventory and move[1] == 'map':
            if currentRoom == 'Pantry':
                printMapPantry()
            elif currentRoom == 'Dining Room':
                printMapDiningRoom()
            elif currentRoom == 'Hall':
                printMapHall()
            elif currentRoom == 'Living Room':
                printMapLivingRoom()
            elif currentRoom == 'Bedroom 1':
                printMapBedroom1()
            elif currentRoom == 'Bedroom 2':
                printMapBedroom2()
            elif currentRoom == 'Kitchen':
                printMapKitchen()
            elif currentRoom == 'Basement':
                printMapBasement()
            else:
                printMapGarden()
        else:
            print("Can't use that item here!")

    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    # If a player enters a room with a monster BUT HAS A COOKIE
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'cookie' in inventory:
        print('The monster takes your cookie and runs away! Whew!')
        del rooms[currentRoom]['item']
        inventory.remove('cookie')

    # If a player enters a room with a monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

