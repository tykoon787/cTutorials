#!/usr/bin/env node
/* 
Things to note: 
    var - Global variables
    let - Inscope variables
    Use the let keyword to declare variables
*/

function doSomething(message) {
    for (var i = 0; i < 5; i++) {
        console.log(message + " [" + i + "]");
    }
    console.log("Finally: " + i);
}


let message = "Hello World";
doSomething(message);