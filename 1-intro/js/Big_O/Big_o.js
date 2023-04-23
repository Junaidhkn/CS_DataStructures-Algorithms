function crossAdd ( input ) {
   let answer = []
   for ( let i = 0; i < input.length; i++ ) {
      let goingUp = input[i]
      let goingDown = input[input.length - 1 - i]
      answer.push( goingUp + goingDown )
   }
   return answer
}

// console.log( crossAdd( [2, 2, 3, 4, 1] ) ); // Answer: [3, 6, 6, 6, 3]

// Find Element in Array
function findElement ( needle, haystack ) {
   for ( var i = 0; i < haystack.length; i++ ) {
      if ( haystack[i] === needle ) return true;
   }
}

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
