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


## Python and the `time` module:

Python provides the `time` module to work with time-related functionalities, including measuring execution time. In this context, we use the `time.perf_counter()` function from the `time` module to measure the elapsed time with higher precision.

Example:

```python
import time

start_time = time.perf_counter()
# Code to be measured
end_time = time.perf_counter()
elapsed_time = end_time - start_time

The elapsed_time variable will store the time taken by the code block to execute and is expressed in fractional seconds.
``` 

### F-strings in Python:
F-strings are a feature introduced in Python 3.6 that provide a concise and convenient way to format strings, allowing the inclusion of variables or expressions directly within the string.

Example:
```
ls_time = time.perf_counter()  # -> 1.6999983927235007e-06
print(f"linear time is: {ls_time:.6f} seconds")  # 0.000002 seconds

Note: In this example, the variable ls_time is inserted into the string using an f-string, and :.6f ensures that the time is formatted to display up to 6 decimal places.
```

### Using the unittest class for testing:
The `unittest` framework is a built-in Python module that provides a test automation framework, inspired by Java's JUnit. It allows developers to create test cases, organize them into test suites, and run them to verify that their code behaves as expected.

The `setUp()` method is a special method in the unittest.TestCase class. It runs before each individual test method, providing a setup environment for the tests. It's similar to the concept of beforeEach in JavaScript's Jest testing framework.

### Unloading data from a file using json.load():
The json module in Python is used for working with JSON data. The json.load(file) function allows you to read JSON data from a file and convert it into a Python dictionary or list, depending on the JSON data's structure.

Example:
```
import json

with open("file_path", "r", encoding="utf-8") as file:
    data = json.load(file)

The data variable will now hold the contents of the JSON file, converted into a Python dictionary or list.
```

### if __name__ == '__main__':
This is a common Python idiom used to ensure that specific code blocks are only executed when the script is run directly as the main program. It allows you to control which parts of the script should run when it's being used as a standalone script versus when it's imported as a module in another script.

Explanation:

- __name__: It's a special variable in Python that holds the name of the current module or script. When the script is the main program being executed, __name__ is set to "__main__".
- __name__ == '__main__': This expression specifies that if the script is being executed as the main program (not being imported into another file), then run the following code block.
Example:
```
if __name__ == '__main__':
    # Code block to be executed only when the script is run directly as the main program
    # This code may include function calls, test cases, etc.

NOTE: When the script is imported as a module in another script, the code block under if __name__ == '__main__': will not be executed. This allows you to define reusable functions, classes, or constants in the module without unintended side effects when importing it elsewhere.
```

### Some Key Takeaways:
- Algorithm speed isn't measured in seconds but in the growth of the number of operations.
- Instead, we talk about how quickly the runtime of an algorithm increases as the size of the input increases.
- We express run times of an algorithm in Big O notation.
- O(log n) is faster than O(n), but it becomes a lot faster as the size of the list of input grows.

## Graph Algorithms (AI System that follows the user around in a video game)
- k-nearest Algorithm (KNN) - to build a recommendation System.
- Some problems can't be solved in a timely manner:
    - The challenge is to IDENTIFY these kinds of problems and come up with an algorithm that gives an approximate answer.
