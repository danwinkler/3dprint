

union() {
	translate(v = [10, 10, 0]) {
		difference() {
			difference() {
				cylinder(h = 25, r = 9.1000000000);
				translate(v = [0, 0, 5]) {
					cylinder(h = 30, r = 6.6000000000);
				}
			}
			translate(v = [0, -5, 17]) {
				rotate(a = 90, v = [1, 0, 0]) {
					cylinder($fn = 12, h = 6, r = 1.5000000000);
				}
			}
		}
	}
}