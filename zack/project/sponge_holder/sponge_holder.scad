difference() {
	union() {
		// base
		translate([6,-1,0])
		cube([2,80,110]);

		// bottom curve
		difference() {
			difference() {
				cylinder(r=8,h=110);
				translate([0,0,-1])
				cylinder(r=6,h=112);
			}
			translate([-10,0,-1])
			cube([20,20,114]);
		}
		
		// first support
		rotate(15,[0,0,1])
		translate([-8,-1,0])
		cube([2,80,110]);

		// middle curve
		translate([-39,71,0])
		difference() {
			difference() {
				cylinder(r=14,h=110);
				translate([0,0,-1])
				cylinder(r=12,h=112);
			}
			translate([-20,-20,-1])
			cube([40,20,114]);
		}

		// second support
		translate([-52.5,5,0])
		cube([2,70,110]);

		// bottom curve
		translate([-58,5,0])
		difference() {
			difference() {
				cylinder(r=8,h=110);
				translate([0,0,-1])
				cylinder(r=6,h=112);
			}
			translate([-10,0,-1])
			cube([20,20,114]);
		}

		// top support
		rotate(10,[0,0,1])
		translate([-64.5,14,0])
		cube([2,70,110]);
	}
	// minus
	translate([0,-8,50])
	cylinder(r=1,h=10);

	// plus
	translate([-57,-3,50])
	cylinder(r=1,h=10);

	translate([-62,-2.5,55])
	rotate(90,[0,1,0])
	cylinder(r=1,h=10);
}