class Node {
    constructor( value ) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

// // Notes

// Check to see if the root is null, if null then root is newNode
// Declare a Variable for root
//  ie; let temp = this.root

//  Also note that we might have a node value being a dupicate, thus additional property count would be added, in the Node class, the following example ignores this scenerio

// While Loop:
//      if newNode = temp return undefined
//      if < Left else > Right
//      if null insert newNode else move to next
// 


class BST {
    constructor() {
        this.root = null;
    }

    /// WRITE INSERT METHOD HERE ///

    insert ( value ) {
        const newNode = new Node( value );
        if ( this.root === null ) {
            this.root = newNode;
            return this;
        }
        let temp = this.root;
        while ( true ) {
            if ( newNode.value === temp.value ) return undefined;
            if ( newNode.value < temp.value ) {
                if ( temp.left === null ) {
                    temp.left = newNode;
                    return this;
                }
                temp = temp.left;
            } else {
                if ( temp.right === null ) {
                    temp.right = newNode;
                    return this;
                }
                temp = temp.right;
            }
        }
    }
    ////////////////////////////////

}



function test () {

    let myBST = new BST();

    myBST.insert( 2 );
    myBST.insert( 1 );
    myBST.insert( 3 );

    /*
        THE LINES ABOVE CREATE THIS TREE:
                     2
                    / \
                   1   3
    */


    console.log( "Root:", myBST.root.value );
    console.log( "\nRoot->Left:", myBST.root.left.value );
    console.log( "\nRoot->Right:", myBST.root.right.value );
}


test();


/*
    EXPECTED OUTPUT:
    ----------------
    Root: 2

    Root->Left: 1

    Root->Right: 3

*/

