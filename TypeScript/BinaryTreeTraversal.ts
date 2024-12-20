interface BinaryNode<T> {
    value: T,
    left: BinaryNode<T>,
    right: BinaryNode<T>,
}

function walk(curr: BinaryNode<number> | null, path: number[]): void {
    if(!curr) {
        return;
    }

    path.push(curr.value);
    walk(curr.left, path);
    walk(curr.right, path);
}

export default function per_order_search(head: BinaryNode<number>): number[] {
    const path: number[] = []
    walk(head, path);

    return path;
}