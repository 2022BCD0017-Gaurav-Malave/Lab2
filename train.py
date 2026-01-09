"""
Wine Quality Prediction - Training Script
Lab 2: Automated Training with GitHub Actions

This script trains a regression model on the Wine Quality dataset,
evaluates it, and saves results for automated CI/CD workflows.
"""

import pandas as pd
import numpy as np
import json
import os
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
import joblib


def load_data(filepath='dataset/winequality-red.csv'):
    """Load the wine quality dataset."""
    print(f"Loading dataset from {filepath}...")
    df = pd.read_csv(filepath, sep=';')
    print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


def preprocess_data(df, test_size=0.3, random_state=42):
    """
    Preprocess the dataset:
    - Split features and target
    - Train-test split
    - Feature scaling
    """
    print("\nPreprocessing data...")
    
    # Separate features and target
    X = df.drop('quality', axis=1)
    y = df['quality']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    print(f"Train set: {X_train.shape[0]} samples")
    print(f"Test set: {X_test.shape[0]} samples")
    
    # Feature scaling
    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("Features scaled using StandardScaler")
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


def train_model(X_train, y_train):
    """Train the regression model."""
    print("\nTraining model...")
    
    # Initialize and train model
    model = Ridge(alpha=1.0)
    model.fit(X_train, y_train)
    
    print(f"Model trained: {model.__class__.__name__}")
    return model


def evaluate_model(model, X_test, y_test):
    """Evaluate model performance."""
    print("\nEvaluating model...")
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mse)
    
    # Print metrics
    print(f"\n{'='*50}")
    print("EVALUATION METRICS")
    print(f"{'='*50}")
    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
    print(f"R² Score: {r2:.4f}")
    print(f"{'='*50}\n")
    
    return {
        'mse': float(mse),
        'rmse': float(rmse),
        'r2_score': float(r2)
    }


def save_model(model, scaler, filepath='models/model.pkl'):
    """Save the trained model and scaler."""
    print(f"Saving model to {filepath}...")
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    # Save model and scaler together
    model_data = {
        'model': model,
        'scaler': scaler
    }
    joblib.dump(model_data, filepath)
    print("Model saved successfully")


def save_results(metrics, model, filepath='results/results.json'):
    """Save evaluation metrics to JSON file."""
    print(f"Saving results to {filepath}...")
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    # Prepare results dictionary
    results = {
        'timestamp': datetime.now().isoformat(),
        'model_type': model.__class__.__name__,
        'metrics': metrics
    }
    
    # Save to JSON
    with open(filepath, 'w') as f:
        json.dump(results, f, indent=4)
    
    print("Results saved successfully")
    return results


def main():
    """Main training pipeline."""
    print("="*60)
    print("Wine Quality Prediction - Model Training")
    print("="*60)
    
    try:
        # Load data
        df = load_data()
        
        # Preprocess data
        X_train, X_test, y_train, y_test, scaler = preprocess_data(df)
        
        # Train model
        model = train_model(X_train, y_train)
        
        # Evaluate model
        metrics = evaluate_model(model, X_test, y_test)
        
        # Save model
        save_model(model, scaler)
        
        # Save results
        results = save_results(metrics, model)
        
        print("\n" + "="*60)
        print("Training completed successfully!")
        print("="*60)
        
        return 0
        
    except Exception as e:
        print(f"\nError during training: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
