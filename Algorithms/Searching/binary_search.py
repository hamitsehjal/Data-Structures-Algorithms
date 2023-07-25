""" Binary Search using Iterative and Recursive Approach"""


class BinarySearch():
    ''' class provides methods for looking up elements using Binary Search'''

    def search_iterative(self, item_list, item):
        '''
        Iteratively searches for an item within a sorted list using binary search algorithm
        '''
        # low and high keep track of which part of the list you'll search in.
        low = 0
        high = len(item_list)-1

        while low <= high:
            # Calculate the middle index
            mid = (low+high) // 2
            # Get the element at middle index
            guess = item_list[mid]
            # Found the element
            if item == guess:
                return mid
            # Guess too High
            if item < guess:
                high = mid-1
            # Guess too low
            else:
                low = mid+1

        # Not Found
        return None

    def search_recursive(self, item_list, low, high, item):
        """Recursive implementation of binary search."""

        # Check base condition
        if low <= high:
            mid = (low + high)//2
            guess = item_list[mid]

            if guess == item:
                return mid
            if guess > item:
                # Too high
                high = mid-1
                return self.search_recursive(item_list, low, high, item)
            # Too low
            low = mid+1
            return self.search_recursive(item_list, low, high, item)
        # NOT FOUND
        return None


if __name__ == "__main__":
    # We must initialize the class to use the methods of this class
    bs = BinarySearch()
    my_list = [1, 3, 5, 7, 9]

    print(bs.search_iterative(my_list, 3))  # => 1

    # 'None' means nil in Python. We use to indicate that the item wasn't found.
    print(bs.search_iterative(my_list, -1))  # => None
