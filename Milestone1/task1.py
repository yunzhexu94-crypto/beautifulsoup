# task1.py
# Goal: read a file and then save it back out but prettier.

import sys
from bs4 import BeautifulSoup

# need to make sure the user gave us a file
if len(sys.argv) != 2:
    print("Error: You need to provide a filename.")
    print("Usage: python task1.py <filename>")
    exit()

input_filename = sys.argv[1]
output_filename = "output_task1_pretty.html"

# print("DEBUG: Reading file:", input_filename)

try:
    # open the file to read it
    file_handle = open(input_filename, 'r', encoding='utf-8')
    file_contents = file_handle.read()
    file_handle.close() # remember to close it

    # make the soup
    soup = BeautifulSoup(file_contents, 'html.parser')

    # use the prettify function
    pretty_version = soup.prettify()

    # now write it to a new file
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(pretty_version)

    print("Successfully created prettified file: " + output_filename)

except FileNotFoundError:
    print("Error! The file '" + input_filename + "' was not found.")
except Exception as e:
    print("An unknown error occurred.")
    print(e)