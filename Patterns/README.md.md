# 4-General Rules for solving a Pattern Based Questions

1. For the outer for loop, count the number of lines
2. For the inner(nested) loop, 'focus' on the columns and somehow connect them to rows
3. Print the '*' inside the nested loop
4. Observe the symmetry in the pattern or check if the pattern is a combination of two or more pattern


*IMP*: Make sure you know basic arithmetic logics like 'generating a sequence of odd numbers'

Let's say N is 5 and i grows from 0 to 4

- (2*i)+1: Gives a sequence of odd numbers (Quite handy when solving problems) -> [1,3,5,7,9]
- 2N-((2*i)+1): Gives a sequence of reverse odd numbers --> [9,7,5,3,1]

## Sliding Window

How to identify the Sliding Window Questions?
- Question contains things we can iterate over sequentially
	- Contiguous sequence of elements
	- Arrays, Strings, Linked Lists
- Question asks us to find Max,min, longest, shortest, contained
	- maybe we need to calculate something

Question Variants
1. Fixed Window Variant
	- max Sum subarray of size k
2. Dynamic Window Variant
	- Smallest sum >= some value S
3. Dynamic variant with Auxially data structure
	- Longest substring with no more than k distinct characters
	- String Permutation
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQzNjQ0NTk3MywtMTAxNzcwNTA1MF19
-->