import random  # noqa # pylint: disable=unused-import
from pythia.util import MagicString, dice_roll# noqa # pylint: disable=unused-import
from typing import Any

# Any table you make should be defined here first if you plan on making tables
# that point to other tables.
tableSomething = {}
tableAnotherthing = {}



# tables are dictionaries. they could have been lists. Maybe i will make them
# into lists later.
# For now though they are dictionaries, and they should always have a 0 key
# that gives you as a value type of value the table provides you with. for
# example bellow you find a Letters table so there should be an element `0:
# "Letter"`. This element will never be accesed by the generator.
# You can add multiple entries of a value to make it weighted. This means it
# will be more likely to happen compared to other entries.
list_Letters = [
    "a",
    "b",
    "c",
    "c",
    "c",
    "d",
    "e",
    "f"
]
# If you want to easily transform a table from a book to the above example,
# copy paste the above to chatgpt, and then copy paste the table from the book
# asking it to format it like this example. It shouldn't have an issue with
# doing it for you. It can then help you debug throughout this endeavor. Just
# copy any error messages you get.
# If you dont have a digital version of the table you want to make, or want to
# make one of your own, then you can use the bellow 1000 elements in the below
# example to save some time

# If you want to point at a list, then you just add the key that points to
# that list as a value from your TABLES dictionary. It basically
# replaces any instance of the string, so you need to be careful not to have
# two tables where one's key is part of anothers. Eg.
# ROOM will replace ROOM-THEME and the result will end up being
# something like "[RoomListRandomValue]-THEME"
list_things = [
    "thing 1"
    "thing 4"
    # LETTERS is a reference to another table.
    "LETTERS"
    # This is a reference as part of a larger string. This can end up being:
    # a powerfull, b powerfull, c powerfull etc.
    "LETTERS powerfull"
    # This will give you two rolls on the LETTERS list
    "LETTERS LETTERS"
    # You can have "Roll Again"s by referencing this list.
    "THINGS"
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
]

list_three = [
    "One",
    "Three",
    "Cute",
    "Three",
    "Four",
    "Three",
]

# This is an example of a preset that uses no porgramming. It makes a "Dungeon"
# with a random amount of rooms. It showcases various way in which presets can
# be made, and tehcniques that can be used. the SecretRooms sable shows that
# every room has a letter designation with something random from the Anything
# table in it, except for that special 1/6 chance that table Three happens, or
# the 1/6 chance it has 1d300 elements from the Anything table in it.
secret_room = [
    "\n(This is room LETTERS with THINGS in it. "
    + "Something with a 1/6 chance of happening in this config: THREE)",
    "\n(This is room LETTERS with "
        + str(random.randint(0, 300))
        + " THINGS in it.)",
    "\n(This is room LETTERS with THINGS in it.)",
    "\n(This is room LETTERS with THINGS in it.)",
    "\n(This is room LETTERS with THINGS in it.)",
    "\n(This is room LETTERS with THINGS in it.)",
]


# Here we see how we can essentially choose randomly how many rooms we have.
# The likelyhood that making one room give's us a second room as well is 20/25,
# pretty high! This chance stacks, so we have pretty interesting statistics
# here. where its most dungeons will have around 7 rooms but they can also have
# as low number as 1 and as high number as fate decides.
secret_roomAmount = [
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms tableSecretRoomAmount",
    "tableSecretRooms",
    "tableSecretRooms",
    "tableSecretRooms",
    "tableSecretRooms",
    "",
]

preset_dungeon = [
    "A THREE dungeon with the following rooms: "
     + "sROOM sA-O-ROOM."
]

# This does a similar thing, but uses programming for the logic of
# probabilities. dice_roll can be really usefull as a function. There is
# documentation on how to use it in the util.py file where it's defined, but
# pretty simply:
# dice_roll(
#           sides of die,
#           number of dice of this type rolled,
#           whether to crit, basically a d20 is rolled, and on a nat 1 the
#               amount of dice is halved, and on a nat 20 it's doubled.
#               Default is False
#           )
#
#
#
# this list rolls a d6 and on a 1 it adds something from the THREE list to the
# room
secret_room = [
    MagicString(lambda:
                "LETTERS room with THINGS in it."
                + f"{" Three: THREE"
                        if dice_roll(6) == 1 else "" }"
                + "\n"
                ),
]

# This rolls 2d6 for the ammount of rooms, but also rolls a d20 with a
# possibility for half or double the dice
preset_dungeon = [
    MagicString(lambda: (
                "THREE Dungeon with the following rooms:\n"
                + "".join(f"{secret_room[0]}"
                            for _ in range(dice_roll(6, 2, True)))
                )),
]

# You need to add to this dict any lists you want users to have access to when
# running the command
TABLES = {
    "LETTERS": list_Letters,
    "THINGS": list_things,
    "THREE": list_three,
}

# Here you add any secret lists that shouldn't be accessed directly by users
SECRETS = {
    "sROOM": secret_room,
    "sA-O-ROOM": secret_roomAmount,
}

# Presets that take advantage of the  lists in TABLES and SECRETS to generate
# compound things. This exists only if you are implementing tables that exist
# already in a book so you can organize presets you've made that use those
# tables, compared to "presets" provided by the resource you're using.
PRESETS = {
    "pDUNGEON": preset_dungeon,
}

masterTable: dict[str, list[Any]] = {}
masterTable.update(TABLES)
masterTable.update(SECRETS)
masterTable.update(PRESETS)
