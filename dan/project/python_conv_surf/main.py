import math
import time

import mcubes
import numba
import numpy as np
from numba import float32, float64, guvectorize, njit, vectorize

from cuda_conv import cuda_calculate_field


def generate_field(minx, miny, minz, maxx, maxy, maxz, resolution):
    # The following code generates a 2d array: (x*y*z, 3), where the last dimension is the xyz coord
    x = np.arange(minx, maxx, resolution)
    y = np.arange(miny, maxy, resolution)
    z = np.arange(minz, maxz, resolution)
    meshgrid = np.meshgrid(x, y, z)
    return np.vstack(meshgrid).reshape(3, -1).T, x.shape[0], y.shape[0], z.shape[0]

    # The following code generates a 4d array: (x, y, z, 3), where the last dimension is the xyz coord
    # meshgrid = np.meshgrid(
    #     np.arange(minx, maxx, resolution),
    #     np.arange(miny, maxy, resolution),
    #     np.arange(minz, maxz, resolution),
    #     indexing="ij",
    # )
    # return np.stack(meshgrid, axis=3)


# TODO: experiment with inlining all of these helpers
# https://numba.pydata.org/numba-doc/latest/developer/inlining.html


field, width, height, depth = generate_field(-2, -2, -4, 12, 12, 4, 0.1)

triangles = []

fn = lambda x, y: math.sin(x) + math.cos(y)
s = 4
for x in np.arange(0, 10, 0.5):
    for y in np.arange(0, 10, 0.5):
        triangles += [
            [
                [x, y, fn(x, y)],
                [x + 1, y, fn(x + 1, y)],
                [x + 1, y + 1, fn(x + 1, y + 1)],
                [s, 0, 0],
            ],
            [
                [x, y, fn(x, y)],
                [x, y + 1, fn(x, y + 1)],
                [x + 1, y + 1, fn(x + 1, y + 1)],
                [s, 0, 0],
            ],
        ]

triangles += [
    [
        [5, 5, -3],
        [5, 5, 3],
        [math.nan, math.nan, math.nan],
        [2, 0, 0],
    ],
]

triangles = np.array(triangles)

print(f"Starting field calulation, field size: {field.shape}")
start = time.time()

field = cuda_calculate_field(field, triangles)
end = time.time()
print(f"Finished field calc, took {end-start:2f} seconds")

grid3 = field.reshape(width, height, depth)

print("Starting marching cubes")
vertices, triangles = mcubes.marching_cubes(field.reshape(width, height, depth), 0.4)
print(f"Finished marching cubes, output model has {len(triangles)} triangles")

mcubes.export_obj(vertices, triangles, "test.obj")
