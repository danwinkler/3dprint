

translate(v = [0, 0, -3]) {
	difference() {
		minkowski() {
			cube(size = [70, 115, 0.0001000000]);
			difference() {
				sphere($fn = 24, r = 5);
				translate(v = [-5, -5, -5]) {
					cube(size = [10, 10, 5]);
				}
			}
		}
		union() {
			translate(v = [1, 1, -1]) {
				cube(size = [67, 112, 7]);
			}
			translate(v = [-0.2000000000, -0.2000000000, 2.8000000000]) {
				cube(size = [70.4000000000, 115.4000000000, 7]);
			}
		}
	}
}