t=0.6;
n=180/3;

difference(){

	union(){ 
        difference(){
			cube([180,15,8]);
			
			translate([t,t,t])
			cube([180-2*t,15-2*t, 8-2*t]);
		}
		intersection(){
			for(i=[1:400]){
				a=rands(180,-90,1)[0];
				b=rands(-90,90,1)[0];
				b=rands(-90,90,1)[0];
				
				x = rands(0,180,1)[0];
				y = rands(0,15,1)[0];

				translate([x,y,0])
				rotate(a,[180,0,1])

				rotate(b,[0,1,0])
				rotate(c,[0,0,1])
				cube([2*t,500,2*t]);
			}
			cube([180,15,8]);
		}
	}

    translate([-t,-t,8-t-0.1])
	cube([180+2*t,15+2*t,8+2*t]);

	translate([5,5,-1])
	cube([5,5,16]);
    
}