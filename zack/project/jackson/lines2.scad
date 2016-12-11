t=0.6;
n=180/3;

difference(){

	union(){ 
		difference(){
			cube([180,15,8]);
			
			translate([t,t,t])
			cube([180-2*t,15-2*t, 8-2*t]);
		}
		
		for(i=[0:180/n:180-1]){
			translate([i,0,0])
			cube([t,15,8]);
		}
	}

	*translate([-t,-t,8-t-0.1])
	cube([180+2*t,15+2*t,8+2*t]);

	translate([5,5,-1])
	cube([5,5,16]);

}