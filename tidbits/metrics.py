import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import (
    classification_report, 
    confusion_matrix
)

from .tidbit_tools import write_json

def generate_metrics(output_dir, y_true, y_pred, label):
    """Generate classification report and confusion matrix for a given dataset."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate and save classification report
    report = classification_report(y_true, y_pred, output_dict=True)
    write_json(report, os.path.join(output_dir, f'{label}_classification_report.json'))

    # Plot and save confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'Confusion Matrix - {label.capitalize()} Data')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.savefig(os.path.join(output_dir, f'{label}_confusion_matrix.png'))
    plt.close()

    return cm


def compare_confusion_matrices(output_dir, cm_train, cm_test):
    """Create a visualization to compare train and test confusion matrices."""
    fig, ax = plt.subplots(1, 2, figsize=(16, 6))

    sns.heatmap(cm_train, annot=True, fmt='d', cmap='Blues', ax=ax[0])
    ax[0].set_title('Confusion Matrix - Training Data')
    ax[0].set_xlabel('Predicted')
    ax[0].set_ylabel('Actual')

    sns.heatmap(cm_test, annot=True, fmt='d', cmap='Blues', ax=ax[1])
    ax[1].set_title('Confusion Matrix - Test Data')
    ax[1].set_xlabel('Predicted')
    ax[1].set_ylabel('Actual')

    plt.suptitle('Comparison of Train and Test Confusion Matrices')
    plt.savefig(os.path.join(output_dir, 'comparison_confusion_matrices.png'))
    plt.close()

def generate_classification_metrics(output_dir, y_train, y_pred_train, y_test=None, y_pred_test=None):
    # Generate metrics for training data
    cm_train = generate_metrics(output_dir, y_train, y_pred_train, 'train')

    cm_test = None
    if y_test is not None and y_pred_test is not None:
        # Generate metrics for test data
        cm_test = generate_metrics(output_dir, y_test, y_pred_test, 'test')

        # Compare and visualize if both train and test data are available
        compare_confusion_matrices(output_dir, cm_train, cm_test)
