// 10 Simple Constructor Exercises Basic Constructor with Properties Create a Person constructor with properties name and age. Add a method introduce() that logs: "Hi, I am <name> and I am <age> years old."

function Person(name, age){
    this.name = name;
    this.age = age;
}

Person.prototype.introduce = function(){
    console.log(`Hi, I am ${this.name} and I am ${this.age} years old.`);
}


// Constructor with Default Parameter Value Create a Book constructor with parameters title and author. If no author is provided, set it to "Unknown". Add a method getDetails() to print the book's details.

function Book(title, author = "Unknown"){
    this.title = title;
    this.author = author;
}

Book.prototype.getDetails = function(){
    console.log(`Title: ${this.title}, Author: ${this.author}`);
}

// Constructor with Arrays Create a Classroom constructor that takes an array of students. Add a method countStudents() to log the number of students in the array.

// State Management with Constructor Create a Counter constructor with an initial value of 0. Add methods increment() and getValue() to increase the counter by 1 and retrieve the current value.

function Counter(){
    this.count = 0;
}

Counter.prototype.increment = function(){
    this.count++;
}

// Constructor with Boolean State Create a Light constructor with a state property initialized to "off". Add a method toggle() to switch the state between "on" and "off".

function Light(){
    this.state = "off";
}

Light.prototype.toggle = function(){
    if(this.state === "off"){
        this.state = "on";
    } else {
        this.state = "off";
    }
}

// Product Constructor with Properties Create a Product constructor with properties name and price. Add a method getDetails() to log: "Product: <name>, Price: <price> USD"

function Product(name, price){
    this.name = name;
    this.price = price;
}

Product.prototype.getDetails = function(){
    console.log(`Product: ${this.name}, Price: ${this.price} USD`);
}

// Constructor with Object Properties Create a User constructor with properties username and contact (an object containing email and phone). Add a method getContactInfo() to print the user’s contact information.

function User(username, contact){
    this.username = username;
    this.contact = contact;
}