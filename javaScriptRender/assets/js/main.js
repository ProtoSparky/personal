function init(){
    console.info("init");
    FrameBufferTest();
};

function DisplayBuffer (){
    const DysplaySizeX = window.innerWidth;
    const DisplaySizeY = window.innerHeight; 
    if(RenderMap.camera.render.type == "div"){
        //display buffer using divs
                
    }   
}

function FrameBufferTest(){
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

            FrameBuffer[vertical_gen_pointer][horisontal_gen_pointer] = {
                "r":horisontal_gen_pointer * color_stepping_x,
                "g":horisontal_gen_pointer * color_stepping_x,
                "b":horisontal_gen_pointer * color_stepping_x,
                "z":0, 
            };
        
        }
    }
}