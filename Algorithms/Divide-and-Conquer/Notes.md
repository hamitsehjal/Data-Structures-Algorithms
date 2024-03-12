
## Farm-Plot Example
In the **Farm example** why did author choose `when one side is multiple of other` as the base case???


It simplifies the problems and provides a clear stopping condition. Explained below:

1. **Simplicity**: The base case should be the simplest possible scenario to solve. In this problem, `having one side as multiple of another` simplifies the `division of land` because you can `create square plots of equal size without any remainder`.

2. **Clear Stopping condition**: The base case should also provide a clear stopping condition. When one side is multiple of another, you have reached a situation, where you `don't need to divide the land further`. You can simply create 2 equal sized square plots of largest possible size and stop recursing.

3. **Efficiency**: This base case can lead to a more efficient solution as you `don't have to deal with partial slots or remainder`, which can complicate the algorithm.


## Recap
1. D&C works by breaking down the problem into smaller and smaller pieces. If you are using D&C on a list, the `base case` is probably an empty list or list with just 1 element
2. If you are implementing QuickSort, choose `random element` as pivot. The Average Runtime of QuickSort is `O(n log n)`
3. The `Constant` in Big O Notation can matter sometimes. Classic Example: MergeSort Vs QuickSort - that's why QuickSort is faster than MergeSort
4. The `Constant` almost never matters for Simple search vs Binary Search. `O( log n)` is so much faster than `O(n)` as the list size increases.
    

