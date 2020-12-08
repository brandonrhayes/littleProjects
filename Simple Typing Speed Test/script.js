/*BRANDON R HAYES 01 DEC 2020
This is a typing speed test adopted from JS Essential Training
taught by Morten Rand-Hendriksen.  
*/

//CONSTANTS
const TESTWRAPPER = document.querySelector(".test-wrapper");
const TESTAREA = document.querySelector("#test-area");
const ORIGINTEXT = document.querySelector("#origin-text p").innerHTML;
const RESETBUTTON = document.querySelector("#reset");
const TIMER = document.querySelector(".timer");

//GLOBAL VARS
var timer = [0, 0, 0, 0]; // to hold the actual minute, seconds, ...
var interval; // tracks the interval set inside start that begins counting
    //this var allows me to stop the timer at completion of a correct response that matches exactly.
var timerRunning = false; // This prevents the timer from resetting if the user clears the text field

// Add leading zero to numbers below 10:
function leadingZero(time){
    if (time <= 9){  // any single digit number will be replaced with a leading 0 for aesthetics
        time = "0" + time;
    }
    return time;
}

// Run a standard minute/second/hundredths timer:
function runTimer(){
    let currentTime = leadingZero(timer[0]) + ":" + leadingZero(timer[1]) + ":" + leadingZero(timer[2])
    TIMER.innerHTML = currentTime;
    timer[3]++; // increment the timer every thousandth of a sec.
    //minutes seconds
    timer[0] = Math.floor((timer[3] / 100) / 60); // convert from 100th of sec -> sec then   sec -> min
    //seconds
    timer[1] = Math.floor((timer[3] / 100) - (timer[0] * 60));
    //hundreds of seconds
    timer[2] = Math.floor((timer[3]) - (timer[1] * 100) - (timer[0] * 6000)); 
}

// Match the text entered with the provided text on the page:
function validate(){
    let textEntered = TESTAREA.value;
    let originTextMatch = ORIGINTEXT.substring(0, textEntered.length) //allow us to parse string
    
    if (textEntered == ORIGINTEXT){
        clearInterval(interval) // text matches correctly, stop clock!
        TESTWRAPPER.style.borderColor = "green";
    } else {
        if(textEntered == originTextMatch){ // user is on the right track to success
            TESTWRAPPER.style.borderColor = "blue"
        } else{ // user made a mistake give them a visual clue
            TESTWRAPPER.style.borderColor = "orange"
        }
    }
}

// Start the timer:
function start(){
    let textEnteredLength = TESTAREA.value.length;  //originally 0

    if (textEnteredLength === 0 && !timerRunning){
        timerRunning = true;
        interval = setInterval(runTimer, 10); //run every thousand of a second
    }
    console.log(textEnteredLength);
}

// Reset everything:
function reset(){
    //functional reset
    clearInterval(interval);
    interval = null;
    timer = [0, 0, 0, 0];
    timerRunning = false;

    //visual reset
    TESTAREA.value = "";
    TIMER.innerHTML = "00:00:00";
    TESTWRAPPER.style.borderColor="grey";
}

// Event listeners for keyboard input and the reset button:
TESTAREA.addEventListener("keypress", start, false);
TESTAREA.addEventListener("keyup", validate, false);
RESETBUTTON.addEventListener("click", reset, false);