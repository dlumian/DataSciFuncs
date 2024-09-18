import os
import glob
import shutil
import nbformat
from nbconvert.preprocessors import ClearOutputPreprocessor

def remove_files(file_patterns):
    for pattern in file_patterns:
        for file in glob.glob(pattern):
            try:
                os.remove(file)
                print(f"Removed file: {file}")
            except OSError as e:
                print(f"Error removing file {file}: {e}")

def remove_directories(directories):
    for directory in directories:
        try:
            shutil.rmtree(directory)
            print(f"Removed directory: {directory}")
        except OSError as e:
            print(f"Error removing directory {directory}: {e}")

def reset_notebooks(notebook_dir):
    notebook_files = glob.glob(os.path.join(notebook_dir, "*.ipynb"))
    
    for notebook_file in notebook_files:
        try:
            with open(notebook_file, 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)
            
            # Clear outputs
            clear_output_preprocessor = ClearOutputPreprocessor()
            nb, _ = clear_output_preprocessor.preprocess(nb, {})

            # Save the cleared notebook
            with open(notebook_file, 'w', encoding='utf-8') as f:
                nbformat.write(nb, f)
            
            print(f"Cleared output in notebook: {notebook_file}")

        except Exception as e:
            print(f"Failed to clear output in {notebook_file}: {e}")
