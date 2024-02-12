//perses obj files
function parseObj(content) {
    var lines = content.split('\n');
    var vertices = [];
    var texcoords = [];
    var normals = [];

    for (var i = 0; i < lines.length; i++) {
        var line = lines[i];
        var parts = line.trim().split(' ');
        
        switch (parts[0]) {
            case 'v':
                vertices.push({ x: parseFloat(parts[1]), y: parseFloat(parts[2]), z: parseFloat(parts[3]) });
                break;
            case 'vt':
                texcoords.push({ u: parseFloat(parts[1]), v: parseFloat(parts[2]) });
                break;
            case 'vn':
                normals.push({ x: parseFloat(parts[1]), y: parseFloat(parts[2]), z: parseFloat(parts[3]) });
                break;
        }
    }
    
    return { vertices: vertices, texcoords: texcoords, normals: normals };
}