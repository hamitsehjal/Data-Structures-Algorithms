# Grokking Algorithms

## Binary Search (Our First Algorithm)
- Time complexity: O(log n) - WORST CASE
- A simple search would take O(n) in WORST CASE.

### Example: A list of 8 numbers
- Simple Search in worst case would take: O(n) -> O(8) -> 8 checks to find the number.
- Binary Search in worst case would take: O(log n) -> O(log 8) -> 2^3 = 8, so O(log 8) = 3 checks to find the number.

### Important Notes:
- The runtime of two different algorithms grows at different rates.
- Taking an example from the Grokking Algorithms Book:
    - Landing of a Rocket (needs an algorithm to decide where to land, only 10 seconds to decide).
    - Let's assume it takes 1 millisecond to check one element.
    - List of 100 elements:
        - Simple Search would take a maximum of 100 milliseconds, so 1 second.
        - Binary Search would take a maximum of 7 milliseconds, so 0.07 seconds.
    - Based on this, we can say "Binary Search" is roughly 15 times faster than "Simple Search".
    - List of a billion elements:
        - Binary Search would take 32 milliseconds, so one might think (based on the above analysis) that "Simple Search" would take (32 * 15) = 450 ms, right?
        - **DEAD WRONG**: "Simple Search" with 1 billion items will take a billion ms, i.e., 11 days in the worst-case scenario.
    - **IMP**: Run times of "Simple Search" and "Binary Search" don't grow at the same rate.

### Important !!!
- Worst-Case vs. Average-Case vs. Best-Case.
- Different Big O run times:
    1. O(log n) - log time; Example: Binary Search.
    2. O(n) - linear time; Example: Simple Search.
    3. O(n*log n) - linearithmic (combines *linear and *logarithmic) Fast sorting algorithm; Example: Quicksort.
    4. O(n^2) - Quadratic runtime; Example: Selection Sort.
    5. O(n!) - Factorial Time Complexity, A really slow algorithm like the traveling salesperson.

### Some Key Takeaways:
- Algorithm speed isn't measured in seconds but in the growth of the number of operations.
- Instead, we talk about how quickly the runtime of an algorithm increases as the size of the input increases.
- We express run times of an algorithm in Big O notation.
- O(log n) is faster than O(n), but it becomes a lot faster as the size of the list of input grows.

## Graph Algorithms (AI System that follows the user around in a video game)
- k-nearest Algorithm (KNN) - to build a recommendation System.
- Some problems can't be solved in a timely manner:
    - The challenge is to IDENTIFY these kinds of problems and come up with an algorithm that gives an approximate answer.
