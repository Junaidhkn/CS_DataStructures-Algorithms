function crossAdd ( input ) {
   let answer = []
   for ( let i = 0; i < input.length; i++ ) {
      let goingUp = input[i]
      let goingDown = input[input.length - 1 - i]
      answer.push( goingUp + goingDown )
   }
   return answer
}

// console.log( crossAdd( [2, 2, 3, 4, 1] ) ); // Answer; [3, 6, 6, 6, 3]
