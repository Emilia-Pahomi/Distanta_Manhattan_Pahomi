import numpy as np
from scipy.spatial.distance import cityblock

def manhattan_manual(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError("Vectorii au aceeasi lungime")
    
    return sum(abs(a - b) for a, b in zip(vec1, vec2))

def manhattan_scipy(vec1, vec2):
    return cityblock(vec1, vec2)


def citeste(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        v1 = [float(x) for x in lines[0].split()]
        v2 = [float(x) for x in lines[1].split()]
    return v1, v2