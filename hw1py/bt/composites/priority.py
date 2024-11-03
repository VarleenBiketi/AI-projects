import bt_library as btl

class Priority(btl.Composite):
    """
    Specific implementation of the priority composite.
    """

    def __init__(self, children: btl.NodeListType):
        """
        Default constructor.

        :param children: List of children for this node
        """
        super().__init__(children)

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """
        running_child = self.additional_information(blackboard, 0)

        for child_position in range(running_child,len(self.children)):
            child = self.children[child_position]

            # Skip nodes with lower priority if there is a running child
            if running_child is not None and child_position < running_child:
                continue

            result_child = child.run(blackboard)

            if result_child == btl.ResultEnum.SUCCEEDED:
                return self.report_succeeded(blackboard, 0)

            if result_child == btl.ResultEnum.RUNNING:
                return self.report_running(blackboard, child_position)

        return self.report_failed(blackboard, 0)
