// Get Length: Create an array with 5 items. Log the length of the array.

const array = [1,2,3,4,5];
console.log(array.length);

// Convert to String: Convert the same array to a string using toString() and log the result.

const array1 = [1,2,3,4,5,6,7,8,9,10];
const arrayString = array1.toString();
console.log(arrayString);

// Access Element: Use the at() method to access the second element and log it.

const num = [12,45,78];
console.log(num.at());

// Join Elements: Use join() to combine the array elements with - between them.

const numbers = [1,3,5,7,9];
console.log(numbers.join(""));

// Push & Pop: Add two new elements to the array using push(), then remove the last element using pop().


const number = [45,86,74,21];
number.push(1);
const arr = number.pop();
console.log(number);
console.log(arr);

// Shift Element: Create an array and remove the first element using shift().

const numb = [45,87,21,10];
const num1 = numb.shift();
console.log(num1);

// Unshift Element: Add a new element at the beginning using unshift().

const num2 = [1,2,3];
num2.unshift(0);
console.log(num2);

// Delete Element: Use the delete operator to remove the second element. Log the array and observe the result.

const text = [4,5,6];
delete text[4];
console.log(text);


// Concatenate Arrays: Create two arrays and use concat() to merge them.

const ani = [0,1,2,3,4,5];
const ann = [1,2,3,4];
const anii = ani.concat(ann);
console.log(anii);

// Explore Unshift & Length: After using unshift(), log the new length of the array.

const num3 = [7,6,5,4,3,2,1];
num3.unshift(10);
console.log(num3.length);

// Find Index: Create an array with repeated values. Use indexOf() to find the first occurrence of an element.

const name = ["ancho", "giorgi", "gvanca"];
console.log(name.indexOf("gio"));

// Find Last Index: Use lastIndexOf() to find the last occurrence of the same element

const num4 = [1,2,3,4,5];
console.log(num4.lastIndexOf(4));

// Check Inclusion: Use includes() to check if a specific element exists in the array.

const num5 = [1,2,3,4,5,6,10];
console.log(num5.includes(4));

// Check Inclusion: Use includes() to check if a specific element exists in the array.

const numberss = [10,20,30];
console.log(numberss.includes(4));

// Invalid Index Search: Use indexOf() to search for a non-existing element. Log the result.

const numm = [1,2,3,4,5];
console.log(numm.indexOf(6));

// Case Sensitivity: Check if includes() is case-sensitive by searching for different cases of the same string.

const names = ["anni", "eka", "mari"];
console.log(names.includes("anni"))

// Sort Strings: Create an array of strings and sort them using sort().

const fruit = ["apple", "banana", "orange", "kiwi"];
fruit.sort();
console.log(fruit);


// Reverse Array: Use reverse() on a sorted array and log the result.

const numberr = [1,3,5,7,9];
numberr.sort((a, b) => b - a);
console.log(numberr);


// Mix Sort and Reverse: Sort an array, then reverse it.

const numbe = [42, 17, 8, 23, 56, 3];
numbe.sort((a, b) => a - b);
numbe.reverse();
console.log(numbe);

// Sort and Push: Create an array of numbers, sort it, and add a new number using push(). Log the updated array.

const numberrr = [1,5,3,2,4];
numberrr.sort((a, b) => a - b);
numberrr.push(7);
console.log(numberrr);

// Concatenate and Sort: Create two arrays, merge them with concat(), and sort the result.

const num12 = [1,5,3,2,4];
const num13 = [7,9,6,8,0];
const num14 = num12.concat(num12);
num12.sort((a, b) => a - b);
console.log(num12);

// Push and Reverse: Add three new elements to an array, then reverse the entire array.

const numbers1 = [42, 17, 8, 23, 56, 3];
numbers1.push(15, 29, 4);
numbers1.reverse();


// Find and Remove Element: Use indexOf() to locate an element, then use splice() to remove it.

const Mynum = [1,2,3];
const index = Mynum.indexOf(3);
if (index > -1) {
    Mynum.splice(index, 1);
}
console.log(Mynum);


// Join and Include Check: Join the elements of an array into a string, split it back into an array, and check if a specific value is included using includes().

const myarr = ["apple", "banana", "orange"];
const joinArray = myarr.join(", ");
const myArrr = joinArray.split(", ");
console.log(myArrr.includes("banana"));