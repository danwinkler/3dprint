
r = rands( -10, 10, 300 );

for( i=[0:100] ) {
	x = r[i*3+0];
	y = r[i*3+1];
	z = r[i*3+2];
	translate( [ x, y, z ] )
	sphere(r=3, $fn=16 );
}


difference() {
	cylinder( r=10, h=20, $fn=64 );
	translate([0,0,-1]) cylinder( r=3.9, h=15+1, $fn=64 );
	translate([0,0,-1]) cylinder( r=4.1, h=8+1, $fn=64 );
}