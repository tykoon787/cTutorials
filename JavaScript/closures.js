#!/usr/bin/node
function makeFunc() {
    const name = "Panda";
    function displayName () {
        console.log(name);
    }
    return displayName;
}

const myFunc = makeFunc();
myFunc();