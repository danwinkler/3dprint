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



module foot(s) {
    scale([s,s,1])
    translate([-foot_w/2, -foot_l/2, 0])
    cube([foot_w,foot_l,foot_h]);
}

module quarter() {
    union() {
        cube([w,l,h]);
        translate([w-foot_w,l-foot_l,0]) foot(1.0);
    }
}

module pair() {
    quarter();
    mirror([0,1,0]) quarter();
}

module quarter_hole() {
    difference() {
        cube([w,l,h]);
        translate([w-foot_w,l-foot_l,0.5*h]) foot(1.15);
    }
}

module pair_hole() {
    quarter_hole();
    mirror([0,1,0]) quarter_hole();
}


// Sabot
translate([0,12,0])
difference() {
    cylinder(r=penny_rad_cm*1.2, h=penny_height_cm*2, $fn=32);

    color("Lime")
    translate([penny_rad_cm/2,0,penny_height_cm*1.01])
    cylinder(r=penny_rad_cm*1.03, h=penny_height_cm, $fn=32);
    
    color("Red")
    translate([-0.8,0,-1])
    cylinder(r=0.15,h=9, $fn=9);
}


pair();
mirror([1,0,0]) pair();

translate([0,l+4,0]) {
    pair_hole();
    mirror([1,0,0]) pair_hole();
}
