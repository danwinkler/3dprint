
module core( inner, size ) {
	union() {
		// Connectors
		translate( [0, -23, 128] ) {
			rotate( 90, [1,0,0] ) {
				cylinder( size+6.0, size, size, center=true );
			}
		}
		translate( [0, 23, 128] ) {
			rotate( 90, [-1,0,0] ) {
				cylinder( size+6.0, size, size, center=true );
			}
		}
	
		translate( [0, 16.0, 50] ) {
			scale( [1,inner?0.5:0.7,1] ) cylinder( h=85, r=10, r2=5 );
		}
		translate( [0, -16.0, 50] ) {
			scale( [1,inner?0.5:0.7,1] ) cylinder( h=85, r=10, r2=5 );
		}

		if( inner ) {	
			difference() {
				cylinder( h=100, r=28, $fn=100 );
				translate( [0,0,-5] ) cylinder( h=110, r1=19, r2=19, $fn=100 );
			}
		}
		else {
			cylinder( h=100, r=28, $fn=100 );
		}
	}
}


difference() {		
	core( 1, 4.5 );
	for( i=[-90:15:90] ) {
		translate( [0,0,10] ) {
			rotate( 90, [0,0,1] ) {
				rotate( i, [0,1,0] ) {
					translate( [0,0,-128] ) {
						core( 0, 5 );
					}
				}
			}
		}
	}
}

/*

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

*/