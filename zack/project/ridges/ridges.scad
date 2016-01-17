difference() {
	union() {
		for( i=[0:25:360*10] ){
			translate( [ 0,0,0.005*i] )
			translate( [ 10*cos(i), 10*sin(i),0] )
			rotate( i,[0,0,1] )
			rotate( 10,[1,0,0] )
			scale( [0.99e-3*i,1,1] )
			hull() {
				translate([0,0,0]) sphere(r=1);
				translate([5,0,0]) sphere(r=1);
				translate([0,5,0]) sphere(r=1);
			}
		}

		*translate( [0,0,3] )
		for( j=[0:30:180] ){
			rotate( j, [0,1,0] )
			translate( [4,0,0] )
			for( i=[0:45:360] ){
				rotate( i, [0,0,1] )
				translate( [4,0,0] )
				sphere(r=2,$fn=12);
			}
		}
	}
	
	for( i=[0:45:360] ){
		rotate( i, [0,0,1] )
		translate( [0,0,20] )
		rotate( 130, [1,0,0] )
		cylinder(r=3,h=30);
	}
}