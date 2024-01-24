jQuery(function() {
    const $enabledCheckBox = $(".form-check-input");

    $enabledCheckBox.on("click", function () {
        const url = $(this).data("url");

        fetch(url, {
            method: "POST",
            headers: {
                "X-CSRFToken": Cookies.get("csrftoken")
            }
        })
        .then(res => res.json())
        .then(data => console.log(data))
        .catch(console.error);
    });
});