a = rands(1,5,1000);
union() {

//	translate([-5,0,0])
//	cube([20,0.1,0.1]);

	union() {
		translate([0.5,0.5,0]) cylinder( r=sqrt(32),h=0.2);
		for( y=[-10:1:10] ) {
			for( x=[-10:1:10] ) {
				if( x*x + y*y < 30 ) {
					translate([x,y,0])
					cube( [0.9,0.9,a[ floor((y+10)*10 + x)  ] ] );
				}
			}
		}
	}
	
	union() {
		rotate( 180, [1,0,0] )
		translate( [ 12,0,-8] )
		for( y=[-10:1:10] ) {
			for( x=[-10:1:10] ) {
				if( x*x + y*y < 30 ) {
					translate([x,y,a[ floor((y+10)*10 + x) ]])
					cube( [1.01,1.01,8-a[ floor((y+10)*10 + x) ] ] );
				}
			}
		}
	}
}