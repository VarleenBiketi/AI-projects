import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load the dataset
def load_data(file_path):
    df = pd.read_csv(file_path, header=None, delimiter=',',
                     names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])
    label_encoder = LabelEncoder()
    df['class'] = label_encoder.fit_transform(df['class'])
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y, scaler, label_encoder

# Build the model
def build_model(input_shape, num_classes):
    model = Sequential([
        Dense(64, activation='relu', input_shape=input_shape),
        Dense(32, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# Train the model
def train_model(model, X_train, y_train, X_val, y_val):
    history = model.fit(X_train, y_train, epochs=50, batch_size=10, validation_data=(X_val, y_val))
    return history

# Predict function with manual input
def predict_iris(model, scaler, label_encoder, sepal_length, sepal_width, petal_length, petal_width):
    data = scaler.transform([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(data)
    class_idx = prediction.argmax()
    return label_encoder.inverse_transform([class_idx])[0]

# Main function to execute model training and testing
def main():
    file_path = 'ANN - Iris data.txt' 
    X, y, scaler, label_encoder = load_data(file_path)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = build_model(input_shape=(4,), num_classes=3)
    history = train_model(model, X_train, y_train, X_val, y_val)
    
    # Evaluate the model on the validation set
    val_loss, val_accuracy = model.evaluate(X_val, y_val, verbose=0)
    print(f"Validation Accuracy: {val_accuracy:.2f}")

    # Interactive prediction
    while True:
        try:
            sepal_length = float(input("Enter sepal length (in cm): "))
            sepal_width = float(input("Enter sepal width (in cm): "))
            petal_length = float(input("Enter petal length (in cm): "))
            petal_width = float(input("Enter petal width (in cm): "))
            prediction = predict_iris(model, scaler, label_encoder, sepal_length, sepal_width, petal_length, petal_width)
            print(f"Predicted Iris class: {prediction}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

        if input("Predict another? (yes/no): ").strip().lower() != 'yes':
            break

if __name__ == "__main__":
    main()
