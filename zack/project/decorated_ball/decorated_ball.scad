difference() {
	union() {
		sphere (r=10);
		for( t=[0:45:360] ) {
			translate([10*cos(t),10*sin(t),0])
			sphere(r=3);
		}
	}
	translate([0,0,-15])
	cylinder(r=3,h=25,$fn=16);
}