"""
Demonstration of two ways to rename a file using pathlib:

1. Path.rename() with a string target
2. Using Path.with_name() to construct a new path before renaming

Shows how rename() returns a new Path object.
"""
#difference between
from pathlib import Path
file_path=Path(__file__).resolve()/"file.txt"
renamed_file_path=file_path.rename("renamed_file.txt")   
print(renamed_file_path.name)
#and
file_path_with_name=file_path.with_name("renamed_file.txt")
file_path.rename(file_path_with_name)
