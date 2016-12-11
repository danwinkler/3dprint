
h = 5;

module ring( r ) {
	difference() {
		cylinder( h=h, r=r, center=[0,0,0], $fn=64 );
		
		translate([0,0,-0.5])
		cylinder( h=h+1, r=r-0.5, center=[0,0,0], $fn=64 );
	}
}


module pair( neck ) {
	difference() {
		union() {
			ring(5);
			translate([neck,0,0])
			ring(3);

			translate([4.3,-1,0])
			cube([neck-7,2,h]);
		}
		
		translate([0,-0.5,-1])
		cube([neck,1,10]);
	}
}

union() {
	translate([-25,-31,0])
	cube([50,50,1]);
	
	pair(15);
	translate([0,-15,0])
	rotate(180-45,[0,0,1])
	pair(25);

	translate([15,-15,0])
	ring(3);
}