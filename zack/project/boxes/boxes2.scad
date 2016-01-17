difference() {
	union() {

		difference() {
			cube([20,18,10]);

			translate([10,-1,7])
			cube([2,4,4]);
			translate([14,-1,7])
			cube([2,4,4]);

			translate([21,0,8])
			rotate(-45,[0,0,1])
			rotate(-45,[0,1,0])
			rotate(45,[1,0,0])
			cube([2,4,4]);

		}


		translate([5,5,9])
		difference() {
			cube([10,10,14]);

			translate([14,0,10])
			rotate(-45,[0,0,1])
			rotate(-45,[0,1,0])
			rotate(45,[1,0,0])
			cube([8,8,8]);

			translate([8,-1,3])
			cube([3,25,5]);

			translate([-1,-1,-1])
			cube([4,6,16]);
		}

		translate([0,-3,0])
		difference() {
			cube([7,12,28]);

			translate([5,-1,-1])
			cube([3,14,20]);

			translate([3,-1,25])
			cube([1,4,4]);
		}
	}
	
	translate([-1,-5,-1])
	cube([2.5,20,8]);
}