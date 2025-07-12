function isPalindrome ( str ) {
   let palindrome = Boolean;
   const strModified = str.toLowerCase().split( " " ).join( '' )
   const input = removeNonAlphanumeric( strModified )
   for ( let i = 0; i < input.length; i++ ) {
      if ( input[input.length - i - 1] === input[i] ) {
         palindrome = true
      } else {
         palindrome = false
      }
   }
   return palindrome
}

const removeNonAlphanumeric = ( input ) => {
   return input.split( ',' ).join( '' )
}

module.exports = isPalindrome;
