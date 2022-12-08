import pathlib

path1 = pathlib.Path.cwd()
folder_a = path1 / "folder_a"
# folder_a.mkdir(exist_ok=True)
#
# file_paths = [
#     folder_a/"private.img",
#     folder_a/"lyrics.txt",
#     folder_a/"avoid.vid",
#     folder_a/"inside.csv",
#     folder_a/"bible.txt",
#     folder_a/"looks.jpg",
# ]
#
# for path in file_paths:
#     path.touch()
#
# path1 = pathlib.Path.cwd()
# folder_a = path1 / "New_folder"
# folder_a.mkdir(exist_ok=True)
#
# file_paths = [
#     folder_a/"pate.img",
#     folder_a/"lyrics.txt",
#     folder_a/"void.vid",
#     folder_a/"outside.csv",
#     folder_a/"book.txt",
#     folder_a/"view.jpg",
# ]
#
# for path in file_paths:
#     path.touch()
#
#
#
#
#
#
# for files in folder_a.iterdir():
#     print(files.name)
#
# for files in path1.iterdir():
#         print(files.name)
#
# for files in path1.iterdir():
#         print(files.name)
#
# for files in path1.glob("*.py"):
#         print(files.name)
#
# for files in folder_a.glob("*.jpg"):
#         print(files.name)
#
# for files in path1.rglob("*.txt"):
#         print(files.name)
#
# for files in path1.rglob("*.csv"):
#         print(files.name)
#
# source = path1
# print(source)

source = path1 / "folder_a" / "looks.jpg"
destination = path1 / "New_folder" / "looks.jpg"
# destination = path1/"folder_a"/"month.py"
# source.replace(destination)
#
print(source)
#
# print(path1)
