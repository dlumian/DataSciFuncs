import unittest
import os
import glob
import nbformat
from datascifuncs.reset_project import remove_files, remove_directories, reset_notebooks

class TestResetProject(unittest.TestCase):

    def setUp(self):
        self.test_dir = 'test_dir'
        self.test_files = ['file1.csv', 'file2.json', 'file3.txt', 'notebook1.ipynb', 'notebook2.ipynb']
        os.makedirs(self.test_dir, exist_ok=True)
        
        for file_name in self.test_files:
            file_path = os.path.join(self.test_dir, file_name)
            if file_name.endswith('.ipynb'):
                # Create a sample notebook with outputs
                nb = nbformat.v4.new_notebook()
                nb.cells.append(nbformat.v4.new_code_cell("print('Hello, world!')", outputs=["output1"]))
                with open(file_path, 'w') as f:
                    nbformat.write(nb, f)
            else:
                with open(file_path, 'w') as f:
                    f.write("Sample content")

    def tearDown(self):
        # Clean up: Remove the test directory after tests
        if os.path.exists(self.test_dir):
            for file_name in glob.glob(os.path.join(self.test_dir, '*')):
                os.remove(file_name)
            os.rmdir(self.test_dir)

    def test_remove_files(self):
        # Remove CSV and JSON files
        remove_files([os.path.join(self.test_dir, '*.csv'), os.path.join(self.test_dir, '*.json')])

        # Check that the CSV and JSON files are removed
        remaining_files = os.listdir(self.test_dir)
        self.assertNotIn('file1.csv', remaining_files)
        self.assertNotIn('file2.json', remaining_files)

        # Check that the TXT and IPYNB files are not removed
        self.assertIn('file3.txt', remaining_files)
        self.assertIn('notebook1.ipynb', remaining_files)
        self.assertIn('notebook2.ipynb', remaining_files)

    def test_remove_directories(self):
        # Remove the test directory
        remove_directories([self.test_dir])

        # Check that the directory is removed
        self.assertFalse(os.path.exists(self.test_dir))

    def test_reset_notebooks(self):
        # Apply reset to all notebooks in the test directory
        reset_notebooks(self.test_dir)

        # Verify that the outputs in the notebooks have been cleared
        for notebook_file in ['notebook1.ipynb', 'notebook2.ipynb']:
            notebook_path = os.path.join(self.test_dir, notebook_file)
            with open(notebook_path, 'r') as f:
                nb = nbformat.read(f, as_version=4)
                for cell in nb.cells:
                    if cell.cell_type == 'code':
                        self.assertEqual(cell.outputs, [])

if __name__ == "__main__":
    unittest.main()
