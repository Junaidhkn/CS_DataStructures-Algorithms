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

    prepend(item: T): SinglyLinkedList<T> {
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
    insertAt(item: T, idx: number): void {
        // Implementation here
    }

    append(item: T): SinglyLinkedList<T> {
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

    remove(item: T): T | undefined {
        // Implementation here
        return;
    }

    get(idx: number): T | undefined {
        // Implementation here
        return;
    }

    removeAt(idx: number): T | undefined {
        // Implementation here
        return;
    }
}
