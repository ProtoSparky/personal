function init(){
    //script spawns menu
    StartGame();
}

function StartGame(){
    //spawns game

    //create background
    const GameBackground = document.createElement("canvas");
    GameBackground.style.position = "absolute";
    GameBackground.id = RenderMap.settings.canvas.id; 
    GameBackground.style.top = "0px";
    GameBackground.style.left = "0px";
    GameBackground.style.backgroundColor = RenderMap.settings.canvas.background_color; 
    document.body.appendChild(GameBackground);


    
    setInterval(CheckForInput,10);
    setInterval(BackgroundUpdate,1000);
    setInterval(RenderFrameBuffer,10);
    //TEST_Rotate();
}

function CheckForInput(){
    //function that runs every 10ms
    

}
function BackgroundUpdate(){
    //update things in the background

}

function RenderFrameBuffer(){
    //iterate trough framebuffer
    const Canvas = document.getElementById(RenderMap.settings.canvas.id);
    const ctx = Canvas.getContext(RenderMap.settings.render_settings.dimention);
    ctx.clearRect(0,  0, Canvas.width, Canvas.height); // Clear the canvas

    for(let FB_pointer = 0; FB_pointer < Object.keys(RenderMap.objects).length; FB_pointer ++){
        const CurrentObject = RenderMap.objects[Object.keys(RenderMap.objects)[FB_pointer]]; 
        //console.log(CurrentObject); 
        const Canvas = document.getElementById(RenderMap.settings.canvas.id);
        const ctx = Canvas.getContext(RenderMap.settings.render_settings.dimention);
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


        
        //apply styles
        if(CurrentObject.object_data.style.LineStyle != undefined){
            //set line thickness
            if(CurrentObject.object_data.style.LineStyle.width != undefined){
                ctx.lineWidth = CurrentObject.object_data.style.LineStyle.width;  //TODO fux this bug
            }

            //set color
            if(CurrentObject.object_data.style.LineStyle.background_color != undefined){
                ctx.strokeStyle = CurrentObject.object_data.style.LineStyle.background_color; 
            }
            
        }

        //transform object space to world space coordinates
        //Read from vtex, transform, and write to vtex_transformed
        function applyTranslation(vertex, translation) {
            return {
                x: vertex.x + translation.x,
                y: vertex.y + translation.y,
            };
        }
        CurrentObject.object_data.vtex_transformed = CurrentObject.object_data.vtex.map(vertex => applyTranslation(vertex, CurrentObject.transform.loc));

        
        //apply rotation to transformed data
        if(CurrentObject.transform.rot != undefined){
            // Calculate the center of the polygon
            let centerX =  0;
            let centerY =  0;
            for (let i =  0; i < CurrentObject.object_data.vtex_transformed.length; i++) {
                centerX += CurrentObject.object_data.vtex_transformed[i].x;
                centerY += CurrentObject.object_data.vtex_transformed[i].y;
            }
            centerX /= CurrentObject.object_data.vtex_transformed.length;
            centerY /= CurrentObject.object_data.vtex_transformed.length;

            // Translate to the center of the polygon
            ctx.translate(centerX, centerY);

            // Rotate the context
            const angleInRadians = CurrentObject.transform.rot.z * Math.PI /  180;
            ctx.rotate(angleInRadians);

            // Translate back
            ctx.translate(-centerX, -centerY);
        }
        

        //draw vertex data from transforemed data
        ctx.beginPath();
        ctx.moveTo(CurrentObject.object_data.vtex_transformed[0].x,CurrentObject.object_data.vtex_transformed[0].y);

        for (let i =  1; i < CurrentObject.object_data.vtex_transformed.length; i++) {
            ctx.lineTo(CurrentObject.object_data.vtex_transformed[i].x, CurrentObject.object_data.vtex_transformed[i].y); // Additional points
        }
        ctx.stroke();

        
    }


}

