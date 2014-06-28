translate( [-20,-5,12] ) {
	cube( [40,10,2] );
}


union() {
	// Connectors
	translate( [0, -25, 130] ) {
		rotate( 90, [1,0,0] ) {
			cylinder( 4.5, 4.55, 4.5, center=true );
		}
	}
	translate( [0, 25, 130] ) {
		rotate( 90, [-1,0,0] ) {
			cylinder( 4.5, 4.5, 4.5, center=true );
		}
	}
	translate( [0, 18.0, 105] ) {
		cube( [10,10,65], center=true );
	}
	translate( [0, -18.0, 105] ) {
		cube( [10,10,65], center=true );
	}

	difference() {
		difference() {
			difference() {
				difference() {
					cylinder(h=100,r1=33,r2=28, $fn=100);
					translate([0,0,-1]) cylinder(h=110,r=23,$fn=100);
				}
		
				// Indents
				rotate( 90, [0,0,1] ) {
					translate( [0, -25, 20] ) {
						rotate( 90, [1,0,0] ) {
							cylinder( 5, 5, 5, center=true );
						}
					}
					translate( [0, 25, 20] ) {
						rotate( 90, [-1,0,0] ) {
							cylinder( 5, 5, 5, center=true );
						}
					}
				}
			}
			translate( [0,24,5] ) {
				scale( [1,1,1.7] )
				sphere( 30 );
			}
			translate( [0,-24,5] ) {
				scale( [1,1,1.7] )
				sphere( 30 );
			}
		}
		translate( [0,0,-38] ) {
			cube( [100,100,100],center=true );
		}
	}
}