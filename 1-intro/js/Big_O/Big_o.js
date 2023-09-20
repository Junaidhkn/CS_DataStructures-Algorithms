function addItems ( input ) {
   return input + input
}

// O(1) as it is constant, because it does not matter how big the input is, it will always be 1
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