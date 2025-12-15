from typing import NamedTuple
from math import prod
from rich import print

class Junction(NamedTuple):
    x: int
    y: int
    z: int

with open("input.txt", "r") as f:
    raw = f.readlines()
data = [Junction(*(int(y) for y in (x.strip().split(",")))) for x in raw]

def distance(j1: Junction, j2: Junction):
    return (j1.x - j2.x) ** 2 + (j1.y - j2.y) ** 2 + (j1.z - j2.z) ** 2

circuits: list[set[Junction]] = list()
connections: set[tuple[Junction, Junction]] = set()

def all_possible_connections(data: list[Junction]):
    already = set()
    for j1 in data:
        for j2 in data:
            if (j1 == j2):
                continue
            if (j1, j2) in already or (j2, j1) in already:
                continue
            x = j1, j2
            already.add(x)
            yield x

sorted_connections = sorted([(x, distance(x[0], x[1])) for x in all_possible_connections(data)], key=lambda x: x[1])

sorted_connections = sorted_connections[:1000]
for (j1, j2), dis in sorted_connections:
    for circuit in circuits:
        if j1 in circuit or j2 in circuit:
            circuit.add(j1)
            circuit.add(j2)
            break
    else:
        circuit = set((j1, j2))
        circuits.append(circuit)
    #simplification des circuits
    for c1 in list(circuits):
        _break = False
        for c2 in list(circuits):
            if c1 == c2:
                continue
            inter = c1.intersection(c2)
            if len(inter) > 0:
                circuits.remove(c1)
                circuits.remove(c2)
                circuits.append(c1.union(c2))
                _break = True
                break
        if _break: break

print()
print(circuits)
lenghts = [len(x) for x in circuits]
lenghts.sort(reverse=True)
print(lenghts)
print(lenghts[0] * lenghts[1] * lenghts[2])
