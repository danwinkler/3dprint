

difference() {
	union() {
		intersection() {
			hull() {
				rotate(a = 82.4188627777, v = [-0.5008320644, -0.8554307121, 0.0000013563]) {
					cylinder(h = 50, r = 9.6000000000);
				}
				rotate(a = 82.4188166408, v = [0.4904087085, 0.8614485173, -0.0000013519]) {
					cylinder(h = 50, r = 9.6000000000);
				}
				rotate(a = 82.4187720484, v = [-0.9876284897, 0.0847585512, 0.0000009029]) {
					cylinder(h = 50, r = 9.6000000000);
				}
				rotate(a = 102.4070247186, v = [-0.1369076128, 0.9670023808, -0.0000008301]) {
					cylinder(h = 50, r = 9.6000000000);
				}
			}
			sphere(r = 60);
		}
		translate(v = [0, 0, -3.0180940819]) {
			union() {
				rotate(a = 30.3478553177, v = [0, 0, 1]) {
					translate(v = [0, -6.6000000000, 0]) {
						cube(size = [50, 13.2000000000, 0.1000000000]);
					}
				}
				rotate(a = -150.3478509310, v = [0, 0, 1]) {
					translate(v = [0, -6.6000000000, 0]) {
						cube(size = [50, 13.2000000000, 0.1000000000]);
					}
				}
				rotate(a = 94.9051279457, v = [0, 0, 1]) {
					translate(v = [0, -6.6000000000, 0]) {
						cube(size = [50, 13.2000000000, 0.1000000000]);
					}
				}
				rotate(a = 171.9416664847, v = [0, 0, 1]) {
					translate(v = [0, -6.6000000000, 0]) {
						cube(size = [50, 13.2000000000, 0.1000000000]);
					}
				}
			}
		}
	}
	union() {
		rotate(a = 82.4188627777, v = [-0.5008320644, -0.8554307121, 0.0000013563]) {
			translate(v = [0, 0, 25]) {
				cylinder(h = 100, r = 6.6000000000);
			}
		}
		rotate(a = 82.4188166408, v = [0.4904087085, 0.8614485173, -0.0000013519]) {
			translate(v = [0, 0, 25]) {
				cylinder(h = 100, r = 6.6000000000);
			}
		}
		rotate(a = 82.4187720484, v = [-0.9876284897, 0.0847585512, 0.0000009029]) {
			translate(v = [0, 0, 25]) {
				cylinder(h = 100, r = 6.6000000000);
			}
		}
		rotate(a = 102.4070247186, v = [-0.1369076128, 0.9670023808, -0.0000008301]) {
			translate(v = [0, 0, 25]) {
				cylinder(h = 100, r = 6.6000000000);
			}
		}
	}
}