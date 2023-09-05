import re

#with open('names.txt') as f:
#  data = f.read()
#  print(data)
#for ele in data:
#   [A-Za-z]+/[@][a-zA-z]

#for name in data:
#    match = re.compile('^([A-Za-z -]+), ([A-Z][a-zA-Z-]+)(?:\s+(?:[^@\n]+@([A-Za-z0-9-_]+))|.*?(@[A-Za-z0-9-_]+))?$')
#    found = match.findall(name)
#    if found:
#       print(found)

#for name in data:
#    match = re.compile('^[A-Za-z ]+,[ ][A-za-z ]+|[^a-zA-z][@][a-zA-z]+| [@][a-zA-z]+')
#    found = match.findall(name)
    
# Define the regex pattern data of failed atttempls
#pattern = r'^[A-Za-z ]+,[ ][A-za-z ]+|[^A-Za-z][@][a-zA-z]+'
#pattern = r'^[A-Za-z ]+,[ ][A-Za-z ]+|[^A-Za-z][@][a-zA-Z]+'
#^[A-Za-z- ]+,[ ][A-za-z- ]+|[^A-Za-z][@][a-zA-z]+
#^[A-Za-z- ]+,[ ][A-za-z- ]+|[^A-Za-z][@][a-zA-z]+
#^[A-Za-z- ]+,[ ][A-za-z- ]+|[^A-Za-z][@][a-zA-z]+


#text = """
#Hawkins, Derek    derek@codingtemple.com    (555) 555-5555    Teacher, Coding Temple    @derekhawkins
#Zhai, Mo    mozhai@codingtemple.com    (555) 555-5554    Teacher, Coding Temple
#Johnson, Joe    joejohnson@codingtemple.com    Johson, Joe
#Osterberg, Sven-Erik    governor@norrbotten.co.se    Governor, Norrbotten    @sverik
#, Tim    tim@killerrabbit.com    Enchanter, Killer Rabbit Cave
#Butz, Ryan    ryanb@codingtemple.com    (555) 555-5543    CEO, Coding Temple    @ryanbutz
#Doctor, The    doctor+companion@tardis.co.uk    Time Lord, Gallifrey
#Exampleson, Example    me@example.com    555-555-5552    Example, Example Co.    @example
#Pael, Ripal    ripalp@codingtemple.com    (555) 555-5553    Teacher, Coding Temple    @ripalp
#Vader, Darth    darth-vader@empire.gov    (555) 555-4444    Sith Lord, Galactic Empire    @darthvader
#Fernandez de la Vega Sanz, Maria Teresa    mtfvs@spain.gov    First Deputy Prime Minister, Spanish Gov
#"""

#pattern = r"^[A-Za-z ]+,[ ][A-za-z ]+|[^a-zA-z][@][a-zA-z]+| [@][a-zA-z]+"
#matches = re.findall(pattern, text, re.MULTILINE)

#for match in matches:
#    last_name = match[0].strip()
#    first_name = match[1].strip() if match[1] else ""
#    twitter = match[2].strip() if match[2] else ""
#    if first_name:
#        print(f"{last_name}, {first_name} {twitter}")
#    else:
#        print(f"{last_name} {twitter}")

with open('names.txt', 'r') as file:
    for line in file:
        # Apply the regex pattern to each line
        matches = re.findall("^[A-Za-z ]+,[ ][A-za-z ]+|[^a-zA-z][@][a-zA-z]+| [@][a-zA-z]+", line)

        # Initialize variables to store the extracted information
        last_name = ""
        first_name = ""
        twitter = ""

        # Process the matches
        for match in matches:
            if match.startswith('@'):
                # Extract Twitter handle
                twitter = match.strip()
            elif ',' in match:
                # Extract last name and first name
                last_name, first_name = [name.strip() for name in match.split(',')]

        # Print or store the extracted information
        if last_name and first_name:
            print(f"Last Name: {last_name}, First Name: {first_name}, Twitter Handle: {twitter}")
        elif twitter:
            print(f"Twitter Handle: {twitter}")