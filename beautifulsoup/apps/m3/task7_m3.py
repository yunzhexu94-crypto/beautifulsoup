import sys
import os
from bs4 import BeautifulSoup, SoupReplacer

def add_test_class_to_p(tag):
    """
    This is an M3 'xformer' function.
    If the tag is <p>, it adds or replaces its class 
    attribute with "test" via side-effect.
    """
    # Check if the tag name is 'p'
    if tag.name == 'p':
        # Directly modify the tag's attrs dictionary.
        # This will add the 'class' key if it doesn't exist
        # or replace its value if it does.
        tag.attrs['class'] = 'test'

def main():
    """
    Main application function.
    """
    # --- 1. Handle command-line arguments (part of M1 Task 1) ---
    if len(sys.argv) < 2:
        print("Error: Please provide an HTML/XML file as an argument.")
        print("Usage: python m3_app.py <input_file.html>")
        sys.exit(1)

    input_filename = sys.argv[1]

    # Create an output filename based on the input filename
    base, ext = os.path.splitext(input_filename)
    output_filename = f"{base}.m3-output{ext}"

    # --- 2. Use the SoupReplacer M3 API ---
    # We use the 'xformer' argument to pass our function,
    # which will modify tags during the parsing process.
    replacer = SoupReplacer(xformer=add_test_class_to_p)

    try:
        # --- 3. Read, Parse, Write ---
        with open(input_filename, 'r', encoding='utf-8') as f:
            html_content = f.read()

        print(f"Parsing {input_filename} with SoupReplacer...")

        # Pass the replacer to the BeautifulSoup constructor
        soup = BeautifulSoup(html_content, 'html.parser', soup_replacer=replacer)

        # M1 Task 7: ...then write the tree to a file
        # (We use prettify() from M1 Task 1 to make it readable)
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(soup.prettify())

        print(f"Success! Set class='test' for all <p> tags.")
        print(f"Result saved to: {output_filename}")

    except FileNotFoundError:
        print(f"Error: File not found '{input_filename}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()