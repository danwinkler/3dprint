
len = 50+30;
rad = 14.5 / 2;

difference() {
	union() {
		cylinder( r=rad, h=len, $fn=100 );
	
		for( i=[0:4:12] ) {	
			translate([0,0,i]) cylinder( r1=rad-0.5, r2=rad+0.6, h=5, $fn=100 );
		}
	
		translate([0,0,len]) 
		scale( [1,1,-1] ) {
			for( i=[0:4:12] ) {	
				translate([0,0,i]) cylinder( r1=rad-0.5, r2=rad+0.6, h=5, $fn=100 );
			}
		}
	}

	translate([0,0,-10]) cylinder( r=rad-2, h=len+20 );
}
