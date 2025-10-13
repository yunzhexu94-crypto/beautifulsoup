# task7.py
# find all <p> tags and add a class attribute

import sys
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    print("Usage: python task7.py <filename>")
    exit()

input_file = sys.argv[1]
output_file = "output_task7_styled.html"

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        html_data = f.read()

    soup = BeautifulSoup(html_data, 'html.parser')

    all_paragraphs = soup.find_all('p')

    print(f"Found {len(all_paragraphs)} paragraphs. Adding a class to them...")

    for p_element in all_paragraphs:
        
        p_element['class'] = 'student-modified'

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print("Finished! New file is " + output_file)

except Exception as e:
    print("Something went wrong: ", e)