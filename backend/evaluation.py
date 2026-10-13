"""
Evaluation Pipeline Module
Computes detailed classification metrics and reports on saved model test splits.
"""
import numpy as np
from sklearn.metrics import classification_report, accuracy_score

def evaluate_predictions(true_labels, predicted_labels):
    """
    Generates quantitative performance metrics.
    Args:
        true_labels (list): Ground truth labels.
        predicted_labels (list): Model prediction labels.
    Returns:
        dict: Accuracy and classification report summary.
    """
    accuracy = accuracy_score(true_labels, predicted_labels)
    report = classification_report(true_labels, predicted_labels, target_names=["Fake (0)", "Real (1)"], output_dict=True)
    
    return {
        "accuracy": accuracy,
        "classification_report": report
    }