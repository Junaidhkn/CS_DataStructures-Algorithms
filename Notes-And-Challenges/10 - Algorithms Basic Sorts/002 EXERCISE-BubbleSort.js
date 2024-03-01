// WRITE BUBBLESORT FUNCTION HERE //
function bubbleSort ( array ) {
    for ( let i = array.length - 1; i > 0; i-- ) {
        for ( let j = 0; j < i; j++ ) {
            if ( array[j] > array[j + 1] ) {
                let temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
            }
        }
    }
    return array
}

/*
i  j  |  i  j  |  i  j  |  i  j  |  i  j  |

5  0  |  4  0  |  3  0  |  2  0  |  1  0  |
   1        1        1        1
   2        2        2        
   3        3   
   4       
        
*/

///////////////////////////////////



function test () {
    let myArray = [4, 2, 6, 5, 1, 3];
    bubbleSort( myArray );
    console.log( myArray );
}


test();


/*
    EXPECTED OUTPUT:
    ----------------
    [ 1, 2, 3, 4, 5, 6 ]

*/