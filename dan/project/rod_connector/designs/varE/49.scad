

difference() {
	difference() {
		difference() {
			hull() {
				union() {
					union() {
						rotate(a = -38.8890474236, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [44.9756473265, 13.2000000000, 1]);
							}
						}
						rotate(a = 142.9398037102, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [43.2092376299, 13.2000000000, 1]);
							}
						}
						rotate(a = 42.8526075503, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [44.9756475134, 13.2000000000, 1]);
							}
						}
						rotate(a = 87.6032088779, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [38.3300699748, 13.2000000000, 1]);
							}
						}
						rotate(a = -86.0937287637, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [43.6938412066, 13.2000000000, 1]);
							}
						}
						rotate(a = -142.0914045035, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [44.9756470965, 13.2000000000, 1]);
							}
						}
					}
					translate(v = [0, 0, 11.0802595229]) {
						intersection() {
							hull() {
								rotate(a = 91.8850474945, v = [0.6274744909, 0.7779419805, -0.0000014054]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 73.7818655431, v = [-0.5786710397, -0.7662467707, 0.0000013449]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 91.8849679141, v = [-0.6797466878, 0.7327090101, -0.0000000530]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 58.4056704063, v = [-0.8510336500, 0.0356206300, 0.0000008154]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 76.1616661654, v = [0.9687187484, 0.0661468868, -0.0000010349]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 91.8851454324, v = [0.6140710382, -0.7885649050, 0.0000001745]) {
									cylinder(h = 45, r = 9.6000000000);
								}
							}
							sphere(r = 45);
						}
					}
				}
			}
			translate(v = [0, 0, 11.0802595229]) {
				rotate(a = 91.8850474945, v = [0.6274744909, 0.7779419805, -0.0000014054]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 73.7818655431, v = [-0.5786710397, -0.7662467707, 0.0000013449]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 91.8849679141, v = [-0.6797466878, 0.7327090101, -0.0000000530]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 58.4056704063, v = [-0.8510336500, 0.0356206300, 0.0000008154]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 76.1616661654, v = [0.9687187484, 0.0661468868, -0.0000010349]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 91.8851454324, v = [0.6140710382, -0.7885649050, 0.0000001745]) {
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
				text(halign = "center", size = 8, text = "49", valign = "center");
			}
		}
	}
}