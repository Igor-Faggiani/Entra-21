$(document).ready(() => {
    const campo = $(".campo-digitacao");
    const tempoInicial = $("#tempo-digitacao").text();


    attSizePhrase();
    initializeCounter();
    initializeTimer();
    $("#botao-reiniciar").click(resetGame);


    function attSizePhrase() {

        /** Acessando o conteúdo da classe através do .text() */
        let frase = $(".frase").text();

        /**
         * Quebrando a frase em strings através do .split() -> array
         * Acessando o número de palavras do array com uma variável utilizando o .length()
         */
        let numPalavras = frase.split(" ").length;

        /** Atualizando o número de palavras */
        let tamanhoFrase = $("#tamanho-frase");
        tamanhoFrase.text(numPalavras);
    }


    function initializeCounter() {

        //* Detectando um evento de input */
        campo.on("input", function () {
            //* Função para contar a quantidade de palavras dentro do <textarea> */
            let conteudo = campo.val(); // Acessando o conteúdo do <textarea> utilizando .val()

            let qntdPalavras = conteudo.split(/\S+/).length - 1; // contando as palavras com .split(/\S+/)
            $("#contador-palavras").text(qntdPalavras); // Atualizando o contador de palavras

            /** Atualiznando a quantidade de caracteres */
            let qntdCaracteres = conteudo.length;
            $("#contador-caracteres").text(qntdCaracteres);
        });
    }


    function initializeTimer() {

        /** Implementando o contador de tempo */
        let tempoRestante = $("#tempo-digitacao").text();
        campo.one("focus", function () { // Detectando a ação do usuário ao entrar no <textarea>


            /** Timer */
            let cronometroID = setInterval(function () { // Implementando um intervalo de 1 seg com .setInterval()
                tempoRestante--; // Subtraindo 1 do nosso tempo restante
                $("#tempo-digitacao").text(tempoRestante); // Atualizando o contador de tempo


                /** Desabilitando o timer quando chegar ao 0 */
                if (tempoRestante < 1) {
                    campo.attr("disabled", true);
                    clearInterval(cronometroID);
                }
            }, 1000);

        });
    }


    function resetGame() {

        /** Implementando botão de reset */
        campo.attr("disabled", false);
        campo.val(" ");
        $("#contador-palavras").text("0");
        $("#contador-caracteres").text("0");
        $("#tempo-digitacao").text(tempoInicial);
        initializeTimer();
    }
});
