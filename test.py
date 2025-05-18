import os

file_path = 'uploads/audio0.mp3'
if os.path.exists(file_path):
    print("File exists at:", file_path)
else:
    print("File does not exist at:", file_path)
