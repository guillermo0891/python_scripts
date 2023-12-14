import os

#directory name
directory = "my_files"

#check if directory already exits or not
if os.path.exists(directory):
  print("Directory already exists...")
else:
  print("Creating directory: "+directory)
  os.mkdir(directory)

#loop to create files
print("Creating files...")
for x in range(1, 11):
  with open(os.path.join(directory,"files{}.txt".format(x)), "w") as f:
    f.write("")
