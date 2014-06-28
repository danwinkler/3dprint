module pipe( od, id, h ) {
	difference() {
		cylinder( r=od/2, h=h, $fn=64 );
		translate( [0,0,-1] ) cylinder( r=id/2, h=h+2, $fn=64 );
	}
}

od = 20;
id = 18;
l = 50;

difference() {
	union() {	

		// Sheath
		difference() {
			pipe( od, id, l );
			translate( [od-(od-id),0,-1] ) cylinder( r=od/2, h=l+2 );
		}
		
		// Roller
		translate( [0,0,0] ) cylinder( r=(id/2)-1.5, h=l-2, $fn=64 );

		// Ends
//		translate( [-od/2-1,-od/2-1,-2] ) cube( [ od+2,od+2,3] );

		// Cups
//		pipe( od+2, od+0.3, 5 );
	}

	// Axle
	translate( [0,0,-3] ) cylinder( r=3.5/2, h=l+10, $fn=64 );
}