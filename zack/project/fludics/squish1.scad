module wedge(a,h) {
	p1 = [ 0, cos(a), 0 ];
	p2 = [ sin(a), 0, 0 ];
	p3 = [ -sin(a), 0, 0 ];
	p4 = [ 0, cos(a), h ];
	p5 = [ sin(a), 0, h ];
	p6 = [ -sin(a), 0, h ];
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

r1 = 6;
h = 15;
r2 = 5*r1/10;
r3 = r2+0.4;
r4 = r1-0.4;
s = 3.2;

module squeezy() {
	difference() {
		cylinder( r=r1, h=h, $fn=50 );
		translate([0,0,-1]) cylinder( r=r2, h=h+2, $fn=50 );
	
		for( a=[0:45:360] ) {
			rotate(a,[0,0,1])
			translate([0,r3,-1])
			scale([s,1.5*s,1])
			wedge( 13,h+4 );
		}
	
		for( a=[0:45:360] ) {
			rotate(a+45/2,[0,0,1])
			translate([0,r4,-1])
			rotate(180,[0,0,1])
			scale([s,s,1])
			wedge( 30,h+4 );
		}
	}
}

squeezy();
