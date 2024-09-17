# tests/test_reset_project.py

import unittest
import os
import shutil
from tidbits.reset_project import remove_files, remove_directories, reset_notebooks

class TestResetProject(unittest.TestCase):

    def setUp(self):
        # Set up files and directories for testing
        self.test_dir = "test_dir"
        self.test_file_1 = os.path.join(self.test_dir, "file1.txt")
        self.test_file_2 = os.path.join(self.test_dir, "file2.txt")
        self.test_subdir = os.path.join(self.test_dir, "subdir")

        os.makedirs(self.test_dir, exist_ok=True)
        os.makedirs(self.test_subdir, exist_ok=True)

        with open(self.test_file_1, 'w') as f:
            f.write("Sample content")
        with open(self.test_file_2, 'w') as f:
            f.write("Sample content")

        # Set up a simple notebook file for reset_notebooks
        self.test_notebook = os.path.join(self.test_dir, "test_notebook.ipynb")
        notebook_content = '{"cells": [{"cell_type": "code", "outputs": ["output1", "output2"]}], "metadata": {}}'
        with open(self.test_notebook, 'w') as f:
            f.write(notebook_content)

    def tearDown(self):
        # Clean up after tests
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_remove_files(self):
        remove_files([self.test_file_1, self.test_file_2])
        self.assertFalse(os.path.exists(self.test_file_1))
        self.assertFalse(os.path.exists(self.test_file_2))

    def test_remove_directories(self):
        remove_directories([self.test_subdir])
        self.assertFalse(os.path.exists(self.test_subdir))

    def test_reset_notebooks(self):
        reset_notebooks(self.test_dir)

        # Check that the notebook's outputs have been reset
        with open(self.test_notebook, 'r') as f:
            content = f.read()
        self.assertIn('"outputs": []', content)
        self.assertNotIn('"outputs": ["output1", "output2"]', content)

if __name__ == "__main__":
    unittest.main()
