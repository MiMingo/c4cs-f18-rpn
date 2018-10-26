#!/usr/bin/env python3

def calculate(arg):
  stack = []
  tokens = arg.split()

  for tok in tokens:
    try:
      stack.append(int(tok))
    except ValueError:
      b = stack.pop()
      a = stack.pop()
      
      if (tok == '+'):
        res = a + b
      elif (tok == '-'):
        res = a - b

      stack.append(res)

  return stack[0]


def main():
  while True:
    res = calculate(input("rpn calc> "))
    print(res)

if __name__ == "__main__":
  main()