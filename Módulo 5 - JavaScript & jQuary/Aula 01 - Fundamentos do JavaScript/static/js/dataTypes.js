// Tipos de dados
/*
    Number --> Valor numérico
    string --> Caracteres
    boolean --> Verdadeiro ou falso
    null --> Vazio (None)
    undefined --> Quando não é atribuido um valor
*/

// Variáveis
// var valor = 1; Não utilizar
let number = 1;
let string = 'Hello world!';
let boolean = true;
let nothing = null;
let NotDefined;

console.log(typeof number);
console.log(typeof string);
console.log(typeof boolean);
console.log(typeof nothing);
console.log(typeof undefined);

// type casting
console.log(typeof String(number));
console.log(typeof Number("10.2"));
console.log(typeof +"10.2");

const ANO_ATUAL = 2023;
ANO_ATUAL = 2024;
console.log(ANO_ATUAL);
