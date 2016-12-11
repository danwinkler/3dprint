t=0.6;
n=5;

difference(){

	union(){ 
		difference(){
			cube([180,15,8]);
			
			translate([t,t,t])
			cube([180-2*t,15-2*t, 8-2*t]);
		}
		
		for(i=[0:15/n:15-1]){
			translate([0,i,0])
			cube([180,t,8]);
		}
	}

	translate([-t,-t,8-t-0.1])
	cube([180+2*t,15+2*t,8+2*t]);

	translate([5,5,-1])
	cube([5,5,16]);

}