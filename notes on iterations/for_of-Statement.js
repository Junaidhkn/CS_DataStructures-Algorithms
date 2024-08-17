/* 
The for...of statement creates a loop Iterating over iterable objects( including Array, Map, Set, arguments object and so on ), invoking a custom iteration hook with statements to be executed for the value of each distinct property.


for (variable of iterable)
  statement


*/


// The following example shows the difference between a for...of loop and a for...in loop.While for...in iterates over property names, for...of iterates over property values:

const arr = [3, 5, 7];
arr.foo = "hello";

for ( const i in arr ) {
   console.log( i );
}
// "0" "1" "2" "foo"

for ( const i of arr ) {
   console.log( i );
}
// Logs: 3 5 7

// The for...of and for...in statements can also be used with destructuring.For example, you can simultaneously loop over the keys and values of an object using Object.entries().

const obj = { foo: 1, bar: 2 };

for ( const [key, val] of Object.entries( obj ) ) {
   console.log( key, val );
}
// "foo" 1
// "bar" 2