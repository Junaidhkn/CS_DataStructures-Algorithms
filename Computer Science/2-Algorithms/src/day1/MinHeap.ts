/*

 A heap is stored in an array without using explicit pointers for parent-child relationships.
 For a given node at index i:
    >The left child is at index 2 * i + 1.
    >The right child is at index 2 * i + 2.
    >The parent node is at index (i - 1) // 2.

    ie:Consider a heap represented as an array: [10, 20, 30, 40, 50, 60]
!Finding Parent of a Node:
    Suppose you are at index 4 (50).
    To find the parent of the node at index 4:
    Use (4 - 1) // 2 = 3 // 2 = 1. (Or in simple words Math.floor((i-1)/2))
    So, the parent of the node at index 4 is at index 1 (20).

        10 (index 0)
       /   \
    20 (1)  30 (2)
   /   \     \
40 (3) 50 (4) 60 (5)


*/
export default class MinHeap {
    public length: number;
    public data: number[];

    constructor() {
        this.length = 0;
        this.data = [];
    }

    insert(value: number): void {}
    delete(): number {}

    private heapifyDown(idx: number): void {
        const leftIndex = this.leftChild(idx);
        const rightChild = this.rightChild(idx);

        if (idx >= this.length || leftIndex >= this.length) {
            return;
        }
        const leftValue = this.data[]
    }

    private heapifyUp(idx: number): void {
        if (idx === 0) return;
        const parentIndex = this.parent(idx);
        const parentValue = this.data[parentIndex];
        const value = this.data[idx];

        if (parentValue > value) {
            this.data[idx] = parentValue;
            this.data[parentIndex] = value;
            this.heapifyUp(idx);
        }
    }

    private parent(idx: number): number {
        return Math.floor((idx - 1) / 2);
    }
    private leftChild(idx: number): number {
        return idx * 2 + 1;
    }
    private rightChild(idx: number): number {
        return idx * 2 + 2;
    }
}
