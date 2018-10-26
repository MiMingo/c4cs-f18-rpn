#!/usr/bin/env python3

def calculate(arg):
  stack = []
  tokens = arg.split()

  for tok in tokens:
    try:
      stack.append(int(tok))
    except ValueError as e:
      a = stack.pop()
      b = stack.pop()
      res = a + b
      stack.append(res)

  return stack[0]


def main():
  while True:
    res = calculate(input("rpn calc> "))
    print(res)

if __name__ == "__main__":
  main()