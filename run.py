my_files = {
  "root" : [
    "file-a.txt",
    {
      "directory-a": [
        "file-a.txt",
        "file-b.json",
        {
          "directory-c" : [
            "file-c.csv"
          ]
        }
      ]
    },
    {
      "directory-b" : [
        "file-d.txt",
        "file-e.csv"
      ]
    },
    {
      "directory-c" : [
      ]
    }
  ],
}

# Directory Search by name
def FindDirectory(name, files):
    if isinstance(files, dict):
        if name in files:
            return files[name]
        for key, value in files.items():
            found_directory = FindDirectory(name, value)
            if found_directory is not None:
                return found_directory
    elif isinstance(files, list):
        for item in files:
            found_directory = FindDirectory(name, item)
            if found_directory is not None:
                return found_directory
    return None

# Print directories then files as human readable text
def TransformObjectToList(object):
  if len(object) == 0:
    print(f"\tNo files or directories found.\n")
  for item in object:
    if isinstance(item, dict):
      for thing in item:
        print(f"\t/{thing}")
  for item in object:
    if isinstance(item, str):
      print(f"\t{item}")
  return ""

commands = [
   "cd",
   "ls",
   "mkdir",
   "touch",
   "pwd"
]

# Set defaults
current_directory = my_files["root"]
breadcrumbs = []

print("\n\n~~~ Welcome to Python File System Simulator ~~\n\n")

while True:
  
  # Set breadcrumbs to root if breadcrumbs are empty
  if len(breadcrumbs) == 0:
    breadcrumbs = ["root"]
  
  # Initial prompt
  commands_string = "/".join(commands)
  command = input(f"Enter a command ({commands_string}): ")
  # target_directory = "root"

  # Invalid command
  if command not in commands:
    print("Not a valid command. Try again.")
    continue

  # Change directory
  if command == "cd":
    target_directory = input(f"Enter a directory name: ")
    directory_found = False

    # Up one level
    if target_directory == "../":
      if breadcrumbs[-1] == "root":
        print(f"\nYou are already in the root directory.\n")
        continue
      else:
        breadcrumbs.pop()
        current_directory = FindDirectory(breadcrumbs[-1],my_files)
        directory_found = True
        print(f"\nHere are the items in {str(breadcrumbs[-1])}:\n")
        print(TransformObjectToList(current_directory))

    # Root
    elif target_directory == "/":
      current_directory = my_files["root"]
      directory_found = True
      breadcrumbs = ["root"]

    # To sub-directory
    else:
      search_directory = FindDirectory(target_directory, my_files)
      if search_directory == None:
        directory_found = False
        print(f"\n{target_directory} was not found. Try again.\n")
      else:
        current_directory = search_directory
        directory_found = True
        breadcrumbs.append(target_directory)
        print(f"\nHere are the items in {str(breadcrumbs[-1])}:\n")
        print(TransformObjectToList(current_directory))

  # List files and directories
  if command == "ls":
    print(f"\nHere are the items in {str(breadcrumbs[-1])}:\n")
    if breadcrumbs[-1] != "root":
      print(f"\t../")
    print(TransformObjectToList(current_directory))

  # Make directory
  if command == "mkdir":
    target_directory = input("Enter a directory name: ")
    directory_exists = False
    for directory in current_directory:
      if target_directory in directory:
        directory_exists = True
        break

    if directory_exists == True:
      print(f"A directory with that name already exists. Try again.\n")
      continue
    else:
      current_directory.append({target_directory:[]})
      print("")
      print(TransformObjectToList(current_directory))

  # Touch
  if command == "touch":
    target_file = input("Enter a file name: ")

    current_directory.append(target_file)
    print(f"\nHere are the items in {str(breadcrumbs[-1])}:\n")
    print(TransformObjectToList(current_directory))

  # Breadcrumbs
  if command == "pwd":
    pwd_text = "/".join(breadcrumbs)
    print(f"/{pwd_text}")