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
        }, 
        "position":{
            "location":{
                "x":0,
                "y":0,
                "z":0,
            },
            "rotation":{
                "x":0,
                "y":0,
                "z":0
            },
            "scale":{
                "x":1,
                "y":1,
                "z":1, 
            }
        }
    },
    "objects":{
        
    }
};

//this is the frame buffer used to render stuff on screen
var FrameBuffer = {

}; 