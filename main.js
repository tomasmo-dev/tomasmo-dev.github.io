const GithubLink = "https://github.com/tomasmo-dev";

if(!window.localStorage.getItem("mode")){

    window.localStorage.setItem("mode", "0");
}

if(window.localStorage.getItem("mode") == "1"){

    document.body.classList.toggle("dark-mode", true);
}else{

    document.body.classList.toggle("dark-mode", false);
}

document.getElementById("copy_link").onclick = function() {
    window.open(GithubLink);
}

window.onbeforeunload = function() {

    let ref = document.body;
    let bgColor = window.getComputedStyle(ref).getPropertyValue("background-color");

    if (bgColor == "rgb(0, 0, 0)"){

        window.localStorage.setItem("mode", "1");
    }else {

        window.localStorage.setItem("mode", "0");
    }

}

function darkModeToggle(){
    document.body.classList.toggle("dark-mode");
    
}
