var Data = {
    "parralax_active":false, 
    "img_array":[0,1,2], 
    "frame":{
        "width":400,
        "height":300
    }, 
    "img":{

    }

}

function init(){
    console.info("init run");
    const FileType = ".png"; 
    const content = document.getElementById("content-fullscreen"); 


    const ImgFrame = document.createElement("div"); 
    ImgFrame.style.position = "relative";
    ImgFrame.style.top = "50%";
    ImgFrame.style.left = "50%";
    ImgFrame.style.transform = "translate(-50%,-50%)";
    ImgFrame.style.overflow = "hidden"; 
    ImgFrame.style.width = Data.frame.width;
    ImgFrame.style.height = Data.frame.height;
    ImgFrame.style.backgroundColor = "red"; 
    content.appendChild(ImgFrame);  

    for(let pointer = 0; pointer < Data.img_array.length; pointer ++){
        //create images
        const IMG = document.createElement("img");
        IMG.style.position = "absolute";
        IMG.style.top = 0;
        IMG.style.width = "100%";
        IMG.style.height = "auto"; 
        IMG.style.left = 0; 
        IMG.style.objectFit = "cover";
        IMG.src = "./assets/img/" + pointer + FileType; 
        IMG.style.zIndex = pointer;
        IMG.id = "IMG" + pointer; 
        ImgFrame.appendChild(IMG); 

        //writ loc to data
        Data.img[pointer] = {
            "x":parseInt(IMG.style.left),
            "y":parseInt(IMG.style.top)
        }
    }
    //add detector frame
    const Detector = document.createElement("div");
    Detector.style.position = "absolute";
    Detector.style.width = Data.frame.width + 40;
    Detector.style.height = Data.frame.height + 40;
    Detector.style.left = "-20px";
    Detector.style.top = "-20px";
    Detector.id = "detector";
    Detector.style.zIndex = Data.img_array.length + 1; 
    Detector.addEventListener("mousemove", function(event){
        SaveCoordinates(event); 
    });
    Detector.addEventListener("mouseleave", function(){
        ResetImages(); 
    })
    ImgFrame.appendChild(Detector);
    
    

}

function SaveCoordinates(event){
    const MouseX = event.layerX; 
    const MouseY = event.layerY; 
    const MouseFromCenterY = MouseY - (Data.frame.height/2); 
    const MouseFromCenterX = MouseX - (Data.frame.width/2); 

    for(let pointer = 1; pointer < Data.img_array.length; pointer ++){
        const Img = document.getElementById("IMG" + pointer);
        const pointerOffset = 0.008 + (pointer-1) * 0.01; 
        const padding =  pointerOffset; 
        Img.style.left = Data.img[pointer].x + (-MouseFromCenterX) * padding; 
        Img.style.top = Data.img[pointer].y + (-MouseFromCenterY) * padding; 
        Img.style.transition = "0.2s"; 
    }


}
function ResetImages(){
    for(pointer = 0; pointer < Data.img_array.length; pointer ++){
        const Img = document.getElementById("IMG" + pointer); 
        Img.style.top = 0;
        Img.style.left = 0; 
    }
}