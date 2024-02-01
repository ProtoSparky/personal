//this is where all data to be rendered will be stored
var RenderMap = {
    "settings":{
        "objects":{
            "object_loc":"./assets/meshes/", //this is the location where all meshes will be
        }
    },
    "camera":{
        "render":{
            "resolution":{
                "x":GetDisplayRes("x"),
                "y":GetDisplayRes("y"),
                "scale":1
            },
            "type":"canvas", //if div, render using divs as pixels | if svg, render as an svg file | Same goes for canvas
            "render_distance":30, 
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
        "test.obj":{
            "type":"external",
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
            },
            "releative_mesh_data":{

            }

        }
    }
};

//this is the frame buffer used to render stuff on screen
var FrameBuffer = {

}; 