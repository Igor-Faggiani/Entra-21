// Criando um objeto
const user = {
    name: "Igor",
    age: 23
};

// user.age = 24;

// Obtendo os valores
console.log(Object.values(user));

// Obtendo as chaves
console.log(Object.keys(user));

// Desructuring
const userCopy = { ...user };

const numbers = [1, 2, 3, 4, 5];
const  numbersCopy = [ ...numbers ];