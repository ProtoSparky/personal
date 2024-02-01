//run to test display bufer
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

//clear frame buffer
function ClearFrameBuffer(){
    const res_x = RenderMap.camera.render.resolution.x;
    const res_y = RenderMap.camera.render.resolution.y;
    //generate pixels
    for(let vertical_gen_pointer = 0; vertical_gen_pointer < res_y; vertical_gen_pointer ++){
        FrameBuffer[vertical_gen_pointer] = {

        }; 
        for(let horisontal_gen_pointer = 0; horisontal_gen_pointer < res_x; horisontal_gen_pointer ++){
            FrameBuffer[vertical_gen_pointer][horisontal_gen_pointer] = {
                "r":0,
                "g":0,
                "b":0,
                "z":0, 
            };            
        
        }
    }
}