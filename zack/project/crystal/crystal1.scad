function r(x) = rands(0,x,1)[0];

union() {
	for( i=[1:1:1000] ) {
		translate( [r(10),r(10),0] ) 
		rotate( r(360), [r(1),r(1),r(1)] ) 
		scale( r(1) ) 
		cube( [1,1,1] );
	}
}