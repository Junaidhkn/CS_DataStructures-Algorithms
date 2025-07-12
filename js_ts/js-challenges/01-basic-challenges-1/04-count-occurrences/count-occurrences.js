function countOccurrences ( word, charactor ) {
   // // First Method
   let count = 0;
   for ( i = 0; i < word.length; i++ ) {
      if ( word[i] === charactor ) {
         count++;
      }
   }
   return count;

   // // Second Method
   // let count = 0;
   // let arr = [];
   // for ( i = 0; i < word.length; i++ ) {
   //    arr.push( word[i] )
   // }
   // arr.map( ( char ) => {
   //    char === charactor ? count++ : count
   // } )
   // return count
}

module.exports = countOccurrences;
