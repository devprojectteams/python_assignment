from pathlib import Path

print(Path.home())

file_path = Path.home() / "my_folder" / "my_marv.txt"
file_path.mkdir(exist_ok=True)
new_file = file_path / "my_file.txt"
new_file.touch(exist_ok=True)
new_file.touch()

print(file_path.exists())
print(new_file.exists())

print(new_file.name)
print(new_file.parent)