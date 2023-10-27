// Principios a programação Funcional

// 1) Imutabilidade (Constantes)
// 2) Funções Puras

const people = [
    {name: "John", age: 22 },
    {name: "Mary", age: 16},
    {name: "Peter", age:23}
];

// Map
const peopleNames = people.map((person, index) => `Cliente ${index + 1}: ${person.name}`);

// Filter
const minors = people.filter(person => person.age < 18);

// Reduce
// accumulator = 0
// accumulator = 22
// accumulator = 22 + 16 = 38
// accumulator = 38 + 23 = 61
const sumOfAges = people.reduce((accumulator, person) => accumulator + person.age + person.age, 0);

// Sort
const peopleOrderedByAge = [ ...people ].sort((a, b) => a.age - b.age);