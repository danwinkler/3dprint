module bump() {
	hull() {
		sphere( r=0.5, $fn=4 );

		translate( [0,-9,2] )
		sphere( r=1, $fn=4 );

		translate( [-3,-10,0] )
		sphere( r=0.5, $fn=4 );

		translate( [+3,-10,0] )
		sphere( r=0.5, $fn=4 );
	}
}

union() {
	translate( [ 0, 0, +8 ] )
	difference() {
		cylinder( r=50, h=3, $fn=64 );
		translate( [ 0, 0, -1 ] )
		cylinder( r=45, h=10, $fn=64 );
	}
	
	union() {
		translate( [ 0, 0, 6 ] )
		cylinder( r=50, h=2, $fn=64 );
		intersection() {
			cylinder( r=50, h=20, $fn=64 );
			for( y=[-50:12:50] ) {
				for( x=[-50:6:50] ) {
					translate( [ 10*sin(1*y), 0, 0 ] )
					translate( [ x, y, 8 ] )
					bump();
				}
			}
		}
	}
}
