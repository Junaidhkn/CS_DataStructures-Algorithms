/*
The for...in statement iterates a specified variable over all the enumerable properties of an object. For each distinct property, JavaScript executes the specified statements. A for...in statement looks as follows:


for (variable in object)
  statement
*/


function dumpProps ( obj, objName ) {
   let result = "";
   for ( const i in obj ) {
      result += `${objName}.${i} = ${obj[i]}<br>`;
   }
   result += "<hr>";
   return result;
}