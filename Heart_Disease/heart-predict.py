import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score

# Load the UCI Heart Disease Dataset
data = pd.read_csv('heart.csv')

# Define features and target variable
X = data.drop(columns=['num'])
y = data['num']

# Identify categorical columns
categorical_cols = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal', 'dataset']
numeric_cols = [col for col in X.columns if col not in categorical_cols and col != 'id']

# Preprocessing pipeline for numeric and categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ]), numeric_cols),
        ('cat', Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ]), categorical_cols)
    ])

# Create a pipeline with preprocessing and a LogisticRegression model
model_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', LogisticRegression(max_iter=1000))
])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the model
model_pipeline.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model_pipeline.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy:.2f}')

# Function to predict based on user input
def predict_heart_disease():
    print("Enter values for the following features:")
    id_val = input("ID: ")
    age = float(input("Age: "))
    sex = input("Sex (1 = Male, 0 = Female): ")
    dataset = input("Dataset: ")
    cp = input("Chest Pain Type (0-3): ")
    trestbps = float(input("Resting Blood Pressure: "))
    chol = float(input("Serum Cholesterol: "))
    fbs = input("Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False): ")
    restecg = input("Resting Electrocardiographic Results (0-2): ")
    thalach = float(input("Maximum Heart Rate Achieved: "))
    exang = input("Exercise-Induced Angina (1 = Yes, 0 = No): ")
    oldpeak = float(input("ST Depression Induced by Exercise: "))
    slope = input("Slope of the Peak Exercise ST Segment (0-2): ")
    ca = input("Number of Major Vessels Colored by Fluoroscopy (0-3): ")
    thal = input("Thalassemia (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect): ")
    
    # Create a DataFrame for the input
    user_data = pd.DataFrame([[id_val, age, sex, dataset, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],
                             columns=X.columns)
    
    # Ensure the input data goes through the same preprocessing pipeline
    user_data_preprocessed = model_pipeline.named_steps['preprocessor'].transform(user_data)
    prediction = model_pipeline.named_steps['model'].predict(user_data_preprocessed)
    intensity = "High" if prediction[0] == 1 else "Low"
    print(f"The predicted intensity of heart disease is: {intensity}")

# Call the function to predict based on user input
predict_heart_disease()
