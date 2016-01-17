union() {
	difference() {
	
		translate( [ 0, 0, 6.5 ] )
		cube( [ 70, 13, 15+6.5 ] );
		
		translate( [ -1, 13/2, 15+13 ] )
		rotate( 90, [0,1,0] )
		cylinder( r=13/2, h=72 );

		translate( [ 15, -1, 15 ] )
		cube( [ 7, 15, 3 ] );
		
		translate( [ 70-15-7, -1, 15 ] )
		cube( [ 7, 15, 3 ] );

	}

	translate( [ 0, 13/2, 6.5 ] )
	rotate( 90, [0,1,0] )
	cylinder( r=13/2, h=70 );
}
