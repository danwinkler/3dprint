r = 10;
hh = 50;

intersection() {
	union() {
		for( r=[1:1:100] ) {
			rotate( 10*r, [0,1,0] )
			translate([0,3*exp(0.04*r),r])
			rotate( 90, [0,1,0] )
			difference() {
				cylinder( r=2*r, h=hh, $fn=16 );
				translate([0,0,-0.02]) cylinder( r=2*r*0.9, h=hh+1, $fn=16 );	
			}
		}
	}
	*translate([-500,100,-500]) cube( [1000,100,1000] );
}