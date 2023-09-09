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
    }
  ]
}

def TransformObjectToList(object):
  for item in object:
    if isinstance(item, dict):
      for thing in item:
        print(f"\t/{thing}")
  for item in object:
    if isinstance(item, str):
      print(f"\t{item}")
  return ""

current_directory = my_files["root"]
previous_directory = None

print("\n\n~~~ Welcome to my Python File System Simulator ~~\n\n")

while True:
  command = input("Choose a command (ls/cd/mkdir/touch): ")
  target_directory = "root"

  # Invalid command
  if command != "cd" and command != "ls" and command != "mkdir" and command != "touch":
    print("Not a valid command. Try again.")

  # Change directory
  if command == "cd":
    target_directory = input("Enter a directory: ")
    directory_found = False

    if target_directory == "../":
      current_directory = previous_directory
      directory_found = True
    elif target_directory == "/":
      current_directory = my_files["root"]
      directory_found = True
    else:
      for directory in current_directory:
        if target_directory in directory:
          directory_found = True
          previous_directory = current_directory
          try:
            current_directory = directory[target_directory]
          except KeyError as e:
            print(f"There was an error. Try again.")
            continue
          print(f"\nHere are the items in {target_directory}:\n")
          print(TransformObjectToList(current_directory))
      
    if directory_found == False:
      print(f"\n\"{target_directory}\" does not exist. Try again.\n")

  # List files and directories
  if command == "ls":
    print(f"Here are the items in the current directory:\n")
    print(f"\t../")
    print(TransformObjectToList(current_directory))

  # Make directory
  if command == "mkdir":
    target_directory = input("Enter a directory name: ")

    current_directory.append({target_directory:[]})
    print("")
    print(TransformObjectToList(current_directory))

  # Touch
  if command == "touch":
    target_file = input("Enter a file name: ")

    current_directory.append(target_file)
    print(f"\nHere are the items in this directory:\n")
    print(TransformObjectToList(current_directory))