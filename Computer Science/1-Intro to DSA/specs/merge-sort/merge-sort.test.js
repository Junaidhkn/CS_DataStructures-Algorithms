/*
  Write a function that performs mergesort
  Name the function mergeSort
  It will take in a array of numbers and return a sorted array numbers

  You'll need to write more than just one function
*/

const mergeSort = ( nums ) => {
  // base case, return of length 1 or 0
  if ( nums.length == 1 || nums.length == 0 ) return nums

  // break into smaller arrays
  const length = Math.floor( nums.length / 2 )
  const left = nums.slice( 0, length )
  const right = nums.slice( length )


  // call mergesort on left and right
  const sortedLeft = mergeSort( left )
  const sortedRight = mergeSort( right )

  return merge( sortedLeft, sortedRight );

};


const merge = ( left, right ) => {
  let result = [];
  let leftIndex = 0;
  let rightIndex = 0;

  while ( leftIndex < left.length && rightIndex < right.length ) {
    if ( left[leftIndex] < right[rightIndex] ) {
      result.push( left[leftIndex] );
      leftIndex++;
    } else {
      result.push( right[rightIndex] );
      rightIndex++;
    }
  }

  return result.concat( left.slice( leftIndex ) ).concat( right.slice( rightIndex ) );


}


console.log( mergeSort( [10, 5, 3, 8, 2, 6, 4, 7, 9, 1] ) )


// unit tests
// do not modify the below code
// test.skip( "merge sort", function () {
//   const nums = [10, 5, 3, 8, 2, 6, 4, 7, 9, 1];
//   const ans = mergeSort( nums );
//   expect( ans ).toEqual( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] );
// } );
