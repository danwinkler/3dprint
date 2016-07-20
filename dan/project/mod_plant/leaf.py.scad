

union() {
	difference() {
		union() {
			translate(v = [0, 2.5000000000, 0]) {
				rotate(a = 90, v = [1, 0, 0]) {
					linear_extrude(height = 5) {
						polygon(paths = [[0, 1, 2, 3, 4, 5, 6]], points = [[10, 10], [22, 20], [20, 54], [0, 80], [-20, 54], [-22, 20], [-10, 10]]);
					}
				}
			}
			cylinder(h = 78, r1 = 5, r2 = 1);
		}
		cylinder(h = 10, r = 3);
	}
}