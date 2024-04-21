function init(){
    //create frames
    const centerer = document.createElement("div");
    centerer.style.width = "80%";
    centerer.style.height = "80%";
    centerer.style.left = "50%";
    centerer.style.top = "45%"; 
    centerer.style.position = "absolute";
    centerer.style.transform = "translate(-50%,-50%)";
    centerer.style.borderRadius = AccessCSSVar("--CornerRad");
    centerer.style.backgroundColor = AccessCSSVar("--col_bg_lighter");
    document.getElementById("content-fullscreen").appendChild(centerer); 

    //create header






    



}