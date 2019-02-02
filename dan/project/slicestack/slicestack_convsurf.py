import pickle
import random

from tqdm import tqdm
from plumbum import local

from dan.project.slicestack.differential_line import DiffLine, NodeData
from dan.lib.convolution_surface import ConvolutionSurface

df = DiffLine()
df.init_circle()

layers = []
points_per_layer = 300
height = 710
flip = False
cache_file = local.path('sim_{}.pickle'.format(height))

if cache_file.exists():
    with open(cache_file, 'rb') as f:
        layers = pickle.load(f)
else:
    print("Running Simulation")
    for i in tqdm(range(height)):
        df.update()

        if i % 1 == 0:
            layer = []
            for ring in df.rings:
                ring_layer = []
                for n in ring:
                    nd = NodeData(n)
                    if flip:
                        nd.pos.z = height - i
                    else:
                        nd.pos.z = i
                    ring_layer.append(nd)
                layer.append(ring_layer)
            layers.append(layer)
    with open(cache_file, 'wb') as f:
        pickle.dump(layers, f)

layers = layers[:100]

surface = ConvolutionSurface(3, .8)

# Scale
for li, layer in enumerate(layers):
    for ring in layer:
        for ni, nd in enumerate(ring):
            nd.pos.z *= .5

def get_node_index_from_layer(layer, node_id):
    return [i for i, n in enumerate(layer) if n.id == node_id][0]

last_node = None
for i in range(3):
    for li, layer in enumerate(layers):
        layer = layer[0]
        if last_node is None:
            last_node = random.choice(layer)
        else:
            node_index = get_node_index_from_layer(layer, last_node.id)
            node = layer[(node_index + random.randint(-1, 1) + len(layer)) % len(layer)]
            surface.add_line(
                last_node.pos.to_list(),
                node.pos.to_list(),
                1.8
            )
            last_node = node

    last_node = None

"""
for li, layer in enumerate(layers[:10]):
    layer = layer[0]
    for ni, nd in enumerate(layer):
        surface.add_line(
            nd.pos.to_list(),
            layer[(ni+1) % len(layer)].pos.to_list(),
            1.8
        )

        random.seed( li * 1000 + ni )
        if li+1 < len(layers) and random.random() > .6:
            surface.add_line(
                nd.pos.to_list(),
                [l for l in layers[li+1][0] if l.id == nd.id][0].pos.to_list(),
                2
            )
"""
surface.render()