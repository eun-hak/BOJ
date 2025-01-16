const binarySearch = (array, value) => {
  let start = 0;
  let end = array.length;
  while (end - start > 0) {
    let mid = Math.floor((end - start) / 2) + start;
    if (array[mid] === value) {
      return mid;
    } else if (array[mid] > value) {
      end = mid;
    } else {
      start = mid + 1;
    }
  }
  return -1;
};
const dataB = [1, 3, 5, 7, 9, 17];

console.log(binarySearch(dataB, 28)); // 3
