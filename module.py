from pathlib import Path
path=Path("ecommerce")
print(path.exists())
# path1=Path("emails")
# print(path1.mkdir())
path3=Path()
for file in path3.glob("*.py"):
    print(file)

