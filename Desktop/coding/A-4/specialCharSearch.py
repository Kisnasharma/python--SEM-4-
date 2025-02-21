import re

s = input("Enter a string: ")
if re.search(r"[^a-zA-Z0-9]", s):
    print("String contains special characters")
else:
    print("No special characters found")