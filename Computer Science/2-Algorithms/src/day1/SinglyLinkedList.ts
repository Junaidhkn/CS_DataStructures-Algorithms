class Node<T> {
    value: T;
    next: Node<T> | null;

    constructor(value: T) {
        this.value = value;
        this.next = null;
    }
}

export default class SinglyLinkedList<T> {
    public length: number;
    private head: Node<T> | null;
    private tail: Node<T> | null;

    constructor(value: T) {
        const newNode = new Node(value);
        this.head = newNode;
        this.tail = this.head;
        this.length = 1;
    }

    prepend(item: T): void {
        // Implementation here
    }

    insertAt(item: T, idx: number): void {
        // Implementation here
    }

    append(item: T): void {
        // Implementation here
    }

    remove(item: T): T | undefined {
        // Implementation here
    }

    get(idx: number): T | undefined {
        // Implementation here
    }

    removeAt(idx: number): T | undefined {
        // Implementation here
    }
}
