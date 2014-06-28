num_louvres = 6;
spacing = 35;

union() {
	translate( [-50,-30,-45] ) {
		cube( [200, 100, 20] );
	}

	translate( [-12,-30,280] ) {
		difference() {
			cube( [124, 100, 10] );
			translate( [62,40,-1] ) {
				cylinder( 30, 8, 8 );
			}
		}
	}
	
	translate( [-12,-30,-30] ) {
		scale( [1,1,1] ) {
			color( [ 1, 0, 0, 0.5 ] ) {
				difference() {
					cube( [10,100,num_louvres*spacing+100] );
					translate( [0,0,96] ) {
						for( i=[0:num_louvres-1] ) {
							translate( [1,81.2,i*spacing+8.3] ) {
								rotate(90,[0,1,0]) {
									cylinder(10,0,6);
								}
							}
						}
					}
				}
			}
		}
	}
	
	translate( [-12+124,-30,-30] ) {
		scale( [-1,1,1] ) {
			color( [ 1, 0, 0, 0.5 ] ) {
				difference() {
					cube( [10,100,num_louvres*spacing+100] );
					translate( [0,0,96] ) {
						for( i=[0:num_louvres-1] ) {
							translate( [1,81.2,i*spacing+8.3] ) {
								rotate(90,[0,1,0]) {
									cylinder(10,0,6);
								}
							}
						}
					}
				}
			}
		}
	}
}

for( i=[0:num_louvres-1] ) {
	translate( [0,0,i*spacing] ) {
		rotate( 50, [1,0,0] ) {
			union() {
				translate( [-10,90,8.5] ) {
					rotate(90,[0,1,0]) {
						cylinder(10,0,5);
					}
				}
				translate( [100,90,8.5] ) {
					rotate(90,[0,1,0]) {
						cylinder(10,5,0);
					}
				}

				difference() {
					cube([100,100,17]);
					translate( [50,34,-5] ) {
						scale( [1,2.5,1] ) {
							cylinder( 30,13,13 );
						}
					}
				}

			}
		}
	}
}
translate( [50,9,-20] ) {
	union() {
		for( i=[0:num_louvres-1] ) {
			translate( [-5,-10,i*spacing+9] ) {
				cube( 10 );
			}
		}
		translate( [-5,-10,311] ) {
			cube( 10 );
		}
		cylinder(340,5,5);
	}
}
