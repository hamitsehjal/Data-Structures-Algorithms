export default function crystall_balls(breaks: boolean[]): number {
  const jumAmount = Math.floor(Math.sqrt(breaks.length));

  let i = jumAmount;

  for (; i < breaks.length; i += jumAmount) {
    if (breaks[i]) {
      break;
    }
  }

  i -= jumAmount;

  for (let j = 0; j < jumAmount && i < breaks.length; ++j, ++i) {
    if (breaks[i]) {
      return i;
    }
  }
  return -1;
}
