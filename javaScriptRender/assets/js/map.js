//this is where all data to be rendered will be stored
var RenderMap = {
    "settings":{
        "objects":{
            "object_loc":"./assets/meshes/", //this is the location where all meshes will be
        },
        "render_settings":{
            "dimention":"2d",
        },
        "canvas":{
            "id":"canvas",
            "background_color":"black",
        }

    },
    "camera":{
        "transform":{
            "loc":{
                //location
                "x":0,
                "y":0,
                "z":0,
            },
            "rot":{
                //rotation
                "x":0,
                "y":0,
                "z":0
            },
            "sc":{
                //scale
                "x":1,
                "y":1,
                "z":1, 
            }
        }
    },
    "objects":{
        "player":{ //key should be file name but since this is an internal object, itll be fine
            "type":"internal",
            "transform":{
                "loc":{
                    //location
                    "x":0,
                    "y":0,
                    "z":0,
                },
                "rot":{
                    //rotation
                    "x":0,
                    "y":0,
                    "z":0
                },
                "sc":{
                    //scale
                    "x":1,
                    "y":1,
                    "z":1, 
                }
            },
            "object_data":{
                //releative vertex data
                "vtex":[
                    { x:  20, y:    30},
                    { x:  10, y:    0},
                    { x:  30, y:    0},
                    { x:  20, y:    30},
                ],
                "vtex_transformed":[
                    //this is where processed vertex data is stored
                ],
                "style":{
                    "LineStyle":{
                        "width":2, 
                        "background_color":"white",
                    }
                }

            }

        }
    }
};



//this is the frame buffer used to render stuff on screen
var FrameBuffer = {

}; 

//temporary storage for render processes
var RendTempBuffer = {

};
