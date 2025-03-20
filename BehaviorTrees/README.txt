#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Varleen Biketi
# 2/12/2024

Run main.py to compile the behavior tree.
               OR
Instructions for Running the Executable:

1. Ensure that your system has the required dependencies(for running python).
2. Open a command prompt or terminal in the directory containing this file.
3. Run the following command to execute the standalone executable:

   main.exe
(It is located in the dist folder) 
                       
Assumptions 
-Behavior tree is implemented such that all nodes in the tree are traversed. Hence, for
my implementation:
     a) The Dock task reports failed so that the priority composite can run the second branch 
        of the tree.
     b) Done Spot and Done general also report failed so that all nodes are traversed in the 
        selection composites.
-The value of the dusty spot sensor and clean floor task  are determined by a random generator.
