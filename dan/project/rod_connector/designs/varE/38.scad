

difference() {
	difference() {
		hull() {
			union() {
				union() {
					rotate(a = 35.3467536168, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [43.4016045701, 13.2000000000, 1]);
						}
					}
					rotate(a = 68.3358867344, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [17.7856732140, 13.2000000000, 1]);
						}
					}
					rotate(a = -31.0901724794, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [45.0000000000, 13.2000000000, 1]);
						}
					}
					rotate(a = 77.0620582972, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [45.0000000000, 13.2000000000, 1]);
						}
					}
					rotate(a = 142.4421393139, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.2679679817, 13.2000000000, 1]);
						}
					}
				}
				translate(v = [0, 0, 9.5999984701]) {
					intersection() {
						hull() {
							rotate(a = 74.6831409809, v = [-0.5579740472, 0.7866931540, -0.0000002287]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 23.2806929473, v = [-0.3673182813, 0.1459067093, 0.0000002214]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 89.9999785733, v = [0.5163864521, 0.8563556691, -0.0000013727]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 89.9999244636, v = [-0.9746131425, 0.2238955613, 0.0000007507]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 79.6512839417, v = [-0.5996461339, -0.7798425803, 0.0000013795]) {
								cylinder(h = 45, r = 9.6000000000);
							}
						}
						sphere(r = 45);
					}
				}
			}
		}
		translate(v = [0, 0, 9.5999984701]) {
			rotate(a = 74.6831409809, v = [-0.5579740472, 0.7866931540, -0.0000002287]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 23.2806929473, v = [-0.3673182813, 0.1459067093, 0.0000002214]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 89.9999785733, v = [0.5163864521, 0.8563556691, -0.0000013727]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 89.9999244636, v = [-0.9746131425, 0.2238955613, 0.0000007507]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 79.6512839417, v = [-0.5996461339, -0.7798425803, 0.0000013795]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
		}
	}
	translate(v = [0, 0, 2]) {
		rotate(a = 180, v = [0, 1, 0]) {
			linear_extrude(height = 3) {
				text(halign = "center", size = 8, text = "38", valign = "center");
			}
		}
	}
}