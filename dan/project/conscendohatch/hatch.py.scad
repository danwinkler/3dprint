

union() {
	translate(v = [0, 0, 18]) {
		rotate(a = 180, v = [1, 0, 0]) {
			difference() {
				translate(v = [0, -8.5000000000, 0]) {
					cube(size = [40, 17, 9]);
				}
				translate(v = [7, -10, 9]) {
					rotate(a = 150, v = [0, 1, 0]) {
						translate(v = [0, 0, -5]) {
							cube(size = [20, 20, 5]);
						}
					}
				}
			}
			translate(v = [7, -8.5000000000, 9]) {
				cube(size = [158, 17, 9]);
			}
			translate(v = [163.5000000000, -4.2500000000, 0]) {
				cube(size = [1.5000000000, 8.5000000000, 9]);
			}
			translate(v = [163.5000000000, -4.2500000000, 4.5000000000]) {
				rotate(a = -90, v = [1, 0, 0]) {
					linear_extrude(height = 8.5000000000) {
						polygon(paths = [[0, 1, 2, 3]], points = [[0, 0], [4.5000000000, 2], [1.5000000000, 4.5000000000], [0, 4.5000000000]]);
					}
				}
			}
		}
	}
}