

difference() {
	difference() {
		difference() {
			hull() {
				union() {
					union() {
						rotate(a = -59.1095269439, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [44.9612278551, 13.2000000000, 1]);
							}
						}
						rotate(a = 121.9900777399, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [44.1252756264, 13.2000000000, 1]);
							}
						}
						rotate(a = 20.2072379594, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [44.9612281593, 13.2000000000, 1]);
							}
						}
						rotate(a = 70.3834074282, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [39.4251636269, 13.2000000000, 1]);
							}
						}
						rotate(a = -105.2734091059, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [43.6517678521, 13.2000000000, 1]);
							}
						}
						rotate(a = -164.6529217853, v = [0, 0, 1]) {
							translate(v = [0, -6.6000000000, 0]) {
								cube(size = [44.9612276900, 13.2000000000, 1]);
							}
						}
					}
					translate(v = [0, 0, 11.4676200387]) {
						intersection() {
							hull() {
								rotate(a = 92.3786255560, v = [0.8574108572, 0.5129562645, -0.0000013704]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 78.6845011643, v = [-0.8316532432, -0.5194747058, 0.0000013511]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 92.3785229118, v = [-0.3451191842, 0.9376408719, -0.0000005925]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 61.1771081686, v = [-0.8252648002, 0.2941325902, 0.0000005311]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 75.9394645667, v = [0.9357775253, -0.2555332024, -0.0000006802]) {
									cylinder(h = 45, r = 9.6000000000);
								}
								rotate(a = 92.3786812865, v = [0.2644374294, -0.9635093526, 0.0000006991]) {
									cylinder(h = 45, r = 9.6000000000);
								}
							}
							sphere(r = 45);
						}
					}
				}
			}
			translate(v = [0, 0, 11.4676200387]) {
				rotate(a = 92.3786255560, v = [0.8574108572, 0.5129562645, -0.0000013704]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 78.6845011643, v = [-0.8316532432, -0.5194747058, 0.0000013511]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 92.3785229118, v = [-0.3451191842, 0.9376408719, -0.0000005925]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 61.1771081686, v = [-0.8252648002, 0.2941325902, 0.0000005311]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 75.9394645667, v = [0.9357775253, -0.2555332024, -0.0000006802]) {
					translate(v = [0, 0, 20]) {
						cylinder(h = 45, r = 6.6000000000);
					}
				}
				rotate(a = 92.3786812865, v = [0.2644374294, -0.9635093526, 0.0000006991]) {
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
				text(halign = "center", size = 8, text = "43", valign = "center");
			}
		}
	}
}