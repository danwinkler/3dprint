

difference(){
	union() {
	}
	/* Holes Below*/
	union(){
		translate(v = [0, 0, -1]) {
			cylinder($fn = 24, h = 7, r = 2);
		}
		translate(v = [0, 0, 1.5000000000]) {
			cylinder($fn = 24, h = 3.5010000000, r1 = 2, r2 = 4);
		}
		translate(v = [0, 0, 5]) {
			cylinder($fn = 24, h = 10, r = 4);
		}
		translate(v = [-20, -20, -20]) {
			cube(size = [40, 40, 20]);
		}
	} /* End Holes */ 
}