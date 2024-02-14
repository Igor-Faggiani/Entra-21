jQuery(function() {
    $("#submitButton").on("click", function () {
        $button = $(this);

        $button.prop("disabled", true);
        
        $("#buttonText").text("carregando...");
        $("#loadingSpinner").show();

        $("form").submit();
    });
});