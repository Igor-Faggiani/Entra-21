// Variábeis

// Questão 1:

// let admin, names;

// names = "John";

// admin = names;

// alert(admin);

// Questão 2:

// let ourPlanetName = earth;
// let visitName = "Igor";

// Questão 3:

// const BIRTHDAY = '18.04.1982'; // make birthday uppercase?

// const AGE = someCode(BIRTHDAY); // make age uppercase? Sim, devemos manter em maiusculo.

// Data Types

// Questão 1:

// let name = "Ilya";

// alert( `hello ${1}` ); // Number "1"
// alert( `hello ${"name"}` ); // String "name"
// alert( `hello ${name}` ); // Variable Value "Ilya"

// Objects

//Questão 1:

function isEmpty(obj) {
    for (let key in obj) {
        return false;
    }
    return true;
}

let schedule = {};

alert( isEmpty(schedule) );

schedule["8:30"] = "get up";

alert ( isEmpty(schedule));

// Questão 2:

let salaries = {
    John: 100,
    Ann: 160,
    Pete: 130
};

let sum = 0;
for (let key in salaries) {
    sum += salaries[key];
};

alert(sum);

// Questão 3:

function multiplyNumeric(obj) {
    for (let key in obj) {
        if (typeof obj[key] === "number") {
            obj[key] *= 2;
        }
    }
}

let menu = {
    with: 200,
    height: 300,
    title: "My menu"
};

multiplyNumeric(menu);

// 