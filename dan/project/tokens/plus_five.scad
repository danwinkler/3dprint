

difference() {
	difference() {
		difference() {
			cylinder($fn = 36, h = 6, r = 10);
			translate(v = [0, 0, -1]) {
				cylinder($fn = 36, h = 3, r = 9);
			}
		}
		translate(v = [0, 0, 4]) {
			difference() {
				cylinder($fn = 36, h = 3, r = 10.5000000000);
				cylinder($fn = 36, h = 3, r = 8);
			}
		}
	}
	translate(v = [0, 0, 4]) {
		linear_extrude(height = 3) {
			text(halign = "center", size = 8, text = "+5", valign = "center");
		}
	}
}