#!/usr/bin/env python3
import os
import sys
from collections import namedtuple

from solid import *
from solid.utils import *

minify = False
if len(sys.argv) >= 3 and sys.argv[2] == '--minify':
    minify = True

output_base = os.path.splitext(sys.argv[1])[0]
output_scad = output_base + '.scad'

with open(sys.argv[1]) as f:
    text = f.read()

if minify:
    from pyminifier import minification, token_utils
    tokens = token_utils.listified_tokenizer(text)
    Options = namedtuple('Options', ['tabs'])
    text = minification.minify(tokens, Options(tabs=False))
    text = text.rstrip()
    with open(output_base + '.min.py', 'w') as f:
        f.write(text)
else:
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
print('Saving: {}'.format(output_scad))
with open(output_scad, 'w') as f:
	f.write(scad_render(union()(code_globals['o'])))
