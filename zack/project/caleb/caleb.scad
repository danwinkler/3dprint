difference(){
	sphere(r = 10);
	translate([0,0,-10]){
		cylinder(r = 5, h = 20);
	}
	sphere(r = 9);

	
	translate([-10,0,0])
	rotate(90,[0,1,0])
	cylinder(r = 5, h = 20);

	translate([0,10,0])
	rotate(90,[1,0,0])
	cylinder(r = 5, h = 20);
	
}