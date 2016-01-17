e = 0.037;

module tube() {
	difference() {
		cylinder( r=1, h=1, $fn=16 );
		translate([0,0,-0.02]) cylinder( r=0.9, h=2, $fn=16 );	
	}
}

difference() {
	union() {
		for( r=[1:1:200] ) {
			rotate( 20*r, [0,1,0] )
			translate([0,exp(1.10*e*r),exp(e*r)])
			rotate( 90, [0,1,0] )
			scale( [0.8*exp(e*r), 1.6*exp(e*r), 0.6*exp(e*r)] )
			tube();
		}
	}
	rotate( 90, [1,0,0] )
	translate([-5000,-5000,-12500])
	cube( [10000,10000,10000] );
}