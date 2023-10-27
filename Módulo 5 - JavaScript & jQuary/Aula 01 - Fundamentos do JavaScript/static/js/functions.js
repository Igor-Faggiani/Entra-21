/**
 * Mostra uma mensagem no navegador.
 * @param {string} from - Quem está enviando a mensagem.
 * @param {string} message 
 */
// function showMessage(from, message = "Mensagem não fornecida.") {
//     alert(`${from}: ${message}`);
// }

// showMessage("Igor", "Declarando Funções!");
// showMessage("Desconhecido");

// Sintaxe normal
// function sum(n1, n2) {
//     return n1 + n2;
// }

// Sintaxe de arrow function
//**
 * Retorna a soma dos dois numeros
 * @param {number} n1 
 * @param {number} n2 
 * @returns {number}
 */
// const sum = (n1, n2) => n1 + n2;

//Multiline arrow function
const double = n => {
    const resultado = n * 2;
    return resultado;
}

console.log(double(8));

// Função anônima
const quadrado = function(n) {
    return n * n;
}

console.log(quadrado(5));

// IIFE
(function() {
    alert("IIFE");
})();