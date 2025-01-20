import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lib.constants import ZERO_VEC, npdarr
from lib.Object import Object
from lib.functions import normalize


class Wall(Object):
    "A Wall in a 3-Dimensinal Space"

    def __init__(
        self,
        pos: npdarr = np.copy(ZERO_VEC),
        end_pos: npdarr = np.copy(ZERO_VEC),
        color: str = "#FF0000",
        opacity: float = 1.0,
    ) -> None:
        print(f"start_pos: {pos}")
        # self.width: float = pos[0] - end_pos[0]
        # self.height: float = pos[1] - end_pos[1]
        # self.depth: float = pos[2] - end_pos[2]
        self.end_pos = end_pos
        self.pos = pos
        self.dir_vec = end_pos - pos
        first_bbox_x_pt = pos[0] if pos[0] < end_pos[0] else end_pos[0]
        first_bbox_y_pt = pos[1] if pos[1] < end_pos[1] else end_pos[1]
        first_bbox_z_pt = pos[2] if pos[2] < end_pos[2] else end_pos[2]
        first_bbox_pts = [first_bbox_x_pt, first_bbox_y_pt, first_bbox_z_pt]
        
        last_bbox_x_pt = pos[0] if pos[0] > end_pos[0] else end_pos[0]
        last_bbox_y_pt = pos[1] if pos[1] > end_pos[1] else end_pos[1]
        last_bbox_z_pt = pos[2] if pos[2] > end_pos[2] else end_pos[2]
        last_bbox_pts = [last_bbox_x_pt, last_bbox_y_pt, last_bbox_z_pt]
        bbox_pts: npdarr = np.array([first_bbox_pts, last_bbox_pts])
        super().__init__(pos, bbox_pts=bbox_pts, color=color, opacity=opacity)


if __name__ == "__main__":
    print("Testing the Wall class")
    wal = Wall(
        pos=np.array([1, 3, 0]),
        end_pos=np.array([2, 0, 0]),
        color="#FF0000",
        opacity=1,
    )
    print(wal)
    print("Bounding box points " + wal.bbox.__str__())
