# Milestone 1 - BeautifulSoup

This project contains 8 practice tasks for learning web scraping and HTML parsing using Python and BeautifulSoup.

## Requirements

- Python 3.x
- Required libraries:
  - `requests` - for downloading web pages
  - `beautifulsoup4` - for parsing HTML

## Installation

```bash
pip install requests beautifulsoup4
```

## Task Overview

### Task 1: Download a Webpage (`task1.py`)

**Purpose**: Download a webpage from the internet and save it as a local HTML file

**Usage**:
```bash
python task1.py <website_url>
```

**Example**:
```bash
python task1.py https://example.com
```

**Output**: Saves the downloaded page as `downloaded_page.html`

**Key Features**:
- Uses `requests.get()` to download web content
- Parses HTML with `BeautifulSoup`
- Formats HTML using `prettify()`
- Error handling for network issues

---

### Task 2: Extract All Links (`task2.py`)

**Purpose**: Find and list all links (`<a>` tags) in an HTML file

**Usage**:
```bash
python task2.py <html_file_path>
```

**Example**:
```bash
python task2.py downloaded_page.html
```

**Key Features**:
- Uses `find_all('a')` to locate all link tags
- Extracts `href` attributes
- Displays numbered list of all links

---

### Task 3: List All Tag Types (`task3.py`)

**Purpose**: Scan an HTML file and list all different types of HTML tags present

**Usage**:
```bash
python task3.py <html_file_path>
```

**Example**:
```bash
python task3.py downloaded_page.html
```

**Key Features**:
- Uses `find_all(True)` to find all tags
- Collects unique tag names
- Outputs sorted alphabetical list

---

### Task 4: Find Tags with ID Attributes (`task4.py`)

**Purpose**: Locate all tags in an HTML file that have an `id` attribute

**Usage**:
```bash
python task4.py <html_file_path>
```

**Example**:
```bash
python task4.py downloaded_page.html
```

**Key Features**:
- Uses `find_all(id=True)` to find tags with IDs
- Displays tag names and their corresponding ID values

---

### Task 5: Find Parent Elements (`task5.py`)

**Purpose**: Demonstrates the `find_parent()` method by finding the parent `<div>` of an image tag

**Usage**:
```bash
python task5.py <html_file_path>
```

**Example**:
```bash
python task5.py downloaded_page.html
```

**Key Features**:
- Uses `find('img')` to locate the first image tag
- Uses `find_parent('div')` to find its parent div container
- Displays parent element's ID and class attributes

---

### Task 6: Replace Tags (`task6.py`)

**Purpose**: Replace all `<b>` tags with `<blockquote>` tags in an HTML file

**Usage**:
```bash
python task6.py <html_file_path>
```

**Example**:
```bash
python task6.py downloaded_page.html
```

**Output**: Saves modified HTML as `output_task6_edited.html`

**Key Features**:
- Uses `find_all('b')` to find all bold tags
- Changes tag type by modifying the `.name` attribute
- Saves modified HTML to new file

---

### Task 7: Add CSS Classes (`task7.py`)

**Purpose**: Add a CSS class attribute to all `<p>` paragraph tags in an HTML file

**Usage**:
```bash
python task7.py <html_file_path>
```

**Example**:
```bash
python task7.py downloaded_page.html
```

**Output**: Saves modified HTML as `output_task7_styled.html`

**Key Features**:
- Uses `find_all('p')` to find all paragraph tags
- Adds `class='student-modified'` attribute to each paragraph
- Saves modified HTML to new file

---

### Task 8: Find Sibling Elements (`task8.py`)

**Purpose**: Demonstrates the `find_next_sibling()` method by finding the next list item after the first one

**Usage**:
```bash
python task8.py <html_file_path>
```

**Example**:
```bash
python task8.py downloaded_page.html
```

**Key Features**:
- Uses `find('li')` to find the first list item
- Uses `find_next_sibling('li')` to find the next list item
- Displays text content of both list items

---

## Complete Workflow Example

Here's a complete workflow using all tasks:

```bash
# 1. Download a webpage
python task1.py https://quotes.toscrape.com

# 2. Extract all links
python task2.py downloaded_page.html

# 3. View all tag types
python task3.py downloaded_page.html

# 4. Find elements with IDs
python task4.py downloaded_page.html

# 5. Find parent of image
python task5.py downloaded_page.html

# 6. Replace tag types
python task6.py downloaded_page.html

# 7. Add CSS classes
python task7.py downloaded_page.html

# 8. Find sibling elements
python task8.py downloaded_page.html
```

## File Descriptions

- `task1.py` - `task8.py`: Eight Python practice scripts
- `downloaded_page.html`: Web page downloaded by task1 (generated)
- `quotes.html`: Sample HTML file for testing
- `output_task6_edited.html`: Output file from task6
- `output_task7_styled.html`: Output file from task7

## Learning Objectives

Through these 8 tasks, you will learn:

1. **Web Downloading** - Using requests library to fetch web content
2. **HTML Parsing** - Parsing HTML documents with BeautifulSoup
3. **Element Finding** - Mastering find() and find_all() search methods
4. **Attribute Operations** - Reading and modifying HTML element attributes
5. **DOM Navigation** - Navigating parent and sibling relationships
6. **HTML Modification** - Changing tag types and adding attributes
7. **File Operations** - Reading and writing HTML files
8. **Error Handling** - Using try-except for error management

## Notes

- All scripts require command-line arguments; they will show usage instructions if run without arguments
- Ensure HTML files use UTF-8 encoding
- Task1 requires internet connection to download web pages
- Task6 and task7 create new HTML files without modifying the original

## Troubleshooting

**Q: Getting "file not found" error when running task1?**  
A: Task1 downloads a webpage; after first run it will generate `downloaded_page.html`

**Q: How can I test these scripts?**  
A: Use the `quotes.html` file in the project, or run task1 first to download a webpage

**Q: Some tasks can't find expected HTML elements?**  
A: Different HTML files have different structures; ensure your test file contains the required elements (img, li, etc.)
