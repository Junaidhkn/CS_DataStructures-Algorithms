class Node<T> {
    value: T;
    next: Node<T> | null;
    prev: Node<T> | null;

    constructor(value: T) {
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

export default class DoublyLinkedList<T> {
    public length: number;
    private head: Node<T> | null;
    private tail: Node<T> | null;

    constructor(value: T) {
        const newNode = new Node(value);
        this.head = newNode;
        this.tail = this.head;
        this.length = 1;
    }

    prepend(item: T): DoublyLinkedList<T> {
        const newNode = new Node(item);
        if (this.length === 0) {
            this.head = newNode;
            this.tail = newNode;
            this.length++;
            return this;
        }
        newNode.next = this.head;
        this.head = newNode;
        this.length++;
        return this;
    }
    insertAt(item: T, idx: number): void {}
    append(item: T): DoublyLinkedList<T> {
        const newNode = new Node(item);

        if (this.length === 0) {
            this.head = newNode;
            this.tail = newNode;
        } else if (this.tail) {
            this.tail.next = newNode;
            this.tail = newNode;
        }

        this.length++;
        return this;
    }
    remove(item: T): T | undefined {}
    get(idx: number): T | undefined {
        if (!this.head) return undefined;
        let current: Node<T> | null = this.head;
        for (let i = 0; i < idx && current !== null; i++) {
            current = current.next;
        }
        return current?.value;
    }
    removeAt(idx: number): T | undefined {}
}
