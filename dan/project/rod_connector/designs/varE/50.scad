

difference() {
	difference() {
		hull() {
			union() {
				union() {
					rotate(a = 84.7656981313, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [43.2386959105, 13.2000000000, 1]);
						}
					}
					rotate(a = 105.2954155284, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [23.1349533520, 13.2000000000, 1]);
						}
					}
					rotate(a = 14.6474921445, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [45.0000000000, 13.2000000000, 1]);
						}
					}
					rotate(a = 129.1090641417, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [45.0000000000, 13.2000000000, 1]);
						}
					}
					rotate(a = -171.5132474013, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.4078238244, 13.2000000000, 1]);
						}
					}
				}
				translate(v = [0, 0, 9.5999993468]) {
					intersection() {
						hull() {
							rotate(a = 73.9166308660, v = [-0.9568528080, 0.0876578007, 0.0000008692]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 30.9379495089, v = [-0.4958986816, -0.1356209726, 0.0000006315]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 89.9999230857, v = [-0.2528714002, 0.9674998992, -0.0000007146]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 89.9999908520, v = [-0.7759466250, -0.6307985694, 0.0000014067]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 80.6946822064, v = [0.1456388134, -0.9760347992, 0.0000008304]) {
								cylinder(h = 45, r = 9.6000000000);
							}
						}
						sphere(r = 45);
					}
				}
			}
		}
		translate(v = [0, 0, 9.5999993468]) {
			rotate(a = 73.9166308660, v = [-0.9568528080, 0.0876578007, 0.0000008692]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 30.9379495089, v = [-0.4958986816, -0.1356209726, 0.0000006315]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 89.9999230857, v = [-0.2528714002, 0.9674998992, -0.0000007146]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 89.9999908520, v = [-0.7759466250, -0.6307985694, 0.0000014067]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 80.6946822064, v = [0.1456388134, -0.9760347992, 0.0000008304]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
		}
	}
	translate(v = [0, 0, 2]) {
		rotate(a = 180, v = [0, 1, 0]) {
			linear_extrude(height = 3) {
				text(halign = "center", size = 8, text = "50", valign = "center");
			}
		}
	}
}