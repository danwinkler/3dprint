difference() {
	cube( [ 40, 100, 66+20 ] );
	translate( [ 10, -1, 10 ] ) cube( [ 40, 102, 66 ] );	

	translate( [ -1, 100/2, (66+20)/2 ] )
	rotate( 90, [ 0, 1, 0 ] )
	cylinder( r=2.9, h=24, $fn=16 );	

	translate( [ 10-5+0.1, 100/2, (66+20)/2 ] )
	rotate( 90, [ 0, 1, 0 ] )
	cylinder( r=5.5, h=5, $fn=16 );	
}

*difference() {
	cube( [ 50, 50, 80 ] );
	translate( [ -1, -1, 10 ] ) cube( [ 50-6+1, 50+2, 80 ] );

	translate( [ 50-11, 50/2, (66+60)/2 ] )
	rotate( 90, [ 0, 1, 0 ] )
	cylinder( r=2.9, h=24, $fn=16 );	

	translate( [ 10, 10, -1 ] )
	cylinder( r=2.3, h=24, $fn=16 );	

	translate( [ 50-20, 10, -1 ] )
	cylinder( r=2.3, h=24, $fn=16 );	

	translate( [ 10, 50-10, -1 ] )
	cylinder( r=2.3, h=24, $fn=16 );	

	translate( [ 50-20, 50-10, -1 ] )
	cylinder( r=2.3, h=24, $fn=16 );	
}

