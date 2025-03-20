import bt_library as btl
from ..globals import GENERAL_CLEANING


class DoneGeneral(btl.Task):
    """
    Implementation of the Task "Done General".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Done General cleaning")

        blackboard.set_in_environment(GENERAL_CLEANING, False)

        return self.report_failed(blackboard)