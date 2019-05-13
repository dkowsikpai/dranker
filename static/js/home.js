function authen() {
    var passcode = $('#pcodelogin').val();
    var user = $('#scodelogin').val();
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    $.ajax({
        url: 'authen/',
        type:'POST',
        data:{
            'csrfmiddlewaretoken': csrftoken,
            'ucode': user,
            'pcode': passcode,
        },
        error: function () {
            alert("Error!!!");
        },
        success: function (response) {
            window.location.href=response;
        }
    });
}
