type Node<T> = {
    value: T;
    next?: Node<T>;
};

export default class Queue<T> {
    public length: number;
    private head?: Node<T>;
    private tail?: Node<T>;

    constructor() {
        this.head = this.tail = undefined;
        this.length = 0;
    }

    enqueue(item: T): void {
        this.length++;
        if (!this.tail) {
            this.tail = this.head = { value: item } as Node<T>;
            return;
        }
        let temp = this.tail;
        this.tail.next = { value: item } as Node<T>;
        this.tail = temp.next;

        // OR

        // const node = { value: item } as Node<T>;
        // this.length++;
        // if (!this.tail) {
        //     this.tail = this.head = node;
        //     return;
        // }
        // this.tail.next = node;
        // this.tail = node;
    }

    deque(): T | undefined {
        if (!this.head) {
            return undefined;
        }
        this.length--;
        let temp = this.head;
        this.head = temp.next;
        temp.next = undefined;
        return temp.value;
    }

    peek(): T | undefined {
        return this.head?.value;
    }
}
