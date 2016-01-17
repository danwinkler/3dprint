difference() {
	
	cube( [ 35,40,70 ] );
	
	translate( [-0.1,35/2,(70-31)/2] ) {
		rotate( 90, [0,1,0] )
		cylinder( r=1.85, h=23, $fn=16 );
		
		translate( [ 0, 0, 31 ] )
		rotate( 90, [0,1,0] )
		cylinder( r=1.85, h=23, $fn=16 );
	}

	translate( [20,-0.1+20,(70-55)/2] ) {
		translate( [0,23,0] )
		rotate( 90, [1,0,0] )
		cylinder( r=1.85, h=45, $fn=16 );

		translate( [0,23,55] )
		rotate( 90, [1,0,0] )
		cylinder( r=1.85, h=45, $fn=16 );
	}

	translate( [-1,-1,-1] )
	cube( [40,20,14] );

	translate( [-1,-1,-1+60] )
	cube( [40,20,14] );

	translate( [-1+20,-1,0] )
	cube( [20,10,100] );

}