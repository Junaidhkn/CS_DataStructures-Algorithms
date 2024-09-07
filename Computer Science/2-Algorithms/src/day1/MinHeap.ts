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

    constructor() {}

    insert(value: number): void {}
    delete(): number {}
}
