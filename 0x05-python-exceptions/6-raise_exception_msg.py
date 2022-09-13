#!/usr/bin/python3
def raise_exception_msg(message=""):
  try:
    raise NameError("Sorry, The name Is Incorrect.. Try Again Please")
  except NameError as e:
    print(e)
