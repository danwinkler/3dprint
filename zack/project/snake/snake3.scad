module core() {
	translate( [0,-35,0] )
	rotate( 90, [1,0,0] )
	cylinder( r=13, h=30 );

	union() {
		for( i=[-1:2:1] ) {
			scale( [1,1,i] )
			translate( [0,5,8.9] ) {
				difference() {
					cylinder( r=10, h=4 );
					translate([0,0,-1]) cylinder( r=8.3, h=6 );
				}
			
				difference() {
					translate([-10,-50,0]) {
						cube( [20,50,4] );
					}
					translate([0,0,-1]) cylinder( r=10, h=6 );
				}
			}
		}
	}
}

module rem() {
	union() {
		for( i=[-1:2:1] ) {
			scale( [1,1,i] )
			translate( [0,0,10] ) {
				difference() {
					translate([-10,-20,-2])
						cube( [20,33,10] );
					translate([0,0,-3]) cylinder( r=8, h=6 );
				}
			
			}
		}
	}
}

difference() {
	core( 0 );
	translate( [0,-55,0] ) rotate( 90, [0,1,0]) rem();
}