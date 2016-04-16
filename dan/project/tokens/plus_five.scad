

difference() {
	difference() {
		difference() {
			cylinder($fn = 36, h = 6, r = 20);
			translate(v = [0, 0, -1]) {
				cylinder($fn = 36, h = 3, r = 18);
			}
		}
		translate(v = [0, 0, 4]) {
			difference() {
				cylinder($fn = 36, h = 3, r = 21);
				cylinder($fn = 36, h = 3, r = 17.5000000000);
			}
		}
	}
	translate(v = [0, 0, 4]) {
		linear_extrude(height = 3) {
			text(halign = "center", size = 16, text = "+5", valign = "center");
		}
	}
}