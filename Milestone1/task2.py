# task2.py
# This one finds all the links. Links are 'a' tags.

import sys
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    print("Usage: python task2.py <your_html_file.html>")
    exit()

html_file = sys.argv[1]

try:
    with open(html_file, 'r', encoding='utf-8') as f:
        html_string = f.read()

    soup = BeautifulSoup(html_string, 'html.parser')

    print("--- Searching for links ---")

    # find all tags that are 'a'
    all_a_tags = soup.find_all('a')

    if not all_a_tags:
        print("No links found in this file.")
    else:
        counter = 1
        for tag in all_a_tags:
            # get the 'href' part of the link
            url = tag.get('href')
            if url:
                print(str(counter) + ". " + str(url))
            else:
                print(str(counter) + ". Found an <a> tag with no href.")
            counter += 1

except Exception as e:
    print("Something went wrong: " + str(e))