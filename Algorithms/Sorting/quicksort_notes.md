# QuickSort!!


## Facts about QuickSort!
- It's much faster than selectionSort
- Used in real life. C Standard Library's `qsort` function uses 'QuickSort' Implementation
- QuickSort uses `Divide and Conquer`
- Runtime of 


## How to Perform `QuickSort`? 

1. Pick a pivot.

2. Partition the array into two sub-arrays: elements less than the pivot and elements greater than the pivot.

3. Call quicksort recursively on the two sub-arrays.

## What are `Inductive Proofs` in Algorithms?

Inductive proofs are a mathematical technique used in the analysis of algorithms to prove their correctness and time complexity. It is based on the principle of `Mathematical Induction` that involves proving a statement for `all natural numbers`, typically starting with a base case and then show that if it holds true for some natural numbers 'n', it also holds true for 'n+1'.


## `List Comprehension` in Python?

Usual Way:
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
```

List Comprehension:
```python

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist=[x for x in fruits if "a" in x]

print(newlist)

```