import unittest
import numpy as np
import shutil
import os
from tidbits.metrics import generate_classification_metrics

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

    def test_train_only(self):
        generate_classification_metrics(self.output_dir, self.y_train, self.y_pred_train)

        # Check if train files are generated
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'train_classification_report.json')))
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'train_confusion_matrix.png')))

        # Check that no test files are generated
        self.assertFalse(os.path.exists(os.path.join(self.output_dir, 'test_classification_report.json')))
        self.assertFalse(os.path.exists(os.path.join(self.output_dir, 'test_confusion_matrix.png')))
        self.assertFalse(os.path.exists(os.path.join(self.output_dir, 'comparison_confusion_matrices.png')))

    def test_train_and_test(self):
        generate_classification_metrics(self.output_dir, self.y_train, self.y_pred_train, self.y_test, self.y_pred_test)

        # Check if train files are generated
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'train_classification_report.json')))
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'train_confusion_matrix.png')))

        # Check if test files are generated
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'test_classification_report.json')))
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'test_confusion_matrix.png')))
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'comparison_confusion_matrices.png')))

if __name__ == "__main__":
    unittest.main()
