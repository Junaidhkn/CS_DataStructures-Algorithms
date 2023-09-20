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