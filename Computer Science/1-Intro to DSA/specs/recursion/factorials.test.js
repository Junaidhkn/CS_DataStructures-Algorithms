/*
  Make a function that computes a factorial recursively.
  A factorial is when you take a number n and multiply by each preceding integer until you hit one.
  n * (n-1) * (n-2) ... * 3 * 2 * 1
  
  Call the function factorial
  
  factorial(1) = 1
  factorial(2) = 2
  factorial(3) = 6 
*/

// Fibonacci Sequence

// function fibonacci ( n ) {
//   if ( n === 2 || n === 1 ) {
//     return 1
//   } else if ( n <= 0 ) {
//     return 0
//   }

//   // Recursive calls
//   return fibonacci( n - 1 ) + fibonacci( n - 2 )

// }


// Iterative Approach:
function fibonacci ( n ) {
  if ( n === 0 ) return 0;
  if ( n === 1 ) return 1;

  let prev = 0, curr = 1;
  for ( let i = 2; i <= n; i++ ) {
    let next = prev + curr;
    prev = curr;
    curr = next;
  }
  return curr;
}

// Recursive Approach with Memoization:
function fibonacciRecursive ( n, memo = {} ) {
  if ( n in memo ) return memo[n];
  if ( n === 0 ) return 0;
  if ( n === 1 ) return 1;

  memo[n] = fibonacciRecursive( n - 1, memo ) + fibonacciRecursive( n - 2, memo );
  return memo[n];
}

console.log( fibonacciRecursive( 100 ) ); // Outputs the 100th Fibonacci number



/**

// Iterative Approach:

Initialize two variables, prev (previous Fibonacci number) and curr (current Fibonacci number), to 0 and 1 respectively.
Use a loop to iterate from 2 to n, updating the prev and curr variables to get the next Fibonacci number.
Return curr as the n-th Fibonacci number.

// Recursive Approach with Memoization:

Use an object memo to store previously calculated Fibonacci numbers.
Check if the result for the current n is already in memo. If so, return the stored value.
If n is 0 or 1, return 0 or 1 respectively.
Recursively calculate the Fibonacci number by summing the results of fibonacciRecursive(n - 1, memo) and fibonacciRecursive(n - 2, memo), and store the result in memo before returning it.
Both implementations efficiently compute the Fibonacci sequence, but the iterative approach is typically more straightforward and faster for large values of n.

 */




function factorial ( n ) { }

// unit tests
// do not modify the below code
// test.skip( "factorials", () => {
//   expect( factorial( 1 ) ).toEqual( 1 );
//   expect( factorial( 2 ) ).toEqual( 2 );
//   expect( factorial( 3 ) ).toEqual( 6 );
//   expect( factorial( 10 ) ).toEqual( 3628800 );
// } );
