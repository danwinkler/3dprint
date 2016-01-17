rotate( 90, [1,0,0] )
cylinder( r=5, h=100 );

translate( [0, -100,0] )
rotate( 90, [1,0,0] )
cylinder( r1=5, r2=0, h=15 );

module wing() {
	hull() {
		translate( [ 70, 0, 0 ] )
		sphere( r=2 );
	
		translate( [ 0, -30, 0 ] )
		sphere( r=2 );
	
		translate( [ 0, 0, 0 ] )
		sphere( r=2 );
	}	
}

translate( [0,-30,-3] ) {
	wing();
	mirror( [-1,0,0] ) wing();
}

hull() {
	translate( [ 0, -20, 0 ] )
	sphere( r=2 );

	translate( [ 0, 0, 20 ] )
	sphere( r=2 );

	translate( [ 0, 0, 0 ] )
	sphere( r=2 );
}	


translate( [0,0,10] )
hull() {
	translate( [ 0, -10, 0 ] )
	sphere( r=2 );

	translate( [ 20, 0, 0 ] )
	sphere( r=2 );

	translate( [ -20, 0, 0 ] )
	sphere( r=2 );
}	

translate( [7,-5,0] )
rotate( 90, [1,0,0] )
cylinder( r=3, h=20, $fn=16 );

translate( [-7,-5,0] )
rotate( 90, [1,0,0] )
cylinder( r=3, h=20, $fn=16 );

