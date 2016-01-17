
difference() {

	union() {

		translate([0,0,5])
		difference() {
			cube( [20,20,20] );

			translate([4,-1,16])
			cube( [2,5,5] );
			translate([8,-1,16])
			cube( [2,5,5] );
		}

		translate([20-6,-2,+3])
		cube( [6,10,15] );

		translate([10,-8,0])
		difference() {
			cube( [15,28,12] );

			translate([2,-1,9])
			cube( [4,6,4] );

			translate([12,-1,2])
			cube( [4,6,2] );
		}

		for( i=[1:4] ) {
			translate([10,-8+i,-i])
			cube( [15,28-2*i,1] );
		}

		translate([0,-15,-20])
		cube( [5,35,30] );

		for( i=[1:4] ) {
			translate([0,-8-i*1,-20])
			cube( [15,25,20-i*1] );
		}

		translate([0,-15,-20])
		cube( [30,35,12] );

		for( i=[0:5] ) {
			translate([22,-3+3*i,-10])
			cube( [1,1,10] );
		}

	}

	translate([-1,-20,-21])
	cube( [40,50,12] );
	
}