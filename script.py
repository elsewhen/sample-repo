import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greetings = "Hello, {}".format(who_to_greet)
    return greetings


# print(greet('World'))
# print(greet('Ankit'))

# For input
# name  = input("Your Name?")
# print("Hello,", name)

r = requests.get("https://google.com")
print(r.status_code)
