

difference() {
	difference() {
		hull() {
			union() {
				union() {
					rotate(a = 164.7886357031, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [43.0855412573, 13.2000000000, 1]);
						}
					}
					rotate(a = -17.4284239141, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.8787166652, 13.2000000000, 1]);
						}
					}
					rotate(a = 94.4448581405, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [41.5129379243, 13.2000000000, 1]);
						}
					}
					rotate(a = 25.8222615810, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [43.7878239288, 13.2000000000, 1]);
						}
					}
					rotate(a = -163.8058894154, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [43.7878212574, 13.2000000000, 1]);
						}
					}
					rotate(a = -80.8022124970, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [43.7878216848, 13.2000000000, 1]);
						}
					}
				}
				translate(v = [0, 0, 19.9742654382]) {
					intersection() {
						hull() {
							rotate(a = 73.2272146022, v = [-0.2512176951, -0.9239117677, 0.0000011751]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 94.2075148484, v = [0.2987068259, 0.9515204788, -0.0000012502]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 67.2957373806, v = [-0.9197347885, -0.0714945390, 0.0000009912]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 103.3288130025, v = [-0.4238477558, 0.8759022790, -0.0000004521]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 103.3289752894, v = [0.2713795561, -0.9344536308, 0.0000006631]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 103.3289493282, v = [0.9605512597, 0.1555375594, -0.0000011161]) {
								cylinder(h = 45, r = 9.6000000000);
							}
						}
						sphere(r = 45);
					}
				}
			}
		}
		translate(v = [0, 0, 19.9742654382]) {
			rotate(a = 73.2272146022, v = [-0.2512176951, -0.9239117677, 0.0000011751]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 94.2075148484, v = [0.2987068259, 0.9515204788, -0.0000012502]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 67.2957373806, v = [-0.9197347885, -0.0714945390, 0.0000009912]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 103.3288130025, v = [-0.4238477558, 0.8759022790, -0.0000004521]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 103.3289752894, v = [0.2713795561, -0.9344536308, 0.0000006631]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 103.3289493282, v = [0.9605512597, 0.1555375594, -0.0000011161]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
		}
	}
	translate(v = [0, 0, 2]) {
		rotate(a = 180, v = [0, 1, 0]) {
			linear_extrude(height = 3) {
				text(halign = "center", size = 8, text = "7", valign = "center");
			}
		}
	}
}