import sys
from bs4 import BeautifulSoup, SoupStrainer

# Task 2: Find all <a> tags

# Only look at <a> tags
my_strainer = SoupStrainer("a")

# Check if user gave a filename
if len(sys.argv) < 2:
    print("Please provide a filename.")
    sys.exit(1)

# The first argument is the filename
filename = sys.argv[1]
print("--- Task 2: Finding links in " + filename + " ---")

try:
    # Open the file
    f = open(filename, "r")

    # Parse with beautifulsoup
    # parse_only=my_strainer makes it only parse <a> tags
    soup = BeautifulSoup(f, "html.parser", parse_only=my_strainer)

    # Remember to close the file
    f.close()

    # The soup object now only has <a> tags
    # Loop and print all the links we found
    for link in soup:
        print(link)

except FileNotFoundError:
    print("Error: Could not find file " + filename)
except Exception as e:
    print("An error happened:")
    print(e)