
r = 7;
iw = 136;
ih = 95;
id = 8;

ow = 159.5+1.25;
oh = 109.5+1.25;
od = 3;

sw = 51;
sh = 28;
sd = 6;
st = 4;

hw = 5;
hh = sw+15;
hd = 3;

pw = sw/4;
ph = sh/2;
pd = 3;

/*
union() {
	difference() {
		union() {
			union() {
				translate( [0,r,0] ) cube( [iw, ih-2*r, id] );
				translate( [r,0,0] ) cube( [iw-2*r, ih, id] );
				translate( [r,r,0] ) cylinder( r=r, h=id, $fn=32 );
				translate( [iw-r,r,0] ) cylinder( r=r, h=id, $fn=32 );
				translate( [r,ih-r,0] ) cylinder( r=r, h=id, $fn=32 );
				translate( [iw-r,ih-r,0] ) cylinder( r=r, h=id, $fn=32 );
			}
			
			translate( [(iw-ow)/2,(ih-oh)/2,id] )
			union() {
				translate( [0,r,0] ) cube( [ow, oh-2*r, od] );
				translate( [r,0,0] ) cube( [ow-2*r, oh, od] );
				translate( [r,r,0] ) cylinder( r=r, h=od, $fn=32 );
				translate( [ow-r,r,0] ) cylinder( r=r, h=od, $fn=32 );
				translate( [r,oh-r,0] ) cylinder( r=r, h=od, $fn=32 );
				translate( [ow-r,oh-r,0] ) cylinder( r=r, h=od, $fn=32 );
			}
		}
	
		translate([(iw-sw)/2,(ih-sh)/2,-1])
		cube( [ sw+st+1, sh+st+1, id+od+2 ] );

		for( x=[0:7.5:sw+5] ) {
			translate([x+(iw-sw)/2,(ih-hh)/2+5,-1]) cylinder( r=1.5, h=100, $fn=30 );
			translate([x+(iw-sw)/2,(ih-hh)/2+hh-5,-1]) cylinder( r=1.5, h=100, $fn=30 );
		}
	}
	
	translate([(iw-sw)/2,(ih-sh)/2,0]) cylinder( r=3, h=2 );
	translate([(iw-sw)/2+sw+st+1,(ih-sh)/2,0]) cylinder( r=3, h=2 );
	translate([(iw-sw)/2,(ih-sh)/2+sh+st+1,0]) cylinder( r=3, h=2 );
	translate([(iw-sw)/2+sw+st+1,(ih-sh)/2+sh+st+1,0]) cylinder( r=3, h=2 );
}



translate([(iw-sw)/2,(ih-sh)/2,2])
union() {
	difference() {
		cube( [sw+st,sh+st,sd] );
		translate([st/2,st/2,1]) cube( [sw,sh,sd] );
		translate([st/2,6+st/2,-1]) cube( [30,13,10] );
	}
	translate( [8.3+st/2,22+st/2,0] ) cylinder( r=1.5, h=4, $fn=32 );
	translate( [23.3+st/2,22+st/2,0] ) cylinder( r=1.5, h=4, $fn=32 );
	translate( [25+st/2,0.6+st/2,0] ) cylinder( r=1.7, h=4, $fn=32 );
}

*/

translate( [(iw-ph)/2+15,(ih-hh)/2,id+od] ) 
difference() {
	union() {
		cube( [hw,hh,hd] );
		translate( [hw-hw,(hh-ph)/2,-pd] )
		cube( [pw,ph,pd+hd] );
	}
	translate( [hw/2,5,-1] )
	cylinder( r=1.5, h=hd+2, $fn=30 );

	translate( [hw/2,hh-5,-1] )
	cylinder( r=1.5, h=hd+2, $fn=30 );
}

