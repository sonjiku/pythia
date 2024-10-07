import random  # noqa # pylint: disable=unused-import
from pythia.util import MagicString, dice_roll# noqa # pylint: disable=unused-import
from typing import Any

list_activities = [""]
list_animals = [""]
list_archetypes = [""]
list_assets = [""]
list_books = [""]
list_buildings = [""]
list_careers = [""]
list_carousing = [""]
list_chaosSpells = [""]
list_cityEvents = [""]
list_cityThemes = [""]
list_clothing = [""]
list_colors = [""]
list_decorations = [""]
list_delusions = [""]
list_delveShifts = [""]
list_disasters = [""]
list_domains = [""]
list_dungeons = [""]
list_dungeonHazards = [""]
list_effects = [""]
list_elements = [""]
list_femaleNames = [""]
list_fabrics = [""]
list_factionTraits = [""]
list_factions = [""]
list_food = [""]
list_foodTraits = [""]
list_forms = [""]
list_goals = [""]
list_hazards = [""]
list_hexcrawl = [""]
list_ingredients = [""]
list_innNameOne = [""]
list_innNameTwo = [""]
list_itemTraits = [""]
list_liabilities = [""]
list_locations = [""]
list_maleNames = [""]
list_magicSchools = [""]
list_mannerisms = [""]
list_materials = [""]
list_mechanisms = [""]
list_miscItems = [""]
list_missions = [""]
list_monsterTraits = [""]
list_monsters = [""]
list_mutations = [""]
list_npcDetails = [""]
list_npcReactions = [""]
list_organs = [""]
list_personalities = [""]
list_placeTraits = [""]
list_potions = [""]
list_powers = [""]
list_professions = [""]
list_qualities = [""]
list_relationships = [""]
list_rewards = [""]
list_roomDetails = [""]
list_roomThemes = [""]
list_rooms = [""]
list_scents = [""]
list_signs = [""]
list_sounds = [""]
list_spells = [""]
list_streetDetails = [""]
list_structures = [""]
list_surnameOne = [""]
list_surnameTwo = [""]
list_symbols = [""]
list_tactics = [""]
list_tastes = [""]
list_textures = [""]
list_tools = [""]
list_trapEffects = [""]
list_travelHazards = [""]
list_travelShifts = [""]
list_treasures = [""]
list_weaknesses = [""]
list_weapons = [""]
list_weather = [""]
list_wizardNames = [""]



preset_surname = [
    "SURNAME-ONESURNAME-TWO"
]

preset_innName = [
    "INN-NAME-ONE INN-NAME-TWO"
]

preset_food = [
    "TRAITS-FOOD FOODS"
]
preset_clothes = [
    "FABRICS CLOTHING",
]

preset_city = [
    "A city of CITY-THEMES. EVENT: CITY-EVENTS.",
]

preset_triplemechanismtrap = [
    "A trap that uses: MECHANISMS, MECHANISMS and MECHANISMS."
]

secret_room = [
    MagicString(lambda:
                "ROOM-THEMES room with ROOM-DETAILS in it."
                + f"{" Delve Shift: DELVE-SHIFTS"
                        if dice_roll(6) == 1 else "" }"
                + "\n"),
]

preset_dungeon = [
    MagicString(lambda: (
                "DUNGEONS dungeon with the following rooms:\n"
                + "".join(f"{secret_room[0]}"
                            for _ in range(dice_roll(6, 2, True)))
                )),
]


secret_ingredient = [
    MagicString(lambda: "".join(
                    f"{dice_roll(4, 2)} INGREDIENTS, "
                    for _ in range(dice_roll(4, 2, True))
                    )),
]


preset_potion = [
    "\nIngredients: sINGREDIENT"
    + "\n"
    + "Potion of "
    + "POTIONS"
    + "\nColor: COLORS"
    + "\nScent: SCENTS"
    + "\nTaste: TASTES"
    + "\nTexture: TEXTURES",
    "\nIngredients: sINGREDIENT"
    + "\n"
    + "Potion of "
    + "DELUSIONS"
    + "\nColor: COLORS"
    + "\nScent: SCENTS"
    + "\nTaste: TASTES"
    + "\nTexture: TEXTURES",
    "\nIngredients: sINGREDIENT"
    + "\n"
    + "Potion of "
    + "MUTATIONS"
    + "\nColor: COLORS"
    + "\nScent: SCENTS"
    + "\nTaste: TASTES"
    + "\nTexture: TEXTURES",
    "\nIngredients: sINGREDIENT"
    + "\n"
    + "QUALITIES "
    + "potion of "
    + "POTIONS"
    + "\nColor: COLORS"
    + "\nScent: SCENTS"
    + "\nTaste: TASTES"
    + "\nTexture: TEXTURES",
    "\nIngredients: sINGREDIENT"
    + "\n"
    + "QUALITIES "
    + "potion of "
    + "DELUSIONS"
    + "\nColor: COLORS"
    + "\nScent: SCENTS"
    + "\nTaste: TASTES"
    + "\nTexture: TEXTURES",
    "\nIngredients: sINGREDIENT"
    + "\n"
    + "QUALITIES "
    + "potion of "
    + "MUTATIONS"
    + "\nColor: COLORS"
    + "\nScent: SCENTS"
    + "\nTaste: TASTES"
    + "\nTexture: TEXTURES"
]

