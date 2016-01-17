difference() {
	cube( [ 60,104-7,130 ] );
	translate( [39-50,35,-2] ) cube( [ 50, 49, 150 ] );
	translate( [-1,-1,130-20+1] ) cube( [ 70, 25+1, 20 ] );
	translate( [-1,-1,-1] ) cube( [ 70, 25+1, 20 ] );

	translate( [-1,34/2,(130-87)/2+12] )
	rotate(90,[0,1,0])
	cylinder( r=1.85, h=23, $fn=16 );

	translate( [-1,34/2,(130-87)/2+12+66] )
	rotate(90,[0,1,0])
	cylinder( r=1.85, h=23, $fn=16 );
}
*translate( [-15,0,(130-87)/2] ) cube( [ 15,34,87 ] );
