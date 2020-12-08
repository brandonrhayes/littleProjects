const HOURHAND = document.querySelector("#hour");
const MINUTEHAND = document.querySelector("#minute");
const SECONDHAND = document.querySelector("#second");

//required base details because of current time
var date = new Date();
let hr = date.getHours();
let min = date.getMinutes();
let sec = date.getSeconds();

let hrPosition = (hr*360/12)+(min*360/60/12); // arbitrary
let minPosition = (min*360/60)+(sec*360/60/60);
let secPosition = sec*360/60;

function runTheClock(){ 
    //If the browser throttles the JS, we may lose track of time 
    // and the clock will get out of time.  But, for the animation, must do this way
    // could remove smoothing animation and revert to simpler script.
     
    hrPosition = hrPosition + (3/360)
    minPosition = minPosition+(1/60*6);  // 6/60 = 1/10
    secPosition = secPosition+(360/60) // = 6

    HOURHAND.style.transform = "rotate(" + hrPosition + "deg)";
    MINUTEHAND.style.transform = "rotate(" + minPosition + "deg)";
    SECONDHAND.style.transform = "rotate(" + secPosition + "deg)";
}

var interval = setInterval(runTheClock, 1000); 
//update time every second
