$(document).ready(() => {
    const $clicker = $("#clicker");
    const $secret = $("#secret");

    let isMessageVisible = false;

    const toggleMessage = () => {
        isMessageVisible = !isMessageVisible;
        if (isMessageVisible) {
            $secret.show();
        } else {
            $secret.hide();
        }

        $clicker.text(isMessageVisible ? "Clique para esconder o segredo!" : "Clique para revelar um segredo!");
    }

    $clicker.click(toggleMessage);
});