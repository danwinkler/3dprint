#!/usr/bin/env python3
import os
import sys

from solid import *
from solid.utils import *

output_path = os.path.splitext(sys.argv[1])[0] + '.scad'

with open(sys.argv[1]) as f:
    text = f.read()

# We'll be nice and cut off trailing whitespace before the count (Because a lot of editors will add a newline)
text = text.rstrip()

size = len(text.encode('utf-8'))

code='''
import math
import random
from solid import *
from solid.utils import *
{}
'''.format(text)

code_globals = {}
exec(code, code_globals)

if 'o' not in code_globals:
    print('Please assign a solidpython object to "o" (Lists are OK).')
    sys.exit(1)

print('File Size: {}'.format(size))
print('Saving: {}'.format(output_path))
with open(output_path, 'w') as f:
	f.write(scad_render(union()(code_globals['o'])))
