s = 20;
//w = 140;
w = 122;
m = 4;

difference() {
	union() {
	
		translate( [0,0,0] ) {
			difference() {
				cube( [w,w,6]);
				translate( [m,m,2] ) cube( [w-2*m,w-2*m,10]);
			}
		}
	
		translate( [m+m,m+m,0] )
		scale( [(w-4*m)/s,(w-4*m)/s,1] )
		difference() {
			cube( [s,s,5] );
			for( y=[-0.0:s] ) {
				for( x=[-0.0:s] ) {
					translate( [x-0.01,y-0.01,rands(1,6,1)[0]] )
					cube( [1.01,1.01,10] );
				}
			}
		}
	}
	translate( [ 1.7*m, 1.7*m, -1] ) cylinder( r=2, h=10 );
	translate( [ w-1.7*m, 1.7*m, -1] ) cylinder( r=2, h=10 );
	translate( [ w-1.7*m, w-1.7*m, -1] ) cylinder( r=2, h=10 );
	translate( [ 1.7*m, w-1.7*m, -1] ) cylinder( r=2, h=10 );
}