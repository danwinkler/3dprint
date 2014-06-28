module gable() {
	hull() {
		translate( [0,0,0] ) sphere( 1 );
		translate( [20,0,0] ) sphere( 1 );
		translate( [0,20,0] ) sphere( 1 );
		translate( [20,20,20] ) sphere( 1 );
	}
}

module brow() {
	difference() {
		gable();
		translate( [5,5,-1] ) gable();
	}
}

module furr() {
	difference() {
		union() {
			//cylinder( r=25, h=10 );
			for( i=[0:45:360] ) {
				rotate( i, [0,0,1] )
				translate( [7,7,0] )
				gable();
			}
		}
		translate([0,0,-1])
		cylinder( r=20, h=12 );
	}
}


for( i=[0:10:100] ) {
	difference() {
		union() {
			scale( exp(-0.005*i) )
			rotate( i*2.7, [0,0,1] )
			translate( [0,0,i] )
			furr();
		}
		scale( exp(-0.005*i) )
		rotate( i*2.7, [0,0,1] )
		translate( [0,0,i] )
		for( j=[0:45:360] ) {
			rotate( j, [0,0,1] )
			scale( 1.1 )
			translate( [8,8,0] )
			gable();
		}
	}
}