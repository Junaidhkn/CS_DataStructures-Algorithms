function reverseString ( input ) {
   let arr = []
   for ( let i = 0; i < input.length; i++ ) {
      arr.push( input.slice()[i] )
   }
   return arr.reverse().join( '' )
}


module.exports = reverseString;
