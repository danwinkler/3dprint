

difference() {
	difference() {
		hull() {
			union() {
				union() {
					rotate(a = 118.5190809644, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.9051042603, 13.2000000000, 1]);
						}
					}
					rotate(a = -61.8702837395, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.9999999812, 13.2000000000, 1]);
						}
					}
					rotate(a = -169.0667888368, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.9051038009, 13.2000000000, 1]);
						}
					}
					rotate(a = -105.3856022510, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [42.0785265703, 13.2000000000, 1]);
						}
					}
					rotate(a = 75.8877702221, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [43.5626199564, 13.2000000000, 1]);
						}
					}
					rotate(a = 6.5627499058, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.9051044666, 13.2000000000, 1]);
						}
					}
				}
				translate(v = [0, 0, 12.5208760080]) {
					intersection() {
						hull() {
							rotate(a = 93.7215889021, v = [-0.8768053135, -0.4764444908, 0.0000013532]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 90.0016795434, v = [0.8818824583, 0.4714693298, -0.0000013534]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 93.7216880234, v = [0.1892645674, -0.9797783474, 0.0000007905]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 69.2408800157, v = [0.9015674822, -0.2480895902, -0.0000006535]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 75.4794823209, v = [-0.9388419672, 0.2360336654, 0.0000007028]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 93.7215443727, v = [-0.1140503467, 0.9913523741, -0.0000008773]) {
								cylinder(h = 45, r = 9.6000000000);
							}
						}
						sphere(r = 45);
					}
				}
			}
		}
		translate(v = [0, 0, 12.5208760080]) {
			rotate(a = 93.7215889021, v = [-0.8768053135, -0.4764444908, 0.0000013532]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 90.0016795434, v = [0.8818824583, 0.4714693298, -0.0000013534]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 93.7216880234, v = [0.1892645674, -0.9797783474, 0.0000007905]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 69.2408800157, v = [0.9015674822, -0.2480895902, -0.0000006535]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 75.4794823209, v = [-0.9388419672, 0.2360336654, 0.0000007028]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 93.7215443727, v = [-0.1140503467, 0.9913523741, -0.0000008773]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
		}
	}
	translate(v = [0, 0, 2]) {
		rotate(a = 180, v = [0, 1, 0]) {
			linear_extrude(height = 3) {
				text(halign = "center", size = 8, text = "29", valign = "center");
			}
		}
	}
}