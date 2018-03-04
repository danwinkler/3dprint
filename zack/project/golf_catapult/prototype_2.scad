// <  H  >     <  H  >
// +-----+< P >+-----+
// |     |     |     |
// +--------------+  |
// |              |  |
// |              |  |
// +--------------+  |
// |     |     |     |
// <       F      >
//                 <Q>
// Know H, P, I want to find F and Q
// H+H+P = F+Q
// Q = H/2
// 2*H+P = F+H/2
// 2*H-0.5*H = F-P
// 1.5H+P = F

penny_rad_cm = 0.9525;
penny_height_cm = 0.152;
penny_diam_cm = penny_rad_cm*2 * 1.1;
penny_thick_cm = penny_height_cm * 1.1;
w = 10;
l = penny_diam_cm * 2.5 / 2.0;
h = 1;
foot_w = 0.5;
foot_l = 0.5;
foot_h = 1.5*h + penny_thick_cm;
indent = 0;
q = 2;
enlarge = 2.0;

base_thick = 0.5;
space = penny_height_cm * 2.3;
sabot_h = space * 0.95;
half_width = penny_rad_cm*2;
edge_width = 0.25;
length = 18;

module edge(s) {
    color("Red")
    translate([0,half_width-edge_width-0.2,base_thick/2])
    scale([1,s,1])
    cube([length,edge_width,space+base_thick]);
}

module detent_part() {
    difference() {
        cube([length,half_width,base_thick]);
        edge(1.1);

        color("Pink")
        translate([length-0.5,0,-1])
        cylinder(r=0.15,h=9, $fn=9);

    }
}

module tab_part() {
    difference() {
        union() {
            cube([length,half_width,base_thick]);
            edge(1);
        }
        color("Blue")
        translate([0.5,0,base_thick])
        cube([1,half_width,space*4]);

        color("Pink")
        translate([length-0.5,0,-1])
        cylinder(r=0.15,h=9, $fn=9);

    }
}

scale(10) {
    detent_part();
    mirror([0,1,0])
    detent_part();

    translate([0,4,0]) {
        tab_part();
        mirror([0,1,0])
        tab_part();
    }

    // Sabot
    translate([2,8,0])
    difference() {
        cylinder(r=penny_rad_cm*1.2, h=sabot_h, $fn=32);

        color("Lime")
        translate([penny_rad_cm/2,0,sabot_h-penny_height_cm])
        cylinder(r=penny_rad_cm*1.03, h=penny_height_cm, $fn=32);
        
        color("Red")
        translate([-0.8,0,-1])
        cylinder(r=0.15,h=9, $fn=9);
    }
}

