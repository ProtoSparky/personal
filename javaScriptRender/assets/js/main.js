function init(){
    console.info("init");
    FrameBufferTest();
    setInterval(ConstantUpdate,10);
    setInterval(FrameBufferTest, 50);
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

var runner = 0; 
function FrameBufferTest(){
    if(runner > 254){
        runner = runner - 1;
    }
    else{
        runner = runner + 1;
    }

    const res_x = RenderMap.camera.render.resolution.x;
    const res_y = RenderMap.camera.render.resolution.y;

    //generate pixels
    for(let vertical_gen_pointer = 0; vertical_gen_pointer < res_y; vertical_gen_pointer ++){
        FrameBuffer[vertical_gen_pointer] = {

        }; 
        for(let horisontal_gen_pointer = 0; horisontal_gen_pointer < res_x; horisontal_gen_pointer ++){
            //generate gradient
            
            //generate pixel stepping for colors
            const max_r = 255; //max red color
            const max_g = 255; //max green color
            const max_b = 255; //max blue color            
            const color_stepping_x = (max_r * 3) / (res_x * 3);

            const color_divide = res_y / 3;

            if(vertical_gen_pointer < color_divide){
                //red
                FrameBuffer[vertical_gen_pointer][horisontal_gen_pointer] = {
                    "r":(horisontal_gen_pointer * color_stepping_x) + RandomRangedIntiger(-5,5),
                    "g":(vertical_gen_pointer * color_stepping_x),
                    "b":runner,
                    "z":0, 
                };
            }
            else if(vertical_gen_pointer < color_divide * 2){
                //green
                FrameBuffer[vertical_gen_pointer][horisontal_gen_pointer] = {
                    "r":(horisontal_gen_pointer * color_stepping_x) + RandomRangedIntiger(-5,5),
                    "g":(vertical_gen_pointer * color_stepping_x),
                    "b":runner,
                    "z":0, 
                };
            }
            else if(vertical_gen_pointer > color_divide * 2){
                //blue
                FrameBuffer[vertical_gen_pointer][horisontal_gen_pointer] = {
                    "r":(horisontal_gen_pointer * color_stepping_x) + RandomRangedIntiger(-5,5),
                    "g":(vertical_gen_pointer * color_stepping_x),
                    "b":runner, //(horisontal_gen_pointer * color_stepping_x) + RandomRangedIntiger(-5,5),
                    "z":0, 
                };
            }
            
        
        }
    }
}