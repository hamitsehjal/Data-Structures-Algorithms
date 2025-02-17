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

When Do we use it?
- Things we can iterate over sequentially
	- Contiguous sequence of elements
	- Arrays, Strings, Linked Lists
- Find Max,min, longest, shortest, contained
	- maybe we need to calculate something
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwMTc3MDUwNTBdfQ==
-->