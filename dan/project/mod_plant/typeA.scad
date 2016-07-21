

union() {
	union() {
		union() {
			union() {
				difference() {
					union() {
						cylinder(h = 150, r = 5);
						translate(v = [0, 0, 150]) {
							cylinder($fn = 36, h = 8, r = 2.5000000000);
						}
					}
					cylinder($fn = 36, h = 10, r = 2.5000000000);
				}
				translate(v = [0, 0, 15]) {
					rotate(a = 0, v = [0, 0, 1]) {
						rotate(a = 45, v = [0, 1, 0]) {
							union() {
								cylinder(h = 40, r = 5);
								translate(v = [0, 0, 40]) {
									cylinder($fn = 36, h = 8, r = 2.5000000000);
								}
							}
						}
					}
				}
			}
			translate(v = [0, 0, 45]) {
				rotate(a = 180, v = [0, 0, 1]) {
					rotate(a = 45, v = [0, 1, 0]) {
						union() {
							cylinder(h = 40, r = 5);
							translate(v = [0, 0, 40]) {
								cylinder($fn = 36, h = 8, r = 2.5000000000);
							}
						}
					}
				}
			}
		}
		translate(v = [0, 0, 75]) {
			rotate(a = 0, v = [0, 0, 1]) {
				rotate(a = 45, v = [0, 1, 0]) {
					union() {
						cylinder(h = 40, r = 5);
						translate(v = [0, 0, 40]) {
							cylinder($fn = 36, h = 8, r = 2.5000000000);
						}
					}
				}
			}
		}
	}
	translate(v = [0, 0, 105]) {
		rotate(a = 180, v = [0, 0, 1]) {
			rotate(a = 45, v = [0, 1, 0]) {
				union() {
					cylinder(h = 40, r = 5);
					translate(v = [0, 0, 40]) {
						cylinder($fn = 36, h = 8, r = 2.5000000000);
					}
				}
			}
		}
	}
}