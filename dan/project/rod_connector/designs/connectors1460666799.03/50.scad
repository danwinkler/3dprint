

difference() {
	intersection() {
		hull() {
			rotate(a = -123.3588517168, v = [-0.8221247159, -0.1474510127, 0.0000000000]) {
				rotate(a = -90.0000000000, v = [-0.8660254038, 0.5000000000, 0.0000000000]) {
					cylinder(h = 60, r = 16.2000000000);
				}
			}
			rotate(a = -123.3588517168, v = [-0.8221247159, -0.1474510127, 0.0000000000]) {
				rotate(a = -90.0000000000, v = [-0.0000000000, -1.0000000000, 0.0000000000]) {
					cylinder(h = 60, r = 16.2000000000);
				}
			}
			rotate(a = -123.3588517168, v = [-0.8221247159, -0.1474510127, 0.0000000000]) {
				rotate(a = -18.4383929552, v = [-0.2692672153, 0.1659253944, 0.0000000000]) {
					cylinder(h = 60, r = 16.2000000000);
				}
			}
			rotate(a = -123.3588517168, v = [-0.8221247159, -0.1474510127, 0.0000000000]) {
				rotate(a = -149.1684967374, v = [-0.3268370039, 0.3947774996, 0.0000000000]) {
					cylinder(h = 60, r = 16.2000000000);
				}
			}
			rotate(a = -123.3588517168, v = [-0.8221247159, -0.1474510127, 0.0000000000]) {
				rotate(a = -159.6517266695, v = [0.1948712799, -0.2879902172, 0.0000000000]) {
					cylinder(h = 60, r = 16.2000000000);
				}
			}
		}
		sphere(r = 60);
	}
	union() {
		rotate(a = -123.3588517168, v = [-0.8221247159, -0.1474510127, 0.0000000000]) {
			rotate(a = -90.0000000000, v = [-0.8660254038, 0.5000000000, 0.0000000000]) {
				translate(v = [0, 0, 35]) {
					cylinder(h = 100, r = 13.2000000000);
				}
			}
		}
		rotate(a = -123.3588517168, v = [-0.8221247159, -0.1474510127, 0.0000000000]) {
			rotate(a = -90.0000000000, v = [-0.0000000000, -1.0000000000, 0.0000000000]) {
				translate(v = [0, 0, 35]) {
					cylinder(h = 100, r = 13.2000000000);
				}
			}
		}
		rotate(a = -123.3588517168, v = [-0.8221247159, -0.1474510127, 0.0000000000]) {
			rotate(a = -18.4383929552, v = [-0.2692672153, 0.1659253944, 0.0000000000]) {
				translate(v = [0, 0, 35]) {
					cylinder(h = 100, r = 13.2000000000);
				}
			}
		}
		rotate(a = -123.3588517168, v = [-0.8221247159, -0.1474510127, 0.0000000000]) {
			rotate(a = -149.1684967374, v = [-0.3268370039, 0.3947774996, 0.0000000000]) {
				translate(v = [0, 0, 35]) {
					cylinder(h = 100, r = 13.2000000000);
				}
			}
		}
		rotate(a = -123.3588517168, v = [-0.8221247159, -0.1474510127, 0.0000000000]) {
			rotate(a = -159.6517266695, v = [0.1948712799, -0.2879902172, 0.0000000000]) {
				translate(v = [0, 0, 35]) {
					cylinder(h = 100, r = 13.2000000000);
				}
			}
		}
	}
}