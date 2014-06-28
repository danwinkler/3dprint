oring = 19.5;

/*
difference() {
	cylinder( r=oring/2+2, h=50, $fn=100 );
	translate( [0,0,2] ) cylinder( r=oring/2+0.3, h=240, $fn=100 );
}


translate( [30,0,0] ) {
	union() {
		difference() {
			cylinder( r=oring/2-0.5, h=4, $fn=100 );
			difference() {
				translate([0,0,1]) cylinder( r=oring/2, h=1.5, $fn=100 );
				translate([0,0,-2]) cylinder( r=oring/2-2, h=6, $fn=100 );
			}
		}
		cylinder( r=3, h=60, $fn=100 );
	}
}
*/

translate( [60,0,0] ) {
	difference() {
		cylinder( r=oring/2+4, h=10, $fn=100 );
		translate( [0,0,2] ) cylinder( r=oring/2+2.3, h=240, $fn=100 );
		translate( [0,0,-1] ) cylinder( r=3.4, h=10, $fn=100 );
	}
}