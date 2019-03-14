
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

var doc = document.getElementById('thanksuser')
var newText = ''

jQuery.ajax({
    url: 'https://api.spotify.com/v1/me',
    headers: {
       'Authorization': 'Bearer ' + hash
    },
    dataType: "json",
    success: function(result){
        newText = result.id + "<br>"  + result.display_name + "<br>" +  result.birthdate + "<br>" + result.email + "<br>" + result.external_urls.spotify
        console.log(result)
        console.log(result.birthdate)
        console.log(result.display_name)
        console.log(result.email)
        console.log(result.id);
        console.log(result.external_urls.spotify)

        //doc.innerHTML = newText
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

        }
        doc.innerHTML = newText
    }
});

//document.getElementById("imageid").src="../template/save.png";
