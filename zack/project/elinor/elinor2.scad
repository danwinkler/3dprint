union() {
	difference() {
		cylinder( r=10, h=30 );
		translate([0,0,5]) cylinder( r=9, h=30 );
	}
	difference() {
		translate([9,0,5]) cube( [8,2,18] );
		translate([9,-1,6.5]) cube( [6,4,15] );
	}
}