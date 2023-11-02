function findMaxNumber ( arr ) {
   let max = arr[0];

   for ( let i = 1; i < arr.length; i++ ) {
      if ( arr[i] > max ) {
         max = arr[i];
      }
   }

   return max;
}

console.log( 'Answer:--', findMaxNumber( [13, 5, 12, 9] ) )

module.exports = findMaxNumber;
