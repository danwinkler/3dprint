

difference() {
	difference() {
		hull() {
			union() {
				union() {
					rotate(a = -81.0242278944, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.9420034366, 13.2000000000, 1]);
						}
					}
					rotate(a = 97.7506422867, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.6693439378, 13.2000000000, 1]);
						}
					}
					rotate(a = -157.3790313254, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.6693427596, 13.2000000000, 1]);
						}
					}
					rotate(a = -34.1696483982, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.6693436164, 13.2000000000, 1]);
						}
					}
					rotate(a = 27.6970486357, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [43.9486498357, 13.2000000000, 1]);
						}
					}
				}
				translate(v = [0, 0, 15.0451645909]) {
					intersection() {
						hull() {
							rotate(a = 87.0908102812, v = [0.9864814221, 0.1558156734, -0.0000011423]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 96.9499685939, v = [-0.9835837218, -0.1338709624, 0.0000011175]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 96.9501049622, v = [0.3818067845, -0.9162867346, 0.0000005345]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 96.9500057958, v = [0.5575181206, 0.8212988260, -0.0000013788]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 77.5904233239, v = [-0.4539370269, 0.8647310451, -0.0000004108]) {
								cylinder(h = 45, r = 9.6000000000);
							}
						}
						sphere(r = 45);
					}
				}
			}
		}
		translate(v = [0, 0, 15.0451645909]) {
			rotate(a = 87.0908102812, v = [0.9864814221, 0.1558156734, -0.0000011423]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 96.9499685939, v = [-0.9835837218, -0.1338709624, 0.0000011175]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 96.9501049622, v = [0.3818067845, -0.9162867346, 0.0000005345]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 96.9500057958, v = [0.5575181206, 0.8212988260, -0.0000013788]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 77.5904233239, v = [-0.4539370269, 0.8647310451, -0.0000004108]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
		}
	}
	translate(v = [0, 0, 2]) {
		rotate(a = 180, v = [0, 1, 0]) {
			linear_extrude(height = 3) {
				text(halign = "center", size = 8, text = "37", valign = "center");
			}
		}
	}
}