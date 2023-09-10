import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, accuracy_score, precision_score, recall_score, f1_score


def perform_regression(data, feature_names, target_name):
    """
    Perform linear regression on the given data.

    Parameters:
    - data (array-like): The input data as a 2D array.
    - feature_names (list): A list of feature names.
    - target_name (str): The name of the target variable.

    Returns:
    - model: Trained linear regression model.
    - metrics (dict): Dictionary containing regression metrics.
    """

    # Create a DataFrame from the input data
    df = pd.DataFrame(data, columns=feature_names + [target_name])

    # Separate input features and target variable
    X = df[feature_names]
    y = df[target_name]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Instantiate and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = model.predict(X_test)

    # Calculate regression metrics
    metrics = {
        'MAE': mean_absolute_error(y_test, y_pred),
        'MSE': mean_squared_error(y_test, y_pred),
        'R2 Score': r2_score(y_test, y_pred)
    }

    return model, metrics


def perform_classification(data, feature_names, target_name, classifier):
    """
    Perform classification on the given data using the specified classifier.

    Parameters:
    - data (array-like): The input data as a 2D array.
    - feature_names (list): A list of feature names.
    - target_name (str): The name of the target variable.
    - classifier: The classifier to use (e.g., DecisionTreeClassifier, RandomForestClassifier, etc.).

    Returns:
    - model: Trained classifier model.
    - metrics (dict): Dictionary containing classification metrics.
    """

    # Create a DataFrame from the input data
    df = pd.DataFrame(data, columns=feature_names + [target_name])

    # Separate input features and target variable
    X = df[feature_names]
    y = df[target_name]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Instantiate and train the classifier
    model = classifier()
    model.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = model.predict(X_test)

    # Calculate classification metrics
    metrics = {
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred),
        'Recall': recall_score(y_test, y_pred),
        'F1 Score': f1_score(y_test, y_pred)
    }

    return model, metrics
