function addItems ( input ) {
   return input + input
}

// O(1) as it is constant, because it does not matter how big the input is, it will always be 1, this is the most efficient way big O, also referred to as constant time
// console.log( addItems( 5 ) ); // Answer: 10 


function crossAdd ( input ) {
   let answer = []
   for ( let i = 0; i < input.length; i++ ) {
      let goingUp = input[i]
      let goingDown = input[input.length - 1 - i]
      answer.push( goingUp + goingDown )
   }
   return answer
}
// THe above example is O(n) as it is linear,because we go through all the inputs once in a loop
// console.log( crossAdd( [2, 2, 3, 4, 1] ) ); // Answer: [3, 6, 6, 6, 3]



// Find Element in Array
function findElement ( needle, haystack ) {
   for ( var i = 0; i < haystack.length; i++ ) {
      if ( haystack[i] === needle ) return true;
   }
}
// The above example is O(n) as it is linear,because we go through all the inputs once in a loop, and the worst case is that the element is not in the array
// console.log( findElement( 3, [1, 2, 3, 4, 5] ) ); // Answer: true as 3 is in the array


function makeTuples ( input ) {
   let answer = []
   for ( let i = 0; i < input.length; i++ ) {
      for ( let j = 0; j < input.length; j++ ) {
         answer.push( [input[i], input[j]] )
      }
   }
   return answer
}

// console.log( makeTuples( ['Junaid', 'Hassan', 'Khan'] ) );
// The O(n^2) as it is quadratic, because we go through all the inputs twice in a loop


//  Common Big O Notations
// O(1) Constant - no loops
// O(log N) Logarithmic - usually searching algorithms have log n if they are sorted (Binary Search) - Divide and conquer
// O(n) Linear - for loops, while loops through n items
// O(n log(n)) Log Linear - usually sorting operations
// O(n^2) Quadratic - every element in a collection needs to be compared to ever other element. Two nested loops
// O(2^n) Exponential - recursive algorithms that solves a problem of size N
// O(n!) Factorial - you are adding a loop for every element

