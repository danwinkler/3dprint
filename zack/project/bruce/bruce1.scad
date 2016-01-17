w = 30;
h = 60;
d = 10;
cw = 20;
ch = 30;
sh = 20;

module hinge() {
	difference() {
		cube( [w,h,d] );
	
		translate([-1,-1,-1]) cube( [cw+1,ch+1,d+2] );
	
		translate([-(w-w-cw)/2,ch,0])
		rotate(45,[1,0,0])
		cube( [w-cw,sh,d] );
	
	}
}

hinge();	
translate([w,0,0])
rotate(180,[0,0,1]) hinge();	
