
//1.
function showMessage() {
    setTimeout(() => {
        console.log();
    }, 3000);
}

showMessage();



// 2.
setInterval(() => {
    const now = new Date();
    const timeString = now.toLocaleTimeString();
    console.log(timeString);
}, 1000);


// 3.
const colors = ["red", "green", "blue", "yellow", "purple", "orange"];
let index = 0;

setInterval(() => {
    document.body.style.backgroundColor = colors[index];
    index = (index + 1) % colors.length; 
}, 3000);


// 4.
const paragraphs = [
    
];

let paraIndex = 0;
const paragraphElement = document.getElementById("myParagraph");

setInterval(() => {
    paragraphElement.textContent = paragraphs[paraIndex];
    paraIndex = (paraIndex + 1) % paragraphs.length; 
}, 5000);



