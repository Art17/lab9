/**
 * Created by Artem on 12/4/2016.
 */

$(document).ready(function() {
    $('.nav li').click(function(e) {
        $('.nav li.active').removeClass('active');
        console.log('hello')
        var $this = $(this);
        if(!$this.hasClass('active')) {
            $this.addClass('active')
        }
    });
});