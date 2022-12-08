import pathlib
# import shutil

path1 = pathlib.Path.cwd()
Chapter_12_Practice = path1 / "Chapter_12_Practice"
Chapter_12_Practice.mkdir(exist_ok=True)

# Chapter =[ Chapter_12_Practice / "Chapter_13_Practice",
# Chapter_12_Practice / "Chapter_14_Practice", Chapter_12_Practice / "documents"]
# Chapter_12_Practice = path1 / "chapter_12_Practice" / "documents"
# Chapter_12_Practice.mkdir(exist_ok=True)
new = [Chapter_12_Practice / "image10.png", Chapter_12_Practice / "image20.gif", Chapter_12_Practice / "image30.png",
       Chapter_12_Practice / "image40.jpg"]
# new.touch(exist_ok=True)

for path in new:
    path.touch(exist_ok=True)

# Chapter_12_Practice = path1 / "chapter_12_Practice" /"images2"
# Chapter_12_Practice.mkdir(exist_ok=True)

source = path1 / "chapter_12_Practice" /"images4.jpg"
source.touch(exist_ok=True)
print(source.exists())
# destination = path1 / "chapter_12_Practice" / "images" / "images3.png"/"images1.png"/"images2"/"images4.jpg"
destination = path1 / "chapter_12_Practice" / "images" / "images4.jpg"
destination.touch(exist_ok=True)
print(destination.exists())
# shutil.move(source, destination)
source.replace(destination)

