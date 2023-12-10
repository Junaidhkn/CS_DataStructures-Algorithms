// WRITE NODE CLASS HERE //



///////////////////////////

class BST {
    // WRITE BST CONSTRUCTOR HERE //



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