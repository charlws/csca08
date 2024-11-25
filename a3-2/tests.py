"""
CSCA08: Winter 2024 -- Assignment 3: Wacky's Michelin Restaurant

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.
"""

import unittest
import restaurant

class TestRestaurant(unittest.TestCase):
    def test_get_restaurant_name_valid(self):
        self.assertEqual(restaurant.get_restaurant_name(), "Wacky's Restaurant")

class TestIsValidItem(unittest.TestCase):
    def test_general_case_1(self):
        '''Test general case with HAMBURGER.'''
        actual = restaurant.is_valid_item("HAMBURGER")
        expected = True
        self.assertEqual(actual, expected)

    def test_general_case_2(self):
        '''Test general case with HOT DOG.'''
        actual = restaurant.is_valid_item("HOT DOG")
        expected = True
        self.assertEqual(actual, expected)
    
    def test_missing_space(self):
        '''Test missing space in HOT DOG.'''
        actual = restaurant.is_valid_item("HOTDOG")
        expected = False
        self.assertEqual(actual, expected)

    def test_invalid_case_1(self):
        '''Test full lower case.'''
        actual = restaurant.is_valid_item("soda")
        expected = False
        self.assertEqual(actual, expected)

    def test_invalid_case_2(self):
        '''Test mixed case.'''
        actual = restaurant.is_valid_item("fRiEs")
        expected = False
        self.assertEqual(actual, expected)

    def test_empty_string(self):
        '''Test empty string.'''
        actual = restaurant.is_valid_item("")
        expected = False
        self.assertEqual(actual, expected)
    
    def test_partial_string(self):
        '''Test only part of item string is provided.'''
        actual = restaurant.is_valid_item("HAMB")
        expected = False
        self.assertEqual(actual, expected)
    
    def test_extra_string(self):
        '''Test item starting with a valid item but contains
            extra content is provided.'''
        actual = restaurant.is_valid_item("HAMBURGER FRIES")
        expected = False
        self.assertEqual(actual, expected)

class TestCanBeCombo(unittest.TestCase):
    def test_general_case(self):
        '''Test general case with HAMBURGER.'''
        actual = restaurant.can_be_combo("HAMBURGER")
        expected = True
        self.assertEqual(actual, expected)
    
    def test_not_combo_item(self):
        '''Test not combo item.'''
        actual = restaurant.can_be_combo("FRIES")
        expected = False
        self.assertEqual(actual, expected)
    
    def test_lower_case(self):
        '''Test lower case item.'''
        actual = restaurant.can_be_combo("hamburger")
        expected = False
        self.assertEqual(actual, expected)
    
    def test_mixed_case(self):
        '''Test mixed case item.'''
        actual = restaurant.can_be_combo("hAmBuRgEr")
        expected = False
        self.assertEqual(actual, expected)
    
    def test_empty_string(self):
        '''Test empty string.'''
        actual = restaurant.can_be_combo("")
        expected = False
        self.assertEqual(actual, expected)

