import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import (
    classification_report, 
    confusion_matrix
)

from .tidbit_tools import write_json

def generate_classification_metrics(output_dir, y_train, y_pred_train, y_test=None, y_pred_test=None):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate and save classification report for training data
    train_report = classification_report(y_train, y_pred_train, output_dict=True)
    train_report_path = os.path.join(output_dir, 'train_classification_report.json')
    write_json(train_report, train_report_path)

    # Plot and save confusion matrix for training data
    train_cm = confusion_matrix(y_train, y_pred_train)
    plt.figure(figsize=(8, 6))
    sns.heatmap(train_cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix - Training Data')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.savefig(os.path.join(output_dir, 'train_confusion_matrix.png'))
    plt.close()

    if y_test is not None and y_pred_test is not None:
        # Generate and save classification report for test data
        test_report = classification_report(y_test, y_pred_test, output_dict=True)

        test_report_path = os.path.join(output_dir, 'test_classification_report.json')
        write_json(test_report, test_report_path)

        # Plot and save confusion matrix for test data
        test_cm = confusion_matrix(y_test, y_pred_test)
        plt.figure(figsize=(8, 6))
        sns.heatmap(test_cm, annot=True, fmt='d', cmap='Blues')
        plt.title('Confusion Matrix - Test Data')
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.savefig(os.path.join(output_dir, 'test_confusion_matrix.png'))
        plt.close()

        # Visualization to compare train and test metrics
        fig, ax = plt.subplots(1, 2, figsize=(16, 6))

        sns.heatmap(train_cm, annot=True, fmt='d', cmap='Blues', ax=ax[0])
        ax[0].set_title('Confusion Matrix - Training Data')
        ax[0].set_xlabel('Predicted')
        ax[0].set_ylabel('Actual')

        sns.heatmap(test_cm, annot=True, fmt='d', cmap='Blues', ax=ax[1])
        ax[1].set_title('Confusion Matrix - Test Data')
        ax[1].set_xlabel('Predicted')
        ax[1].set_ylabel('Actual')

        plt.suptitle('Comparison of Train and Test Confusion Matrices')
        plt.savefig(os.path.join(output_dir, 'comparison_confusion_matrices.png'))
        plt.close()

