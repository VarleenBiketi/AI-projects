import bt_library as btl
import random

class CleanFloor(btl.Task):
    """
    Implementation of the Task "Clean Floor".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        somethingToClean = True
        while somethingToClean:
            self.print_message("Floor Clean? ")

            # Introduce randomness to determine success or failure
            if random.random() < 0.1:  
                somethingToClean = False
                
        return self.report_succeeded(blackboard)            