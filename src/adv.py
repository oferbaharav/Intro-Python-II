from room import Room
from player import Player
from item import Item
# Declare all the rooms

sword = Item("sword", "this will be used to kill the oncoming passengers")
coins = Item("coins", "this will ge used to help you buy more ammo")
flashlight = Item("flashlight", "this will help you see in the dark")
monsters = Item("monsters", "this will help you be entertained")
coffee = Item("coffee beans", "this will help you be productive")
rainbows = Item("rainbows", "this will help you attract unicorns")
unicorns = Item("unicorns", "this will help you become a billionaire")

items = {
    'sword': sword,
    'coins': coins,
    'flashlight': flashlight,
    'monsters': monsters,
    'coffee': coffee,
    'rainbows': rainbows,
    'unicorns': unicorns,
    
}

room = {
    'outside':  Room(" Cave OutsideEntrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [sword, coins]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [flashlight, monsters]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [coffee, rainbows]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [unicorns]),
}



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'])



# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


command = None


while True:
    print("\nyou are in room:", player.room.name)
    print("your room description is:", player.room.description)
    print("items that I have:") 
    for item in player.items:
         print(f"   {item.name}: {item.description}") #printing out items I have
    print("items in the room:") 
    for item in player.room.items:
        print(f"   {item.name}: {item.description}")

    command = input("Enter either n,s,e,w, or take item or drop item: ")
    if command == "q":
        exit()
    elif command in ['n','s','e','w']: 
        new_room = getattr(player.room,f"{command}_to", None)
        if new_room == None:
            print("You FAIL!!!!!!!!!!!")
        else: 
            player.room = new_room
    elif command[0:5] == "take ":
        item_name = command[5:]
        item_to_take = items[item_name]
        if item_to_take in player.room.items:
            player.room.remove_item(item_to_take)
            player.add_item(item_to_take)
    elif command[0:5] == "drop ":
        item_name = command[5:]
        item_to_drop = items[item_name]
        if item_to_drop in player.items:
            player.remove_item(item_to_drop)
            player.room.add_item(item_to_drop)

