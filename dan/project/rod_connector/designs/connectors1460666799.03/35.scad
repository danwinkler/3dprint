

difference() {
	intersection() {
		hull() {
			rotate(a = -118.9051365199, v = [0.4336068963, -0.7604915073, 0.0000000000]) {
				rotate(a = -90.0000000000, v = [-0.1305261922, -0.9914448614, 0.0000000000]) {
					cylinder(h = 60, r = 16.2000000000);
				}
			}
			rotate(a = -118.9051365199, v = [0.4336068963, -0.7604915073, 0.0000000000]) {
				rotate(a = -90.0000000000, v = [0.9238795325, 0.3826834324, -0.0000000000]) {
					cylinder(h = 60, r = 16.2000000000);
				}
			}
			rotate(a = -118.9051365199, v = [0.4336068963, -0.7604915073, 0.0000000000]) {
				rotate(a = -24.0657434263, v = [-0.0956376174, -0.3964110704, 0.0000000000]) {
					cylinder(h = 60, r = 16.2000000000);
				}
			}
			rotate(a = -118.9051365199, v = [0.4336068963, -0.7604915073, 0.0000000000]) {
				rotate(a = -141.7661142776, v = [-0.2679213795, -0.5578727405, 0.0000000000]) {
					cylinder(h = 60, r = 16.2000000000);
				}
			}
			rotate(a = -118.9051365199, v = [0.4336068963, -0.7604915073, 0.0000000000]) {
				rotate(a = -154.1384175201, v = [0.2629773042, 0.3480116253, -0.0000000000]) {
					cylinder(h = 60, r = 16.2000000000);
				}
			}
		}
		sphere(r = 60);
	}
	union() {
		rotate(a = -118.9051365199, v = [0.4336068963, -0.7604915073, 0.0000000000]) {
			rotate(a = -90.0000000000, v = [-0.1305261922, -0.9914448614, 0.0000000000]) {
				translate(v = [0, 0, 35]) {
					cylinder(h = 100, r = 13.2000000000);
				}
			}
		}
		rotate(a = -118.9051365199, v = [0.4336068963, -0.7604915073, 0.0000000000]) {
			rotate(a = -90.0000000000, v = [0.9238795325, 0.3826834324, -0.0000000000]) {
				translate(v = [0, 0, 35]) {
					cylinder(h = 100, r = 13.2000000000);
				}
			}
		}
		rotate(a = -118.9051365199, v = [0.4336068963, -0.7604915073, 0.0000000000]) {
			rotate(a = -24.0657434263, v = [-0.0956376174, -0.3964110704, 0.0000000000]) {
				translate(v = [0, 0, 35]) {
					cylinder(h = 100, r = 13.2000000000);
				}
			}
		}
		rotate(a = -118.9051365199, v = [0.4336068963, -0.7604915073, 0.0000000000]) {
			rotate(a = -141.7661142776, v = [-0.2679213795, -0.5578727405, 0.0000000000]) {
				translate(v = [0, 0, 35]) {
					cylinder(h = 100, r = 13.2000000000);
				}
			}
		}
		rotate(a = -118.9051365199, v = [0.4336068963, -0.7604915073, 0.0000000000]) {
			rotate(a = -154.1384175201, v = [0.2629773042, 0.3480116253, -0.0000000000]) {
				translate(v = [0, 0, 35]) {
					cylinder(h = 100, r = 13.2000000000);
				}
			}
		}
	}
}