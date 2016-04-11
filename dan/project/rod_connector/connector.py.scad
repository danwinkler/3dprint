

difference() {
	union() {
		difference() {
			sphere(r = 20);
			translate(v = [-100, -100, -100]) {
				cube(size = [200, 200, 100]);
			}
		}
		rotate(a = 45, v = [0, 1, 0]) {
			translate(v = [0, 0, 15]) {
				translate(v = [0, 0, 0]) {
					cylinder(h = 25, r = 9.1000000000);
				}
			}
		}
		rotate(a = 0, v = [0, 1, 0]) {
			translate(v = [0, 0, 15]) {
				translate(v = [0, 0, 0]) {
					cylinder(h = 25, r = 9.1000000000);
				}
			}
		}
		rotate(a = 45, v = [1, 0, 0]) {
			translate(v = [0, 0, 15]) {
				translate(v = [0, 0, 0]) {
					cylinder(h = 25, r = 9.1000000000);
				}
			}
		}
		rotate(a = -60, v = [1, 0, 0]) {
			translate(v = [0, 0, 15]) {
				translate(v = [0, 0, 0]) {
					cylinder(h = 25, r = 9.1000000000);
				}
			}
		}
		rotate(a = -90, v = [0, 1, 0]) {
			translate(v = [0, 0, 15]) {
				translate(v = [0, 0, 0]) {
					cylinder(h = 25, r = 9.1000000000);
				}
				translate(v = [-9.1000000000, -9.1000000000, 0]) {
					cube(size = [18.2000000000, 18.2000000000, 25]);
				}
			}
		}
		translate(v = [0, 0, -9.1000000000]) {
			cylinder(h = 9.1000000000, r = 20);
		}
	}
	union() {
		rotate(a = 45, v = [0, 1, 0]) {
			translate(v = [0, 0, 15]) {
				rotate(a = 0, v = [0, 0, 1]) {
					translate(v = [0, 0, 0]) {
						translate(v = [0, 0, 5]) {
							cylinder(h = 30, r = 6.6000000000);
						}
						translate(v = [0, -5, 17]) {
							rotate(a = 90, v = [1, 0, 0]) {
								cylinder($fn = 12, h = 6, r = 1.5000000000);
							}
						}
					}
				}
			}
		}
		rotate(a = 0, v = [0, 1, 0]) {
			translate(v = [0, 0, 15]) {
				rotate(a = 45, v = [0, 0, 1]) {
					translate(v = [0, 0, 0]) {
						translate(v = [0, 0, 5]) {
							cylinder(h = 30, r = 6.6000000000);
						}
						translate(v = [0, -5, 17]) {
							rotate(a = 90, v = [1, 0, 0]) {
								cylinder($fn = 12, h = 6, r = 1.5000000000);
							}
						}
					}
				}
			}
		}
		rotate(a = 45, v = [1, 0, 0]) {
			translate(v = [0, 0, 15]) {
				rotate(a = 0, v = [0, 0, 1]) {
					translate(v = [0, 0, 0]) {
						translate(v = [0, 0, 5]) {
							cylinder(h = 30, r = 6.6000000000);
						}
						translate(v = [0, -5, 17]) {
							rotate(a = 90, v = [1, 0, 0]) {
								cylinder($fn = 12, h = 6, r = 1.5000000000);
							}
						}
					}
				}
			}
		}
		rotate(a = -60, v = [1, 0, 0]) {
			translate(v = [0, 0, 15]) {
				rotate(a = -90, v = [0, 0, 1]) {
					translate(v = [0, 0, 0]) {
						translate(v = [0, 0, 5]) {
							cylinder(h = 30, r = 6.6000000000);
						}
						translate(v = [0, -5, 17]) {
							rotate(a = 90, v = [1, 0, 0]) {
								cylinder($fn = 12, h = 6, r = 1.5000000000);
							}
						}
					}
				}
			}
		}
		rotate(a = -90, v = [0, 1, 0]) {
			translate(v = [0, 0, 15]) {
				rotate(a = 0, v = [0, 0, 1]) {
					translate(v = [0, 0, 0]) {
						translate(v = [0, 0, 5]) {
							cylinder(h = 30, r = 6.6000000000);
						}
						translate(v = [0, -5, 17]) {
							rotate(a = 90, v = [1, 0, 0]) {
								cylinder($fn = 12, h = 6, r = 1.5000000000);
							}
						}
					}
				}
			}
		}
	}
}