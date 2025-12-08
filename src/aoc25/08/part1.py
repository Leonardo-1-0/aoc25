from __future__ import annotations
from collections import defaultdict
from itertools import combinations
import math
from typing import NamedTuple


class Box(NamedTuple):
    x: int
    y: int
    z: int

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"


def distance(a: Box, b: Box) -> float:
    return abs(math.sqrt(((b.x - a.x) ** 2 + (b.y - a.y) ** 2 + (b.z - a.z) ** 2)))


boxes: list[Box] = []
for line in open(0).readlines():
    x, y, z = map(int, line.strip().split(","))
    box = Box(x, y, z)
    boxes.append(box)

unsorted_network: dict[tuple[Box, Box], float] = {}
for combo in combinations(boxes, 2):
    unsorted_network[(combo[0], combo[1])] = distance(combo[0], combo[1])

network = dict(sorted(unsorted_network.items(), key=lambda x: x[1]))

limit = 1_000
circuits: list[set[Box]] = []
connections: dict[Box, set[Box]] = defaultdict(set)
for i, edge in enumerate(network):
    if i >= limit:
        break

    left, right = edge
    connections[left].add(right)
    connections[right].add(left)

    to_connect = [
        circuit for circuit in circuits if (left in circuit) or (right in circuit)
    ]

    if not to_connect:
        circuit: set[Box] = {left, right} | connections[left] | connections[right]
        circuits.append(set(sorted(circuit)))
        continue

    merged: set[Box] = {left, right} | connections[left] | connections[right]
    for circuit in to_connect:
        merged.update(circuit)
        circuits.remove(circuit)

    circuits.append(merged)

total = 1
for circuit in sorted(circuits, key=len, reverse=True)[:3]:
    total *= len(circuit)

print(total)
