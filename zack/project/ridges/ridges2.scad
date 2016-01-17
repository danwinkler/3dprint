union() {
	*for( i=[0:25:360*10] ){
		translate( [ 0,0,0.005*i] )
		translate( [ 10*cos(i), 10*sin(i),0] )
		rotate( i,[0,0,1] )
		rotate( 10,[1,0,0] )
		scale( [0.99e-3*i,1,1] )
		hull() {
			translate([0,0,0]) sphere(r=3);
			translate([5,0,0]) sphere(r=1);
			translate([0,5,0]) sphere(r=1);
		}
	}
	for( i=[0:100] ){
		translate([
			(0.1*i+5)*cos(i*10.),
			(0.1*i+5)*sin(i*10.0),
			0
		])
		sphere(r=1);
	}
}

