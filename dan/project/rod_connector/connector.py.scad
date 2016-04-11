

union() {
	cube(size = [60, 20, 5]);
	translate(v = [10, 10, 0]) {
		difference() {
			difference() {
				cylinder(h = 30, r = 7.8500000000);
				translate(v = [0, 0, 10]) {
					cylinder(h = 30, r = 5.8500000000);
				}
			}
			translate(v = [0, -5, 22]) {
				rotate(a = 90, v = [1, 0, 0]) {
					cylinder($fn = 8, h = 6, r = 1);
				}
			}
		}
	}
	translate(v = [30, 10, 0]) {
		difference() {
			difference() {
				cylinder(h = 30, r = 8.3500000000);
				translate(v = [0, 0, 10]) {
					cylinder(h = 30, r = 6.3500000000);
				}
			}
			translate(v = [0, -5, 22]) {
				rotate(a = 90, v = [1, 0, 0]) {
					cylinder($fn = 8, h = 6, r = 1);
				}
			}
		}
	}
	translate(v = [50, 10, 0]) {
		difference() {
			difference() {
				cylinder(h = 30, r = 8.8500000000);
				translate(v = [0, 0, 10]) {
					cylinder(h = 30, r = 6.8500000000);
				}
			}
			translate(v = [0, -5, 22]) {
				rotate(a = 90, v = [1, 0, 0]) {
					cylinder($fn = 8, h = 6, r = 1);
				}
			}
		}
	}
}