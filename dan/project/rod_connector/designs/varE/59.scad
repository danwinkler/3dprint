

difference() {
	union() {
		rotate(a = -68.6936138018, v = [-0.5671530724, -0.7391281906, -0.0000001306]) {
			intersection() {
				hull() {
					rotate(a = 90.0000000000, v = [0.6712971803, -0.7411882998, 0.0000000000]) {
						cylinder(h = 50, r = 9.6000000000);
					}
					rotate(a = 90.0000000000, v = [-0.8896774161, 0.4565896356, 0.0000000000]) {
						cylinder(h = 50, r = 9.6000000000);
					}
					rotate(a = 133.4303559138, v = [0.1813528847, -0.7032018797, 0.0000000000]) {
						cylinder(h = 50, r = 9.6000000000);
					}
					rotate(a = 167.9994481359, v = [-0.1937545976, 0.0754343741, 0.0000000000]) {
						cylinder(h = 50, r = 9.6000000000);
					}
				}
				sphere(r = 60);
			}
		}
		translate(v = [0, 0, -1.9813319583]) {
			union() {
				rotate(a = 48.7098524278, v = [0, 0, 1]) {
					translate(v = [0, -6.6000000000, 0]) {
						cube(size = [50, 13.2000000000, 0.1000000000]);
					}
				}
				rotate(a = -123.7098412684, v = [0, 0, 1]) {
					translate(v = [0, -6.6000000000, 0]) {
						cube(size = [50, 13.2000000000, 0.1000000000]);
					}
				}
				rotate(a = -2.0412884776, v = [0, 0, 1]) {
					translate(v = [0, -6.6000000000, 0]) {
						cube(size = [50, 13.2000000000, 0.1000000000]);
					}
				}
				rotate(a = -49.5851685725, v = [0, 0, 1]) {
					translate(v = [0, -6.6000000000, 0]) {
						cube(size = [50, 13.2000000000, 0.1000000000]);
					}
				}
			}
		}
	}
	rotate(a = -68.6936138018, v = [-0.5671530724, -0.7391281906, -0.0000001306]) {
		union() {
			rotate(a = 90.0000000000, v = [0.6712971803, -0.7411882998, 0.0000000000]) {
				translate(v = [0, 0, 25]) {
					cylinder(h = 100, r = 6.6000000000);
				}
			}
			rotate(a = 90.0000000000, v = [-0.8896774161, 0.4565896356, 0.0000000000]) {
				translate(v = [0, 0, 25]) {
					cylinder(h = 100, r = 6.6000000000);
				}
			}
			rotate(a = 133.4303559138, v = [0.1813528847, -0.7032018797, 0.0000000000]) {
				translate(v = [0, 0, 25]) {
					cylinder(h = 100, r = 6.6000000000);
				}
			}
			rotate(a = 167.9994481359, v = [-0.1937545976, 0.0754343741, 0.0000000000]) {
				translate(v = [0, 0, 25]) {
					cylinder(h = 100, r = 6.6000000000);
				}
			}
		}
	}
}