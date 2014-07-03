difference() {
	union() {
		rotate( 45, [0,0,1] )
		difference() {
			cube( [ 200, 200, 20 ] );
			translate([10,10,10]) cube( [ 180, 180, 20 ] );
		}
		
//		translate([-70,100,5])
//		linear_extrude( height=10 ) import( "midlife.dxf" );

		translate([-105,90,5])
		linear_extrude( height=10 ) import( "wildlife.dxf" );
	}
	
	translate([0,250,-5])
	cylinder( r=5, h=20 );
}