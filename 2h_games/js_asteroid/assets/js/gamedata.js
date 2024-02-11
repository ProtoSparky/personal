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