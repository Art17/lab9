/**
 * Created by Artem on 11/26/2016.
 */
jQuery(document).ready(function($) {
    $(".clickable-row").click(function(e) {
        if(e.target.id != "id_delete_btn")
        window.document.location = $(this).data("href");
        return true;
    });
});

/*function addEvent(node, type, callback) {
    if(node.addEventListener) {
        node.addEventListener(type, function(e) {
            callback(e, e.target);
        }, false);
    }
    else if (node.attachEvent) {
        node.attachEvent('on' + type, function(e) {
            callback(e, e.srcElement);
        }, false);
    }
}

clickable_elements = document.getElementsByClassName('clickable-row');

for (var i = 0; i < clickable_elements.length; i++) {
    addEvent(clickable_elements[i], 'click', function (e) {
    if (e.target.id != "id_delete_btn") {
        window.document.location = "/"
    }
});
}*/