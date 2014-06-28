difference() {
	cube( [20,150,15] );
	for( z=[4:6:15] ) {
		for( x=[4:6:20] ) {
			translate( [x, 160, z] ) rotate(90,[1,0,0]) cylinder( r=2, h=170, $fn=16 );
		}
	}
}
