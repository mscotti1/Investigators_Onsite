// References to DOM Elements
const prevBtn = document.querySelector("#prev-btn");
const nextBtn = document.querySelector("#next-btn");
const book = document.querySelector("#book");

const paper1 = document.querySelector("#p1");
const paper2 = document.querySelector("#p2");
const paper3 = document.querySelector("#p3");
const paper4 = document.querySelector("#p4");
const paper5 = document.querySelector("#p5");

// Event Listener
prevBtn.addEventListener("click", goPrevPage);
nextBtn.addEventListener("click", goNextPage);

// Business Logic
let currentLocation = 1;
let numOfPapers = 5;
let maxLocation = numOfPapers + 1;

function openBook() {
    book.style.transform = "translateX(50%)";
    prevBtn.style.transform = "translateX(-180px)";
    nextBtn.style.transform = "translateX(180px)";
}

function closeBook(isAtBeginning) {
    if(isAtBeginning) {
        book.style.transform = "translateX(0%)";
    } else {
        book.style.transform = "translateX(100%)";
    }
    
    prevBtn.style.transform = "translateX(0px)";
    nextBtn.style.transform = "translateX(0px)";
}

function goNextPage() {
    //console.log(currentLocation)
    if(currentLocation < maxLocation) {
        switch(currentLocation) {
            case 1:
                openBook();
                paper1.classList.add("flipped");
                setTimeout(function() {
                    paper1.style.zIndex = 0;
                    console.log("This line will execute after 0.5 seconds.");
                  }, 250); // 500 milliseconds = 0.5 seconds
                break;
            case 2:
                paper2.classList.add("flipped");
                setTimeout(function() {
                    paper2.style.zIndex = 0;
                    console.log("This line will execute after 0.5 seconds.");
                  }, 250); // 500 milliseconds = 0.5 seconds
                break;
            case 3:
                paper3.classList.add("flipped");
                setTimeout(function() {
                    paper3.style.zIndex = 0;
                    console.log("This line will execute after 0.5 seconds.");
                  }, 250); // 500 milliseconds = 0.5 seconds
                break;
            case 4:
                paper4.classList.add("flipped");
                setTimeout(function() {
                    paper4.style.zIndex = 0;
                    console.log("This line will execute after 0.5 seconds.");
                  }, 250); // 500 milliseconds = 0.5 seconds
                break;
            case 5:
                paper5.classList.add("flipped");
                paper5.style.zIndex = 0;
                closeBook(false);
                break;
            default:
                throw new Error("unkown state");
        }
        currentLocation++;
    }
}

function goPrevPage() {
    //console.log(currentLocation)
    if(currentLocation > 1) {
        switch(currentLocation) {
            case 2:
                closeBook(true);
                paper1.classList.remove("flipped");
                paper1.style.zIndex = 6;
                break;
            case 3:
                paper2.classList.remove("flipped");
                paper2.style.zIndex = 5;
                break;
            case 4:
                paper3.classList.remove("flipped");
                paper3.style.zIndex = 4;
                break;
            case 5:
                paper4.classList.remove("flipped");
                paper4.style.zIndex = 3;
                setTimeout(function() {
                    paper4.style.zIndex = 3;
                    console.log("This line will execute after 0.5 seconds.");
                  }, 500); // 500 milliseconds = 0.5 seconds
                break;
            case 6:
                openBook();
                paper5.style.zIndex = 1;
                setTimeout(function() {
                    paper5.style.zIndex = 1;
                    console.log("This line will execute after 0.5 seconds.");
                  }, 250); // 500 milliseconds = 0.5 seconds
                paper5.classList.remove("flipped");
                break;
            default:
                throw new Error("unkown state");
        }

        currentLocation--;
    }
}