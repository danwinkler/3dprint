

difference() {
	difference() {
		difference() {
			hull() {
				union() {
					union() {
						rotate(a = 48.0879071675, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [22.6920655075, 13.2000000000, 1]);
							}
						}
						rotate(a = 4.5231499124, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [43.6786658992, 13.2000000000, 1]);
							}
						}
						rotate(a = 99.5617542539, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [44.8407924213, 13.2000000000, 1]);
							}
						}
						rotate(a = 44.6494538069, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [45.0000000000, 13.2000000000, 1]);
							}
						}
						rotate(a = -60.2273170790, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [18.6721476773, 13.2000000000, 1]);
							}
						}
						rotate(a = -69.2344256637, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [45.0000000000, 13.2000000000, 1]);
							}
						}
					}
					translate(v = [0, 0, 9.6000026122]) {
						intersection() {
							hull() {
								rotate(a = 30.2826998305, v = [-0.3752606361, 0.3368450154, 0.0000000384]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 76.0809989617, v = [-0.0765460254, 0.9676137805, -0.0000008911]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 85.1789059921, v = [-0.9826182599, -0.1655229371, 0.0000011481]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 89.9999108704, v = [-0.7027673637, 0.7114197302, -0.0000000087]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 24.5153461773, v = [0.3601668454, 0.2060400893, -0.0000005662]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 90.0000365858, v = [0.9350388705, 0.3545452166, -0.0000012896]) {
									cylinder(h = 45, r = 9.6000000000);
								}
							}
							sphere(r = 45);
						}
					}
				}
			}
			translate(v = [0, 0, 9.6000026122]) {
				rotate(a = 30.2826998305, v = [-0.3752606361, 0.3368450154, 0.0000000384]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 76.0809989617, v = [-0.0765460254, 0.9676137805, -0.0000008911]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 85.1789059921, v = [-0.9826182599, -0.1655229371, 0.0000011481]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 89.9999108704, v = [-0.7027673637, 0.7114197302, -0.0000000087]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 24.5153461773, v = [0.3601668454, 0.2060400893, -0.0000005662]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 90.0000365858, v = [0.9350388705, 0.3545452166, -0.0000012896]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
			}
		}
		translate(v = [-100, -100, -100]) {
			cube(size = [200, 200, 100]);
		}
	}
	translate(v = [0, 0, 2]) {
		rotate(a = 180, v = [0, 1, 0]) {
			linear_extrude(height = 3) {
				text(halign = "center", size = 8, text = "36", valign = "center");
			}
		}
	}
}