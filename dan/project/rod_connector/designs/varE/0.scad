

difference() {
	difference() {
		hull() {
			union() {
				union() {
					rotate(a = 142.4109105310, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [45.0000000000, 13.2000000000, 1]);
						}
					}
					rotate(a = -142.4109105310, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [45.0000000000, 13.2000000000, 1]);
						}
					}
					rotate(a = 108.0225105204, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [28.7746396149, 13.2000000000, 1]);
						}
					}
					rotate(a = -147.7117672506, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [36.6667092485, 13.2000000000, 1]);
						}
					}
				}
				translate(v = [0, 0, 9.6000063083]) {
					intersection() {
						hull() {
							rotate(a = 90.0000114961, v = [-0.6099942813, -0.7924058157, 0.0000014024]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 90.0000883836, v = [0.6099942813, -0.7924058157, 0.0000001824]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 39.7497720115, v = [-0.6080617410, -0.1978364069, 0.0000008059]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 54.5692278774, v = [0.4352578368, -0.6888226501, 0.0000002536]) {
								cylinder(h = 45, r = 9.6000000000);
							}
						}
						sphere(r = 45);
					}
				}
			}
		}
		translate(v = [0, 0, 9.6000063083]) {
			rotate(a = 90.0000114961, v = [-0.6099942813, -0.7924058157, 0.0000014024]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 90.0000883836, v = [0.6099942813, -0.7924058157, 0.0000001824]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 39.7497720115, v = [-0.6080617410, -0.1978364069, 0.0000008059]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 54.5692278774, v = [0.4352578368, -0.6888226501, 0.0000002536]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
		}
	}
	translate(v = [0, 0, 2]) {
		rotate(a = 180, v = [0, 1, 0]) {
			linear_extrude(height = 3) {
				text(halign = "center", size = 8, text = "0", valign = "center");
			}
		}
	}
}