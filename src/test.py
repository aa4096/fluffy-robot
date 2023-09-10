def some_function():
  print("hello world")

class File:

  def __init__ (self, id, name, parent, children, timestamp, owner, permissions):
    self.id = id
    self.name = name
    self.parent = parent
    self.timestamp = timestamp
    self.owner = owner
    self.permissions = permissions

  def print_class(self):
    print(self.id)

  def __str__(self):
    return str(self.id)