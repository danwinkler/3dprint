import os
import json
import subprocess

filename = os.path.join( os.environ['TEMP'], 'convsurftest.json' )

data = {
	"margins": 2,
	"resolution" : 0.03,
	"lines": [
		[[0, 0, 0], [1, 1, 1], 10],
		[[1, 1, 1], [2, 1, 1], 7],
		[[1, 1, 1], [1, 2, 1], 7],
		[[1, 1, 1], [1, 1, 2], 7]
	]
}

with open(filename, 'w') as f:
    f.write(json.dumps(data))

subprocess.run(["java", "-jar", "dan/lib/convsurfapp.jar", filename])