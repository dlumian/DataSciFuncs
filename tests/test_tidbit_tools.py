import unittest
import os
from datascifuncs.tidbit_tools import load_json, write_json

class TestTidbitTools(unittest.TestCase):

    def setUp(self):
        # Set up a sample dictionary to be saved as JSON
        self.data = {"name": "John Doe", "age": 30, "city": "New York"}
        self.file_path = "test.json"

    def tearDown(self):
        # Clean up: Remove the test file if it exists
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_save_json(self):
        write_json(self.data, self.file_path)
        self.assertTrue(os.path.exists(self.file_path))

        # Verify the content is correctly written
        data_loaded = load_json(self.file_path)
        self.assertEqual(self.data, data_loaded)

    def test_load_json(self):
        # First, save the data to the file
        write_json(self.data, self.file_path)

        # Load data back and verify it matches the original
        data_loaded = load_json(self.file_path)
        self.assertEqual(self.data, data_loaded)

if __name__ == "__main__":
    unittest.main()