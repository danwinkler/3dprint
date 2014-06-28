difference() {
	union() {
		translate([0,0,0]) cube([10,10,10]);
		translate([2.5,2.5,10]) cube([5,5,5]);
		translate([5,5,15]) sphere(r=2.5,$fn=32);
		translate([4,-1+2.5+5,10]) cube([2,2,2.5]);
		translate([4+2.5,-1+2.5+2.5,10]) cube([2,2,2.5]);
		translate([4-2.5,-1+2.5+2.5,10]) cube([2,2,2.5]);
		translate([3,-1+10,0]) cube([4,2,5]);
		translate([3+6,-1+4,0]) cube([2,4,5]);
		translate([3-4,-1+4,0]) cube([2,4,5]);
	}
	translate([3,-1,-1]) cube([4,2,5]);
	translate([4,-1+2.5,10]) cube([2,2,2.5]);
}





