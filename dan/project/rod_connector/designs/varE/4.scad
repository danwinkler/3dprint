

difference() {
	difference() {
		hull() {
			union() {
				union() {
					rotate(a = 22.4109105310, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [45.0000000000, 13.2000000000, 1]);
						}
					}
					rotate(a = 97.5890894690, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [45.0000000000, 13.2000000000, 1]);
						}
					}
					rotate(a = -11.9775063242, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [28.7746391682, 13.2000000000, 1]);
						}
					}
					rotate(a = 92.2882357156, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [36.6667031495, 13.2000000000, 1]);
						}
					}
				}
				translate(v = [0, 0, 9.5999961353]) {
					intersection() {
						hull() {
							rotate(a = 89.9999177095, v = [-0.3812464258, 0.9244734516, -0.0000005432]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 89.9999458523, v = [-0.9912407072, -0.1320676359, 0.0000011233]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 39.7497638717, v = [0.1327015173, 0.6255145820, -0.0000007582]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 54.5690804774, v = [-0.8141653234, -0.0325334230, 0.0000008467]) {
								cylinder(h = 45, r = 9.6000000000);
							}
						}
						sphere(r = 45);
					}
				}
			}
		}
		translate(v = [0, 0, 9.5999961353]) {
			rotate(a = 89.9999177095, v = [-0.3812464258, 0.9244734516, -0.0000005432]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 89.9999458523, v = [-0.9912407072, -0.1320676359, 0.0000011233]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 39.7497638717, v = [0.1327015173, 0.6255145820, -0.0000007582]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 54.5690804774, v = [-0.8141653234, -0.0325334230, 0.0000008467]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
		}
	}
	translate(v = [0, 0, 2]) {
		rotate(a = 180, v = [0, 1, 0]) {
			linear_extrude(height = 3) {
				text(halign = "center", size = 8, text = "4", valign = "center");
			}
		}
	}
}