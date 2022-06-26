

union() {
	difference() {
		hull() {
			translate(v = [2.0000000000, 2.0000000000, 2.0000000000]) {
				sphere($fn = 16, r = 2.0000000000);
			}
			translate(v = [2.0000000000, 8.0000000000, 2.0000000000]) {
				sphere($fn = 16, r = 2.0000000000);
			}
			translate(v = [98.0000000000, 5.0000000000, 2.0000000000]) {
				sphere($fn = 16, r = 2.0000000000);
			}
		}
		translate(v = [0, 0, 1]) {
			union() {
				translate(v = [85, -110, 0]) {
					import(file = "c:/Users/Dan/workspace/3dprint/dan/project/heliostat_servo/Servo_Arm.stl", origin = [0, 0]);
				}
				translate(v = [0, 0.2000000000, 0]) {
					translate(v = [85, -110, 0]) {
						import(file = "c:/Users/Dan/workspace/3dprint/dan/project/heliostat_servo/Servo_Arm.stl", origin = [0, 0]);
					}
				}
				translate(v = [0, -0.2000000000, 0]) {
					translate(v = [85, -110, 0]) {
						import(file = "c:/Users/Dan/workspace/3dprint/dan/project/heliostat_servo/Servo_Arm.stl", origin = [0, 0]);
					}
				}
				translate(v = [0, 0, 0.2000000000]) {
					translate(v = [85, -110, 0]) {
						import(file = "c:/Users/Dan/workspace/3dprint/dan/project/heliostat_servo/Servo_Arm.stl", origin = [0, 0]);
					}
				}
				translate(v = [0, 0, -0.2000000000]) {
					translate(v = [85, -110, 0]) {
						import(file = "c:/Users/Dan/workspace/3dprint/dan/project/heliostat_servo/Servo_Arm.stl", origin = [0, 0]);
					}
				}
				translate(v = [-1, 0, -0.2000000000]) {
					translate(v = [85, -110, 0]) {
						import(file = "c:/Users/Dan/workspace/3dprint/dan/project/heliostat_servo/Servo_Arm.stl", origin = [0, 0]);
					}
				}
				translate(v = [-1, 0, 0.2000000000]) {
					translate(v = [85, -110, 0]) {
						import(file = "c:/Users/Dan/workspace/3dprint/dan/project/heliostat_servo/Servo_Arm.stl", origin = [0, 0]);
					}
				}
				translate(v = [0, 5, 0]) {
					cylinder(h = 4, r = 3);
				}
			}
		}
		translate(v = [0, 5, -0.1000000000]) {
			cylinder($fn = 16, h = 4, r = 2);
		}
	}
}