class TestCalculateItemPrice(unittest.TestCase):
    def test_general_case(self):
        '''Test general case with 3 HAMBURGER.'''
        actual = restaurant.calculate_item_price("HAMBURGER", 3)
        expected = 52.5
        self.assertEqual(actual, expected)

    def test_invalid_item_1(self):
        '''Test invalid item name.'''
        actual = restaurant.calculate_item_price("HAM", 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_invalid_item_2(self):
        '''Test invalid item name (wrong case).'''
        actual = restaurant.calculate_item_price("hamburger", 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_invalid_item_3(self):
        '''Test invalid item name (wrong case).'''
        actual = restaurant.calculate_item_price("hAmBurGeR", 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_empty_item(self):
        '''Test empty item name.'''
        actual = restaurant.calculate_item_price("", 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_negative_amount(self):
        '''Test negative amount.'''
        actual = restaurant.calculate_item_price("HAMBURGER", -1)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_zero_amount(self):
        '''Test zero amount.'''
        actual = restaurant.calculate_item_price("HAMBURGER", 0)
        expected = 0.0
        self.assertEqual(actual, expected)
    
class TestCalculateItemCost(unittest.TestCase):
    def test_general_case_1(self):
        '''Test general case with 3 HAMBURGER.'''
        actual = restaurant.calculate_item_cost("HAMBURGER", 3)
        expected = 10.5
        self.assertEqual(actual, expected)

    def test_general_case_2(self):
        '''Test general case with 3 HOT DOG.'''
        actual = restaurant.calculate_item_cost("HOT DOG", 3)
        expected = 7.5
        self.assertEqual(actual, expected)

    def test_invalid_item_1(self):
        '''Test invalid item name.'''
        actual = restaurant.calculate_item_cost("HAM", 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_invalid_item_2(self):
        '''Test invalid item name (wrong case).'''
        actual = restaurant.calculate_item_cost("hamburger", 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_invalid_item_3(self):
        '''Test invalid item name (wrong case).'''
        actual = restaurant.calculate_item_cost("hAmBurGeR", 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_empty_item(self):
        '''Test empty item name.'''
        actual = restaurant.calculate_item_cost("", 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_negative_amount(self):
        '''Test negative amount.'''
        actual = restaurant.calculate_item_cost("HAMBURGER", -1)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_zero_amount(self):
        '''Test zero amount.'''
        actual = restaurant.calculate_item_cost("HAMBURGER", 0)
        expected = 0.0
        self.assertEqual(actual, expected)

class TestCalculateComboPrice(unittest.TestCase):
    def test_general_case_1(self):
        '''Test general case with 3 HAMBURGER.'''
        actual = restaurant.calculate_combo_price("HAMBURGER", 3)
        expected = 78.0
        self.assertEqual(actual, expected)

    def test_general_case_2(self):
        '''Test general case with 3 HOT DOG.'''
        actual = restaurant.calculate_combo_price("HOT DOG", 3)
        expected = 57.0
        self.assertEqual(actual, expected)

    def test_non_combo_item(self):
        '''Test the case where item is not combo-able.'''
        actual = restaurant.calculate_combo_price("FRIES", 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_invalid_item_1(self):
        '''Test invalid item name.'''
        actual = restaurant.calculate_combo_price("HAM", 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_invalid_item_2(self):
        '''Test invalid item name (wrong case).'''
        actual = restaurant.calculate_combo_price("hamburger", 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_invalid_item_3(self):
        '''Test invalid item name (wrong case).'''
        actual = restaurant.calculate_combo_price("hAmBurGeR", 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_empty_item(self):
        '''Test empty item name.'''
        actual = restaurant.calculate_combo_price("", 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_negative_amount(self):
        '''Test negative amount.'''
        actual = restaurant.calculate_combo_price("HAMBURGER", -1)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_zero_amount(self):
        '''Test zero amount.'''
        actual = restaurant.calculate_combo_price("HAMBURGER", 0)
        expected = 0.0
        self.assertEqual(actual, expected)

class TestCalculateComboCost(unittest.TestCase):
    def test_general_case_1(self):
        '''Test general case with 3 HAMBURGER.'''
        actual = restaurant.calculate_combo_cost("HAMBURGER", 3)
        expected = 22.5
        self.assertEqual(actual, expected)

    def test_general_case_2(self):
        '''Test general case with 3 HOT DOG.'''
        actual = restaurant.calculate_combo_cost("HOT DOG", 3)
        expected = 19.5
        self.assertEqual(actual, expected)

    def test_non_combo_item(self):
        '''Test the case where item is not combo-able.'''
        actual = restaurant.calculate_combo_cost("FRIES", 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_invalid_item_1(self):
        '''Test invalid item name.'''
        actual = restaurant.calculate_combo_cost("HAM", 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_invalid_item_2(self):
        '''Test invalid item name (wrong case).'''
        actual = restaurant.calculate_combo_cost("hamburger", 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_invalid_item_3(self):
        '''Test invalid item name (wrong case).'''
        actual = restaurant.calculate_combo_cost("hAmBurGeR", 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_empty_item(self):
        '''Test empty item name.'''
        actual = restaurant.calculate_combo_cost("", 3)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_negative_amount(self):
        '''Test negative amount.'''
        actual = restaurant.calculate_combo_cost("HAMBURGER", -1)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_zero_amount(self):
        '''Test zero amount.'''
        actual = restaurant.calculate_combo_cost("HAMBURGER", 0)
        expected = 0.0
        self.assertEqual(actual, expected)

class TestGetItemFromSentence(unittest.TestCase):
    def test_general_case_1(self):
        '''Test general non-combo case in first format.'''
        actual = restaurant.get_item_from_sentence("Please give me a FRIES.")
        expected = "FRIES"
        self.assertEqual(actual, expected)

    def test_general_case_2(self):
        '''Test general combo case in first format.'''
        actual = restaurant.get_item_from_sentence("Please give me a combo of HOT DOG.")
        expected = "COMBO HOT DOG"
        self.assertEqual(actual, expected)

    def test_general_case_3(self):
        '''Test general non-combo case in second format.'''
        actual = restaurant.get_item_from_sentence("Can I have a HAMBURGER?")
        expected = "HAMBURGER"
        self.assertEqual(actual, expected)
        
    def test_general_case_4(self):
        '''Test general combo case in second format.'''
        actual = restaurant.get_item_from_sentence("Can I have a HAMBURGER combo?")
        expected = "COMBO HAMBURGER"
        self.assertEqual(actual, expected)
        
    def test_general_invalid(self):
        '''Test general invalid setence.'''
        actual = restaurant.get_item_from_sentence("Who is Purva?")
        expected = "UNKNOWN"
        self.assertEqual(actual, expected)

    def test_invalid_item_1(self):
        '''Test invalid item in first format.'''
        actual = restaurant.get_item_from_sentence("Please give me a combo of Purva.")
        expected = "UNKNOWN"
        self.assertEqual(actual, expected)
        
    def test_invalid_item_2(self):
        '''Test invalid item in second format.'''
        actual = restaurant.get_item_from_sentence("Can I have a Purva?")
        expected = "UNKNOWN"
        self.assertEqual(actual, expected)
        
    def test_invalid_combo_1(self):
        '''Test invalid combo in first format.'''
        actual = restaurant.get_item_from_sentence("Please give me a FRIES combo.")
        expected = "UNKNOWN"
        self.assertEqual(actual, expected)
        
    def test_invalid_combo_2(self):
        '''Test invalid combo in second format.'''
        actual = restaurant.get_item_from_sentence("Can I have a FRIES combo?")
        expected = "UNKNOWN"
        self.assertEqual(actual, expected)

    def test_bad_combo_format_1(self):
        '''Test bad combo format in first format.'''
        actual = restaurant.get_item_from_sentence("Please give me a combo HAMBURGER.")
        expected = "UNKNOWN"
        self.assertEqual(actual, expected)

    def test_bad_combo_format_2(self):
        '''Test bad combo format in second format.'''
        actual = restaurant.get_item_from_sentence("Can I have a combo HAMBURGER?")
        expected = "UNKNOWN"
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
