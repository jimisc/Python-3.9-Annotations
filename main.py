# Example of annotations in Python 3.9.
# By @jimisc on GitHub

def add(x: int, y: int) -> int:
  return x + y

add(1, 10)

# Can only "hint" (type hints) cannot enforce
add('a', 'b')
print(add.__annotations__)
