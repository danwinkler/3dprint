difference(){
	union(){
		for(i = [0:30:1000]){
			translate([(1000-i)/150*cos(i),(1000-i)/150*sin(i),i/100])
			sphere(r = 3, $fn=20);
		}
	}
	translate([-12.5,-12.5,-9])
	cube([25,25,10]);
}