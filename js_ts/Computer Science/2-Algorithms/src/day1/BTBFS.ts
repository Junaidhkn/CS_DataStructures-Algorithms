export default function bfs(head: BinaryNode<number>, needle: number): boolean {
    const queue: (BinaryNode<number> | null)[] = [head];

    while (queue.length) {
        const curr = queue.shift() as BinaryNode<number> | null | undefined;
        //    In a BFS traversal, when nodes are added to the queue, their left and right children are also added regardless of whether they are null or not.This can result in null values being added to the queue.Without the continue statement, if curr is null, attempting to access curr.value would cause an error since null does not have a value property.continue helps to bypass these potential null values and keeps the loop running smoothly, only processing actual nodes.
        if (!curr) continue;

        if (curr.value === needle) return true;

        queue.push(curr.left);
        queue.push(curr.right);
    }
    return false;
}
