thick = 0.6;

union() {
	difference() {
		cube([10,10,10]);

		translate([thick,thick,thick])
		cube([10-2*thick,10-2*thick,10-2*thick]);

		translate([-1,-1,9])
		cube([12,12,12]);
	}
	
	translate([5,0,0])
	cube([thick,10,10]);
	
	translate([0,5,0])
	cube([10,thick,10]);
	

}
