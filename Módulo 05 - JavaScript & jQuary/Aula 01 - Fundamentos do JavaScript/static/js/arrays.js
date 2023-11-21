// Criando um array
const colors = ["red", "green", "blue", "black", "white"];

// O tamanho de array
console.log(colors.length);

// Adicionar um elemento
colors.push("Yellow");

// Fatiamendo do array
console.log(colors.slice(0, 2));

// Remover um elemento do array
colors.pop();

// Remover um elemento pelo indice
colors.splice(0, 1);

// Iterando em um array
for (let i = 0; i <colors.length; i++) {
    console.log(colors[i]);
}

for (let color of colors) {
    console.log(color);
}

colors.forEach((item, index, array) => {
    console.log(`${item} está no índice ${index} do array ${array}`);

});