union() {
	translate([0,0,-19])
	difference() {
		cylinder(r=26/2+3,h=20);
		translate([0,0,-1])
		cylinder(r=7.4,h=22);
	}
	difference() {
		cylinder(r=26/2+3,h=20);
		translate([0,0,-1])
		cylinder(r=26/2+0.5,h=22);
	}
}