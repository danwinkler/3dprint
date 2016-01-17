difference() {
	union() {
        cube( [5,5,20] );
        translate([5,0,0]) cube( [10,5,15] );
        translate([15,0,0]) cube( [5,5,20] );
	
		translate( [2.5,2.5,20] )
		rotate( 45, [0,0,1] )
		cylinder( r1=3.5, r2=0, h=3, $fn=4 );
		
		translate( [15+2.5,2.5,20] )
		rotate( 45, [0,0,1] )
        cylinder( r1=3.5, r2=0, h=3, $fn=4 );
	}

	translate( [7.5,-1,-1] )
	cube([5,2,10]);
}



