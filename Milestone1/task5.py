# task5.py
# a meaningful use of find_parent()

import sys
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    print("Usage: python task5.py <filename>")
    exit()

filename = sys.argv[1]

try:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')


    # Step 1
    first_image = soup.find('img')

    if first_image:
        print("Found an image tag to start with:")
        print(first_image)

        # Step 2
        parent_div = first_image.find_parent('div')

        if parent_div:
            print("\nFound its parent 'div' container:")
            print("Parent ID:", parent_div.get('id', '(no id)'))
            print("Parent class:", parent_div.get('class', '(no class)'))
        else:
            print("\nThis image doesn't seem to be inside a 'div'.")
    else:
        print("Couldn't find any image tags in this file to test find_parent().")

except Exception as e:
    print("Error: ", e)