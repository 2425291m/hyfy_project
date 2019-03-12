
$('#reviewForm').submit(function(event) {
    alert("You made a review!");
    event.preventDefault();
    });
    $.ajax({
        type: "POST",
        url:"/hyfy/post_comment/{{ venue.slug }}/",
        data:{
            'csrfmiddlewaretoken': $('input[name=csrf_token]').val()
        },
        success: function(data) {
            $('#commentlist').append(data);
        },
        dataType: 'html'
    });
});



