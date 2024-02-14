// WRITE NODE CLASS HERE //
//  Note that Binary Search trees are O(Log(n)), often called - Divide and Conquor
// Worst case scenerio, if the item that we are looking for ie; consider a number that is the greatest number positioned at leaf and all of its parent nodes are also to the furthest right being larger number, that would turn it to a linked list then its - O(n)


class Node {
    constructor( value ) {
        this.value = value
        this.left = null
        this.right = null
    }
}

///////////////////////////

class BST {
    // WRITE BST CONSTRUCTOR HERE //

    constructor() {
        // const newNode = new Node( value )
        this.root = null
    }

    ////////////////////////////////
}


// //  Object Perspective

// {
//     value: 4,
//         left: {
//                  value: 3,
//                  left: null,
//                  right: null
//     },
//     right: {
//                  value: 3,
//                  left: null,
//                  right: null
//     },
// }


function test () {
    let myBST = new BST();

    if ( myBST.root === null ) {
        console.log( "Root: null" );
    } else {
        console.log( "Root:", myBST.root.value );
    }
}


test();


/*
    EXPECTED OUTPUT:
    ----------------
    Root: null

*/