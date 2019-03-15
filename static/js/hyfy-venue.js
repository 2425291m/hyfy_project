<script type="text/javascript">
var frm = '#review_form';

frm.submit(function(event) {
    alert("You made a review!");
    event.preventDefault();
    $.ajax({
        type: "POST",
        url:"/hyfy/show_review/{{ venue.slug }}/",
        data:{
            'csrfmiddlewaretoken': $('input[name=csrf_token]').val(),
            'review': frm.serialize(),
        },
        success: function(data) {
            $('#review-user').children().append(data);
            $('#review-text').children().append(data);
        },
        dataType: 'html'
    });
});
</script>