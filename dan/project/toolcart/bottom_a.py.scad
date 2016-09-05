

difference(){
	union() {
		cube(size = [60, 27, 46]);
		cube(size = [27, 60, 46]);
		translate(v = [0, 0, 42]) {
			cube(size = [27, 46, 40]);
		}
		translate(v = [13.5000000000, 23.0000000000, 0]) {
			rotate(a = 180, v = [1, 0, 0]) {
			}
		}
		translate(v = [13.5000000000, 34.5000000000, 0]) {
			rotate(a = 180, v = [1, 0, 0]) {
			}
		}
	}
	/* Holes Below*/
	union(){
		translate(v = [4, 4, 4]) {
			cube(size = [19, 60, 1000]);
			cube(size = [60, 19, 1000]);
		}
		translate(v = [4, 4, 56]) {
			cube(size = [1000, 1000, 1000]);
		}
		translate(v = [13.5000000000, 23.0000000000, 0]){
			rotate(a = 180, v = [1, 0, 0]){
				union() {
					union() {
						translate(v = [0, 0, -5]) {
							cylinder($fn = 12, h = 5, r = 1.9000000000);
						}
						translate(v = [0, 0, -3]) {
							cylinder($fn = 12, h = 3, r1 = 1.9000000000, r2 = 4);
						}
					}
					cylinder($fn = 12, h = 1, r = 4);
				}
			}
		}
		translate(v = [13.5000000000, 34.5000000000, 0]){
			rotate(a = 180, v = [1, 0, 0]){
				union() {
					union() {
						translate(v = [0, 0, -5]) {
							cylinder($fn = 12, h = 5, r = 1.9000000000);
						}
						translate(v = [0, 0, -3]) {
							cylinder($fn = 12, h = 3, r1 = 1.9000000000, r2 = 4);
						}
					}
					cylinder($fn = 12, h = 1, r = 4);
				}
			}
		}
	} /* End Holes */ 
}