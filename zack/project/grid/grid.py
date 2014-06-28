function quadPatchPoints() {
    var points = [];
    for( var y=0; y<11; y+=1 ) {
        for( var x=0; x<11; x+=1 ) {
            points.push( [x,y,0] );
        }
    }
    return points;
}

function quadPatchTriangles() {
    var triangles = [];
    for( var y=0; y<10; y++ ) {
        for( var x=0; x<10; x++ ) {
            triangles.push( [
                (y+0)*11+(x+0),
                (y+1)*11+(x+0),
                (y+0)*11+(x+1)
            ] );
            
            triangles.push( [
                (y+1)*11+(x+0),
                (y+1)*11+(x+1),
                (y+0)*11+(x+1)
            ] );
            
        }
    }
    return triangles;
}

function main() {
    return polyhedron({
        points: quadPatchPoints(),
        triangles: quadPatchTriangles()
    });
}