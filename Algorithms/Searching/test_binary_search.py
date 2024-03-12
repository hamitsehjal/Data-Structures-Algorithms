""" Testing binary_search module"""
import unittest
import json
import time
from binary_search import BinarySearch

bs = BinarySearch()

# Unloading all lists from a file
with open("items.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Setting values to created variables
simple_list = data["simple_list"]
list_with_10_items = data["list_with_10_items"]
list_with_100_items = data["list_with_100_items"]
list_with_1000_items = data["list_with_1000_items"]


# Test cases to test Binary Search algorithm
class TestBinarySearch(unittest.TestCase):
    '''
        class defining methods for Testing binary_search module
    '''

    def setUp(self):
        print(f".......... {self._testMethodName}")

    def test_iterative_binary_search_with_simple_list(self):
        '''Checking the implementation of iterative binary search'''
        # ARRANGE
        # You can check the index of each item in the items.json file
        item, expected_index = 3, 1

        # ACT
        # Run the method we created and get the index of the item we were looking for
        index = bs.search_iterative(simple_list, item)  # => 1

        # ASSERT
        # Compare the resulting index with the expected index
        self.assertEqual(expected_index, index)  # => 1 == 1

    def test_recursive_binary_search_with_simple_list(self):
        '''Checking the implementation of recursive binary search'''
        item, expected_index = 3, 1
        # To run recursive search for an item,
        # we need to determine the minimum and maximum indexes of the list
        low, high = 0, len(simple_list) - 1

        index = bs.search_recursive(simple_list, low, high, item)

        self.assertEqual(expected_index, index)

    def test_search_for_nonexistent_item(self):
        '''Specifically set a number that is not in the list'''
        item, expected_result = 100, None

        # Trying to find an item that doesn't exist
        index = bs.search_iterative(simple_list, item)  # => None

        self.assertEqual(expected_result, index)

    def test_binary_search_and_linear_search_execution_time(self):
        '''
            execution times for binary_search and linear_search
        '''
        item, expected_index = 9887, 990

        # Time required to search
        start_time = time.perf_counter()
        binary_search_index = bs.search_iterative(
            list_with_1000_items, item)  # => None
        bs_time = time.perf_counter() - start_time

        # list.index(x) return the index in the list of the first item whose value is x.
        # It is an error if there is no such item.
        # Complexity of list.index(x) is O(n)
        start_time = time.perf_counter()
        linear_search_index = list_with_1000_items.index(item)
        ls_time = time.perf_counter() - start_time

        self.assertEqual(expected_index, binary_search_index)
        self.assertEqual(expected_index, linear_search_index)
        self.assertTrue(bs_time < ls_time)

        print("--- ******START OF TEST****** ---")
        print("--- Time required to search item at the ending ---")
        print(f"--- Linear Search {ls_time:.6f} seconds ---")
        print(f"--- Binary Search {bs_time:.6f} seconds ---")
        print("--- ******END OF TEST****** ---\n")

    def test_execution_time_for_item_at_the_beginning(self):
        '''
            Test Execution time for item at the beginning
                - comparing binary vs linear
        '''
        item, expected_index = 7, 0

        # Binary search - time required to search
        start_time = time.perf_counter()
        binary_search_index = bs.search_iterative(
            list_with_1000_items, item)  # => None
        bs_time = time.perf_counter() - start_time

        # Linear search - time required to search
        start_time = time.perf_counter()
        linear_search_index = list_with_1000_items.index(item)
        ls_time = time.perf_counter() - start_time

        self.assertEqual(expected_index, binary_search_index)
        self.assertEqual(expected_index, linear_search_index)

        # linear search will be faster, since the item we are looking for
        # is at the beginning of the list
        self.assertTrue(bs_time > ls_time)
        print("--- ******START OF TEST****** ---")
        print("--- Time required to search item at the beginning ---")
        print(f"--- Linear Search {ls_time:.6f} seconds ---")
        print(f"--- Binary Search {bs_time:.6f} seconds ---")
        print("--- ******END OF TEST****** ---\n")


if __name__ == '__main__':
    unittest.main()
