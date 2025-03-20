import bt_library as btl
from ..globals import HOME_PATH


class GoHome(btl.Task):
    """
    Implementation of the Task "Go Home".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Going home")

        self.print_message(blackboard.get_in_environment(HOME_PATH, 0))

        return self.report_succeeded(blackboard)