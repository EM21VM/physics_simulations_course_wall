import numpy as np
from lib.constants import ZERO_VEC, npdarr
import lib.functions
from lib.Object import Object

class Wall(Object):
    "A Wall in a 3-Dimensinal Space"
    
    
    def __init__(
        self,
        start_pos: npdarr = np.copy(ZERO_VEC),
        end_pos: npdarr = [1,1,1],
        color : str = "#FF0000",
        opacity : float = 1.0,
    ) -> None: 
        first_bbox_pts = [start_pos[0], start_pos[1], start_pos[2]]
        last_bbox_pts = [end_pos[0], end_pos[1], end_pos[2]]
        bbox_pts: npdarr = np.array([first_bbox_pts, last_bbox_pts])
        vel = [end_pos[0] - start_pos[0], end_pos[1] - start_pos[1], end_pos[2] - start_pos[2]]
        super().__init__(start_pos,vel, bbox_pts=bbox_pts, color=color, opacity=opacity)
        