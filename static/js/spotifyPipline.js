console.log("jsRunning")

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
            document.getElementById("userprofile").src=result.images[0].url;
            document.getElementById("spotifyphotof").value=result.images[0].url;
        }
    });

    jQuery.ajax({
        url: 'https://api.spotify.com/v1/me/top/artists?time_range=long_term&limit=10&offset=0',
        headers: {
        'Authorization': 'Bearer ' + hash
        },
        dataType: "json",
        success: function(result){
            for(var i=0; i<9;i++){
                //newText += "<br>" + result.items[i].name + "<br>" + result.items[i].images[2].url + "<br>" + result.items[i].external_urls.spotify
                document.getElementById("artist"+i).src=result.items[i].images[0].url
                document.getElementById("artist"+i+"link").href=result.items[i].external_urls.spotify
                document.getElementById("artist"+i+"linkf").value=result.items[i].external_urls.spotify
                document.getElementById("artist"+i+"imgf").value=result.items[i].images[0].url

            }
        }
    });

    console.log($('#userinfo_form input[name=crsfmiddlewaretoken]').val())
    $('#userinfo_form').submit(function(event){
        event.preventDefault();
        $.ajax({
            type: "POST",
            url:"/hyfy/user_details/",
            data:{
                'csrfmiddlewaretoken': $('#userinfo_form input[name=csrfmiddlewaretoken]').val(),
                'id': $('#usernamef').val(),
                'displayname': $('#displaynamef').val(),
                'spotifylink': $('#spotifylinkf').val(),
                'spotifyphoto': $('#spotifyphotof').val(),
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
                console.log(csrfmiddlewaretoken)
            }
        })
    })
})




//document.getElementById("imageid").src="../template/save.png";
