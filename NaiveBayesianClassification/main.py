import pandas as pd
import numpy as np

def load_data(filepath):
    """ Load data from a text file and convert space-separated values to a list of floats. """
    return pd.read_csv(filepath, header=None, sep=' ', dtype=float)

def interpolate_nan_values(data):
    """ Interpolate NaN values linearly and fill any remaining NaNs using forward/backward fill directly. """
    return data.apply(lambda x: x.interpolate().ffill().bfill(), axis=1)

def calculate_likelihood_distribution(velocity_data, num_bins=400):
    """ Calculate likelihood distribution for the velocity and handle zero counts properly. """
    likelihood = np.zeros(num_bins)
    counts = np.zeros(num_bins)

    for velocities in velocity_data.values:
        for velocity in velocities:
            if not np.isnan(velocity):
                index = int(np.clip(velocity / 0.5, 0, num_bins - 1))
                likelihood[index] += 1
                counts[index] += 1

    # Normalize likelihoods and prevent division by zero
    with np.errstate(divide='ignore', invalid='ignore'):
        likelihood = np.divide(likelihood, counts, where=counts != 0)
        likelihood = np.where(np.isnan(likelihood), 0, likelihood)  # Replace NaN with 0
    return likelihood

def naive_recursive_bayesian_classifier(velocities, likelihood_birds, likelihood_airplanes):
    """ Classify based on naive recursive Bayesian updates using log probabilities. """
    # Pre-calculate log likelihoods, safely handling zeros by replacing -inf with a large negative number
    log_likelihood_birds = np.log(likelihood_birds.clip(min=1e-300))
    log_likelihood_airplanes = np.log(likelihood_airplanes.clip(min=1e-300))
    
    # Initial probabilities (logarithmic)
    prob_bird = np.log(0.5)
    prob_airplane = np.log(0.5)

    for velocity in velocities:
        if not np.isnan(velocity):
            index = int(np.clip(velocity / 0.5, 0, len(likelihood_birds) - 1))
            prob_bird += log_likelihood_birds[index]
            prob_airplane += log_likelihood_airplanes[index]

    return 'b' if prob_bird > prob_airplane else 'a'

# Load and preprocess data
likelihood_data = load_data('likelihood.txt')
training_data = load_data('dataset.txt')
testing_data = load_data('testing.txt')

training_data_interpolated = interpolate_nan_values(training_data)
testing_data_interpolated = interpolate_nan_values(testing_data)

# Split training data into birds and airplanes
bird_tracks = training_data_interpolated.iloc[:10]
airplane_tracks = training_data_interpolated.iloc[10:]

# Calculate likelihood distributions
likelihood_birds = calculate_likelihood_distribution(bird_tracks)
likelihood_airplanes = calculate_likelihood_distribution(airplane_tracks)

# Classify the testing data
classifications = []
for index, track in testing_data_interpolated.iterrows():
    classification = naive_recursive_bayesian_classifier(track, likelihood_birds, likelihood_airplanes)
    classifications.append(classification)

# Output the classifications
for i, classification in enumerate(classifications, 1):
    classification_str = 'bird' if classification == 'b' else 'airplane'
    print(f"O{i} = {classification_str}")
