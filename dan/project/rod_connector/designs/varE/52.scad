

difference() {
	difference() {
		hull() {
			union() {
				union() {
					rotate(a = -155.2343134586, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [43.2386989199, 13.2000000000, 1]);
						}
					}
					rotate(a = -134.7046071869, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [23.1349615153, 13.2000000000, 1]);
						}
					}
					rotate(a = 134.6474812410, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [45.0000000000, 13.2000000000, 1]);
						}
					}
					rotate(a = -110.8909467618, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [45.0000000000, 13.2000000000, 1]);
						}
					}
					rotate(a = -51.5132604139, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.4078231141, 13.2000000000, 1]);
						}
					}
				}
				translate(v = [0, 0, 9.6000000000]) {
					intersection() {
						hull() {
							rotate(a = 73.9167830089, v = [0.4025125489, -0.8724885374, 0.0000004700]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 30.9380828061, v = [0.3654010777, -0.3616526716, -0.0000000037]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 89.9999994516, v = [-0.7114439245, -0.7027428706, 0.0000014142]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 90.0000813564, v = [0.9342608304, -0.3565903823, -0.0000005777]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 80.6946206803, v = [0.7724517540, 0.6141437440, -0.0000013866]) {
								cylinder(h = 45, r = 9.6000000000);
							}
						}
						sphere(r = 45);
					}
				}
			}
		}
		translate(v = [0, 0, 9.6000000000]) {
			rotate(a = 73.9167830089, v = [0.4025125489, -0.8724885374, 0.0000004700]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 30.9380828061, v = [0.3654010777, -0.3616526716, -0.0000000037]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 89.9999994516, v = [-0.7114439245, -0.7027428706, 0.0000014142]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 90.0000813564, v = [0.9342608304, -0.3565903823, -0.0000005777]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 80.6946206803, v = [0.7724517540, 0.6141437440, -0.0000013866]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
		}
	}
	translate(v = [0, 0, 2]) {
		rotate(a = 180, v = [0, 1, 0]) {
			linear_extrude(height = 3) {
				text(halign = "center", size = 8, text = "52", valign = "center");
			}
		}
	}
}