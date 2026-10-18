
import os

def list_files(path):
    return [os.path.join(root, file) for root, dirs, files in os.walk(path) for file in files]

files = list_files('.')
