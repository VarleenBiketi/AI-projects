import bt_library as btl
from ..globals import SPOT_CLEANING


class DoneSpot(btl.Task):
    """
    Implementation of the Task "Done Spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Not Done Spot cleaning")

        blackboard.set_in_environment(SPOT_CLEANING, False)

        return self.report_failed(blackboard)