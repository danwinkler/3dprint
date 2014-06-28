r = 5.5;
d = 5;
t = 2;
c = 0.5;
w = r*4 + t*2 + c*2;
s = 0.5;
b = 13;
g = 4;
h = t + g + b + s + t;
a = 1.7;

module roller() {
	union() {
		translate([-0.5,-4,0])	
		cube([1,8,15]);
	
		translate([4,-0.5,0])	
		rotate(90,[0,0,1])
		cube([1,8,15]);
	
		translate([0,0,-3])	 cylinder( r=a-0.1, h=30, $fn=30 );
	}
}

union() {
	translate([-w/2,-d/2,-2]) {
		difference() {
			translate([0,0,0]) cube([w,d,h]);
			translate([t,-d/2,t]) cube([4*r+2*c, d+3, g+b+s]);
			translate([w/2-r,d/2,-1]) cylinder(r=a,h=h+2,$fn=100);
			translate([w/2-r,d/2-2.0,t]) cylinder(r=a,h=h+2,$fn=100);
			translate([w/2+r,d/2,-1]) cylinder(r=a,h=h+2,$fn=100);
			translate([w/2+r,d/2-2.0,t]) cylinder(r=a,h=h+2,$fn=100);

		}
	}
}

translate([-r,0,1]) roller();
//translate([+r,0,1]) roller();


