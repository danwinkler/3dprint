module arc(outRad,inRad) {
    translate([outRad,0,0])
    difference() {
        difference() {
            cylinder(r=outRad,h=2);
            translate([0,0,-1])
            cylinder(r=inRad,h=4);
        }
        translate([-outRad-1,0,-1])
        cube([outRad*2+2,outRad*2+2,4]);
    }
}

module arrow(t1,t2,l) {
    union() {
        translate([-t1/2,0,0])
        cube([t1,l-t2,2]);

        translate([0,l-t2,0])
        rotate(-30,[0,0,1])
        cylinder(r=t2,h=2,$fn=3);
    }
}

module arrows() {
    t1 = 7;
    t2 = 15;
    l = 80;
    
    rotate(-45,[0,0,1]) {
        union() {
            rotate(0,[0,0,1])
            arrow(t1,t2,l);

            translate([0,l-2,0])
            rotate(90,[0,0,1])
            arrow(t1,t2,l);
        }
    }
}

union() {
    arrows();

    translate([230,0,0])
    mirror([1,0,0])
    arrows();

    outRad=13;
    inRad=7;
    d = outRad-inRad;

    translate([52,58,0])
    union() {
        for(i=[0:2]) {
            translate([i*4*(outRad-d/2),0,0]) {
                arc(outRad=outRad,inRad=inRad);

                mirror([0,1,0])
                translate([2*outRad-1*d,0,0])
                arc(outRad=outRad,inRad=inRad);
            }
        }
    }
}
