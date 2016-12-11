//h = 115;

union() {
	h1 = 40;
	difference() {
		cylinder( r=101/2, h=h1 );
		translate([0,0,-1])
		cylinder( r=101/2-4, h=h1+2 );
	}

	h2 = 100;
	translate([0,0,h1])
	difference() {
		cylinder( r=108/2+4, h=h2 );
		translate([0,0,-1])
		cylinder( r=110/2, h=h2+2 );
	}

	h3 = 20;
	translate([0,0,h1-h3])
	difference() {
		cylinder( r2=108/2+4, r1=108/2-4, h=h3 );
		translate([0,0,-1])
		cylinder( r=108/2-8, h=h2+2 );
	}
}