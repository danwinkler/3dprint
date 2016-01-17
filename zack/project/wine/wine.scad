union() {
	for( t=[0:72] ) {
		translate( [10*cos(t*10),10*sin(t*10),t*0.45+3] )
		sphere( r=3, $fn=16 );
	
		translate( [10*cos(-t*10),10*sin(-t*10),t*0.45+3] )
		sphere( r=3, $fn=16 );
	}
	
	translate([0,0,35])
	sphere( r=10, $fn=32 );
	
	difference() {
		cylinder( r=10, h=35, $fn=64 );
	
		translate([0,0,-1])
		cylinder( r=4.0, h=16+1, $fn=64 );
	
		translate([0,0,-1])
		cylinder( r=4.2, h=8+1, $fn=64 );
	}
}