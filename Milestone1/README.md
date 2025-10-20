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

**Output**: Saves the downloaded page as `downloaded_page.html`


---

### Task 2: Find All Hyperlinks(`task2.py`)

**Purpose**: Find and list all links (`<a>` tags) in an HTML file

**Usage**:
```bash
python task2.py <html_file_path>
```


---

### Task 3: List All Tag Types (`task3.py`)

**Purpose**: Scan an HTML file and list all different types of HTML tags present

**Usage**:
```bash
python task3.py <html_file_path>
```


---

### Task 4: Find Tags with an ID (`task4.py`)

**Purpose**: Locate all tags in an HTML file that have an `id` attribute

**Usage**:
```bash
python task4.py <html_file_path>
```


---

### Task 5: Use find_parent() (`task5.py`)

**Purpose**: Demonstrates the `find_parent()` method by finding the parent `<div>` of an image tag

**Usage**:
```bash
python task5.py <html_file_path>
```


---

### Task 6: Replace `<b>` Tags (`task6.py`)

**Purpose**: Replace all `<b>` tags with `<blockquote>` tags in an HTML file

**Usage**:
```bash
python task6.py <html_file_path>
```


**Output**: Saves modified HTML as `output_task6_edited.html`


---

### Task 7: Add Class to `<p>` Tags (`task7.py`)

**Purpose**: Add a CSS class attribute to all `<p>` paragraph tags in an HTML file

**Usage**:
```bash
python task7.py <html_file_path>
```


**Output**: Saves modified HTML as `output_task7_styled.html`


---

### Task 8: Use Another API Function (find_next_sibling()) (`task8.py`)

**Purpose**: Demonstrates the `find_next_sibling()` method by finding the next list item after the first one

**Usage**:
```bash
python task8.py <html_file_path>
```



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
- `output_task6_edited.html`: Output file from task6
- `output_task7_styled.html`: Output file from task7


## Notes
### Large File Processing
As required by the  description, I attempted to process a gigabyte-scale XML file. The scripts failed to process the file, consuming all available system memory before crashing. 

### What I Learned
This milestone provided a great hands-on introduction to the BeautifulSoup library. The find_all() method proved to be incredibly versatile. I learned how to navigate the parse tree using functions like find_parent() and find_next_sibling(), and how to manipulate the tree by modifying tag names and attributes directly. 

## Author

Student: YUNZHE XU(Kevin) - 2025