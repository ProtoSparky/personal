//this is where all data to be rendered will be stored
var RenderMap = {
    "settings":{
        "objects":{
            "object_loc":"./assets/meshes/", //this is the location where all meshes will be
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
        "test.obj":{
            "type":"external",
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
                
            }

        }
    }
};


var GameState = {
    "player":{
        "position":{
            "heading":0,
            "velocity":{
                "current_velocity":0,
                "min_velocity":0,
                "max_velocity":400,
            }
        }
    },
    "gamearea":{
        "style":{
            "background_color":"black", //canvas background color
            "id":"canvas" //canvas id name
        }
    },
    "framebuffer":{
        "0":{
            "ObjectProperties":{
                "id":{
                    "id":"camera",
                    "render_id":"camera",
                }
            },
            "position":{
                "position":[{x:30,y:30}],
                "scale":{},

            }
        },
        "1":{
            "ObjectProperties":{
                "id":{
                    "id":"player",
                    "render_id":"object",
                }
            },
            "position":{
                "position":[
                    { x:  20, y:    30},
                    { x:  10, y:    0},
                    { x:  30, y:    0},
                    { x:  20, y:    30},
                ],
                "scale":{},
                "rotation":180,
            },
            "style":{
                "LineStyle":{
                    "width":2, 
                    "background_color":"white",
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
