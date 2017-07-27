

union() {
	scale(v = [25.4000000000, 25.4000000000, 25.4000000000]) {
		translate(v = [3.0000000000, 3.0000000000, 4]) {
			translate(v = [0, 16.5000000000, 0]) {
				cube(size = [23.0000000000, 1.5000000000, 3.5000000000]);
			}
			cube(size = [23.0000000000, 1.5000000000, 3.5000000000]);
			translate(v = [0, 1.5000000000, 0]) {
				cube(size = [1.5000000000, 15.0000000000, 3.5000000000]);
			}
			translate(v = [0, 0, 3.5000000000]) {
				cube(size = [23.0000000000, 18.0000000000, 0.5000000000]);
			}
			translate(v = [21.5000000000, 1.5000000000, 0]) {
				cube(size = [1.5000000000, 15.0000000000, 3.5000000000]);
			}
		}
		translate(v = [1.5000000000, 1.5000000000, 4]) {
			translate(v = [0, 1.5000000000, 0]) {
				cube(size = [1.5000000000, 3.5000000000, 31.5000000000]);
			}
			translate(v = [-0.7500000000, 0, 0]) {
				cube(size = [5.5000000000, 1.5000000000, 31.5000000000]);
			}
			translate(v = [-0.7500000000, 0, -1.5000000000]) {
				cube(size = [5.5000000000, 5.5000000000, 1.5000000000]);
			}
		}
		translate(v = [27.5000000000, 1.5000000000, 4]) {
			scale(v = [-1, 1, 1]) {
				translate(v = [0, 1.5000000000, 0]) {
					cube(size = [1.5000000000, 3.5000000000, 31.5000000000]);
				}
				translate(v = [-0.7500000000, 0, 0]) {
					cube(size = [5.5000000000, 1.5000000000, 31.5000000000]);
				}
				translate(v = [-0.7500000000, 0, -1.5000000000]) {
					cube(size = [5.5000000000, 5.5000000000, 1.5000000000]);
				}
			}
		}
		translate(v = [1.5000000000, 22.5000000000, 4]) {
			scale(v = [1, -1, 1]) {
				translate(v = [0, 1.5000000000, 0]) {
					cube(size = [1.5000000000, 3.5000000000, 31.5000000000]);
				}
				translate(v = [-0.7500000000, 0, 0]) {
					cube(size = [5.5000000000, 1.5000000000, 31.5000000000]);
				}
				translate(v = [-0.7500000000, 0, -1.5000000000]) {
					cube(size = [5.5000000000, 5.5000000000, 1.5000000000]);
				}
			}
		}
		translate(v = [27.5000000000, 22.5000000000, 4]) {
			scale(v = [1, -1, 1]) {
				scale(v = [-1, 1, 1]) {
					translate(v = [0, 1.5000000000, 0]) {
						cube(size = [1.5000000000, 3.5000000000, 31.5000000000]);
					}
					translate(v = [-0.7500000000, 0, 0]) {
						cube(size = [5.5000000000, 1.5000000000, 31.5000000000]);
					}
					translate(v = [-0.7500000000, 0, -1.5000000000]) {
						cube(size = [5.5000000000, 5.5000000000, 1.5000000000]);
					}
				}
			}
		}
		translate(v = [1.5000000000, 0, 35.5000000000]) {
			cube(size = [26, 24, 0.5000000000]);
		}
		translate(v = [0, 0, 32.0000000000]) {
			translate(v = [-0.7500000000, 22.5000000000, 0]) {
				cube(size = [30.5000000000, 1.5000000000, 3.5000000000]);
			}
			translate(v = [-0.7500000000, 0, 0]) {
				cube(size = [30.5000000000, 1.5000000000, 3.5000000000]);
			}
			translate(v = [-0.7500000000, 1.5000000000, 0]) {
				cube(size = [1.5000000000, 21.0000000000, 3.5000000000]);
			}
			translate(v = [28.2500000000, 1.5000000000, 0]) {
				cube(size = [1.5000000000, 21.0000000000, 3.5000000000]);
			}
		}
		translate(v = [27.5000000000, 0, 36]) {
			translate(v = [2.2500000000, 0, 1]) {
				rotate(a = 0, v = [0, 1, 0]) {
					translate(v = [0, 23.2500000000, 0]) {
						cube(size = [24, 0.7500000000, 4]);
					}
					cube(size = [24, 0.7500000000, 4]);
					translate(v = [0, 0.7500000000, 0]) {
						cube(size = [0.7500000000, 22.5000000000, 4]);
					}
					translate(v = [0, 0, 4]) {
						cube(size = [24, 24, 0.5000000000]);
					}
					translate(v = [23.2500000000, 0.7500000000, 0]) {
						cube(size = [0.7500000000, 22.5000000000, 4]);
					}
					translate(v = [12.0000000000, 0.7500000000, 0]) {
						cube(size = [4, 22.5000000000, 0.7500000000]);
					}
					translate(v = [14.0000000000, 12.0000000000, -4.5000000000]) {
						cylinder(h = 4.5000000000, r = 0.2000000000);
					}
				}
			}
			difference() {
				translate(v = [0, 3.0000000000, -15.0000000000]) {
					cube(size = [0.7500000000, 18.0000000000, 18]);
				}
				translate(v = [-1, 12.0000000000, -13.0000000000]) {
					rotate(a = 90, v = [0, 1, 0]) {
						cylinder(h = 10, r = 1);
					}
				}
			}
			translate(v = [0.7500000000, 0, -0.5000000000]) {
				cube(size = [1.5000000000, 24, 3.5000000000]);
			}
		}
		translate(v = [1.5000000000, 0, 36]) {
			scale(v = [-1, 1, 1]) {
				translate(v = [2.2500000000, 0, 1]) {
					rotate(a = 0, v = [0, 1, 0]) {
						translate(v = [0, 23.2500000000, 0]) {
							cube(size = [24, 0.7500000000, 4]);
						}
						cube(size = [24, 0.7500000000, 4]);
						translate(v = [0, 0.7500000000, 0]) {
							cube(size = [0.7500000000, 22.5000000000, 4]);
						}
						translate(v = [0, 0, 4]) {
							cube(size = [24, 24, 0.5000000000]);
						}
						translate(v = [23.2500000000, 0.7500000000, 0]) {
							cube(size = [0.7500000000, 22.5000000000, 4]);
						}
						translate(v = [12.0000000000, 0.7500000000, 0]) {
							cube(size = [4, 22.5000000000, 0.7500000000]);
						}
						translate(v = [14.0000000000, 12.0000000000, -4.5000000000]) {
							cylinder(h = 4.5000000000, r = 0.2000000000);
						}
					}
				}
				difference() {
					translate(v = [0, 3.0000000000, -15.0000000000]) {
						cube(size = [0.7500000000, 18.0000000000, 18]);
					}
					translate(v = [-1, 12.0000000000, -13.0000000000]) {
						rotate(a = 90, v = [0, 1, 0]) {
							cylinder(h = 10, r = 1);
						}
					}
				}
				translate(v = [0.7500000000, 0, -0.5000000000]) {
					cube(size = [1.5000000000, 24, 3.5000000000]);
				}
			}
		}
		translate(v = [27.5000000000, 0, 36]) {
			translate(v = [0, 3.0000000000, -17.0000000000]) {
				cube(size = [0.7500000000, 18.0000000000, 2]);
			}
			difference() {
				translate(v = [0.7500000000, 1.5000000000, -28.0000000000]) {
					rotate(a = 0, v = [0, 0, 1]) {
						cube(size = [0.7500000000, 21.0000000000, 24]);
					}
				}
				translate(v = [-1, 12.0000000000, -13.0000000000]) {
					rotate(a = 90, v = [0, 1, 0]) {
						cylinder(h = 10, r = 1);
					}
				}
			}
		}
		translate(v = [1.5000000000, 0, 36]) {
			scale(v = [-1, 1, 1]) {
				translate(v = [0, 3.0000000000, -17.0000000000]) {
					cube(size = [0.7500000000, 18.0000000000, 2]);
				}
				difference() {
					translate(v = [0.7500000000, 1.5000000000, -28.0000000000]) {
						rotate(a = 0, v = [0, 0, 1]) {
							cube(size = [0.7500000000, 21.0000000000, 24]);
						}
					}
					translate(v = [-1, 12.0000000000, -13.0000000000]) {
						rotate(a = 90, v = [0, 1, 0]) {
							cylinder(h = 10, r = 1);
						}
					}
				}
			}
		}
	}
}