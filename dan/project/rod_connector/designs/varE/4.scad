

difference() {
	union() {
		intersection() {
			hull() {
				rotate(a = 51.1828617132, v = [-0.1148090146, 0.7706454391, -0.0000006558]) {
					cylinder(h = 50, r = 9.6000000000);
				}
				rotate(a = 51.1828978343, v = [-0.7248032770, -0.2858956595, 0.0000010107]) {
					cylinder(h = 50, r = 9.6000000000);
				}
				rotate(a = 51.1829691655, v = [0.7259353563, 0.2830109415, -0.0000010089]) {
					cylinder(h = 50, r = 9.6000000000);
				}
				rotate(a = 25.9027497415, v = [-0.1854064135, -0.3955476968, 0.0000005810]) {
					cylinder(h = 50, r = 9.6000000000);
				}
			}
			sphere(r = 60);
		}
		translate(v = [0, 0, 17.6730989473]) {
			union() {
				rotate(a = 171.5264865821, v = [0, 0, 1]) {
					translate(v = [0, -6.6000000000, 0]) {
						cube(size = [50, 13.2000000000, 0.1000000000]);
					}
				}
				rotate(a = 68.4735092599, v = [0, 0, 1]) {
					translate(v = [0, -6.6000000000, 0]) {
						cube(size = [50, 13.2000000000, 0.1000000000]);
					}
				}
				rotate(a = -111.2987286965, v = [0, 0, 1]) {
					translate(v = [0, -6.6000000000, 0]) {
						cube(size = [50, 13.2000000000, 0.1000000000]);
					}
				}
				rotate(a = 25.1142116141, v = [0, 0, 1]) {
					translate(v = [0, -6.6000000000, 0]) {
						cube(size = [50, 13.2000000000, 0.1000000000]);
					}
				}
			}
		}
	}
	union() {
		rotate(a = 51.1828617132, v = [-0.1148090146, 0.7706454391, -0.0000006558]) {
			translate(v = [0, 0, 25]) {
				cylinder(h = 100, r = 6.6000000000);
			}
		}
		rotate(a = 51.1828978343, v = [-0.7248032770, -0.2858956595, 0.0000010107]) {
			translate(v = [0, 0, 25]) {
				cylinder(h = 100, r = 6.6000000000);
			}
		}
		rotate(a = 51.1829691655, v = [0.7259353563, 0.2830109415, -0.0000010089]) {
			translate(v = [0, 0, 25]) {
				cylinder(h = 100, r = 6.6000000000);
			}
		}
		rotate(a = 25.9027497415, v = [-0.1854064135, -0.3955476968, 0.0000005810]) {
			translate(v = [0, 0, 25]) {
				cylinder(h = 100, r = 6.6000000000);
			}
		}
	}
}