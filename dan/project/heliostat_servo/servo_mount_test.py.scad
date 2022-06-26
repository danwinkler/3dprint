

union() {
	union() {
		rotate(a = 0.0000000000, v = [0, 0, 1]) {
			union() {
				translate(v = [0, 4.5000000000, 0]) {
					cube(size = [69.2500000000, 15, 3]);
				}
				translate(v = [30.7500000000, 12, 0]) {
					union() {
						difference() {
							cube(size = [5.3000000000, 5, 15.5000000000]);
							translate(v = [2.6500000000, 0, 9.2500000000]) {
								rotate(a = -90, v = [1, 0, 0]) {
									translate(v = [0, 0, -0.5000000000]) {
										cylinder($fn = 16, h = 6, r = 1.5000000000);
									}
								}
							}
						}
						translate(v = [28.8000000000, 0, 0]) {
							difference() {
								cube(size = [5.3000000000, 5, 15.5000000000]);
								translate(v = [2.6500000000, 0, 9.2500000000]) {
									rotate(a = -90, v = [1, 0, 0]) {
										translate(v = [0, 0, -0.5000000000]) {
											cylinder($fn = 16, h = 6, r = 1.5000000000);
										}
									}
								}
							}
						}
					}
				}
			}
		}
		rotate(a = 90.0000000000, v = [0, 0, 1]) {
			union() {
				translate(v = [0, 4.5000000000, 0]) {
					cube(size = [69.2500000000, 15, 3]);
				}
				translate(v = [30.7500000000, 12, 0]) {
					union() {
						difference() {
							cube(size = [5.3000000000, 5, 15.5000000000]);
							translate(v = [2.6500000000, 0, 9.2500000000]) {
								rotate(a = -90, v = [1, 0, 0]) {
									translate(v = [0, 0, -0.5000000000]) {
										cylinder($fn = 16, h = 6, r = 1.5000000000);
									}
								}
							}
						}
						translate(v = [28.8000000000, 0, 0]) {
							difference() {
								cube(size = [5.3000000000, 5, 15.5000000000]);
								translate(v = [2.6500000000, 0, 9.2500000000]) {
									rotate(a = -90, v = [1, 0, 0]) {
										translate(v = [0, 0, -0.5000000000]) {
											cylinder($fn = 16, h = 6, r = 1.5000000000);
										}
									}
								}
							}
						}
					}
				}
			}
		}
		rotate(a = 180.0000000000, v = [0, 0, 1]) {
			union() {
				translate(v = [0, 4.5000000000, 0]) {
					cube(size = [69.2500000000, 15, 3]);
				}
				translate(v = [30.7500000000, 12, 0]) {
					union() {
						difference() {
							cube(size = [5.3000000000, 5, 15.5000000000]);
							translate(v = [2.6500000000, 0, 9.2500000000]) {
								rotate(a = -90, v = [1, 0, 0]) {
									translate(v = [0, 0, -0.5000000000]) {
										cylinder($fn = 16, h = 6, r = 1.5000000000);
									}
								}
							}
						}
						translate(v = [28.8000000000, 0, 0]) {
							difference() {
								cube(size = [5.3000000000, 5, 15.5000000000]);
								translate(v = [2.6500000000, 0, 9.2500000000]) {
									rotate(a = -90, v = [1, 0, 0]) {
										translate(v = [0, 0, -0.5000000000]) {
											cylinder($fn = 16, h = 6, r = 1.5000000000);
										}
									}
								}
							}
						}
					}
				}
			}
		}
		rotate(a = 270.0000000000, v = [0, 0, 1]) {
			union() {
				translate(v = [0, 4.5000000000, 0]) {
					cube(size = [69.2500000000, 15, 3]);
				}
				translate(v = [30.7500000000, 12, 0]) {
					union() {
						difference() {
							cube(size = [5.3000000000, 5, 15.5000000000]);
							translate(v = [2.6500000000, 0, 9.2500000000]) {
								rotate(a = -90, v = [1, 0, 0]) {
									translate(v = [0, 0, -0.5000000000]) {
										cylinder($fn = 16, h = 6, r = 1.5000000000);
									}
								}
							}
						}
						translate(v = [28.8000000000, 0, 0]) {
							difference() {
								cube(size = [5.3000000000, 5, 15.5000000000]);
								translate(v = [2.6500000000, 0, 9.2500000000]) {
									rotate(a = -90, v = [1, 0, 0]) {
										translate(v = [0, 0, -0.5000000000]) {
											cylinder($fn = 16, h = 6, r = 1.5000000000);
										}
									}
								}
							}
						}
					}
				}
			}
		}
		union() {
			difference() {
				cylinder($fn = 32, h = 10, r = 7.5000000000);
				translate(v = [0, 0, 10]) {
					sphere($fn = 32, r = 6.5000000000);
				}
			}
			cylinder($fn = 64, h = 3, r = 19.5000000000);
		}
	}
}