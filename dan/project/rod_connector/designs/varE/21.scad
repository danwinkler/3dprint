

difference() {
	difference() {
		hull() {
			union() {
				union() {
					rotate(a = -22.7032137393, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.8834473252, 13.2000000000, 1]);
						}
					}
					rotate(a = 156.6117949407, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.9415063774, 13.2000000000, 1]);
						}
					}
					rotate(a = 47.5515196212, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.8834476089, 13.2000000000, 1]);
						}
					}
					rotate(a = 115.0783958010, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [42.7336050371, 13.2000000000, 1]);
						}
					}
					rotate(a = -64.0908088880, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [43.5454561665, 13.2000000000, 1]);
						}
					}
					rotate(a = -136.6039430228, v = [0, 0, 1]) {
						translate(v = [0, -6.6000000000, 0]) {
							cube(size = [44.8834466940, 13.2000000000, 1]);
						}
					}
				}
				translate(v = [0, 0, 12.8366280766]) {
					intersection() {
						hull() {
							rotate(a = 94.1246114265, v = [0.3849580616, 0.9201271419, -0.0000013051]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 92.9217101120, v = [-0.3964430133, -0.9166432552, 0.0000013131]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 94.1245562003, v = [-0.7359734324, 0.6731789595, 0.0000000628]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 71.7383656861, v = [-0.8601119511, -0.4025109262, 0.0000012626]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 75.3926712915, v = [0.8704136325, 0.4228223392, -0.0000012932]) {
								cylinder(h = 45, r = 9.6000000000);
							}
							rotate(a = 94.1247343397, v = [0.6852579577, -0.7247398776, 0.0000000395]) {
								cylinder(h = 45, r = 9.6000000000);
							}
						}
						sphere(r = 45);
					}
				}
			}
		}
		translate(v = [0, 0, 12.8366280766]) {
			rotate(a = 94.1246114265, v = [0.3849580616, 0.9201271419, -0.0000013051]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 92.9217101120, v = [-0.3964430133, -0.9166432552, 0.0000013131]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 94.1245562003, v = [-0.7359734324, 0.6731789595, 0.0000000628]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 71.7383656861, v = [-0.8601119511, -0.4025109262, 0.0000012626]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 75.3926712915, v = [0.8704136325, 0.4228223392, -0.0000012932]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
			rotate(a = 94.1247343397, v = [0.6852579577, -0.7247398776, 0.0000000395]) {
				translate(v = [0, 0, 20]) {
					cylinder(h = 45, r = 6.6000000000);
				}
			}
		}
	}
	translate(v = [0, 0, 2]) {
		rotate(a = 180, v = [0, 1, 0]) {
			linear_extrude(height = 3) {
				text(halign = "center", size = 8, text = "21", valign = "center");
			}
		}
	}
}