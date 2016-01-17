union() {
	translate([0,0,0]) cylinder(r=5,h=50,$fn=60);
	
	translate([7,0,0]) cylinder(r=3,h=30,$fn=60);
	translate([7,0,30]) cylinder(r1=3,r2=0,h=7,$fn=60);
	
	translate([-7,0,0]) cylinder(r=3,h=30,$fn=60);
	translate([-7,0,30]) cylinder(r1=3,r2=0,h=7,$fn=60);
	
	translate([0,7,0]) cylinder(r=3,h=30,$fn=60);
	translate([0,7,30]) cylinder(r1=3,r2=0,h=7,$fn=60);
	
	translate([0,-7,0]) cylinder(r=3,h=30,$fn=60);
	translate([0,-7,30]) cylinder(r1=3,r2=0,h=7,$fn=60);
	
	translate([0,0,50]) cylinder(r1=5,r2=0,h=10,$fn=60);
	
}