tab_height = 10;
tab_width = 6;
hole_height = 3;
cyl_height = 30;

*difference() {
	cylinder( r=10, h=cyl_height );
	translate([0,0,-1]) cylinder( r=9, h=cyl_height+2 );
	translate([-15,-tab_width/2,tab_height]) cube( [30,tab_width,hole_height] );
}

module tab() {
	translate( [6,-tab_width/2,cyl_height] )
	cube( [ 2, tab_width, tab_height+hole_height ] );

	hull() {
		translate( [10,+tab_width/2,cyl_height+tab_height] )
		rotate( 90, [1,0,0] )
		cylinder( r=0.1, h=tab_width );
	
		translate( [8,+tab_width/2,cyl_height+tab_height] )
		rotate( 90, [1,0,0] )
		cylinder( r=0.1, h=tab_width );
	
		translate( [8,+tab_width/2,cyl_height+tab_height+3] )
		rotate( 90, [1,0,0] )
		cylinder( r=0.1, h=tab_width );
	}
}

//color([1,0,0,1])
translate( [0,0,-cyl_height] )
union() {
	difference() {
		cylinder( r=10, h=cyl_height );
		translate([0,0,12]) cylinder( r1=9, r2=5, h=15 );
		translate([0,0,-1]) cylinder( r=9, h=cyl_height/2 );
		translate([-15,-tab_width/2,tab_height]) cube( [30,tab_width,hole_height] );
	}
	intersection() {
		translate([0,0,cyl_height]) cylinder( r=8.5, h=8 );
		translate([-5,-10,cyl_height]) cube( [10,20,10] );
	}
	tab();
	scale([-1,1,1]) tab();
}