TABLES: dict[str, list[str]] = {
    "ACTIVITIES": list_activities,
    "ANIMALS": list_animals,
    "ARCHETYPES": list_archetypes,
    "ASSETS": list_assets,
    "BOOKS": list_books,
    "BUILDINGS": list_buildings,
    "CAREERS": list_careers,
    "CAROUSING": list_carousing,
    "CHAOSS-PELLS": list_chaosSpells,
    "CITY-EVENTS": list_cityEvents,
    "CITY-THEMES": list_cityThemes,
    "CLOTHING": list_clothing,
    "COLORS": list_colors,
    "DECORATIONS": list_decorations,
    "DELUSIONS": list_delusions,
    "DELVE-SHIFTS": list_delveShifts,
    "DISASTERS": list_disasters,
    "DOMAINS": list_domains,
    "DUNGEONS": list_dungeons,
    "DUNGEON-HAZARDS": list_dungeonHazards,
    "EFFECTS": list_effects,
    "ELEMENTS": list_elements,
    "FEMALE-NAMES": list_femaleNames,
    "FABRICS": list_fabrics,
    "FACTIONT-RAITS": list_factionTraits,
    "FACTIONS": list_factions,
    "FOODS": list_food,
    "TRAITS-FOOD": list_foodTraits,
    "FORMS": list_forms,
    "GOALS": list_goals,
    "HAZARDS": list_hazards,
    "HEXCRAWL": list_hexcrawl,
    "INGREDIENTS": list_ingredients,
    "INN-NAME-ONE": list_innNameOne,
    "INN-NAME-TWO": list_innNameTwo,
    "ITEM-TRAITS": list_itemTraits,
    "LIABILITIES": list_liabilities,
    "LOCATIONS": list_locations,
    "MALE-NAMES": list_maleNames,
    "MAGIC-SCHOOLS": list_magicSchools,
    "MANNERISMS": list_mannerisms,
    "MATERIALS": list_materials,
    "MECHANISMS": list_mechanisms,
    "MISC-ITEMS": list_miscItems,
    "MISSIONS": list_missions,
    "MONSTER-TRAITS": list_monsterTraits,
    "MONSTERS": list_monsters,
    "MUTATIONS": list_mutations,
    "NPC-DETAILS": list_npcDetails,
    "NPC-REACTIONS": list_npcReactions,
    "ORGANS": list_organs,
    "PERSONALITIES": list_personalities,
    "PLACE-TRAITS": list_placeTraits,
    "POTIONS": list_potions,
    "POWERS": list_powers,
    "PROFESSIONS": list_professions,
    "QUALITIES": list_qualities,
    "RELATIONSHIPS": list_relationships,
    "REWARDS": list_rewards,
    "ROOM-DETAILS": list_roomDetails,
    "ROOM-THEMES": list_roomThemes,
    "ROOMS": list_rooms,
    "SCENTS": list_scents,
    "SIGNS": list_signs,
    "SOUNDS": list_sounds,
    "SPELLS": list_spells,
    "STREET-DETAILS": list_streetDetails,
    "STRUCTURES": list_structures,
    "SURNAME-ONE": list_surnameOne,
    "SURNAME-TWO": list_surnameTwo,
    "SYMBOLS": list_symbols,
    "TACTICS": list_tactics,
    "TASTES": list_tastes,
    "TEXTURES": list_textures,
    "TOOLS": list_tools,
    "TRAP-EFFECTS": list_trapEffects,
    "TRAVEL-HAZARDS": list_travelHazards,
    "TRAVEL-SHIFTS": list_travelShifts,
    "TREASURES": list_treasures,
    "WEAKNESSES": list_weaknesses,
    "WEAPONS": list_weapons,
    "WEATHER": list_weather,
    "WIZARD-NAMES": list_wizardNames,
}

SECRETS = {
    "sROOM": secret_room,
    "sINGREDIENT": secret_ingredient,
}

PRESETS = {
    "pSURNAME": preset_surname,
    "pINNNAME": preset_innName,
    "pFOOD": preset_food,
    "pCLOTHES": preset_clothes,
    "pDUNGEON": preset_dungeon,
    "pPOTION": preset_potion,
    "pCITY": preset_city,
    "pTRAP": preset_triplemechanismtrap,
}

masterTable: dict[str, list[Any]] = {}
masterTable.update(TABLES)
masterTable.update(SECRETS)
masterTable.update(PRESETS)
