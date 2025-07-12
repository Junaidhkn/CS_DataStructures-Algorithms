const crossAdd = ( input ) => {
   const answer = []
   for ( i = 0; i < input.length; i++ ) {
      let goingUp = input[i]
      let goingDown = input[input.length - 1 - i]
      answer.push( goingDown + goingUp )
   }
   console.log( answer )
   return answer
}

