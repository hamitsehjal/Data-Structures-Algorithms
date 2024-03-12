# Chapter 2 (Selection Sort)

- Run times for common operations on arrays and lists:

    1. Reading:
        - Array: O(1) constant run time
        - List: O(n) linear run time

    2. Insertion:
        - Array: O(n) linear run time
        - List: O(1) constant run time

    3. Deletion:
        - Array: O(n) linear run time
        - List: O(1) constant run time

    *Note: Insertion and deletion are O(1) - constant run time only if you can instantly access the element to be deleted.

## Which is a better choice (Array or List) ??

1. Inserting into the middle of the list:
   - With `LIST`, it's easy as changing what the previous item points to.
   - With `ARRAY`, we have to shift all the rest of the elements down.
   - `LIST` is a better choice if you want to insert elements into the middle.

2. Deletion:
   - `LIST` is a better choice again since it is easy as changing what the previous item points to.

## Important Question from Grokking Algorithms Book:

People sign up for Facebook pretty often, too. Suppose you decided to use an array to store the list of users. What are the downsides of an array for inserts? In particular, suppose you’re using binary search to search for logins. What happens when you add new users to an array?

Possible Downsides of Using an Array for Storing Usernames with Binary Search:
1. Insertion Complexity:
   - Since we need to maintain the sorted order for binary search, we must find the position to insert new elements (similar to linked lists). However, with arrays, this process involves shifting elements to make space for the new element, resulting in a time complexity of O(n) in the worst-case scenario. This can be a significant performance drawback, especially with frequent insertions.

2. Array Resizing:
   - As new users sign up, the array will eventually run out of capacity. Consequently, we need to resize the array, which includes the process of creating a new, larger array and copying the existing elements to it. This resizing process can negatively impact overall performance, particularly if it happens frequently.

3. Memory Overhead:
   - Arrays require contiguous memory allocation, meaning memory chunks for arrays are allocated in a single continuous block. As new users sign up and the array grows, this can lead to inefficient memory utilization due to possible fragmentation.

## Hybrid Data Structure (Array of LinkedList) vs Arrays vs LinkedList

### Insertion:
1. Arrays:
   - Inserting into an array can be slower due to the following factors:
     - Array Resizing: When the array reaches its capacity, resizing is required, which involves creating a new, larger array and copying all elements. This can introduce significant overhead during insertions.
     - Shifting of Elements: If the insertion position is not at the end of the array, shifting of elements is required to make space for the new element, resulting in a time complexity of O(n) in the worst case.
     - Memory Overhead: Frequent resizing and memory allocation can lead to memory fragmentation and inefficiency.

2. Linked Lists:
   - Linked lists are generally faster for insertions than arrays because they do not require resizing or shifting of elements. Insertions at the beginning or end of the linked list are efficient (O(1)), and insertions in the middle can be done in O(1) time if you have direct access to the node, which can be achieved with a doubly linked list.

3. Hybrid Data Structure (Array of Linked Lists):
   - The hybrid data structure can offer advantages over arrays in terms of insertion, especially if you use a hash function to map each username to an index in the array. This approach can provide O(1) insertion time for both the beginning and end of the linked list if you use a doubly linked list.

### Searching:
1. Arrays:
   - Arrays offer constant-time random access (O(1)), making them fast for searching when you know the index of the element you're looking for.

2. Linked Lists:
   - Searching in linked lists is slower than arrays since it requires traversing the list sequentially, resulting in O(n) time complexity in the worst case.

3. Hybrid Data Structure (Array of Linked Lists):
   - Searching in the hybrid data structure would be slower than arrays but potentially faster than a single linked list. If the array is large and contains many linked lists, searching for a specific username would require two steps: hashing to find the correct linked list and then searching within that linked list. This process may take longer than direct array access in the case of arrays.

## Selection Sort has a runtime of O(n2) - Quadratic runtime

