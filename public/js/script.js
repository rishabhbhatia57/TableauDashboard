let isMobile = window.matchMedia("only screen and (max-width: 760px)").matches;
    let newSettings = 'Desktop'

    if (isMobile) { //this returns true or false
        newSettings = 'Phone'
    }

var url = 'https://vetinatableau.azurewebsites.net/GetJWT';
    fetch(url, {
        method: 'GET',
    }).then(res => res.json())
        .then(response => {
            console.log(response['token']);
            var elementVar = document.getElementById("tableauViz");
            elementVar.setAttribute("token", response['token']);
            elementVar.setAttribute("device", newSettings);
            document.getElementById("loadingcheck").innerHTML = "<div class='alert alert-success' role='alert'><h3 id='loadingMessage'>Loaded successfully!</h3></div>";
            
        })