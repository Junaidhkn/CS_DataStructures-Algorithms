function removeDuplicates ( arr ) {
   let output = []
   for ( let i = 0; i < arr.length; i++ ) {
      let item = arr[i]
      if ( !output.includes( item ) ) {
         output.push( item );
      }
   }
   return output
}

console.log( removeDuplicates( [1, 2, 3, 1, 3, 34] ) )

module.exports = removeDuplicates;
