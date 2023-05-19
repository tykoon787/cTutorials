#!/usr/bin/env node

/* 
This is telling the compiler the type
of a variable and this is how it is done
in ts
*/
let user_message = "Panda loves bamboo";

let end = (<string>user_message).endsWith('o');
console.log(end);