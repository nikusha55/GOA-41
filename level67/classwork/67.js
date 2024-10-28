// შექმენით კონსტრუქტორი, რომელსაც ექნება 5 პარამტერი, ამ კონსტრუქტორის დახმარებით შექმენით 5 სხვადასხვა ობიექტი, კომენტარებით ახსენით რა არის კონსტრუქტორი და რას აკეთებს new კეივორდი. (კომენტარები აუცილებელია)

const me = {
    firstname: "nika",
    age: 16,
    city: "Gori",
    email: "nika@example.com",
    height: 1.87
}

console.log(me)

// new - axali - keywordi axal obieqts tmnis

function Person(firstname, lastname, sisters, isWorking){
    this.firstname = firstname;
    this.lastname = lastname;
    this.sisters = sisters;
    this.isWorking = isWorking;
}

// new - ახალი - ეს keyword ქმნის ახალ ცარიელ ობიექტს

const person1 = new Person("nika", "edisherashvili", 2, true);



// Basic Constructor Create a constructor function Person that takes two parameters: name and age. Add a method introduce() that logs: "Hi, I am <name> and I am <age> years old."Example Input:

function person(name, age){
    this.name = name;
    this.age = age;
}

person.prototype.introduce = function(){
    console.log(`Hi, I am ${this.name} and I am ${this.age} years old.`);
}

// Constructor with Default Values Create a constructor function Car with parameters brand and year. If the year isn't provided, set a default value of 2020. Add a method describe() to print: "This is a <brand> from <year>."

function Car(brand, year = 2020){
    this.brand = brand;
    this.year = year;
}

Car.prototype.describe = function(){
    console.log(`This is a ${this.brand} from ${this.year}.`);
}


// Constructor with Arrays as Properties Create a Library constructor that takes name and an array of books. Add a method listBooks() to log all books.

function Library(name, books = []){
    this.name = name;
    this.books = books;
}

Library.prototype.listBooks = function(){
    console.log(`${this.name} library has ${this.books.length} books:`);
}


// Adding Methods Inside a Constructor Create a Rectangle constructor with parameters width and height. Add a method area() that returns the area of the rectangle.

function Rectangle(width, height){
    this.width = width;
    this.height = height;
}

Rectangle.prototype.area = function(){
}

// Constructor with Conditional Logic Create a Student constructor that takes name and marks (an array of numbers). Add a method hasPassed() that returns true if the average of marks is 50 or above; otherwise, false.

function Student(name, marks){
    this.name = name;
    this.marks = marks;
}


Student.prototype.hasPassed = function(){
    const average = this.marks.reduce((acc, current) => acc + current, 0) / this.marks.length;
    return average >= 50;
}

// Using this to Track State Create a Counter constructor with an initial value of 0. Add methods increment() and getValue() to increase the counter by 1 and retrieve the current value, respectively.



// Using Objects as Constructor Parameters Create a Phone constructor that takes an object parameter with brand, model, and price. Add a method info() to print the phone’s details: "This is a
                // <brand> <model> with a price of <price>."

function Phone(phoneInfo){
    this.brand = phoneInfo.brand;
    this.model = phoneInfo.model;
    this.price = phoneInfo.price;
}

Phone.prototype.info = function(){
    console.log(`This is a ${this.brand} ${this.model} with a price of ${this.price}.`);
}