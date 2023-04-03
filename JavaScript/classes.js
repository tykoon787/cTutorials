#!/usr/bin/node
class Person {
    name; 

    constructor(name) {
        this.name = name;
    }
    introduceSelf() {
        console.log(`Hi i'm ${this.name}`);
    }
}

/* Inheritance */
class Professor extends Person {
    teaches;

    constructor(name, teaches) {
        super (name);
        this.teaches = teaches;
    }

    introduceSelf() {
        console.log(`My name is ${this.name}, and I will be your ${this.teaches} professor`);
    }

    grade(paper) {
        const grade = Math.floor(Math.Random() * (5 -1) + 1);
        console.log(grade);
    }
}

const panda = new Person('Mantis');
panda.introduceSelf();

const Mr_Tiger = new Professor('Tiger', 'History');
Mr_Tiger.introduceSelf();
