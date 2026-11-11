import numpy as np
import pyqtgraph.opengl as gl
from . import rotation

class DrawMav:
    def get_mesh(self) -> tuple[
        np.ndarray[tuple[int,int], np.dtype[np.floating]],
        np.ndarray[tuple[int, int, int], np.dtype[np.floating]],
        np.ndarray[tuple[int, int], np.dtype[np.floating]]
    ]:
        # points are in NED coordinates
        # define the points on the aircraft following diagram Fig 2.14
        points = np.array([[0, 0, 0],
                           [1, 0, 0],
                           [1, 0, -1],
                           [0, 0, -1],
                           ]).T

        faces = np.array([
            [0, 1, 2],
            [0, 2, 3]
        ])

        # scale points for better rendering
        scale = 50
        points = scale * points

        #   define the colors for each face of triangular mesh
        red = np.array([1., 0., 0., 1])
        green = np.array([0., 1., 0., 1])
        blue = np.array([0., 0., 1., 1])
        yellow = np.array([1., 1., 0., 1])
        meshColors = np.empty((13, 3, 4), dtype=np.float32)
        meshColors[0] = blue 
        meshColors[1] = green 

        return points, meshColors, faces

    def _compute_mesh(self, state):
        mav_pos = np.array([[state.north], [state.east], [-state.altitude]]) # NED
        R = rotation.euler_to_rotation(state.phi, state.theta, state.psi)
        points = R @ self.mav_points
        points += mav_pos

        # convert to ENU
        R = np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]])
        points = R @ points

        # we use columns as points, gl uses rows
        return points.T

    def __init__(self, state, window):
        self.mav_points, self.mav_meshColors, self.faces = self.get_mesh()
        mesh = self._compute_mesh(state)
        self.mav_body = gl.GLMeshItem(vertexes=mesh, faces=self.faces, vertexColors=self.mav_meshColors,
                                    drawEdges=True, smooth=False, computeNormals=False)
        window.addItem(self.mav_body)

    def update(self, state):
        mesh = self._compute_mesh(state)
        self.mav_body.setMeshData(vertexes=mesh, faces=self.faces, vertexColors=self.mav_meshColors)





