import os
import json
import platform
import subprocess

class ConvolutionSurface(object):
    def __init__(self, margins, resolution):
        self.margins = margins
        self.resolution = resolution
        self.lines = []
    
    def add_line(self, p0, p1, s):
        self.lines.append([p0, p1, s])
    
    def tmp_folder(self):
        if platform.system() == 'Windows':
            return os.environ['TEMP']
        else:
            return '/tmp/'

    def render(self):
        filename = os.path.join( self.tmp_folder(), 'convsurftest.json' )

        data = {
            "margins": self.margins,
            "resolution" : self.resolution,
            "lines": self.lines
        }

        with open(filename, 'w') as f:
            f.write(json.dumps(data))

        subprocess.run(["java", "-jar", "dan/lib/convsurfapp.jar", filename])
    
    def render_python(self):
        pass
