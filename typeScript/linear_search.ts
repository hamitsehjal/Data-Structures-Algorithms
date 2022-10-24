export default function linear_search(
  haystack: number[],
  needle: number
): boolean {
  // classic for loop
  for (let i = 0; i < haystack.length; ++i) {
    if (haystack[i] == needle) {
      return true;
    }
  }
  return false;
}



console.log(linear_search([3,23,42,33,2],23));