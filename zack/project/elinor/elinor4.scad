
union() {

	difference() {
		rotate(-90,[1,0,0]) cylinder(r=5,h=20,$fn=32);
	
		// Door
		translate([0,-1,4]) cube([2,5,2]);
	
		// Bottom windows
		translate([-3,2,4]) cube([2,2,2]);
		translate([+3,2,3]) cube([2,2,2]);
	
		// Middle wide window
		translate([-3,8,3]) cube([6,2,2]);
	
		// Top windows
		translate([-3,12,4]) cube([2,2,2]);
		translate([+2,12,3]) cube([2,2,2]);
	
		// Back Bottom windows
		translate([-3,7,-5]) cube([2,2,2]);
		translate([+2,7,-5]) cube([2,2,2]);
	
		// Back Top windows
		translate([-3,12,-5]) cube([2,2,2]);
		translate([+2,12,-5]) cube([2,2,2]);
	
		// Back wide window
		translate([-3,2,-5]) cube([6,2,2]);
	}

	// Columns
	for( r=[0:8] ) {
		assign( t=r/8*3.14*2 ) {
			translate( [0,25,0] )
			rotate( r/8*360, [0,1,0] )
			translate( [4*cos(t),0,4*sin(t)] )
			rotate( 90, [1,0,0] )
			cylinder( r=1, h=5, $fn=16 );
		}
	}

	// Dome
	difference() {
		translate( [0,25,0] )
		rotate( 90, [1,0,0] )
		difference() {
			sphere( r=5 );
			cylinder( r=10, h=10 );
		}

		translate( [0,25,0] )
		sphere( r=4 );
	}

	// Peak
	translate( [0,35,0] )
	rotate( 90, [1,0,0] )
	cylinder( r1=0, r2=1, h=5 );

	translate( [-1,0,0] )
	difference() {
		// Right building	
		hull() {
			translate([5,0,-5]) cube([12,10,10]);
	
			// Peak
			translate( [11,15,-5] )
			cylinder( r=0.5, h=10 );
		}
	
		// Right bottom windows
		translate([+06,2,4]) cube([2,2,2]);
		translate([+10,2,4]) cube([2,2,2]);
		translate([+14,2,4]) cube([2,2,2]);

		// Right top windows
		translate([+06,7,4]) cube([2,2,2]);
		translate([+10,7,4]) cube([6,2,2]);


	}
}
