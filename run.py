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
          current_directory = directory[target_directory]
          print(f"\nHere are the items in {target_directory}:")
          print(TransformObjectToList(current_directory))
      
    if directory_found == False:
      print(f"\"{target_directory}\" does not exist. Try again.")

  if command == "ls":
    print(f"Here are the items in the current directory:\n")
    print(f"\t../")
    print(TransformObjectToList(current_directory))