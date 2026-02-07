import os

def add(x,y): # Expects a number data type, string will work
  return x+y # Addition

def diff(x,y): # Expects a number data type
  return x-y # Subtraction

def quot(x,y): # Expects a number data type
  return x/y # Division

def prod(x,y): # Expects a number data type
  return x*y # Multiplication

def rem(x,y): # Expects a number data type
  return x%y # Remainder
 
def exp(x,y): # Expects a number data type
  return x**y # Exponent

def calc(x,y,opr): # Calculate function (num, num, string)
  if opr == "+": # Expects a string data type
    return add(x,y)
  elif opr == "-": # Expects a string data type
    return diff(x,y)
  elif opr == "/": # Expects a string data type
    return quot(x,y)
  elif opr == "*": # Expects a string data type
    return prod(x,y)
  elif opr == "%": # Expects a string data type
    return rem(x,y)
  elif opr == "^": # Expects a string data type
    return exp(x,y)
  else:
    return print("Error")


def parse(str): # Check for operator and assign numbers left and right of operator
    line = str.strip()

    if line == "":
        return None

    for opr in ["+", "-", "*", "/", "%", "^"]: # Finds the operator for the line, string
        if opr in line:
            left, right = line.split(opr, 1)
            x = int(left.strip())
            y = int(right.strip())
            return x, y, opr
    return None


  
def read(file_obj): # Read line in file
  line = file_obj.readline()
  if line == "":
    return None
  return line.rstrip("\n")



def write(file, og_line, list): # Write back to file
  file.write(f"{og_line} = {list}\n")


def main():
  path = input("Input the path of the file: ") # Input the file path exluding the name
  filename = input("Input the filename: ") # Filename only, not path
  in_file = os.path.join(path, filename)

  with open(in_file, 'r') as fin: # reading the file
    lines = fin.readlines() # Read the line

    with open(in_file, 'w') as fout: # Writing back into the file
      for line in lines:
        line = line.rstrip("\n")
        parsed = parse(line)

        if parsed is None:
          fout.write(line + "\n")
          continue

        x,y,opr = parsed
        ans = calc(x,y,opr)

        write(fout, line, ans) # Write back to file



main()
