function init(){
    //script spawns menu
    StartGame();
}

function StartGame(){
    //spawns game

    //create background
    const GameBackground = document.createElement("canvas");
    GameBackground.style.position = "absolute";
    GameBackground.id = GameState.gamearea.style.id; 
    GameBackground.style.top = "0px";
    GameBackground.style.left = "0px";

    GameBackground.style.backgroundColor = GameState.gamearea.style.background_color; 
    document.body.appendChild(GameBackground);


    
    setInterval(CheckForInput,10);
    setInterval(BackgroundUpdate,1000);
    setInterval(RenderFrameBuffer,50);
}

function CheckForInput(){
    //function that runs every 10ms
    

}
function BackgroundUpdate(){
    //update things in the background

}

function RenderFrameBuffer(){
    //iterate trough framebuffer
    const Canvas = document.getElementById(GameState.gamearea.style.id);
    const ctx = Canvas.getContext("2d");
    ctx.clearRect(0,  0, Canvas.width, Canvas.height); // Clear the canvas


    for(let FB_pointer = 0; FB_pointer < Object.keys(GameState.framebuffer).length; FB_pointer ++){
        const CurrentObject = GameState.framebuffer[FB_pointer]; 
        //console.log(CurrentObject); 
        const Canvas = document.getElementById(GameState.gamearea.style.id);
        const ctx = Canvas.getContext("2d");

        // Get the device pixel ratio
        const dpr = window.devicePixelRatio ||  1;
        
        // Calculate the size of the canvas in pixels
        const canvasWidth = window.innerWidth * dpr;
        const canvasHeight = window.innerHeight * dpr;
        
        // Set the canvas size
        Canvas.width = canvasWidth;
        Canvas.height = canvasHeight;
        
        // Scale the context to match the device's pixel ratio
        ctx.scale(dpr, dpr);


        if(CurrentObject.ObjectProperties.id.render_id == "camera"){
            //apply camera stuff
        }
        else{
            //render objects
            
            //apply styles
            if(CurrentObject.style.LineStyle != undefined){
                //set line thickness
                if(CurrentObject.style.LineStyle.width != undefined){
                    ctx.lineWidth = CurrentObject.style.LineStyle.width;  //TODO fux this bug
                }

                //set color
                if(CurrentObject.style.LineStyle.background_color != undefined){
                    ctx.strokeStyle = CurrentObject.style.LineStyle.background_color; 
                }
            }
            
            //apply rotation
            if(CurrentObject.position.rotation != undefined){
                // Calculate the center of the polygon
                let centerX =  0;
                let centerY =  0;
                for (let i =  0; i < CurrentObject.position.position.length; i++) {
                    centerX += CurrentObject.position.position[i].x;
                    centerY += CurrentObject.position.position[i].y;
                }
                centerX /= CurrentObject.position.position.length;
                centerY /= CurrentObject.position.position.length;

                // Translate to the center of the polygon
                ctx.translate(centerX, centerY);

                // Rotate the context
                const angleInRadians = CurrentObject.position.rotation * Math.PI /  180;
                ctx.rotate(angleInRadians);

                // Translate back
                ctx.translate(-centerX, -centerY);
            }

            //draw polygons
            ctx.beginPath();
            ctx.moveTo(CurrentObject.position.position[0].x,CurrentObject.position.position[0].y);

            for (let i =  1; i < CurrentObject.position.position.length; i++) {
                ctx.lineTo(CurrentObject.position.position[i].x, CurrentObject.position.position[i].y); // Additional points
            }
            ctx.stroke();

        }
    }


}

