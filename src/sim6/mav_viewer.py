import numpy as np
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import pyqtgraph.Vector as Vector
from . import draw_mav

class MavViewer:
    def __init__(self):
        # initialize Qt gui application and window
        self.app = pg.mkQApp()  # initialize QT
        self.window = gl.GLViewWidget()  # initialize the view object
        self.window.setWindowTitle('MAV Viewer')
        self.window.setGeometry(0, 0, 1000, 1000)  # args: upper_left_x, upper_right_y, width, height

        grid = gl.GLGridItem() # make a grid to represent the ground
        grid.scale(20, 20, 20) # set the size of the grid (distance between each line)
        self.window.addItem(grid) # add grid to viewer

        axes = gl.GLAxisItem()
        axes.setSize(x=25, y=25, z=25)
        axes.translate(0, 0, 0.05)
        self.window.addItem(axes)

        # in ENU
        x_label = gl.GLTextItem(pos=(25, 0, 0), text='X', color='red')
        y_label = gl.GLTextItem(pos=(0, 25, 0), text='Y', color='green')
        z_label = gl.GLTextItem(pos=(0, 0, 25), text='Z', color='blue')

        self.window.addItem(x_label)
        self.window.addItem(y_label)
        self.window.addItem(z_label)

        self.window.setCameraPosition(distance=200) # distance from center of plot to camera
        self.window.setBackgroundColor('k')  # set background color to black
        self.window.show()  # display configured window
        self.window.raise_() # bring window to the front
        self.plot_initialized = False # has the mav been plotted yet?

    def update(self, state):
        if not self.plot_initialized:
            self.mav_plot = draw_mav.DrawMav(state, self.window)
            self.plot_initialized = True
        else:
            self.mav_plot.update(state)

        # redraw
        self.app.processEvents()
