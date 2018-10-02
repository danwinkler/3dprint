import math
import random

from dan.lib.helper import Vec3

_node_id = 0

# TODO: nested rings?

class NodeData:
    def __init__(self, node):
        self.pos = Vec3(node.pos)
        self.id = node.id
        self.prev = node.prev.id
        self.next = node.next.id

        # This is a helper field for trianglulation
        self.opposite = None


class Node:
    NEIGHBOR_DISTANCE = 5
    NEIGHBOR_PUSH_SCALAR = 0.05
    OTHER_PUSH_SCALAR = 10
    MAX_DIST_OTHER = NEIGHBOR_DISTANCE * 5

    def __init__(self, x, y):
        global _node_id
        self.pos = Vec3(x, y)
        self.pos_next = Vec3(self.pos)
        self.prev = None
        self.next = None

        self.id = _node_id
        _node_id += 1

    def set_prev(self, node):
        if self.prev != node:
            self.prev = node
            node.set_next(self)

    def set_next(self, node):
        if self.next != node:
            self.next = node
            node.set_prev(self)

    def update(self, nodes):
        # Maintain distance from neighbors
        self.pos_next.set(self.pos)

        self.neighbor_push(self.prev)
        self.neighbor_push(self.next)

        for node in nodes:
            if node in (self.next, self.prev, self):
                continue

            self.other_push(node)

    def other_push(self, node):
        vec = self.pos - node.pos
        distance2 = vec.length2()

        if distance2 > self.MAX_DIST_OTHER ** 2:
            return

        distance = math.sqrt(distance2)
        vec_norm = Vec3(vec)
        vec_norm /= distance

        push_force = vec_norm * ((1 / distance) * self.OTHER_PUSH_SCALAR)

        self.pos_next += push_force

    def neighbor_push(self, node):
        vec = self.pos - node.pos
        distance = vec.length()
        vec_norm = Vec3(vec)
        vec_norm /= distance

        distance_from_optimal = distance - self.NEIGHBOR_DISTANCE
        push_force = vec_norm * (distance_from_optimal * self.NEIGHBOR_PUSH_SCALAR)
        push_force *= -1

        self.pos_next += push_force

    def __repr__(self):
        return "<Node id:{} prev:{} next:{}>".format(
            self.id, self.prev.id, self.next.id
        )


class DiffLine:
    def __init__(self):
        self.root = None
        self.nodes = []
        random.seed(0)

    def init_circle(self):
        radius = 12
        num_points = math.floor((radius * math.pi * 2) / Node.NEIGHBOR_DISTANCE)

        self.root = Node(radius, 0)
        self.nodes.append(self.root)
        previous = self.root
        for i in range(1, num_points):
            a = (i / num_points) * math.pi * 2
            node = Node(math.cos(a) * radius, math.sin(a) * radius)
            self.nodes.append(node)
            previous.set_next(node)
            previous = node
        previous.set_next(self.root)

    def insert_node(self):
        insert_index = random.randint(1, len(self.nodes) - 1)
        prev = self.nodes[insert_index]
        next = prev.next

        node = Node((prev.pos.x + next.pos.x) * 0.5, (prev.pos.y + next.pos.y) * 0.5)
        self.nodes.insert(insert_index + 1, node)
        prev.set_next(node)
        next.set_prev(node)

    def update(self):
        self.insert_node()

        for i, node in enumerate(self.nodes):
            if self.nodes[(i + 1) % len(self.nodes)] != node.next:
                raise Exception

        for node in self.nodes:
            node.update(self.nodes)

        for node in self.nodes:
            node.pos = node.pos_next

    def get_nodes(self):
        return self.nodes
