difference() {
  union() {
//    for(i=[1:1:100] ) {
      translate([0,0.025000,0.085000])
      rotate(15.000000,[0,1,0])
      rotate(9.000000,[0,0,1])
      scale([0.970000,0.970000,0.970000])
      scale([1.000000,1,1])
      difference() {
        cylinder( r=1, h=1.000000, $fn=32 );
        translate([0,0,-0.02]) cylinder( r=0.9, h=2, $fn=32 );
      }

      translate([0,0.025000,0.085000])
      rotate(15.000000,[0,1,0])
      rotate(9.000000,[0,0,1])
      scale([0.970000,0.970000,0.970000])
      scale([1.000000,1,1])
      difference() {
        cylinder( r=1, h=1.000000, $fn=32 );
        translate([0,0,-0.02]) cylinder( r=0.9, h=2, $fn=32 );
      }


//    }
  }
}
