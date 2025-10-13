# task8.py
# use one more function from the API. I'll try find_next_sibling.

import sys
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    print("Usage: python task8.py <filename>")
    exit()

filename = sys.argv[1]

try:
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()

    soup = BeautifulSoup(data, 'html.parser')

    # try to find the first item in a list and then find the next one
    first_li = soup.find('li')

    if first_li:
        print("First list item is: '" + first_li.text.strip() + "'")

        # I tried this first, but it just gave me a blank line
        # next_thing = first_li.next_sibling
        # print(next_thing)

        second_li = first_li.find_next_sibling('li')

        if second_li:
            print("The next list item is: '" + second_li.text.strip() + "'")
        else:
            print("There is no second list item after the first one.")

    else:
        print("Couldn't find any <li> tags in this file.")

except Exception as e:
    print("Program failed with an error", e)