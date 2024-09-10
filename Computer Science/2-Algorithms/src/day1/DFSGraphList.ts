function walk(
    graph: WeightedAdjacencyList,
    curr: number,
    needle: number,
    seen: boolean[],
    path: number[],
): boolean {
    if (curr === needle) {
        return true;
    }

    if (seen[curr]) {
        return false;
    }

    seen[curr] = true;

    // recurse

    // pre
    path.push(curr);
    // recurse
    const list = graph[curr];

    // post
    path.pop();
    return false;
}

export default function dfs(
    graph: WeightedAdjacencyList,
    source: number,
    needle: number,
): number[] | null {}
