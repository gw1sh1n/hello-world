#!/usr/bin/env python

# ----- Method 1 ---------

import os

def hello_world():
    os.system('echo "hello world"')

hello_world()


# ----- Method 2 ---------

hello_string = "hello world"
output_string = []

for character in hello_string:
    output_string.append(character)

formatted_string = ''.join(output_string)
print(formatted_string)


# ----- Method 3 ---------

print("hello world")

