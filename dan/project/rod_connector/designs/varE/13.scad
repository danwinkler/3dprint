

difference() {
	difference() {
		hull() {
			union() {
				union() {
					rotate(a = -164.0885512475, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.8608908935, 13.2000000000, 1]);
						}
					}
					rotate(a = 15.0152159976, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.7913230676, 13.2000000000, 1]);
						}
					}
					rotate(a = -95.9190252277, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.8608909424, 13.2000000000, 1]);
						}
					}
					rotate(a = -24.7853353406, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [43.2827505919, 13.2000000000, 1]);
						}
					}
					rotate(a = 155.7745340765, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [43.5340642495, 13.2000000000, 1]);
						}
					}
					rotate(a = 80.1571479605, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.8608917393, 13.2000000000, 1]);
						}
					}
				}
				translate(v = [0, 0, 13.1356500208]) {
					intersection() {
						hull() {
							rotate(a = 94.5063811309, v = [0.2733038204, -0.9587135951, 0.0000006854]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 95.5198978963, v = [-0.2578742503, 0.9613782188, -0.0000007035]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 94.5063724305, v = [0.9915937197, -0.1028039616, -0.0000008888]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 74.1203952557, v = [0.4032221147, 0.8732386515, -0.0000012765]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 75.3352699468, v = [-0.3969611434, -0.8822304772, 0.0000012792]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 94.5062303702, v = [-0.9822346084, 0.1704180798, 0.0000008118]) {
								cylinder(h = 45, r = 9.6000000000);
							}
						}
						sphere(r = 45);
					}
				}
			}
		}
		translate(v = [0, 0, 13.1356500208]) {
			rotate(a = 94.5063811309, v = [0.2733038204, -0.9587135951, 0.0000006854]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 95.5198978963, v = [-0.2578742503, 0.9613782188, -0.0000007035]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 94.5063724305, v = [0.9915937197, -0.1028039616, -0.0000008888]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 74.1203952557, v = [0.4032221147, 0.8732386515, -0.0000012765]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 75.3352699468, v = [-0.3969611434, -0.8822304772, 0.0000012792]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 94.5062303702, v = [-0.9822346084, 0.1704180798, 0.0000008118]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
		}
	}
	translate(v = [0, 0, 2]) {
		rotate(a = 180, v = [0, 1, 0]) {
			linear_extrude(height = 3) {
				text(halign = "center", size = 8, text = "13", valign = "center");
			}
		}
	}
}