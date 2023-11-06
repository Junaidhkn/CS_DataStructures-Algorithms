function swap(array, firstIndex, secondIndex) {
    let temp = array[firstIndex];
    array[firstIndex] = array[secondIndex];
    array[secondIndex] = temp;
}

// WRITE THE PIVOT FUNCTION HERE //
//                               //
//                               //
//                               //
//                               //
///////////////////////////////////


   
function test() {
    let myArray = [4,6,1,7,3,2,5];
    pivot(myArray);
    console.log(myArray);
}


test();


/*
    EXPECTED OUTPUT:
    ----------------
    [ 2, 1, 3, 4, 6, 7, 5 ]

*/  
