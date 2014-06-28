tw = 60; // total width
sw = 10; // screw width
lw = 15; // lever width

td = 25; // total depth
sd = 10; // screw depth
th = 10;
lh = 90;

* difference() {
	cube( [ tw, td, th ] );
	translate([-0.1,-0.1,-0.1]) cube( [ sw+0.2, sd+0.2, th+0.2 ] );
	translate([tw-sw-0.1,-0.1,-0.1]) cube( [ sw+0.2, sd+0.2, th+0.2 ] );
	translate([(tw-lw)/2,-0.1,-0.1]) cube( [ lw+0.2, sd+0.2, th+0.2 ] );

	translate( [0,sd/2,sd/2] ) 
	rotate( 90, [0,1,0] )
	cylinder( r=1.6, h=tw, $fn=32 );

	translate( [sw/2,+td+0.1,th/2] ) 
	rotate( 90, [1,0,0] )
	cylinder( r=2.1, h=td, $fn=32 );

	translate( [tw-sw/2,+td+0.1,th/2] ) 
	rotate( 90, [1,0,0] )
	cylinder( r=2.1, h=td, $fn=32 );

}

difference() {
	translate([(tw-lw)/2,0,sd/2])
	union() {
		cube( [ lw-0.2, sd, lh ] );

		translate( [ 8, 0, lh-20 ] )
		cube( [ 20, sd, 20 ] );
	
		translate( [0,sd/2,0] )
		rotate( 90, [0,1,0] )
		cylinder( r=sd/2, h=lw-0.2, $fn=32 );
	}
	
	translate( [0,sd/2,sd/2] ) 
	rotate( 90, [0,1,0] )
	cylinder( r=1.6, h=tw, $fn=32 );
}