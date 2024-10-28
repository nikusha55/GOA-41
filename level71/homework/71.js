//  თითეულ ნასწავლ მეთოდზე გააკეთეთ 10-10 მაგალითი

console.log(Math.abs(20));
console.log(Math.PI);
console.log(Math.ceil(10));
console.log(Math.pow(10));
console.log(Math.floor(6.2));
console.log(Math.sqrt(10));
console.log(Math.max(15, 20, 34, 100, 70));
console.log(Math.min(17, 2, 78, 64));
console.log(Math.E(45));
console.log(Math.random);


// Write a function that generates a random number between 1 and 100 using Math.random(). Ensure the number is an integer.

function randomNumber (){
    return Math.floor(Math.random() * 100) + 1;
}

//  Write a function that calculates the area of a circle given the radius using the formula πr², and use Math.PI for π.

function calculateSarea(radius){
    return Math.PI * Math.pow(radius, 2);
}