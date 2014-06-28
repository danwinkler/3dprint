union() {
	translate([-0.5,-4,0])	
	cube([1,8,15]);

	translate([4,-0.5,0])	
	rotate(90,[0,0,1])
	cube([1,8,15]);

	translate([0,0,-3])	 cylinder( r=1.6, h=30, $fn=30 );
}