const arr = [21, 34, 54, 3, 5]

arr.pop()
arr.push()
// O(1) => Because we don't have to re-index the array

arr.unshift()
arr.shift()
// O(n) => where n is the number of items in the array,as it would also rearrange the index

arr.splice( 2, 0, 32 )
// O(n) => where n is the number of items in the array,as it would also rearrange the index


arr.find( 32 )
//  O(n) => where n is the number of items in the array



// Whereas, finding an element of array using its index number, upon which it returns a value is O(1) 



// // //  General Terms - Representing Big(O)

// O(n^2)  =>  Loop within a Loop
// O(n)  =>  Proportional
// O(log n)  =>  Divide and Conquer
// O(1)  =>  Constant