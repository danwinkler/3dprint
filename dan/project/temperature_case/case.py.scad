

difference(){
	union() {
		scale(v = 25.4000000000) {
			union() {
				difference() {
					difference() {
						difference() {
							minkowski() {
								translate(v = [0.1000000000, 0.1000000000, 0.1000000000]) {
									cube(size = [2.7000000000, 1.5000000000, 1.4000000000]);
								}
								sphere($fn = 12, r = 0.1000000000);
							}
							translate(v = [0.1000000000, 0.1000000000, 0.1000000000]) {
								cube(size = [2.7000000000, 1.5000000000, 1.6000000000]);
							}
						}
						translate(v = [0, 0, 1.4000000000]) {
							cube(size = [2.9000000000, 1.7000000000, 0.2000000000]);
						}
					}
					translate(v = [0.6500000000, 1.5900000000, 0.6000000000]) {
						cube(size = [0.5000000000, 0.1200000000, 1]);
					}
				}
				translate(v = [0.6000000000, 0.1500000000, 0.1000000000]) {
					translate(v = [0.4500000000, 0.1000000000, 0]) {
						union() {
							cube(size = [0.1000000000, 1.2000000000, 0.2500000000]);
							translate(v = [0.0300000000, 0.0300000000, 0]) {
							}
							translate(v = [0.0300000000, 0.1300000000, 0]) {
							}
							translate(v = [0.0300000000, 0.2300000000, 0]) {
							}
							translate(v = [0.0300000000, 0.3300000000, 0]) {
							}
							translate(v = [0.0300000000, 0.4300000000, 0]) {
							}
							translate(v = [0.0300000000, 0.5300000000, 0]) {
							}
							translate(v = [0.0300000000, 0.6300000000, 0]) {
							}
							translate(v = [0.0300000000, 0.7300000000, 0]) {
							}
							translate(v = [0.0300000000, 0.8300000000, 0]) {
							}
							translate(v = [0.0300000000, 0.9300000000, 0]) {
							}
							translate(v = [0.0300000000, 1.0300000000, 0]) {
							}
							translate(v = [0.0300000000, 1.1300000000, 0]) {
							}
						}
					}
					translate(v = [1.1500000000, 0.1000000000, 0]) {
						union() {
							cube(size = [0.1000000000, 1.2000000000, 0.2500000000]);
							translate(v = [0.0300000000, 0.0300000000, 0]) {
							}
							translate(v = [0.0300000000, 0.1300000000, 0]) {
							}
							translate(v = [0.0300000000, 0.2300000000, 0]) {
							}
							translate(v = [0.0300000000, 0.3300000000, 0]) {
							}
							translate(v = [0.0300000000, 0.4300000000, 0]) {
							}
							translate(v = [0.0300000000, 0.5300000000, 0]) {
							}
							translate(v = [0.0300000000, 0.6300000000, 0]) {
							}
							translate(v = [0.0300000000, 0.7300000000, 0]) {
							}
							translate(v = [0.0300000000, 0.8300000000, 0]) {
							}
							translate(v = [0.0300000000, 0.9300000000, 0]) {
							}
							translate(v = [0.0300000000, 1.0300000000, 0]) {
							}
							translate(v = [0.0300000000, 1.1300000000, 0]) {
							}
						}
					}
				}
				translate(v = [0.6000000000, 0.1500000000, 0.1000000000]) {
					translate(v = [0.1000000000, 0.1000000000, 0]) {
						difference() {
							union() {
								translate(v = [-0.6000000000, -0.1500000000, 0]) {
									cube(size = [0.7000000000, 0.1500000000, 0.3750000000]);
									cube(size = [0.6000000000, 0.2500000000, 0.3750000000]);
								}
								cylinder($fn = 24, h = 0.3750000000, r = 0.1000000000);
							}
							cylinder($fn = 24, h = 0.4750000000, r = 0.0550000000);
						}
					}
					translate(v = [1.6000000000, 0.1000000000, 0]) {
						scale(v = [-1, 1, 1]) {
							difference() {
								union() {
									translate(v = [-0.6000000000, -0.1500000000, 0]) {
										cube(size = [0.7000000000, 0.1500000000, 0.3750000000]);
										cube(size = [0.6000000000, 0.2500000000, 0.3750000000]);
									}
									cylinder($fn = 24, h = 0.3750000000, r = 0.1000000000);
								}
								cylinder($fn = 24, h = 0.4750000000, r = 0.0550000000);
							}
						}
					}
					translate(v = [1.6000000000, 1.3000000000, 0]) {
						scale(v = [-1, -1, 1]) {
							difference() {
								union() {
									translate(v = [-0.6000000000, -0.1500000000, 0]) {
										cube(size = [0.7000000000, 0.1500000000, 0.3750000000]);
										cube(size = [0.6000000000, 0.2500000000, 0.3750000000]);
									}
									cylinder($fn = 24, h = 0.3750000000, r = 0.1000000000);
								}
								cylinder($fn = 24, h = 0.4750000000, r = 0.0550000000);
							}
						}
					}
					translate(v = [0.1000000000, 1.3000000000, 0]) {
						scale(v = [1, -1, 1]) {
							difference() {
								union() {
									translate(v = [-0.6000000000, -0.1500000000, 0]) {
										cube(size = [0.7000000000, 0.1500000000, 0.3750000000]);
										cube(size = [0.6000000000, 0.2500000000, 0.3750000000]);
									}
									cylinder($fn = 24, h = 0.3750000000, r = 0.1000000000);
								}
								cylinder($fn = 24, h = 0.4750000000, r = 0.0550000000);
							}
						}
					}
				}
				translate(v = [0.1000000000, 0.1000000000, 0.1000000000]) {
					translate(v = [0.1000000000, 0.1000000000, 0]) {
						union() {
							union() {
								translate(v = [-0.1500000000, -0.1500000000, 0]) {
									cube(size = [0.2500000000, 0.1500000000, 1.0000000000]);
									cube(size = [0.1500000000, 0.2500000000, 1.0000000000]);
								}
								cylinder($fn = 24, h = 1.0000000000, r = 0.1000000000);
							}
						}
					}
					translate(v = [2.6000000000, 0.1000000000, 0]) {
						scale(v = [-1, 1, 1]) {
							union() {
								union() {
									translate(v = [-0.1500000000, -0.1500000000, 0]) {
										cube(size = [0.2500000000, 0.1500000000, 1.0000000000]);
										cube(size = [0.1500000000, 0.2500000000, 1.0000000000]);
									}
									cylinder($fn = 24, h = 1.0000000000, r = 0.1000000000);
								}
							}
						}
					}
					translate(v = [2.6000000000, 1.4000000000, 0]) {
						scale(v = [-1, -1, 1]) {
							union() {
								union() {
									translate(v = [-0.1500000000, -0.1500000000, 0]) {
										cube(size = [0.2500000000, 0.1500000000, 1.0000000000]);
										cube(size = [0.1500000000, 0.2500000000, 1.0000000000]);
									}
									cylinder($fn = 24, h = 1.0000000000, r = 0.1000000000);
								}
							}
						}
					}
					translate(v = [0.1000000000, 1.4000000000, 0]) {
						scale(v = [1, -1, 1]) {
							union() {
								union() {
									translate(v = [-0.1500000000, -0.1500000000, 0]) {
										cube(size = [0.2500000000, 0.1500000000, 1.0000000000]);
										cube(size = [0.1500000000, 0.2500000000, 1.0000000000]);
									}
									cylinder($fn = 24, h = 1.0000000000, r = 0.1000000000);
								}
							}
						}
					}
				}
				translate(v = [0.1000000000, 0.1000000000, 0.1000000000]) {
					translate(v = [2.7000000000, 0, 0]) {
					}
				}
				translate(v = [0.5500000000, 1.7000000000, 0.5000000000]) {
					union() {
						union() {
							difference() {
								hull() {
									cube(size = [1.8000000000, 0.2000000000, 0.1000000000]);
									translate(v = [0, -0.0100000000, -0.4000000000]) {
										cube(size = [1.8000000000, 0.0100000000, 0.0100000000]);
									}
								}
								translate(v = [0.6000000000, 0, 0]) {
									cube(size = [1.0200000000, 0.0625000000, 0.2000000000]);
								}
							}
							translate() {
								cube(size = [0.1000000000, 0.2000000000, 0.9000000000]);
							}
						}
						translate(v = [1.7000000000, 0, 0]) {
							cube(size = [0.1000000000, 0.2000000000, 0.9000000000]);
						}
					}
				}
			}
		}
	}
	/* Holes Below*/
	union(){
		scale(v = 25.4000000000){
			union(){
				translate(v = [0.6000000000, 0.1500000000, 0.1000000000]){
					translate(v = [0.4500000000, 0.1000000000, 0]){
						union(){
							translate(v = [0.0300000000, 0.0300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 0.1300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 0.2300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 0.3300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 0.4300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 0.5300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 0.6300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 0.7300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 0.8300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 0.9300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 1.0300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 1.1300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
						}
					}
					translate(v = [1.1500000000, 0.1000000000, 0]){
						union(){
							translate(v = [0.0300000000, 0.0300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 0.1300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 0.2300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 0.3300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 0.4300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 0.5300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 0.6300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 0.7300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 0.8300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 0.9300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 1.0300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
							translate(v = [0.0300000000, 1.1300000000, 0]){
								cube(size = [0.0400000000, 0.0400000000, 0.2510000000]);
							}
						}
					}
				}
				translate(v = [0.1000000000, 0.1000000000, 0.1000000000]){
					translate(v = [0.1000000000, 0.1000000000, 0]){
						union(){
							cylinder($fn = 24, h = 1.1000000000, r = 0.0550000000);
						}
					}
					translate(v = [2.6000000000, 0.1000000000, 0]){
						scale(v = [-1, 1, 1]){
							union(){
								cylinder($fn = 24, h = 1.1000000000, r = 0.0550000000);
							}
						}
					}
					translate(v = [2.6000000000, 1.4000000000, 0]){
						scale(v = [-1, -1, 1]){
							union(){
								cylinder($fn = 24, h = 1.1000000000, r = 0.0550000000);
							}
						}
					}
					translate(v = [0.1000000000, 1.4000000000, 0]){
						scale(v = [1, -1, 1]){
							union(){
								cylinder($fn = 24, h = 1.1000000000, r = 0.0550000000);
							}
						}
					}
				}
				translate(v = [1.4500000000, -0.1000000000, 1]) {
					rotate(a = -90, v = [1, 0, 0]) {
						cylinder($fn = 24, h = 0.3000000000, r = 0.2500000000);
					}
				}
				translate(v = [0.1000000000, 0.1000000000, 0.1000000000]){
					translate(v = [-0.2000000000, 0.4500000000, 0.2000000000]) {
						minkowski() {
							cube(size = [0.3000000000, 0.0400000000, 0.7000000000]);
							rotate(a = 90, v = [0, 1, 0]) {
								cylinder($fn = 12, h = 0.0010000000, r = 0.0300000000);
							}
						}
					}
					translate(v = [-0.2000000000, 0.6500000000, 0.2000000000]) {
						minkowski() {
							cube(size = [0.3000000000, 0.0400000000, 0.7000000000]);
							rotate(a = 90, v = [0, 1, 0]) {
								cylinder($fn = 12, h = 0.0010000000, r = 0.0300000000);
							}
						}
					}
					translate(v = [-0.2000000000, 0.8500000000, 0.2000000000]) {
						minkowski() {
							cube(size = [0.3000000000, 0.0400000000, 0.7000000000]);
							rotate(a = 90, v = [0, 1, 0]) {
								cylinder($fn = 12, h = 0.0010000000, r = 0.0300000000);
							}
						}
					}
					translate(v = [-0.2000000000, 1.0500000000, 0.2000000000]) {
						minkowski() {
							cube(size = [0.3000000000, 0.0400000000, 0.7000000000]);
							rotate(a = 90, v = [0, 1, 0]) {
								cylinder($fn = 12, h = 0.0010000000, r = 0.0300000000);
							}
						}
					}
					translate(v = [2.7000000000, 0, 0]){
						translate(v = [-0.2000000000, 0.4500000000, 0.2000000000]) {
							minkowski() {
								cube(size = [0.3000000000, 0.0400000000, 0.7000000000]);
								rotate(a = 90, v = [0, 1, 0]) {
									cylinder($fn = 12, h = 0.0010000000, r = 0.0300000000);
								}
							}
						}
						translate(v = [-0.2000000000, 0.6500000000, 0.2000000000]) {
							minkowski() {
								cube(size = [0.3000000000, 0.0400000000, 0.7000000000]);
								rotate(a = 90, v = [0, 1, 0]) {
									cylinder($fn = 12, h = 0.0010000000, r = 0.0300000000);
								}
							}
						}
						translate(v = [-0.2000000000, 0.8500000000, 0.2000000000]) {
							minkowski() {
								cube(size = [0.3000000000, 0.0400000000, 0.7000000000]);
								rotate(a = 90, v = [0, 1, 0]) {
									cylinder($fn = 12, h = 0.0010000000, r = 0.0300000000);
								}
							}
						}
						translate(v = [-0.2000000000, 1.0500000000, 0.2000000000]) {
							minkowski() {
								cube(size = [0.3000000000, 0.0400000000, 0.7000000000]);
								rotate(a = 90, v = [0, 1, 0]) {
									cylinder($fn = 12, h = 0.0010000000, r = 0.0300000000);
								}
							}
						}
					}
				}
			}
		}
	} /* End Holes */ 
}