import numpy as np
import numpy.typing as npt
import math as math

# Types (for hints)
npdarr = npt.NDArray[np.float64]


def cross_vec(vec1: npdarr, vec2: npdarr):
    return np.cross(vec1, vec2)


def value_vec(vec1: npdarr) -> float:
    return abs(
        math.sqrt(math.pow(vec1[0], 2) + math.pow(vec1[1], 2) + math.pow(vec1[2], 2))
    )
    
def calc_distance(vec1: npdarr, vec2: npdarr, vec2_dir: npdarr):
    return value_vec(cross_vec((np.subtract(vec1, vec2)), vec2_dir))/ value_vec(vec2_dir)



if __name__ == "__main__":
    obj_2_pos = np.array([1, 0, 2])
    obj_2_dir_vec = np.array([2, 1, 4])
    obj_1_pos = np.array([8, 4, 5])
    d = calc_distance(obj_1_pos, obj_2_pos, obj_2_dir_vec)
    print(d)
    # print(obj_1_pos)
    # print(obj_2_pos)
    # AP : npdarr = np.subtract(obj_1_pos, obj_2_pos)
    # APxU = cross_vec(AP, obj_2_dir_vec)
    # Betrag_APxU = value_vec(APxU)
    # Betrag_U = value_vec(obj_2_dir_vec)
    # d = Betrag_APxU / Betrag_U
    # print("AP: " + str(AP))
    # print("APxU: " + str(APxU))
    # print("Betrag_APxU: " + str(Betrag_APxU))
    # print("Betrag_U: " + str(Betrag_U)) 
    # print("Abstand: " + str(d) + " LE")
    
