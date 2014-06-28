module wedge(k,b,h) {
	p1 = [ -b/2, 0, 0 ];
	p2 = [ +b/2, 0, 0 ];
	p3 = [ 0, k, 0 ];
	p4 = [ -b/2, 0, h ];
	p5 = [ +b/2, 0, h ];
	p6 = [ 0, k, h ];
	polyhedron(
		points=[p1, p2, p3, p4, p5, p6],
		triangles=[
			[1,0,2],
			[3,4,5],
			[5,1,2],
			[4,1,5],
			[4,0,1],
			[4,3,0],
			[3,5,0],
			[5,2,0],
		]
	);
}

module gear2( r, h ) {
	circumference = 3.1416 * 2 * r;
	t = floor( circumference / 2.5 );
	k = 3;
	union() {
		cylinder( r=1.01*r, h=h, $fn=100 );
		for( a=[0:360/t:360] ) {
			rotate(a,[0,0,1])
			translate([0,r,0])
			//scale([s,1.5*s,1])
			wedge( k, circumference/t, h );
		}
	}
}


br = 3.5/2; // Bolt Radius
mmw = 55+8; // Motor Mount Width
mmd = 48; // Motor Mount Depth
mmh = 9; // Moto Mount Height
mmcr = 13; // Motor Mount Cutout Radius
roh = 30+6; // Roller area Outer Height
rih = roh-mmh-mmh; // Roller area Inner Height
riw = mmw-mmh-mmh; // Roller area Inner Width

/*
// Chassis
difference() {
	union() {
		cube( [ mmw,mmd,mmh] );
		translate( [0,0,-roh+mmh] ) cube( [ mmw,mmh,roh] );
	}

	// Roller cutout
	translate( [mmh,-1,-roh+mmh+mmh] ) cube( [ riw,mmh+2,rih ] );

	// Motor cutout
	translate( [mmw/2,mmd/2,-1] ) cylinder( r=mmcr, h=mmh+2 );

	// Motor bolt holes
	translate([mmw/2,mmd/2,0]) {
		translate( [21,0,-1] ) cylinder( r=br, h=mmh+2, $fn=32 );
		translate( [-21,0,-1] ) cylinder( r=br, h=mmh+2, $fn=32 );
	}

	// Roller holes
	translate( [mmw/2,mmh/2,-roh+mmh-1] ) cylinder( r=br, h=roh+2, $fn=32 );
	translate( [mmw/2+12,mmh/2,-roh+mmh-1] ) cylinder( r=br, h=roh+2, $fn=32 );
}
*/


/*
// Motor (for reference)
translate( [mmw/2,mmd/2,mmh] ) cylinder( r=18, h=17 );
*/

// Roller
rc = 3; // Roller Camber height
rg = 3; // Roller Gear height
rh = rih-0.5; // Roller Height
reh = rh-rc-rc-rg; // Roller Empty Height
rgr = 4.5; // Roller Gear Radius
rr = 5.5; // Roller Radius
rhr = 1.9; // Roller Hole Radius
rs = 12; // Roller Separation
rbr = rs/2; // Roller Block Radius

module roller() {
	translate( [mmw/2,mmh/2,-rh] )
	difference() {
		union() {
			translate([0,0,0]) cylinder( r2=rr, r1=rhr, h=rc, $fn=32 );
			translate([0,0,rc]) cylinder( r=rr, h=rh-rc-rg, $fn=32 );
			translate([0,0,rc+reh+rc]) gear2( rgr, rg );
			translate([0,0,rc]) cylinder( r=rbr, h=3, $fn=64 );
			translate([0,0,reh+rc]) cylinder( r=rbr, h=3, $fn=64 );
		}
		translate([0,0,-1]) cylinder( r=rhr, h=30, $fn=32 );
	}
}
roller();
//translate( [rs,0,0] ) roller();

/*
// Motor gear
translate( [mmw/2,mmd/2,-4] ) 
difference() {
	union() {
		gear2( 12.4, 4 );
		cylinder( r=4, h=5+3, $fn=30 );
	}
	translate([0,0,-1]) cylinder( r=1.8, h=20, $fn=50 );
		// r-2 was too big
		// Was r=1.8, still too small
		// Was 1.6, was too small
}

*/