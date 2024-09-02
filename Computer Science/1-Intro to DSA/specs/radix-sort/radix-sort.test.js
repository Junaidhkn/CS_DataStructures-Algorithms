/*

  Implement a radix sort in a function called radixSort.

  You'll probably need several functions
  
  You can implement it using a binary or decimal based bucketing but I'd recommend the decimal based buckets because
  it ends up being a lot more simple to implement.

*/
/*
//* Pseudo Code for Optimized Radix Sort

RADIX_SORT(array):
    ! Find the maximum number to determine the number of digits
    max_number = find_max(array)
    d = number_of_digits(max_number)

    !  Perform counting sort for each digit from least to most significant
    for i from 0 to d-1:
        array = COUNTING_SORT_BY_DIGIT(array, i)

    return array


COUNTING_SORT_BY_DIGIT(array, digit_position):
    ! Initialize count array for digits 0-9
    count = new Array(10).fill(0)
    output = new Array(array.length)

    ! Store count of occurrences of each digit at the current position
    for each number in array:
        digit = get_digit_value(number, digit_position)
        count[digit] += 1

    ! Update count array to hold actual positions in output
    for i from 1 to 9:
        count[i] += count[i - 1]

    ! Build the output array in reverse to maintain stable sorting
    for each number in array (in reverse order):
        digit = get_digit_value(number, digit_position)
        output[count[digit] - 1] = number
        count[digit] -= 1

    return output


!  Helper functions remain the same as previous explanation
find_max(array), number_of_digits(number), get_digit_value(number, digit_position)

*/

//! Optimized

function radixSort ( array ) {
  if ( array.length === 0 ) return array;

  // Find the maximum number to determine the number of digits
  const maxNumber = Math.max( ...array );
  const maxDigits = Math.floor( Math.log10( maxNumber ) ) + 1;

  // Perform counting sort for each digit from least significant to most significant
  for ( let digitPosition = 0; digitPosition < maxDigits; digitPosition++ ) {
    array = countingSortByDigit( array, digitPosition );
  }

  return array;
}

function countingSortByDigit ( array, digitPosition ) {
  const count = new Array( 10 ).fill( 0 );
  const output = new Array( array.length );

  // Store count of occurrences of each digit at the current digit position
  for ( let i = 0; i < array.length; i++ ) {
    const digit = getDigitValue( array[i], digitPosition );
    count[digit]++;
  }

  // Update the count array to hold actual positions in output
  for ( let i = 1; i < 10; i++ ) {
    count[i] += count[i - 1];
  }

  // Build the output array in reverse order to maintain stable sorting
  for ( let i = array.length - 1; i >= 0; i-- ) {
    const digit = getDigitValue( array[i], digitPosition );
    output[count[digit] - 1] = array[i];
    count[digit]--;
  }

  return output;
}

function getDigitValue ( number, position ) {
  // Get the digit at the specified position from right (0-indexed)
  return Math.floor( Math.abs( number ) / Math.pow( 10, position ) ) % 10;
}

// Code implementation

// number = 1391 , place = 0 , longestNumber = 4
// returns 1
function getDigit ( number, place, longestNumber ) {
  const string = number.toString();
  const size = string.length;

  const mod = longestNumber - size;
  return string[place - mod] || 0;
}

function findLongestNumber ( array ) {
  let longest = 0;
  for ( let i = 0; i < array.length; i++ ) {
    const currentLength = array[i].toString().length;
    longest = currentLength > longest ? currentLength : longest;
  }
  return longest;
}

function radixSort ( array ) {
  const longestNumber = findLongestNumber( array );

  const buckets = new Array( 10 ).fill().map( () => [] ); // make an array of 10 arrays

  for ( let i = longestNumber - 1; i >= 0; i-- ) {
    while ( array.length ) {
      const current = array.shift();
      buckets[getDigit( current, i, longestNumber )].push( current );
    }

    for ( let j = 0; j < 10; j++ ) {
      while ( buckets[j].length ) {
        array.push( buckets[j].shift() );
      }
    }
  }

  return array;
}

// unit tests
// do not modify the below code
describe.skip( "radix sort", function () {
  it( "should sort correctly", () => {
    const nums = [
      20,
      51,
      3,
      801,
      415,
      62,
      4,
      17,
      19,
      11,
      1,
      100,
      1244,
      104,
      944,
      854,
      34,
      3000,
      3001,
      1200,
      633
    ];
    const ans = radixSort( nums );
    expect( ans ).toEqual( [
      1,
      3,
      4,
      11,
      17,
      19,
      20,
      34,
      51,
      62,
      100,
      104,
      415,
      633,
      801,
      854,
      944,
      1200,
      1244,
      3000,
      3001
    ] );
  } );
  it( "should sort 99 random numbers correctly", () => {
    const fill = 99;
    const nums = new Array( fill )
      .fill()
      .map( () => Math.floor( Math.random() * 500000 ) );
    const ans = radixSort( nums );
    expect( ans ).toEqual( nums.sort() );
  } );
} );
