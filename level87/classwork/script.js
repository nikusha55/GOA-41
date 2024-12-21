let num = 0;
let img = document.querySelector('.slider');
function next(){
    num++;
    if (num >= images.length){
        num = 0;
    }
    img.style.display = "none"
    img.style.position = "relative"
    img.style.left = "500px"
    img.src = images[num]
    img.style.display = "inline"
    img.style.transform = "translateX(-500px)"
}
function previus(){
    num--;
    if(num < 0){
        num = images.length - 1;
    }
    img.src = images[num]
}