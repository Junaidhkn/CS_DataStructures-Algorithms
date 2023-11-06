function logItems ( a, b ) {
   for ( let index = 0; index < a; index++ ) {
      console.log( a )
   }
   for ( let index = 0; index < b; index++ ) {
      console.log( b )
   }
}


// O(a+b) => we cannot say that both of these loops are O(n) and just add them together to get a result and that is O(2n), and then we just drop the constant and it becomes O(n). However, it is not correct, because you cannot say that a = n and b = n likewise,what if a = 1 and b = 1000000 ?

// So, the first loop is O(a) and second loop is O(b) => O(a)+O(b) = O(a+b)
