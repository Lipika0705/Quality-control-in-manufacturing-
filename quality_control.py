import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample data for training the AI model
# Each product has [length, width, weight] as features, and 1 = passed, 0 = failed.
data = np.array([
    [9.5, 5.1, 100, 1],
    [9.8, 5.0, 102, 1],
    [10.2, 4.9, 98, 0],
    [9.7, 5.2, 101, 1],
    [10.1, 4.8, 97, 0],
    [9.9, 5.3, 99, 1],
    [9.3, 5.0, 95, 0],
    [10.3, 4.7, 96, 1],
])

# Splitting data into features (X) and labels (y)
X = data[:, :-1]  # All columns except the last one (features: length, width, weight)
y = data[:, -1]   # Last column is the label (passed = 1, failed = 0)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

# Test the model and print accuracy
y_pred = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# Function to get input from user and predict the quality
def get_user_input_and_predict():
    print("Enter the product data for AI prediction (Length, Width, Weight):")
    
    # Taking user input for the product data
    try:
        length = float(input("Length: "))
        width = float(input("Width: "))
        weight = float(input("Weight: "))
        
        # Predict whether the product passes or fails quality control
        input_data = np.array([[length, width, weight]])
        prediction = model.predict(input_data)
        
        # Show the result
        if prediction[0] == 1:
            print(f"Product with Length={length}, Width={width}, Weight={weight} → Passed Quality Control!")
        else:
            print(f"Product with Length={length}, Width={width}, Weight={weight} → Failed Quality Control!")
    except ValueError:
        print("Invalid input! Please enter numerical values for Length, Width, and Weight.")

# Call the function to get user input and predict
get_user_input_and_predict()
