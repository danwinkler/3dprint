import structure_list
from layer_structure import *

import sys

models = dir(structure_list)
models = filter(lambda x: x[0] != '_', models)
models = [getattr(structure_list, model) for model in models]
def model_filter(m):
    try:
        return m.__module__ in ['structure_list']
    except:
        return False
models = filter(model_filter, models)

for model in models:
    print "Building: " + model.__name__
    m = model()
    create_vase( m, model.__name__ )
