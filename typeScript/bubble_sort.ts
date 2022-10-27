// Bubble sort Algorithm - GREATEST of all Sorting Algorithms

export default function bubble_sort(myArray: number[]): void {
  // outer loop
  for (let i = 0; i < myArray.length; i++) {
    // inner for loop
    for (let j = 0; j < myArray.length - 1 - i; j++) {
      if (myArray[j] > myArray[j + 1]) {
        // do swapping here
        const temp = myArray[j];
        myArray[j] = myArray[j + 1];
        myArray[j + 1] = temp;
      }
    }
  }
}
