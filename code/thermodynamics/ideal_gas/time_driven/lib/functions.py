import numpy as np
import math as math
from lib.constants import npdarr


def normalize(v: npdarr) -> npdarr:
    if not np.any(v):
        raise ValueError("Can't normalize zero vector")
    return v / np.linalg.norm(v)


def dist_sqr(vec1: npdarr, vec2: npdarr) -> np.float64:
    return np.dot(vec1 - vec2, vec1 - vec2)


def distance(vec1: npdarr, vec2: npdarr) -> np.float64:
    return np.linalg.norm(vec1 - vec2)

def cross_vec(vec1: npdarr, vec2: npdarr):
    return np.cross(vec1, vec2)

def value_vec(vec1: npdarr) -> float:
        return abs(math.sqrt(math.pow(vec1[0],2) + math.pow(vec1[1],2) + math.pow(vec1[2],2)))
    
def calc_distance(vec1: npdarr, vec2: npdarr, vec2_dir: npdarr):
    return value_vec(cross_vec((np.subtract(vec1, vec2)), vec2_dir))/ value_vec(vec2_dir)

if __name__ == "__main__":
    v: npdarr = np.array([3, -4])
    print(f"{v} -> {normalize(v)}")
    a = np.array([2,2,2])
    erg = value_vec(a)
    print(erg)
