import bt_library as btl
from ..globals import BATTERY_LEVEL


class Dock(btl.Task):
    """
    Implementation of the Task "Dock".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Docked")

        blackboard.set_in_environment(BATTERY_LEVEL, 31)

        return self.report_failed(blackboard)
