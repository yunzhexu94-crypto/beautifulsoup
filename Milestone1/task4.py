# task4.py
# find all the tags that have an 'id' attribute

import sys
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    print("Usage: python task4.py <filename>")
    exit()

filename = sys.argv[1]

try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    print("Tags with an ID attribute:")

    # The documentation says id=True works.
    tags_with_id = soup.find_all(id=True)

    if not tags_with_id:
        print("(None found)")
    else:
        for tag in tags_with_id:
            # print them out
            print(f"<{tag.name}> has id: '{tag['id']}'")

except Exception as e:
    print("An error happened:", e)