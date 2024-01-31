//this is where all data to be rendered will be stored
var RenderMap = {
    "settings":{
        
    },
    "camera":{
        "render":{
            "resolution":{
                "x":window.innerWidth,
                "y":window.innerHeight,
                "scale":1
            },
            "type":"canvas", //if div, render using divs as pixels | if svg, render as an svg file
        }
    },
    "objects":{

    }
};

//this is the frame buffer used to render
var FrameBuffer = {

}; 