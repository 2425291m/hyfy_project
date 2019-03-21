console.log("jsRunning")

//within this javascript file i made the decision to use both AJAX/jQuery and plain JS syntax, in order to practice both.
//This is why, in some cases, I have used document.getElementById('element'), and in others ive used $('#element').

$(document).ready(function(){

    var tempurl = window.location.hash
    //this is a hacky way to get around socialauth not giving us an easy wat to access our access token
    //social auth loads the webpage initially without the token, the if statement then reloads the page
    //with the token
    if(tempurl.length < 30){
        url = 'https://accounts.spotify.com/authorize?client_id=294156b84c3a4659838991a3ebec94e2&redirect_uri=http://127.0.0.1:8000/hyfy/thanks/&scope=user-read-email,user-read-private,user-read-birthdate,user-top-read&response_type=token'
        w = window.open(url, "_self")
    }


    var hash = window.location.hash
    hash = hash.slice(14, hash.length-34)
    console.log(hash)


    //user information getting and setting.
    jQuery.ajax({
        url: 'https://api.spotify.com/v1/me',
        headers: {
        'Authorization': 'Bearer ' + hash
        },
        dataType: "json",
        success: function(result){
            console.log(result)
            console.log(result.birthdate)
            console.log(result.display_name)
            document.getElementById("displaynamef").value = result.display_name
            console.log(result.email)
            document.getElementById("emailf").value = result.email
            console.log(result.id)
            document.getElementById("usernamef").value = result.id
            console.log(result.external_urls.spotify)
            document.getElementById("spotifylinkf").value = result.external_urls.spotify
            document.getElementById("spotifyphotof").value=result.images[0].url;
        }
    });

    //artist information getting and setting

    var genres = [];
    var pop = 0;
    var hiphop = 0;
    var dance = 0;
    var rock = 0;
    var indie = 0;
    var jazz = 0;
    var rap = 0;
    var other = 0;
    var topGenreNo = 0;
    var topGenre = "";


    jQuery.ajax({
        url: 'https://api.spotify.com/v1/me/top/artists?time_range=long_term&limit=10&offset=0',
        headers: {
        'Authorization': 'Bearer ' + hash
        },
        dataType: "json",
        success: function(result){
            for(var i=0; i<9;i++){

                //loop to add artists genres to genre arrays
                for(var j=0; j < result.items[i].genres.length; j++){
                    genres.push(result.items[i].genres[j])
                }

                document.getElementById("artist"+i+"linkf").value=result.items[i].external_urls.spotify
                document.getElementById("artist"+i+"imgf").value=result.items[i].images[0].url
            }

            //loop to calculate top genre using very simple algorithm
            for(var k = 0; k<genres.length;k++){
                if(genres[k].includes("pop")){
                    pop++
                } else if(genres[k].includes("hip hop")){
                    hiphop++
                } else if(genres[k].includes("dance")){
                    dance++
                } else if(genres[k].includes("rock")){
                    rock++
                } else if(genres[k].includes("indie")){
                    indie++
                } else if(genres[k].includes("jazz")){
                    jazz++
                } else if(genres[k].includes("rap")){
                    rap++
                } else if(genres[k].includes("other")){
                    other++
                }
            }
            if(pop > topGenreNo){
                topGenre = "pop"
                topGenreNo = pop
            }
            if(hiphop > topGenreNo){
                topGenre = "hip hop"
                topGenreNo = hipop
            }
            if(dance > topGenreNo){
                topGenre = "dance"
                topGenreNo = dance
            }
            if(rock > topGenreNo){
                topGenre = "rock"
                topGenreNo = rock
            }
            if (indie > topGenreNo){
                topGenre = "indie"
                topGenreNo = indie
            }
            if(jazz > topGenreNo){
                topGenre = "jazz"
                topGenreNo = jazz
            }
            if (rap >topGenreNo){
                topGenre = "rap"
                topGenreNo = rap
            }
            if(other >topGenreNo){
                topGenre = "other"
                topGenreNo = other
            }
            document.getElementById("topGenre").value=topGenre
            submitForm()
        }
    });
 

    //submit the form
    function submitForm(){
        $.ajax({
            type: "POST",
            url:"/hyfy/user_details/",
            data:{
                'csrfmiddlewaretoken': $('#userinfo_form input[name=csrfmiddlewaretoken]').val(),
                'id': $('#usernamef').val(),
                'displayname': $('#displaynamef').val(),
                'spotifylink': $('#spotifylinkf').val(),
                'spotifyphoto': $('#spotifyphotof').val(),
                'topGenre': $('#topGenre').val(),
                'artist0link': $('#artist0linkf').val(),
                'artist0img': $('#artist0imgf').val(),
                'artist1link': $('#artist1linkf').val(),
                'artist1img': $('#artist1imgf').val(),
                'artist2link': $('#artist2linkf').val(),
                'artist2img': $('#artist2imgf').val(),
                'artist3link': $('#artist3linkf').val(),
                'artist3img': $('#artist3imgf').val(),
                'artist4link': $('#artist4linkf').val(),
                'artist4img': $('#artist4imgf').val(),
                'artist5link': $('#artist5linkf').val(),
                'artist5img': $('#artist5imgf').val(),
                'artist6link': $('#artist6linkf').val(),
                'artist6img': $('#artist6imgf').val(),
                'artist7link': $('#artist7linkf').val(),
                'artist7img': $('#artist7imgf').val(),
                'artist8link': $('#artist8linkf').val(),
                'artist8img': $('#artist8imgf').val(),
            },
            success: function(data){
                console.log("form submitted")
                window.open('/hyfy/', "_self")
            }
        })
    }
})
