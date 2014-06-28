module gable() {
	hull() {
		translate( [0,0,0] ) sphere( 1 );
		translate( [20,0,0] ) sphere( 1 );
		translate( [0,20,0] ) sphere( 1 );
		translate( [20,20,20] ) sphere( 1 );
	}
}


module punch() {
	translate( [1,1,0] ) 
	hull() {
		*translate( [3,3,-30] ) sphere( 1 );
		translate( [-25,3,-30] ) sphere( 1 );
		translate( [3,-25,-30] ) sphere( 1 );
		translate( [-25,-25,-30] ) sphere( 1 );
		translate( [23,23,20] ) sphere( 1 );
	}
}

difference() {
	gable();
	punch();
}
