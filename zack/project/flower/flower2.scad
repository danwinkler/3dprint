include <grid.scad>;


union() {
/*
	difference() {
		translate( [0,0,1.4] ) {
			difference() {
				cube( [127,127,5] , center=true);
				translate( [0,0,1] ) cube( [120,120,5] , center=true);
			}
		}
		for( y=[-55:5:58] ) {
			for( x=[-55:5:58] ) {
				if( rands(0,1,1)[0] < 0.8 ) {
					translate( [x,y,0.9] ) sphere( rands(1,2,1)[0], $fn=10 );
				}
			}
		}
	}
*/	
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