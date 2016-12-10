/**
 * Created by Artem on 12/3/2016.
 */


function addScripts() {
        $(".clickable-row").click(function(e) {
    if(e.target.id != "id_delete_btn")
    window.document.location = $(this).data("href");
    return true;
    });

    // $("[name='delete_form']").submit(function(e) {
    // $('#myModal').modal('toggle')
    // if(!c) {
    //     e.preventDefault();
    //     return false;
    // }
    // else {
    //     return true;
    // }
    // });

}

function instantSearch() {
    var ajaxRequest;
    console.log('instant search');
    ajaxRequest = new XMLHttpRequest();
    ajaxRequest.onreadystatechange = function() {
        if(ajaxRequest.readyState == 4 && ajaxRequest.status == 200) {
            var template = $("#table_template").html();
            var all = JSON.parse(ajaxRequest.responseText);
            can_delete = all['can_delete'];
            if(!all['dirs'].length) {
                if(!$('#id_search_error').length)
                    $('#id_name').after('<span id="id_search_error" class="error text-warning">Nothing found</span>')
                $('#template_div').html('');
                $('#pagination').hide()
            }
            else {
                $('#id_search_error').remove();


                var pagination_selector = $('#pagination');
                pagination_selector.show();
                pagination_selector.pagination({
                dataSource: all['dirs'],
                pageSize: 5,
                autoHidePrevious: true,
                autoHideNext: true,
                    ulClassName: 'pagination',
                callback: function(data, pagination) {
                    var dict = {
                        'dirs': data,
                        'can_delete': can_delete
                    };
                html = Mustache.render(template, dict);
                $('#template_div').html(html);
                    addScripts();
                }
            })
            }
        }
    };
    ajaxRequest.open('GET', '/get-directors/?name='+$('#id_name').val());
    ajaxRequest.send()
}

$(document).ready(function() {
    instantSearch();
    $('#id_name').on('input', instantSearch);
    $('#id_settings_btn').on('input', settings);
});