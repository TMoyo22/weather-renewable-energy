import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error


def load_data(csv_path):
    df = pd.read_csv(csv_path)
    print(df.head(5))
    return df


def prepare_data(df):
    df = df.dropna()

    # 👉 Filter out zero energy values
    df = df[df["Energy delta[Wh]"] > 0]

    # Target and features
    y = df["Energy delta[Wh]"]
    X = df.drop(columns=["Energy delta[Wh]"])

    # Optionally remove problematic columns
    columns_to_drop = ["Unnamed: 0", "timestamp", "id"]  # Adjust based on your dataset
    for col in columns_to_drop:
        if col in X.columns:
            X = X.drop(columns=[col])

    # Identify low-cardinality object (categorical) columns
    low_card_cols = [
        col for col in X.columns if X[col].dtype == "object" and X[col].nunique() < 50
    ]
    numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    selected_cols = numeric_cols + low_card_cols
    X = X[selected_cols]

    # Debug: Show most problematic columns
    print("[DEBUG] High cardinality columns:")
    print(X.nunique().sort_values(ascending=False).head(10))

    # Apply one-hot encoding only on low-cardinality object columns
    X = pd.get_dummies(X, columns=low_card_cols, drop_first=True)

    return train_test_split(X, y, test_size=0.2, random_state=42)


def train_models(X_train, y_train):
    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    }

    for name, model in models.items():
        model.fit(X_train, y_train)

    return models


def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    return y_test, predictions, mae, mse
