height = 80;
sub_s = 0.4;


union(){ 
	cylinder(r=5,h=height);

	translate([0,0,height])
	cylinder(r1=5,r2=0,h=10);

	translate([6,0,0])
	scale(sub_s)
	{
		cylinder(r=5,h=height-5);

		translate([0,0,height-5])
		cylinder(r1=5,r2=0,h=10);
	}

	translate([-6,0,0])
	scale(sub_s)
	{
		cylinder(r=5,h=height-5);

		translate([0,0,height-5])
		cylinder(r1=5,r2=0,h=10);
	}

	translate([0,6,0])
	scale(sub_s)
	{
		cylinder(r=5,h=height-5);

		translate([0,0,height-5])
		cylinder(r1=5,r2=0,h=10);
	}

	translate([0,-6,0])
	scale(sub_s)
	{
		cylinder(r=5,h=height-5);

		translate([0,0,height-5])
		cylinder(r1=5,r2=0,h=10);
	}
}



translate( [ -30/2,-30/2,-3 ] )
cube( [30,30,3] );

translate( [ -10-30/2+1,-10+10/2,-3 ] )
cube( [10,10,height*sub_s] );

translate( [ -5-30/2+1,-5+5/2,-3 ] )
difference() {
	cube( [5,5,height-10] );
	translate( [ 2.2,2.5,height-18 ] )
	cylinder( r=1.8, h=10, $fn=32 );
}


translate( [ -19,-5+5/2,height-13 ] )
difference() {
	cube( [9+5,5,5] );

	translate( [ 2.2,2.5,-1 ] )
	cylinder( r=1.8, h=12, $fn=32 );
}


