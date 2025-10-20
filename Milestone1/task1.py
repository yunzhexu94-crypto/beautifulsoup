# task1.py
# This script is supposed to download a webpage from the internet

import sys
import requests
from bs4 import BeautifulSoup

# check if the user gave a URL
if len(sys.argv) != 2:
    print("You need to give me a website URL to run this!")
    print("Usage: python task1.py <website_url>")
    # if not, then exit
    exit()

url = sys.argv[1]
# set the filename to save to
output_file = "downloaded_page.html"

print("Downloading from " + url + "...")

# use a try block so the program doesn't crash if something goes wrong
try:
    # --- 1. Download the page ---
    response = requests.get(url)
    html = response.text
    print("Download successful!")

    # --- 2. Process the page ---
    # give the downloaded html text to BeautifulSoup to handle
    soup = BeautifulSoup(html, 'html.parser')



    # use prettify to make it look nice
    pretty_text = soup.prettify()

    # --- 3. Save the file ---
    print("Saving to file: " + output_file)
    f = open(output_file, 'w', encoding='utf-8')
    f.write(pretty_text)
    f.close()

    print("Done!")

except Exception as e:
    # if any of the steps  went wrong, this code will run
    print("!!! Whoops, something went wrong !!!")
    print("The error was: " + str(e))
    print("Please check if your URL is correct and if your internet is working.")