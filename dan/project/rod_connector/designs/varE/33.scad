

difference() {
	difference() {
		difference() {
			hull() {
				union() {
					union() {
						rotate(a = 19.5495464057, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [44.9255356687, 13.2000000000, 1]);
							}
						}
						rotate(a = -160.4504535943, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [44.9255356687, 13.2000000000, 1]);
							}
						}
						rotate(a = 94.1959762278, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [44.9255355774, 13.2000000000, 1]);
							}
						}
						rotate(a = 153.7468111430, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [41.3098897056, 13.2000000000, 1]);
							}
						}
						rotate(a = -24.3045769617, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [43.5859585651, 13.2000000000, 1]);
							}
						}
						rotate(a = -90.3680568440, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [44.9255350778, 13.2000000000, 1]);
							}
						}
					}
					translate(v = [0, 0, 12.1877206129]) {
						intersection() {
							hull() {
								rotate(a = 93.2965205497, v = [-0.3340682192, 0.9407931675, -0.0000006067]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 86.7034794503, v = [0.3340682192, -0.9407931675, 0.0000006067]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 93.2965427865, v = [-0.9956693461, -0.0730470239, 0.0000010687]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 66.6350969393, v = [-0.4060653595, -0.8233047763, 0.0000012294]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 75.5985190257, v = [0.3986540494, 0.8827320296, -0.0000012814]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 93.2966644603, v = [0.9983245680, -0.0064130722, -0.0000009919]) {
									cylinder(h = 45, r = 9.6000000000);
								}
							}
							sphere(r = 45);
						}
					}
				}
			}
			translate(v = [0, 0, 12.1877206129]) {
				rotate(a = 93.2965205497, v = [-0.3340682192, 0.9407931675, -0.0000006067]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 86.7034794503, v = [0.3340682192, -0.9407931675, 0.0000006067]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 93.2965427865, v = [-0.9956693461, -0.0730470239, 0.0000010687]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 66.6350969393, v = [-0.4060653595, -0.8233047763, 0.0000012294]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 75.5985190257, v = [0.3986540494, 0.8827320296, -0.0000012814]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 93.2966644603, v = [0.9983245680, -0.0064130722, -0.0000009919]) {
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
				text(halign = "center", size = 8, text = "33", valign = "center");
			}
		}
	}
}