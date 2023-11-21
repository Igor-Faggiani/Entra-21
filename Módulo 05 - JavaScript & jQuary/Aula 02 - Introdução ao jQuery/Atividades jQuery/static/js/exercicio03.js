$(document).ready(() => {
    const $counter = $("#counter");
    const $toggleButtonAdd = $("#toggleButtonAdd");
    const $toggleButtonRemove = $("#toggleButtonRemove");

    // Contador
    let counter = 0;

    const updateCounter = () => $counter.text(counter);
    /** Incrementa o contador */
    const incrementCounter = () => {
        counter++;
        updateCounter();
    }
    /** Atualiza o contador */
    const decrementCounter = () => {
        counter--;
        updateCounter();
    }

    $toggleButtonAdd.click(incrementCounter);
    $toggleButtonRemove.click(decrementCounter);
});