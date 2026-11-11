from . import mav_viewer
from .state import State

def main() -> None:
    ts = 0.05 # time step

    state = State()
    mav_view = mav_viewer.MavViewer()

    while True:
        mav_view.update(state)
        state.phi += ts
        state.north += ts

    raise SystemExit(mav_view.app.exec())
