class Heap {
  constructor() {
    this.heap = [];
  }
  getParentIndex(childIndex) {
    return Math.floor((childIndex - 1) / 2);
  }

  getLeftChildIndex(parentIndex) {
    return 2 * parentIndex + 1;
  }

  getRightChildIndex(parentIndex) {
    return 2 * parentIndex + 2;
  }

  swap(index1, index2) {
    [this.heap[index1], this.heap[index2]] = [
      this.heap[index2],
      this.heap[index1],
    ];
  }

  push(element) {
    this.heap.push(element);
    this.heapifyUp();
  }

  pop() {
    if (this.heap.length === 1) return this.heap.pop();
    const min = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.heapifyDown();
    return min;
  }

  heapifyUp() {
    let index = this.heap.length - 1;
    while (index > 0) {
      let ParentIndex = this.getParentIndex(index);
      if (this.heap[index] < this.heap[ParentIndex]) {
        this.swap(index, ParentIndex);
        index = ParentIndex;
      } else {
        break;
      }
    }
  }

  heapifyDown() {
    let index = 0;
    while (this.getLeftChildIndex(index) < this.heap.length) {
      let smallerChildIndex = this.getLeftChildIndex(index);
      let rightChildIndex = this.getRightChildIndex(index);

      if (
        rightChildIndex < this.heap.length &&
        this.heap[rightChildIndex] < this.heap[smallerChildIndex]
      ) {
        smallerChildIndex = rightChildIndex;
      }

      if (this.heap[index] < this.heap[smallerChildIndex]) break;
      else {
        this.swap(index, smallerChildIndex);
        index = smallerChildIndex;
      }
    }
  }
}
