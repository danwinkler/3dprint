

union() {
	difference() {
		cube(size = [106.9000000000, 61.9000000000, 2]);
		union() {
			union() {
				translate(v = [41.2000000000, 25.7500000000, -1]) {
					cube(size = [24.5000000000, 10.4000000000, 10]);
				}
				translate(v = [22.7000000000, 30.9500000000, -0.0010000000]) {
					cylinder($fn = 16, h = 2.0020000000, r1 = 2.3000000000, r2 = 3.7500000000);
				}
			}
			translate(v = [84.2000000000, 30.9500000000, -0.0010000000]) {
				cylinder($fn = 16, h = 2.0020000000, r1 = 2.3000000000, r2 = 3.7500000000);
			}
		}
	}
}