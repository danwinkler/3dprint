

difference() {
	difference() {
		hull() {
			union() {
				union() {
					rotate(a = 97.1950566804, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [19.3009372118, 13.2000000000, 1]);
						}
					}
					rotate(a = 19.7777053336, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [43.8199273245, 13.2000000000, 1]);
						}
					}
					rotate(a = 123.1991320678, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.5633959204, 13.2000000000, 1]);
						}
					}
					rotate(a = 54.4622963327, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [45.0000000000, 13.2000000000, 1]);
						}
					}
					rotate(a = -75.6891168842, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [9.6738172659, 13.2000000000, 1]);
						}
					}
					rotate(a = -44.7840800588, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [45.0000000000, 13.2000000000, 1]);
						}
					}
				}
				translate(v = [0, 0, 9.6000000000]) {
					intersection() {
						hull() {
							rotate(a = 25.3983381831, v = [-0.4255313676, -0.0537208314, 0.0000004793]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 76.8495128920, v = [-0.3294981494, 0.9163353195, -0.0000005868]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 82.0121861809, v = [-0.8286538394, -0.5422381801, 0.0000013709]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 89.9999120814, v = [-0.8137332087, 0.5812385612, 0.0000002325]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 12.4140267006, v = [0.2083038007, 0.0531368865, -0.0000002614]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 89.9999996641, v = [0.7044370247, 0.7097664956, -0.0000014142]) {
								cylinder(h = 45, r = 9.6000000000);
							}
						}
						sphere(r = 45);
					}
				}
			}
		}
		translate(v = [0, 0, 9.6000000000]) {
			rotate(a = 25.3983381831, v = [-0.4255313676, -0.0537208314, 0.0000004793]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 76.8495128920, v = [-0.3294981494, 0.9163353195, -0.0000005868]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 82.0121861809, v = [-0.8286538394, -0.5422381801, 0.0000013709]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 89.9999120814, v = [-0.8137332087, 0.5812385612, 0.0000002325]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 12.4140267006, v = [0.2083038007, 0.0531368865, -0.0000002614]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 89.9999996641, v = [0.7044370247, 0.7097664956, -0.0000014142]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
		}
	}
	translate(v = [0, 0, 2]) {
		rotate(a = 180, v = [0, 1, 0]) {
			linear_extrude(height = 3) {
				text(halign = "center", size = 8, text = "8", valign = "center");
			}
		}
	}
}