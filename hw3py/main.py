#
# The Knapsack Problem
# CS 131 - Artificial Intelligence
#
# Varleen Biketi
# 3/9/2024

import random

# Given data
boxes = [
    (20, 6), (30, 5), (60, 8), (90, 7), (50, 6),
    (70, 9), (30, 4), (30, 5), (70, 4), (20, 9),
    (20, 2), (60, 1)
]
max_weight = 250
population_size = 50
generations = 100

# Function to generate a random individual (genome)
def generate_individual():
    return [random.choice([0, 1]) for _ in range(len(boxes))]

# Function to calculate the fitness of an individual
def fitness(individual):
    total_weight = sum(box[0] * included for box, included in zip(boxes, individual))
    total_importance = sum(box[1] * included for box, included in zip(boxes, individual))
    
    # Penalize solutions exceeding weight limit
    if total_weight > max_weight:
        return 0
    else:
        return total_importance

# Function for crossover (recombination) of two parents
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Function for mutation of an individual
def mutate(individual, mutation_rate):
    mutated_individual = individual.copy()
    for i in range(len(mutated_individual)):
        if random.random() < mutation_rate:
            mutated_individual[i] = 1 - mutated_individual[i]  # Flip the bit
    return mutated_individual

# Main genetic algorithm function
def genetic_algorithm():
    # Generate an initial population of random individuals
    population = [generate_individual() for _ in range(population_size)]

    # Iterate through generations
    for generation in range(generations):
        # Sort the population based on fitness and keep the top 50%
        population = sorted(population, key=fitness, reverse=True)[:population_size]

        # Cull population by 50%
        population = population[:population_size // 2]

        # Create offspring through crossover and mutation
        offspring = []
        for _ in range(population_size // 2):
            # Select two parents randomly from the current population
            parent1, parent2 = random.choices(population, k=2)
            
            # Apply crossover to create two children
            child1, child2 = crossover(parent1, parent2)
            
            # Apply mutation to children
            child1 = mutate(child1, mutation_rate=0.1)
            child2 = mutate(child2, mutation_rate=0.1)
            
            # Add children to the offspring
            offspring.extend([child1, child2])

        # Add offspring to the population
        population.extend(offspring)

    # Find the best solution in the final population
    best_solution = max(population, key=fitness)
    return best_solution

# Run the genetic algorithm
best_solution = genetic_algorithm()

# Display the result
selected_boxes = [boxes[i] for i in range(len(boxes)) if best_solution[i] == 1]
total_weight = sum(box[0] for box in selected_boxes)
total_importance = sum(box[1] for box in selected_boxes)

print("Selected Boxes:", selected_boxes)
print("Total Weight:", total_weight)
print("Total Importance:", total_importance)
