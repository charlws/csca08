"""
CSCA08: Winter 2024 -- Assignment 3: Wacky's Michelin Restaurant

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.
"""
from constants import (MENU_ITEM_INGREDIENTS, MENU_ITEM_COSTS,
                       INGREDIENT_COSTS, COMBO_ITEM_PRICES, ITEMS_IN_COMBO)


def get_restaurant_name() -> str:
    """
    Returns the string "Wacky's Restaurant".

    Note: This is just an utility function that you can play around with.
    This function will not be marked.

    >>> get_restaurant_name()
    "Wacky's Restaurant"
    """
    return "Wacky's Restaurant"


def is_valid_item(item_name: str) -> bool:
    """
    Return True if and only if the given name of an item 'item_name'
    represents a valid item sold by the restaurant.

    >>> is_valid_item('HAMBURGER')
    True
    >>> is_valid_item('WATER')
    False
    """
    return item_name in MENU_ITEM_INGREDIENTS


def can_be_combo(item_name: str) -> bool:
    """
    Return True if and only if the given name of an item 'item_name'
    represents a valid combo item sold by the restaurant.

    >>> can_be_combo('HAMBURGER')
    True
    >>> can_be_combo('FRIES')
    False
    """
    return item_name in COMBO_ITEM_PRICES


def calculate_item_price(item_name: str, amount: int) -> float:
    """
    Calculate and return the total price based on a given item's name
    'item_name' and the quantity 'amount'.

    >>> calculate_item_price('HAMBURGER', 3)
    52.5
    >>> calculate_item_price('WATER', -3)
    0.0
    """
    if (not is_valid_item(item_name)) or (amount <= 0):
        return 0.0
    unit_price = MENU_ITEM_COSTS[item_name]
    total_price = float(unit_price * amount)
    return total_price


def calculate_item_cost(item_name: str, amount: int) -> float:
    """
    Calculate and return the total cost based on a given item's name
    'item_name' and the quantity 'amount'.

    >>> calculate_item_cost('HAMBURGER', 3)
    10.5
    >>> calculate_item_cost('WATER', -3)
    0.0
    """
    if (not is_valid_item(item_name)) or (amount <= 0):
        return 0.0
    ingredients = MENU_ITEM_INGREDIENTS[item_name]
    total_unit_cost = 0
    for ingredient in ingredients:
        ingredient_cost = INGREDIENT_COSTS[ingredient]
        total_unit_cost = total_unit_cost + ingredient_cost
    total_price = float(total_unit_cost * amount)
    return total_price


def calculate_combo_price(combo_item_name: str, amount: int) -> float:
    """
    Calculate and return the total price based on a given combo item's
    name 'combo_item_name' and the quantity 'amount'.

    >>> calculate_combo_price('HAMBURGER', 3)
    78.0
    >>> calculate_combo_price('PIZZA', -3)
    0.0
    """
    if (not can_be_combo(combo_item_name)) or (amount <= 0):
        return 0.0
    unit_price = COMBO_ITEM_PRICES[combo_item_name]
    total_price = float(unit_price * amount)
    return total_price


def calculate_combo_cost(combo_item_name: str, amount: int) -> float:
    """
    Calculate and return the total cost based on a given combo item's
    name 'combo_item_name' and the quantity 'amount'.

    >>> calculate_combo_cost('HAMBURGER', 3)
    22.5
    >>> calculate_combo_cost('PIZZA', -3)
    0.0
    """
    if (not can_be_combo(combo_item_name)) or (amount <= 0):
        return 0.0
    total_cost = calculate_item_cost(combo_item_name, amount)
    for item in ITEMS_IN_COMBO:
        total_cost = total_cost + calculate_item_cost(item, amount)
    return total_cost


def get_item_from_sentence(customer_sentence: str) -> str:
    """
    Extract and return the name of the item the customer is ordering from
    their request sentence 'customer_sentence'.

    >>> get_item_from_sentence("Please give me a FRIES.")
    'FRIES'
    >>> get_item_from_sentence("Can I have a HAMBURGER combo?")
    'COMBO HAMBURGER'
    >>> get_item_from_sentence("Please give me a WATER.")
    'UNKNOWN'
    >>> get_item_from_sentence("Where is the washroom?")
    'UNKNOWN'
    """
    for menu_item in MENU_ITEM_COSTS:
        valid_normal_phrases = [
            "Please give me a " + menu_item + ".",
            "Can I have a " + menu_item + "?"
        ]

        if customer_sentence in valid_normal_phrases:
            return menu_item

    for combo_menu_item in COMBO_ITEM_PRICES:
        valid_combo_phrases = [
            "Please give me a combo of " + combo_menu_item + ".",
            "Can I have a " + combo_menu_item + " combo?"
        ]

        if customer_sentence in valid_combo_phrases:
            return "COMBO " + combo_menu_item

    return "UNKNOWN"


if __name__ == '__main__':
    import doctest
    doctest.testmod()
