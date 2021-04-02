
jQuery(document).ready(function () {
    $('.bt_command').off().click(function(e) {
        e.preventDefault();
        console.log("r cmd");
        jQuery.ajax({
            url: "/",
            method: 'GET',
            data: {
                name: $(this).attr('id'),
                click: true
            }
        });
    });
});
