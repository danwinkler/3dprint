

difference() {
	difference() {
		hull() {
			union() {
				union() {
					rotate(a = 131.0021079645, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [43.4613087120, 13.2000000000, 1]);
						}
					}
					rotate(a = 171.6103322766, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [15.7860078426, 13.2000000000, 1]);
						}
					}
					rotate(a = 66.3006273748, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [45.0000000000, 13.2000000000, 1]);
						}
					}
					rotate(a = 171.3968776740, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [45.0000000000, 13.2000000000, 1]);
						}
					}
					rotate(a = -120.3103406068, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.1978347601, 13.2000000000, 1]);
						}
					}
				}
				translate(v = [0, 0, 9.6000000000]) {
					intersection() {
						hull() {
							rotate(a = 74.9736809283, v = [-0.7288801186, -0.6336533868, 0.0000013625]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 20.5363134754, v = [-0.0511824327, -0.3470470789, 0.0000003982]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 89.9999169575, v = [-0.9156669945, 0.4019377503, 0.0000005137]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 90.0000528883, v = [-0.1495892254, -0.9887482307, 0.0000011383]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 79.1655365112, v = [0.8479154942, -0.4956871936, -0.0000003522]) {
								cylinder(h = 45, r = 9.6000000000);
							}
						}
						sphere(r = 45);
					}
				}
			}
		}
		translate(v = [0, 0, 9.6000000000]) {
			rotate(a = 74.9736809283, v = [-0.7288801186, -0.6336533868, 0.0000013625]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 20.5363134754, v = [-0.0511824327, -0.3470470789, 0.0000003982]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 89.9999169575, v = [-0.9156669945, 0.4019377503, 0.0000005137]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 90.0000528883, v = [-0.1495892254, -0.9887482307, 0.0000011383]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 79.1655365112, v = [0.8479154942, -0.4956871936, -0.0000003522]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
		}
	}
	translate(v = [0, 0, 2]) {
		rotate(a = 180, v = [0, 1, 0]) {
			linear_extrude(height = 3) {
				text(halign = "center", size = 8, text = "34", valign = "center");
			}
		}
	}
}