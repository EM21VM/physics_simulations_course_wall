import numpy as np
from lib.constants import npdarr


def normalize(v: npdarr) -> npdarr:
    if not np.any(v):
        raise ValueError("Can't normalize zero vector")
    return v / np.linalg.norm(v)


def dist_sqr(vec1: npdarr, vec2: npdarr) -> np.float64:
    return np.dot(vec1 - vec2, vec1 - vec2)


def distance(vec1: npdarr, vec2: npdarr) -> np.float64:
    return np.linalg.norm(vec1 - vec2)


# def subtract_vector(vec1: npdarr, value: npdarr | float) -> npdarr:
#     if isinstance(value, npdarr):
#         return [vec1[0] - value[0], vec1[1] - value[1], vec1[2] - value[2]]
#     elif isinstance(value, float):
#         return (vec1[0] - value, vec1[1] - value, vec1[2] - value)


# def add_vector(vec1: npdarr, value: Union[npdarr, float]) -> npdarr:
#     if isinstance(value, np.ndarray):
#         return vec1 + value
#     elif isinstance(value, float):
#         return vec1 + value
#     else:
#         print("VEC1: " + vec1.__str__() + " VALUE: " + value.__str__())
#         raise TypeError("Value must be either a numpy array or a float")


if __name__ == "__main__":
    v: npdarr = np.array([3, -4])
    print(f"{v} -> {normalize(v)}")

    # v1 = npdarr([2,3,5])
    # va = 2
    # print("Add: " + add_vector(v1, va))
