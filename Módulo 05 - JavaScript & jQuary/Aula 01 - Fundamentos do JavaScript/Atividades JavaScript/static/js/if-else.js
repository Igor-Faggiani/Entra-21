// Exercice 2:

// Will alert be shown? 

if ("0") {
    alert( 'Hello' ); // Resposta: Sim, ele vai mostra o Hello
  }

  // ---------------------------------------------------------------- //

  // Exercice 2:

//   Using the if..else construct, write the code which asks: ‘What is the “official” name of JavaScript?’

// If the visitor enters “ECMAScript”, then output “Right!”, otherwise – output: “You don’t know? ECMAScript!”

let nameJavaScript = prompt("Qual o nome oficial do JavaScript?");

if (nameJavaScript == "ECMAScript") {
    alert("Você Acertou!")
} else {
    alert("Você Errou!")
}

// ---------------------------------------------------------------- //

// Exercice 3:

// Using if..else, write the code which gets a number via prompt and then shows in alert:

// 1, if the value is greater than zero,
// -1, if less than zero,
// 0, if equals zero.
// In this task we assume that the input is always a number.

let numberValue = prompt("Digite um número");

if (numberValue >= 1) {
    alert("1");
} else if (numberValue < 0) {
    alert ("-1");
}else {
    alert("0");
};

// ---------------------------------------------------------------- //