import os
import glob
import shutil

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
