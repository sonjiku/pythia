""" Utilities """
import random
import re


def randomize_pick(master_table, tables_table, table_name):
    """
    eg.
    food = access_random_key(AllEvankTables, TableEvankFood)
    """

    # Access the dictionary by name
    if table_name in tables_table:
        current_dict = tables_table[table_name]
        table_type = current_dict[0]
    else:
        return f"Table '{table_name}' not found.", "Error"
    valid_keys = [key for key in current_dict.keys() if key > 0]
    random_key = random.choice(valid_keys)  # Ensure no key is 0
    random_value = current_dict[random_key]

    # print(f"Accessed {tableName}[{randomKey}]") # debug

    # Check if the value is another dictionary,
    # if so, call the function recursively.
    for possible_ref in master_table.keys():
        if possible_ref in random_value:
            # Access the referenced dictionary
            referenced_value, _ = randomize_pick(master_table, master_table, possible_ref)
            random_value = re.sub(possible_ref,
                                  f"{referenced_value}",
                                  random_value)

    return random_value, table_type


def print_table(tables_table):
    """ haha """
    i = 1
    for table_name in tables_table:
        print(f"{i}: {table_name}")
        i = i+1


def print_random_pick_noindexcheck(master_table, tables_table, table_name):
    """ haha """
    table_element, value_type = randomize_pick(master_table,
                                               tables_table,
                                               table_name)
    print(f"{value_type}: {table_element}")
    print("---------")


def print_random_pick(master_table, tables_table, table_name):
    """ haha """
    if table_name.isdigit():
        index_p = int(table_name)
        max_index = len(tables_table) + 1
        if index_p in range(max_index):
            i = 1
            for each_table in tables_table:
                if i == index_p:
                    print_random_pick_noindexcheck(master_table, tables_table, each_table)
                    break
                i = i+1
        else:
            print(f"{table_name} is out of range.")
            print("---------")
    else:
        print_random_pick_noindexcheck(master_table, tables_table, table_name)


def print_random_all(master_table, tables_table):
    """ haha """
    for table_name in tables_table:
        print_random_pick(master_table, tables_table, table_name)


# Helper function to find the name of the dictionary from its value
def dict_name_from_value(tables_table, dictionary_value):
    """ haha """
    for name, dictionary in tables_table.items():
        if dictionary is dictionary_value:
            return name
    return None
