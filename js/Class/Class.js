class Cookie {
   constructor( color ) {
      this.color = color
   }
   getColor () {
      return this.color
   }
   setColor ( color ) {
      this.color = color
   }
}

const cookieOne = new Cookie( 'Brown' )
const cookieTwo = new Cookie( 'Yellow' )
cookieTwo.setColor( 'Green' )
// console.log( cookieOne )
// console.log( cookieTwo )


// Pointer Concept

// not a pointer

let num1 = 10
let num2 = num1
num2 = 20
// console.log( num1 ) // 10 num1 remains 10,because num2 is not a pointer

// pointer

let obj1 = { name: 'John' }
let obj2 = obj1
obj2.name = 'Bob'
// console.log( obj1 ) // { name: 'Bob' } obj1 is a pointer to obj2