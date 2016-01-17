module fin() {
	finT = 60;
	finX = 20;
	hull() {
		translate([0,0,1])
		sphere(r=1);
		
		translate([finX,0,1])
		sphere(r=1);
		
		translate([0,0,finT])
		sphere(r=1);
	}
}

h = 100;
union() {
	translate([0,0,h-0.1])
	cylinder(r=13.5/2,h=30);

	difference() {
		cylinder(r=19/2,h=h);
		
		translate([0,0,-0.1])
		cylinder(r=14.1/2,h=46);
	}

	fins = 1;
	translate([0,0,-2])
	if( fins ) {	
		difference() {
			union() {
				translate([17/2,0,0])
				fin();

				translate([-17/2,0,0])
				mirror([1,0,0])
				fin();

				rotate(90,[0,0,1])
				translate([17/2,0,0])
				fin();

				rotate(-90,[0,0,1])
				translate([17/2,0,0])
				fin();
			}
			translate([-50,-50,-98])
			cube([100,100,100]);
		}
	}
	
	dome=0;
	if( dome ) {
		difference() {
			translate([0,0,h])
			scale([1,1,5])
			sphere(r=19/2);
			
			cylinder(r=19/2,h=h);
		}
	}
}