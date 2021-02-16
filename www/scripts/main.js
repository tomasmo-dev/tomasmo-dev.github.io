function downloadItem(lang, Item){
    let element = document.createElement('a');

    element.setAttribute('href', `../downloads/${lang}`)
    element.setAttribute('download', Item);

    element.style.display = 'none';

    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}

function darkToggle() {
    
    let border = document.getElementById("HeadBorder");

    document.body.classList.toggle("darkMode");

    let BodyRef = document.getElementsByTagName("body");
    let Cstyle = window.getComputedStyle(BodyRef[0]);
    
    let color = Cstyle.getPropertyValue("background-color");

    if (color == "rgb(255, 255, 255)") {
        border.style.setProperty("background-color", "rgb(255, 255, 255)");
    } else {
        border.style.setProperty("background-color", "rgb(0, 0, 0)");
    }
}

//window.location.href = "something";