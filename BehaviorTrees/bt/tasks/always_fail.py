import bt_library as btl


class AlwaysFail(btl.Task):
    """
    Implementation of the Task "Always Fail".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Always Failing")

        return self.report_failed(blackboard)
