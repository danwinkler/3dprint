

difference() {
	difference() {
		hull() {
			union() {
				union() {
					rotate(a = -142.8049439380, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [19.3009464314, 13.2000000000, 1]);
						}
					}
					rotate(a = 139.7777185746, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [43.8199287549, 13.2000000000, 1]);
						}
					}
					rotate(a = -116.8008588526, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.5633969413, 13.2000000000, 1]);
						}
					}
					rotate(a = 174.4623068804, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [45.0000000000, 13.2000000000, 1]);
						}
					}
					rotate(a = 44.3109248765, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [9.6738078791, 13.2000000000, 1]);
						}
					}
					rotate(a = 75.2159304890, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [45.0000000000, 13.2000000000, 1]);
						}
					}
				}
				translate(v = [0, 0, 9.6000040447]) {
					intersection() {
						hull() {
							rotate(a = 25.3984811239, v = [0.2592899814, -0.3416628621, 0.0000000824]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 76.8496009494, v = [-0.6288202949, -0.7435221355, 0.0000013723]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 82.0122890819, v = [0.8839191377, -0.4465163847, -0.0000004374]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 90.0000566492, v = [-0.0965005721, -0.9953329290, 0.0000010918]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 12.4138920847, v = [-0.1501691412, 0.1538253704, -0.0000000037]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 89.9999229785, v = [-0.9668943752, 0.2551769330, 0.0000007117]) {
								cylinder(h = 45, r = 9.6000000000);
							}
						}
						sphere(r = 45);
					}
				}
			}
		}
		translate(v = [0, 0, 9.6000040447]) {
			rotate(a = 25.3984811239, v = [0.2592899814, -0.3416628621, 0.0000000824]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 76.8496009494, v = [-0.6288202949, -0.7435221355, 0.0000013723]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 82.0122890819, v = [0.8839191377, -0.4465163847, -0.0000004374]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 90.0000566492, v = [-0.0965005721, -0.9953329290, 0.0000010918]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 12.4138920847, v = [-0.1501691412, 0.1538253704, -0.0000000037]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 89.9999229785, v = [-0.9668943752, 0.2551769330, 0.0000007117]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
		}
	}
	translate(v = [0, 0, 2]) {
		rotate(a = 180, v = [0, 1, 0]) {
			linear_extrude(height = 3) {
				text(halign = "center", size = 8, text = "10", valign = "center");
			}
		}
	}
}