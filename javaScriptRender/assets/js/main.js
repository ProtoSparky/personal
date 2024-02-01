function init(){
    console.info("init");
    FrameBufferTest();
    setInterval(ConstantUpdate,1);
    ClearFrameBuffer();
    ImportMeshes(); 
};
function ConstantUpdate(){
    DisplayBuffer();
}

function DisplayBuffer (){
    if(RenderMap.camera.render.type == "div"){
        //display buffer using divs
        const DisplaySizeX = RenderMap.camera.render.resolution.x * RenderMap.camera.render.resolution.scale;
        const DisplaySizeY = RenderMap.camera.render.resolution.y* RenderMap.camera.render.resolution.scale;

        const render_area = document.getElementById("render");
        render_area.innerHTML = "";

        const FB_len_y = Object.keys(FrameBuffer).length;
        for(let vertical_gen_pointer = 0; vertical_gen_pointer < FB_len_y; vertical_gen_pointer ++){
            const FB_len_x = Object.keys(FrameBuffer[vertical_gen_pointer]).length;
            for(let horisontal_gen_pointer = 0; horisontal_gen_pointer < FB_len_x;horisontal_gen_pointer ++ ){
                const pixel = document.createElement("div");
                pixel.style.position = "absolute";
                pixel.style.width = RenderMap.camera.render.resolution.x * RenderMap.camera.render.resolution.scale;
                pixel.style.height = RenderMap.camera.render.resolution.y * RenderMap.camera.render.resolution.scale;
                pixel.style.left = (DisplaySizeX / RenderMap.camera.render.resolution.x) * horisontal_gen_pointer;
                pixel.style.top = (DisplaySizeY / RenderMap.camera.render.resolution.y) * vertical_gen_pointer;
                const col_r = FrameBuffer[vertical_gen_pointer][horisontal_gen_pointer]["r"];
                const col_g = FrameBuffer[vertical_gen_pointer][horisontal_gen_pointer]["g"];
                const col_b = FrameBuffer[vertical_gen_pointer][horisontal_gen_pointer]["b"]; 
                pixel.style.backgroundColor = currentColor = "rgb(" + col_r + ", " + col_g + ", " + col_b + ")";
                render_area.appendChild(pixel);
            }
        }        
    }  
    else if(RenderMap.camera.render.type == "canvas"){
        const DisplaySizeX = RenderMap.camera.render.resolution.x * RenderMap.camera.render.resolution.scale;
        const DisplaySizeY = RenderMap.camera.render.resolution.y* RenderMap.camera.render.resolution.scale;
        const render_area = document.getElementById("render");
        render_area.innerHTML = "";

        var canvas = document.createElement('canvas');
        canvas.style.position = "absolute";
        canvas.style.top = 0;
        canvas.style.left = 0;
        canvas.style.width = DisplaySizeX;
        canvas.style.height = DisplaySizeY;
        render_area.appendChild(canvas);
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        var ctx = canvas.getContext('2d');
        var imgData = ctx.getImageData(0, 0, DisplaySizeX, DisplaySizeY);
        var data = imgData.data;

        const FB_len_y = Object.keys(FrameBuffer).length;
        for(let vertical_gen_pointer = 0; vertical_gen_pointer < FB_len_y; vertical_gen_pointer++){
            const FB_len_x = Object.keys(FrameBuffer[vertical_gen_pointer]).length;
            for(let horisontal_gen_pointer = 0; horisontal_gen_pointer < FB_len_x; horisontal_gen_pointer++){
                const CurrentFB = FrameBuffer[vertical_gen_pointer][horisontal_gen_pointer];
                const col_r = CurrentFB["r"];
                const col_g = CurrentFB["g"];
                const col_b = CurrentFB["b"];

                // Calculate the index in the data array for the pixel
                var index = (vertical_gen_pointer * DisplaySizeX + horisontal_gen_pointer) * 4;

                // Set the color of the pixel
                data[index] = col_r;
                data[index + 1] = col_g;
                data[index + 2] = col_b;
                data[index + 3] = 255; // Alpha channel
            }
        }

        // Put the modified image data back onto the canvas
        ctx.putImageData(imgData, 0, 0);
    } 
}
//gets display resolution
function GetDisplayRes(type){
    if(type == "x"){
        return window.innerWidth; 
    }
    else if(type == "y"){
        return window.innerHeight; 
    }
}

function ImportMeshes(){
    //get all meshes
    const all_meshes_array = Object.keys(RenderMap.objects);
    const all_meshes_array_length = all_meshes_array.length; 
    
    //iterate trough meshes
    for(let mesh_pointer = 0; mesh_pointer < all_meshes_array_length; mesh_pointer ++){
        const current_mesh_name = all_meshes_array[mesh_pointer];
        
        //check if mesh is external 
        if(RenderMap.objects[current_mesh_name].type == "external"){
            //import mesh
            const OBJ_contents = ReadAnything(RenderMap.settings.objects.object_loc + current_mesh_name);
            const OBJ_parsed = parseObj(OBJ_contents);
            console.log(OBJ_parsed); 
        }
    }
}








