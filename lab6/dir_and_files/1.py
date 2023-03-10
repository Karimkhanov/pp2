import os

path = "C:\pp2\lab2" #Example

# List only directories
print("Directories:")
for entry in os.listdir(path):
    if os.path.isdir(os.path.join(path, entry)):
        print(entry)

# List only files
print("Files:")
for entry in os.listdir(path):
    if os.path.isfile(os.path.join(path, entry)):
        print(entry)

# List all directories and files
print("All Directories and Files:")
for entry in os.listdir(path):
    print(entry)
