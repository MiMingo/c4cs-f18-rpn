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

      if (len(stack) > 1):
        raise ValueError('Too many arguents on the stack')

  return stack[0]


def main():
  while True:
    try:
      res = calculate(input("rpn calc> "))
      print(res)
    except ValueError:
      pass

if __name__ == "__main__":
  main()