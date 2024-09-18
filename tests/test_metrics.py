import unittest
import numpy as np
import shutil
import os
from datascifuncs.metrics import (
    generate_classification_metrics, 
    generate_metrics, 
    compare_confusion_matrices
)


class TestClassificationMetrics(unittest.TestCase):

    def setUp(self):
        self.output_dir = 'test_output'
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        # Example data
        self.y_train = np.array([0, 1, 0, 1, 0])
        self.y_pred_train = np.array([0, 1, 0, 0, 0])
        self.y_test = np.array([0, 1, 1, 1, 0])
        self.y_pred_test = np.array([0, 1, 0, 1, 0])

    def tearDown(self):
        # Clean up the output directory after tests
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)

    def test_generate_metrics(self):
        # Test metrics generation for training data
        cm_train = generate_metrics(self.output_dir, self.y_train, self.y_pred_train, 'train')
        
        # Check if train files are generated
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'train_classification_report.json')))
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'train_confusion_matrix.png')))

        # Test metrics generation for test data
        cm_test = generate_metrics(self.output_dir, self.y_test, self.y_pred_test, 'test')

        # Check if test files are generated
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'test_classification_report.json')))
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'test_confusion_matrix.png')))

        # Ensure confusion matrices are returned correctly
        self.assertIsNotNone(cm_train)
        self.assertIsNotNone(cm_test)

    def test_compare_confusion_matrices(self):
        # Generate confusion matrices
        cm_train = generate_metrics(self.output_dir, self.y_train, self.y_pred_train, 'train')
        cm_test = generate_metrics(self.output_dir, self.y_test, self.y_pred_test, 'test')

        # Test the comparison of confusion matrices
        compare_confusion_matrices(self.output_dir, cm_train, cm_test)
        
        # Check if the comparison file is generated
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'comparison_confusion_matrices.png')))

    def test_generate_classification_metrics(self):
        # Test the full pipeline with both training and test data
        generate_classification_metrics(self.output_dir, self.y_train, self.y_pred_train, self.y_test, self.y_pred_test)

        # Check if all files are generated
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'train_classification_report.json')))
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'train_confusion_matrix.png')))
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'test_classification_report.json')))
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'test_confusion_matrix.png')))
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'comparison_confusion_matrices.png')))

        # Test the pipeline with only training data
        generate_classification_metrics(self.output_dir, self.y_train, self.y_pred_train)

        # Check if only train files are generated
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'train_classification_report.json')))
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'train_confusion_matrix.png')))
        self.assertFalse(os.path.exists(os.path.join(self.output_dir, 'test_classification_report.json')))
        self.assertFalse(os.path.exists(os.path.join(self.output_dir, 'test_confusion_matrix.png')))
        self.assertFalse(os.path.exists(os.path.join(self.output_dir, 'comparison_confusion_matrices.png')))

if __name__ == "__main__":
    unittest.main()
