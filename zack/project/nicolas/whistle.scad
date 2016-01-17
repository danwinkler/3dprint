

difference() {
	
	union() {
		difference() {
			difference() {
				union() {
					difference() {
						cylinder(r=10,h=15);
						translate([0,0,1])
						cylinder(r=8,h=15-2);
					}
					cube([10,20,15]);
				}
			
				translate([2,-3,2])
				cube([10-7,35,15-4]);
			}

			translate([0,-5,2])
			cube( [ 10,3,10 ] );
		}	
		
		translate([-4,0,11.2])
		sphere(r=3);
	}	
	*translate([-20,-20,-20])
	cube([30,60,30]);
}