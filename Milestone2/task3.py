import sys
from bs4 import BeautifulSoup, SoupStrainer

# Task 3: Find all tags

# name=True means match all tags, but skip text
all_tags_s = SoupStrainer(name=True)

# Get filename from command line
if len(sys.argv) < 2:
    print("Usage: python task3.py <filename>")
    sys.exit(1)

html_file = sys.argv[1]

print("--- Task 3: Finding all tags in " + html_file + " ---")

try:
    # Use 'with open' to read the file
    # This way automatically closes the file
    with open(html_file, "r") as f:
        # First, read the whole file into a string
        html_content = f.read()

    # Pass the string to BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser", parse_only=all_tags_s)

    # Print all the tags we found
    for tag in soup:
        print(tag)

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Something went wrong:")
    print(e)