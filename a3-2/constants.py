"""
CSCA08: Winter 2024 -- Assignment 3: Wacky's Michelin Restaurant

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.
"""

# This is a dictionary mapping between menu item and their ingredients.
MENU_ITEM_INGREDIENTS = {
    'HAMBURGER': [
        'HAMBURGER PATTY',
        'LETTUCE',
        'HAMBURGER BUN'
    ],
    'HOT DOG': [
        'HOT DOG',
        'HOT DOG BUN'
    ],
    'FRIES': [
        'FRIES'
    ],
    'SODA': [
        'SODA'
    ]
}

MENU_ITEM_COSTS = {
    'HAMBURGER': 17.50,
    'HOT DOG': 10.50,
    'FRIES': 7.50,
    'SODA': 2.00
}

# This is a dictionary mapping between ingredients and their cost.
INGREDIENT_COSTS = {
    'HAMBURGER PATTY': 2.50,
    'LETTUCE': 0.50,
    'HAMBURGER BUN': 0.50,
    'HOT DOG': 2.25,
    'HOT DOG BUN': 0.25,
    'FRIES': 3.00,
    'SODA': 1.00
}

# These are the items included in combos.
ITEMS_IN_COMBO = [
    'FRIES', 'SODA'
]

# These are the items that can be a combo.
# This will never include any item that is included in a combo.
COMBO_ITEM_PRICES = {
    'HAMBURGER': 26.00,
    'HOT DOG': 19.00,
}
