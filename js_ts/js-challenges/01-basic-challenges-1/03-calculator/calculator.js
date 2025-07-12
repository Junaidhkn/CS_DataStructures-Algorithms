function calculator ( x, y, operation ) {
   if ( operation == '+' ) {
      return x + y;
   } else if ( operation == '-' ) {
      return x - y;
   } else if ( operation == '*' ) {
      return x * y;
   } else if ( operation == '/' ) {
      return x / y;
   } else {
      return 'Invalid operation';
   }
}

module.exports = calculator;
