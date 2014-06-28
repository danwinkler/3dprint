difference() {
	cube( [30,10,5] );
	translate([10,5,-2]) cylinder( r=1.5, h=20, $fn=50 );
	translate([15,5,-2]) cylinder( r=1.6, h=20, $fn=50 );
		// 1.6 Is the right radius for an attachment to the stepper motor
	translate([20,5,-2]) cylinder( r=1.7, h=20, $fn=50 );
}
