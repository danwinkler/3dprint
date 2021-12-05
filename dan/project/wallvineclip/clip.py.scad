

difference(){
	union() {
		hull() {
			translate(v = [-5.0000000000, -5.0000000000, 0]) {
				sphere($fn = 24, r = 5);
			}
			translate(v = [5.0000000000, -5.0000000000, 0]) {
				sphere($fn = 24, r = 5);
			}
			translate(v = [5.0000000000, 5.0000000000, 0]) {
				sphere($fn = 24, r = 5);
			}
			translate(v = [-5.0000000000, 5.0000000000, 0]) {
				sphere($fn = 24, r = 5);
			}
		}
		translate(v = [0, 0, 15]) {
			rotate(a = 90, v = [1, 0, 0]) {
				rotate(a = -410.0000000000, v = [0, 0, 1]) {
					union() {
						rotate_extrude($fn = 48, angle = 280) {
							translate(v = [-15, 0]) {
								circle($fn = 24, r = 3.5000000000);
							}
						}
						rotate(a = 460, v = [0, 0, 1]) {
							translate(v = [15, 0, 0]) {
								rotate(a = 90, v = [1, 0, 0]) {
									sphere($fn = 24, r = 3.5000000000);
								}
							}
						}
						rotate(a = 180, v = [0, 0, 1]) {
							translate(v = [15, 0, 0]) {
								rotate(a = 90, v = [1, 0, 0]) {
									sphere($fn = 24, r = 3.5000000000);
								}
							}
						}
					}
				}
			}
		}
	}
	/* Holes Below*/
	union(){
		translate(v = [0, 0, -1]) {
			cylinder($fn = 24, h = 7, r = 2);
		}
		translate(v = [0, 0, 1.5000000000]) {
			cylinder($fn = 24, h = 3.5000000000, r1 = 2, r2 = 4);
		}
		translate(v = [-20, -20, -5]) {
			cube(size = [40, 40, 5]);
		}
	} /* End Holes */ 
}