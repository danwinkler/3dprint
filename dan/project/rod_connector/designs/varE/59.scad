

difference() {
	union() {
		intersection() {
			hull() {
				rotate(a = 80.3805511848, v = [0.7408127628, -0.6505942625, -0.0000000902]) {
					cylinder(h = 50, r = 9.6000000000);
				}
				rotate(a = 80.3803748338, v = [-0.8201619484, 0.5471835233, 0.0000002730]) {
					cylinder(h = 50, r = 9.6000000000);
				}
				rotate(a = 80.3805229807, v = [-0.0351186578, -0.9853136361, 0.0000010204]) {
					cylinder(h = 50, r = 9.6000000000);
				}
				rotate(a = 107.5345711213, v = [-0.7259939628, -0.6181928546, 0.0000013442]) {
					cylinder(h = 50, r = 9.6000000000);
				}
			}
			sphere(r = 60);
		}
		translate(v = [0, 0, -1.9813319583]) {
			union() {
				rotate(a = -48.7098524278, v = [0, 0, 1]) {
					translate(v = [0, -6.6000000000, 0]) {
						cube(size = [50, 13.2000000000, 0.1000000000]);
					}
				}
				rotate(a = 123.7098412684, v = [0, 0, 1]) {
					translate(v = [0, -6.6000000000, 0]) {
						cube(size = [50, 13.2000000000, 0.1000000000]);
					}
				}
				rotate(a = 2.0412884776, v = [0, 0, 1]) {
					translate(v = [0, -6.6000000000, 0]) {
						cube(size = [50, 13.2000000000, 0.1000000000]);
					}
				}
				rotate(a = 49.5851685725, v = [0, 0, 1]) {
					translate(v = [0, -6.6000000000, 0]) {
						cube(size = [50, 13.2000000000, 0.1000000000]);
					}
				}
			}
		}
	}
	union() {
		rotate(a = 80.3805511848, v = [0.7408127628, -0.6505942625, -0.0000000902]) {
			translate(v = [0, 0, 25]) {
				cylinder(h = 100, r = 6.6000000000);
			}
		}
		rotate(a = 80.3803748338, v = [-0.8201619484, 0.5471835233, 0.0000002730]) {
			translate(v = [0, 0, 25]) {
				cylinder(h = 100, r = 6.6000000000);
			}
		}
		rotate(a = 80.3805229807, v = [-0.0351186578, -0.9853136361, 0.0000010204]) {
			translate(v = [0, 0, 25]) {
				cylinder(h = 100, r = 6.6000000000);
			}
		}
		rotate(a = 107.5345711213, v = [-0.7259939628, -0.6181928546, 0.0000013442]) {
			translate(v = [0, 0, 25]) {
				cylinder(h = 100, r = 6.6000000000);
			}
		}
	}
}