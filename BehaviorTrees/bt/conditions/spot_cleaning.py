import bt_library as btl
from ..globals import SPOT_CLEANING

class SpotCleaning(btl.Condition):
    """
    Implementation of the condition "spot_cleaning".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("check if spot should be cleaned")

        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(SPOT_CLEANING, 0) == True\
            else self.report_failed(blackboard)