translate([0,0,-1]) cylinder(r=5,h=50,$fn=60);

translate([0,0,49]) cylinder(r1=5,r2=0,h=7,$fn=60);

hull() {
	translate([0,0,0]) sphere(r=1);
	translate([0,-10,0]) sphere(r=1);
	translate([0,0,10]) sphere(r=1);
}

hull() {
	translate([0,0,0]) sphere(r=1);
	translate([0,10,0]) sphere(r=1);
	translate([0,0,10]) sphere(r=1);
}

hull() {
	translate([0,0,0]) sphere(r=1);
	translate([10,0,0]) sphere(r=1);
	translate([0,0,10]) sphere(r=1);
}

hull() {
	translate([0,0,0]) sphere(r=1);
	translate([-10,0,0]) sphere(r=1);
	translate([0,0,10]) sphere(r=1);
}