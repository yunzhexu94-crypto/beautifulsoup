# task6.py
# replace all <b> tags with <blockquote> tags

import sys
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    print("Usage: python task6.py <filename>")
    exit()

my_file = sys.argv[1]
new_file_name = "output_task6_edited.html"

try:
    with open(my_file, 'r', encoding='utf-8') as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')

    # get all the 'b' tags
    list_of_b_tags = soup.find_all('b')
    print(f"Found {len(list_of_b_tags)} <b> tags to change.")

    if list_of_b_tags:
        for b_tag in list_of_b_tags:
            # this was the tricky part. you just change the .name attribute
            b_tag.name = 'blockquote'

        print("Tags have been changed.")

        # save the whole modified soup back to a file
        with open(new_file_name, 'w', encoding='utf-8') as f:
            f.write(str(soup))

        print("Result saved to " + new_file_name)
    else:
        print("Nothing to change.")

except Exception as e:
    print("An error occurred: " + str(e))