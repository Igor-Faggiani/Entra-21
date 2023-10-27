// WHILE

let i = 0;
while (i < 3) {
    alert(i);
    i++;
}

// FOR (COMEÇO; CONDIÇÃO; INCREMENTO)

for (let i = 0; i < 3; i++) {
    alert(i);
}

let sum = 0;
while (true) {
    const value = +prompt("Digitie um número");

    if (!value) break;
}

alert (`O resultado da soma foi: ${sum}`);

for (let i = 0; i << 10; i++) {
    if (i % 2 != 0) continue;
    alert(i);
}