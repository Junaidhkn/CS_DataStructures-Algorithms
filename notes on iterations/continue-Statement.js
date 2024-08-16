let a = 0;
let n = 0;
while ( a < 5 ) {
   a++;
   if ( a === 3 ) {
      continue;
   }
   n += a;
   console.log( n );
}
// Logs:
// 1 3 7 12


// Example 2

/*
A statement labeled checkiandj contains a statement labeled checkj.If continue is encountered, the program terminates the current iteration of checkj and begins the next iteration.Each time continue is encountered, checkj reiterates until its condition returns false.When false is returned, the remainder of the checkiandj statement is completed, and checkiandj reiterates until its condition returns false.When false is returned, the program continues at the statement following checkiandj.

If continue had a label of checkiandj, the program would continue at the top of the checkiandj statement.

*/

let i = 0;
let j = 10;
checkiandj: while ( i < 4 ) {
   console.log( i );
   i += 1;
   checkj: while ( j > 4 ) {
      console.log( j );
      j -= 1;
      if ( j % 2 === 0 ) {
         continue checkj;
      }
      console.log( j, "is odd." );
   }
   console.log( "i =", i );
   console.log( "j =", j );
}