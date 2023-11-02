function countVowels ( str ) {
   let vowels = ['a', 'e', 'i', 'o', 'u']
   let count = 0;
   const input = str.toLowerCase()
   for ( let i = 0; i < input.length; i++ ) {
      vowels.map( ( vowel ) => {
         vowel === input[i] ? count++ : count
      } )
   }
   return count
}

module.exports = countVowels;
