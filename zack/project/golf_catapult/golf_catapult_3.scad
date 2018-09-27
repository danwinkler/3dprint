

union() {
	scale(v = [0.5000000000, 1.5000000000, 1]) {
		union() {
			union() {
				union() {
					cube(size = [9, 9, 2]);
					translate(v = [8, 8, -0.5000000000]) {
						scale(v = 1) {
							translate(v = [-0.5000000000, -0.5000000000]) {
								cube();
							}
						}
					}
				}
				mirror(v = [1, 0, 0]) {
					union() {
						cube(size = [9, 9, 2]);
						translate(v = [8, 8, -0.5000000000]) {
							scale(v = 1) {
								translate(v = [-0.5000000000, -0.5000000000]) {
									cube();
								}
							}
						}
					}
				}
			}
			mirror(v = [0, 1, 0]) {
				union() {
					union() {
						cube(size = [9, 9, 2]);
						translate(v = [8, 8, -0.5000000000]) {
							scale(v = 1) {
								translate(v = [-0.5000000000, -0.5000000000]) {
									cube();
								}
							}
						}
					}
					mirror(v = [1, 0, 0]) {
						union() {
							cube(size = [9, 9, 2]);
							translate(v = [8, 8, -0.5000000000]) {
								scale(v = 1) {
									translate(v = [-0.5000000000, -0.5000000000]) {
										cube();
									}
								}
							}
						}
					}
				}
			}
		}
	}
	translate(v = [20, 0]) {
		scale(v = [0.5000000000, 1.5000000000, 1]) {
			union() {
				union() {
					difference() {
						cube(size = [9, 9, 2]);
						translate(v = [8, 8, -0.5000000000]) {
							scale(v = 1.2000000000) {
								translate(v = [-0.5000000000, -0.5000000000]) {
									cube();
								}
							}
						}
					}
					mirror(v = [1, 0, 0]) {
						difference() {
							cube(size = [9, 9, 2]);
							translate(v = [8, 8, -0.5000000000]) {
								scale(v = 1.2000000000) {
									translate(v = [-0.5000000000, -0.5000000000]) {
										cube();
									}
								}
							}
						}
					}
				}
				mirror(v = [0, 1, 0]) {
					union() {
						difference() {
							cube(size = [9, 9, 2]);
							translate(v = [8, 8, -0.5000000000]) {
								scale(v = 1.2000000000) {
									translate(v = [-0.5000000000, -0.5000000000]) {
										cube();
									}
								}
							}
						}
						mirror(v = [1, 0, 0]) {
							difference() {
								cube(size = [9, 9, 2]);
								translate(v = [8, 8, -0.5000000000]) {
									scale(v = 1.2000000000) {
										translate(v = [-0.5000000000, -0.5000000000]) {
											cube();
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
}