

difference() {
	difference() {
		hull() {
			union() {
				union() {
					rotate(a = 59.9220671748, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [43.3285938395, 13.2000000000, 1]);
						}
					}
					rotate(a = 86.2367268014, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [20.2408007204, 13.2000000000, 1]);
						}
					}
					rotate(a = -8.3206772549, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [45.0000000000, 13.2000000000, 1]);
						}
					}
					rotate(a = 102.9587717380, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [45.0000000000, 13.2000000000, 1]);
						}
					}
					rotate(a = 165.3615408425, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.3381467766, 13.2000000000, 1]);
						}
					}
				}
				translate(v = [0, 0, 9.5999966237]) {
					intersection() {
						hull() {
							rotate(a = 74.3350858760, v = [-0.8332033041, 0.4825623070, 0.0000003506]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 26.7305078588, v = [-0.4488248045, 0.0295211210, 0.0000004193]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 89.9999467587, v = [0.1447132978, 0.9894736285, -0.0000011342]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 89.9999527132, v = [-0.9745316803, -0.2242498698, 0.0000011988]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 80.1611543915, v = [-0.2490017436, -0.9533094956, 0.0000012023]) {
								cylinder(h = 45, r = 9.6000000000);
							}
						}
						sphere(r = 45);
					}
				}
			}
		}
		translate(v = [0, 0, 9.5999966237]) {
			rotate(a = 74.3350858760, v = [-0.8332033041, 0.4825623070, 0.0000003506]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 26.7305078588, v = [-0.4488248045, 0.0295211210, 0.0000004193]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 89.9999467587, v = [0.1447132978, 0.9894736285, -0.0000011342]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 89.9999527132, v = [-0.9745316803, -0.2242498698, 0.0000011988]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 80.1611543915, v = [-0.2490017436, -0.9533094956, 0.0000012023]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
		}
	}
	translate(v = [0, 0, 2]) {
		rotate(a = 180, v = [0, 1, 0]) {
			linear_extrude(height = 3) {
				text(halign = "center", size = 8, text = "44", valign = "center");
			}
		}
	}
}