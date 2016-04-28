import subprocess
import math
import platform

system = platform.system()
if system == "Windows":
    pgm = "C:\Program Files (x86)\OpenSCAD\openscad.exe"
else:
    pgm = "/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD"


def get_structure_images():
    for i in xrange(1,8):
        subprocess.call( [pgm, "-o", "images/image" + str(i) + ".png", "structure" + str(i) + ".py.scad"] )

def get_connector_images():
    for i in xrange(60):
        print i
        subprocess.call( [pgm, "-o", "images/varE/" + str(i) + ".png", "designs/varE/" + str(i) + ".scad"] )

def rotate_scad_file():
    for i in xrange(4):
        subprocess.call( [pgm, "-D", "angle="+str(i*90),"-o", "images/rot/" + str(i) + ".png", "connector.py.scad"] )

def output_stls():
    for i in xrange(60):
        print i
        subprocess.call( [pgm, "-o", "stls/varE/" + str(i) + ".stl", "designs/varE/" + str(i) + ".scad"] )

#get_connector_images()
#get_structure_images()
#rotate_scad_file()
output_stls()
