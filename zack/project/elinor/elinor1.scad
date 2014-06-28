difference() {
	union(){
		cube([20,14,18]);
		translate([-5,-3,8]) cube([30,20,2]);
		for( i=[0:4:20] ) {
			translate([i,-2,0]) cylinder( r=1, h=8, $fn=16 );
			translate([i,16,0]) cylinder( r=1, h=8, $fn=16 );
		}
		for( i=[0:4:16] ) {
			translate([-4,i,0]) cylinder( r=1, h=8, $fn=16 );
			translate([24,i,0]) cylinder( r=1, h=8, $fn=16 );
		}
	}
	translate([10-1.5,-1,10]) cube([3,2,7]);
}