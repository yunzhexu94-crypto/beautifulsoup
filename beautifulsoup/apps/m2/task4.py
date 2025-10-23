import sys
from bs4 import BeautifulSoup, SoupStrainer

# Task 4: Find all tags with an id

s = SoupStrainer(attrs={"id": True})

# Check for filename
if len(sys.argv) < 2:
    print("You forgot to enter a filename!")
    sys.exit(1)

file_to_parse = sys.argv[1]

print("--- Task 4: Finding tags with 'id' in " + file_to_parse + " ---")

try:
    # Open the file
    with open(file_to_parse, 'r') as f:
        # This time, pass the file f directly to soup
        soup = BeautifulSoup(f, "html.parser", parse_only=s)

    # Print all the tags with an id that we found
    for tag in soup:
        print(tag)

except FileNotFoundError:
    print("Error: Could not find the file '" + file_to_parse + "'.")
except:
    # A general except block, catches all other errors
    print("An unknown error occurred.")