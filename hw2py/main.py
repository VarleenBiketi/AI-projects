import heapq
import random

class PancakeProblem:
    def __init__(self, pancakes):
        # Initialize the PancakeProblem instance with the initial state (stack of pancakes)
        self.initial_state = tuple(pancakes)

    def actions(self, state):
        # Define possible actions as the positions where the spatula can be inserted
        return range(1, len(state) + 1)

    def result(self, state, action):
        # Compute the new state after flipping pancakes above the specified position
        return tuple(state[:action][::-1] + state[action:])

    def is_goal_state(self, state):
        # Check if the state is the goal state, i.e., pancakes are sorted in descending order
        return state == tuple(sorted(state, reverse=True))

    def backward_cost(self, state):
        # Compute the backward cost, which is the number of pancakes out of place
        return sum(1 for i, j in zip(state, sorted(state, reverse=True)) if i != j)

    def forward_cost(self, state):
        # Gap Heuristic: Count the number of stack positions with non-adjacent sized pancakes
        return sum(1 for i in range(len(state) - 1) if abs(state[i] - state[i + 1]) > 1)

def uniform_cost_search(problem):
    # Priority queue for UCS with initial cost and state
    frontier = [(0, problem.initial_state)]
    explored = set()  # Set to store explored states

    while frontier:
        cost, state = heapq.heappop(frontier)
        if problem.is_goal_state(state):
            return state  # Return the goal state when found
        explored.add(tuple(state))  # Convert the state to tuple before adding to the explored set

        for action in problem.actions(state):
            child_state = problem.result(state, action)
            child_tuple = tuple(child_state)
            if child_tuple not in explored:
                heapq.heappush(frontier, (problem.backward_cost(child_state), child_state))

def a_star_search(problem):
    # Priority queue for A* with initial cost and state
    frontier = [(0 + problem.forward_cost(problem.initial_state), problem.initial_state)]
    explored = set()  # Set to store explored states

    while frontier:
        _, state = heapq.heappop(frontier)
        if problem.is_goal_state(state):
            return state  # Return the goal state when found
        explored.add(tuple(state))  # Convert the state to tuple before adding to the explored set

        for action in problem.actions(state):
            child_state = problem.result(state, action)
            child_tuple = tuple(child_state)
            if child_tuple not in explored:
                heapq.heappush(frontier, (problem.backward_cost(child_state) + problem.forward_cost(child_state), child_state))


# Generate a random list of pancakes from 1 to 10
random_pancakes = random.sample(range(1, 11), 10)
print("Randomly generated list of pancakes:", random_pancakes)

problem = PancakeProblem(random_pancakes)

print("Uniform Cost Search Result:")
print(uniform_cost_search(problem))

print("A* Search Result:")
print(a_star_search(problem))
