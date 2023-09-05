import re

with open('regex_test.txt') as f:
  data = f.readlines()
  match=re.compile('([A-Z][a-z]+) (A-Z)?[a-z]* ?([A-Z][a-z]+)', line)

for line in data:
    found = re.search(match, line)
    if found.group(1):
      print(found.group(0)+" "+found.group(1)+" "+found.group(2))
    elif found.group(0) and found.group(2):
      print(found.group(1)+" "+found.group+(2))
    else:
      print("None")