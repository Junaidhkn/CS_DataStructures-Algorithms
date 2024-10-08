/*
///! Base case for recursion 
      1- it's a wall 
      2- Off the map
      3- its the end
      4- if we have seen it
*/
function walk(
    maze: string[],
    wall: string,
    curr: Point,
    end: Point,
    seen: boolean[][],
): boolean {
    // off the map
    if (
        curr.x < 0 ||
        curr.x >= maze[0].length ||
        curr.y < 0 ||
        curr.y >= maze.length
    ) {
        return false;
    }
    // on the wall
    if (maze[curr.y][curr.x] === wall) {
        return false;
    }
    // its the end
    if (curr.x === end.x && curr.y === end.y) {
        return true;
    }
    // if you have seen it
    if (seen[curr.y][curr.x]) {
        return false;
    }
    return false;
}

export default function solve(
    maze: string[],
    wall: string,
    start: Point,
    end: Point,
): Point[] {
    return [];
}
