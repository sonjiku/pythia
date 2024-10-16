""" Utilities """
import random
import re
from typing import Callable
from typing import Any

class MagicString:
    def __init__(self, generator: Callable[[], str]) -> None:
        self.generator = generator

    def get(self) -> str:
        return self.generator()

    def __repr__(self) -> str:
        return self.get()  # Call the get method to return the string value


def dice_roll (diesides: int, amount: int=1, crits: bool=False, crit_weight: int = 2) ->int:
    result: int = 0 
    if crits is True:
        critroll = random.randint(1,20)
        if critroll == 1 :
            amount = max(1, int(amount/crit_weight))
        elif critroll == 20:
            amount = int(amount*crit_weight)

    for _ in range(amount):
        result = result + random.randint(1,diesides)
    return result
    
def randomize_pick(master_table: dict[str,list[Any]],
                   list_name: str) ->str:
    # Access the dictionary by name
    if list_name in master_table:
        current_list = master_table[list_name]
    else:
        return f"List '{list_name}' not found."
    random_element = str(random.choice(current_list))

    # Check if the value is another dictionary,
    # if so, call the function recursively.
    for possible_ref in master_table.keys():
        while possible_ref in random_element:
            # Access the referenced dictionary
            referenced_value = randomize_pick(master_table, possible_ref)
            random_element = re.sub(possible_ref, f"{referenced_value}",
                                    random_element, 1)
    return random_element


def print_table(master_table: dict[str, Any]):
    """ haha """
    i = 1
    for table_name in master_table:
        print(f"{i}: {table_name}")
        i = i+1


def print_random_pick(master_table: dict[str,list[Any]],
                      list_name: str) ->None:
    """ haha """
    table_element = randomize_pick(master_table, list_name)
    print(f"{list_name}: {table_element}")
    print("---------")


def print_random_pick_indexcheck(master_table: dict[str,list[Any]],
                                 primary_table:  dict[str,list[Any]],
                                 list_name: Any) ->None:
    """ haha """
    if list_name.isdigit():
        index_p = int(list_name)
        max_index = len(primary_table) + 1
        if index_p in range(max_index):
            i = 1
            for each_table in primary_table:
                if i == index_p:
                    print_random_pick(master_table, each_table)
                    break
                i = i+1
        else:
            print(f"{list_name} is out of range.")
            print("---------")
    else:
        print_random_pick(master_table, list_name)


def print_random_all(master_table: dict[str,list[Any]]):
    """ haha """
    for list_name in master_table:
        print_random_pick(master_table, list_name)


# Helper function to find the name of the dictionary from its value
def dict_key_from_value(dict: dict[Any, Any], dict_value: Any) -> Any:
    for key, value in dict.items():
        if value is dict_value:
            return key
    return None
