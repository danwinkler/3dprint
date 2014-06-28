include <grid.scad>;

grid();

/*
union() {
	translate( [0,0,0.3] ) scale( 65 ) {
		union() {
			translate( [0,0,0.05] )
				sphere( 0.05, $fn=30 );
			for( j=[0:4] ) {
				translate( [0,0,j*0.005] ) {
					rotate( j*15, [0,0,1] )
					scale( [1-j/4,1-j/4,1-j/12] )
					for( i=[0:36:360] ) {
						rotate( i, [0,0,1] ) {
							rotate( 10, [1,0,0] ) {
								rotate( j*2, [0,1,0] )
								translate( [-0.9,0,0] ) {
									grid();
								}
							}
						}
					}
				}
			}
		}
	}

}
*/