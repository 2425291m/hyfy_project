//var frm = '#review_form';

$(document).ready(function() {

    $('#review_form').submit(function(event) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url:"/hyfy/add_review/",
            data:{
                'csrfmiddlewaretoken': $('#review_form input[name=csrfmiddlewaretoken]').val(),
                'venue_slug': $('#review_form input[name=venue_slug]').val(),
                'comment': $('#comment_text').val(),
            },
            success: function(data) {
                $('#review-display').html(data);
            },
            dataType: 'html'
        });
    });

});