difference() {
	union() {
		union() {
			cylinder( r=25/2, h=30 );
			translate( [0,-25/2,0] ) cube( [32,25,30] );
		}
		
		translate( [-22,-25/2-(60-25)/2,-39.9] ) 
		difference() {
			cube( [ 65, 60, 40 ] );
			translate( [10,10,-20] ) cube( [ 45, 40, 50 ] );
		}
	}
	translate( [10,-60,-20] ) 
	rotate( 90, [0,0,1] )
	rotate( 90, [0,1,0] )
	cylinder( r=1.9, h=100, $fn=20 );

	translate( [10,-60,15] ) 
	rotate( 90, [0,0,1] )
	rotate( 90, [0,1,0] )
	cylinder( r=1.9, h=100, $fn=20 );

}