# task3.py
# list out all the different kinds of tags in the file

import sys
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    print("Usage: python task3.py <filename>")
    exit()

the_file = sys.argv[1]

try:
    with open(the_file, 'r', encoding='utf-8') as f:
        data = f.read()

    soup_obj = BeautifulSoup(data, 'html.parser')

    # find every single tag
    all_the_tags = soup_obj.find_all(True)

    tag_names_found = []
    for tag in all_the_tags:
        if tag.name not in tag_names_found:
            tag_names_found.append(tag.name)

    print("Found these unique tags:")
    tag_names_found.sort() 
    for name in tag_names_found:
        print(name)

except:
    print("An error occurred. Could not process the file.")