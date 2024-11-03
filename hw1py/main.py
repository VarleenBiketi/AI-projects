#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 2.0.0 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
import random

from bt.behavior_tree import tree_root
from bt.globals import BATTERY_LEVEL, GENERAL_CLEANING, SPOT_CLEANING, DUSTY_SPOT_SENSOR, HOME_PATH


# Main body of the assignment
current_blackboard = btl.Blackboard()
current_blackboard.set_in_environment(BATTERY_LEVEL, 29)
current_blackboard.set_in_environment(SPOT_CLEANING, True)
current_blackboard.set_in_environment(GENERAL_CLEANING, True)
current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, False)
current_blackboard.set_in_environment(HOME_PATH, "")

done = False
while not done:
    # Each cycle in this while-loop is equivalent to 1 second time

    # Step 1: Change the environment
    if random.random() < 0.5:
        current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, False)
    else:
        current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, True)

    # Step 2: Evaluating the tree
    result = tree_root.run(current_blackboard)
    
    # Step 3: Checking if loop should be terminated
    if result == btl.ResultEnum.SUCCEEDED or result == btl.ResultEnum.FAILED:
        done = True
    
