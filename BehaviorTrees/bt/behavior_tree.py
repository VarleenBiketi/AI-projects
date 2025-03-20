#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 2.0.0 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
#

import bt_library as btl

import bt as bt

# Instantiate the tree according to the assignment. The following are just examples.

# Example 1:
#tree_root = bt.CleanFloor()

# Example 2:
#tree_root = bt.Selection(
#    [
#        bt.BatteryLessThan30(),
#       btl.Timer(5, bt.FindHome())
#    ]
# )

# Example 3:
#tree_root = bt.Sequence(
# [
#      bt.BatteryLessThan30(),
#    btl.Timer(20, bt.CleanSpot()),
#     bt.CleanFloor()
#   ]
#)
tree_1 = bt.Sequence(
[
   bt.BatteryLessThan30(),
   bt.FindHome(),
   bt.GoHome(),
   bt.Dock()
]
)

tree_2 = bt.Sequence(
[
   bt.SpotCleaning(),
   btl.Timer(20, bt.CleanSpot()),
   bt.DoneSpot()
]
)

tree_3 = bt.Sequence(
[
   bt.DustySpot(),
   btl.Timer(35, bt.CleanSpot()),
   bt.AlwaysFail()
]
)

tree_4 = bt.Priority(
[
   tree_3,
   bt.CleanFloor()
]
)

tree_5 = bt.Sequence(
[
   tree_4,
   bt.DoneGeneral()
]
)

tree_6 = bt.Sequence(
[
   bt.GeneralCleaning(),
   tree_5
]
)

tree_7= bt.Selection(
[
   tree_2,
   tree_6
]
)

tree_root = bt.Priority(
[
   tree_1,
   tree_7,
   bt.DoNothing()
]
)


