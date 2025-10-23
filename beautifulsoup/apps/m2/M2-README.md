# Milestone-2

## How to Run the Programs

This section provides exact command-line instructions to run all M2 task programs.

### Prerequisites

1. **Navigate to the beautifulsoup directory:**
```bash
cd beautifulsoup
```

2. **Set Python Path (REQUIRED):**
The modified bs4 library must be in your Python path to use the new SoupReplacer feature:
```bash
export PYTHONPATH=/home/runner/workspace/beautifulsoup:$PYTHONPATH
```

### Running Each Task

#### Task 2: Find All Links
Finds and displays all `<a>` tags using SoupStrainer.

**Command:**
```bash
cd beautifulsoup
PYTHONPATH=/home/runner/workspace/beautifulsoup:$PYTHONPATH python apps/m2/task2.py apps/m2/test.html
```

#### Task 3: List All Tags
Lists all HTML tags (excluding text) using SoupStrainer.

**Command:**
```bash
cd beautifulsoup
PYTHONPATH=/home/runner/workspace/beautifulsoup:$PYTHONPATH python apps/m2/task3.py apps/m2/test.html
```

#### Task 4: Find Tags with ID Attribute
Finds all tags that have an `id` attribute using SoupStrainer.

**Command:**
```bash
cd beautifulsoup
PYTHONPATH=/home/runner/workspace/beautifulsoup:$PYTHONPATH python apps/m2/task4.py apps/m2/test.html
```

#### Task 6: Replace Tags with SoupReplacer
Replaces all `<b>` tags with `<blockquote>` tags during parsing using the new SoupReplacer API.

**Command:**
```bash
cd beautifulsoup
PYTHONPATH=/home/runner/workspace/beautifulsoup:$PYTHONPATH python apps/m2/task6.py apps/m2/test.html
```

### Quick Run - All Tasks at Once

**Option 1: Using the Provided Script**

Simply run the provided bash script:

```bash
cd beautifulsoup/apps/m2
bash run_all_tasks.sh
```



### Using Your Own HTML File

To test with your own HTML file, replace `apps/m2/test.html` with your file path:

```bash
cd beautifulsoup
PYTHONPATH=/home/runner/workspace/beautifulsoup:$PYTHONPATH python apps/m2/task2.py /path/to/your/file.html
```

---

# Part 2: Source Code Analysis

Here is the location of the API definitions used in Milestone 1 and Milestone 2 (Part 1).

*Note: Line numbers refer to the original code commit before any modifications for Part 3.*

## API Locations

| API | File | Line Number |
| --- | --- | --- |
| `class BeautifulSoup` | `bs4/__init__.py` | 133 |
| `class SoupStrainer` | `bs4/filter.py` | 313 |
| `def prettify` | `bs4/element.py` | 2601 |
| `def find_all` | `bs4/element.py` | 137 |
| `def find_parent` | `bs4/element.py` | 992 |
| `def get` | `bs4/element.py` | 2160 |
| `def replace_with` | `bs4/element.py` | 552 |

## Part 3: `SoupReplacer` Implementation

This section details the source code modifications made to implement the `SoupReplacer` feature.

### 1. New API: `SoupReplacer`

* **Location:** Defined in `bs4/__init__.py` (above the `class BeautifulSoup` definition).
* **Purpose:** I added a new class named `SoupReplacer`. Its purpose is to replace one tag (e.g., `<b>`) with another (e.g., `<blockquote>`) **during** the parsing process as the tree is being built.
* **Constructor:** Its constructor is `__init__(self, og_tag, alt_tag)`, which accepts the original tag name to find and the new tag name to use as a replacement.

### 2. Source Code Modifications

To integrate the `SoupReplacer`, I made two key modifications to the `BeautifulSoup` class in `bs4/__init__.py`:

1.  **Modified `BeautifulSoup.__init__` (Constructor):**
    * I added a new optional parameter, `soup_replacer=None`, to the `__init__` method's signature.
    * Inside the method, I added the line `self.soup_replacer = soup_replacer` to store the replacer instance for access during the parsing lifecycle.

2.  **Modified `BeautifulSoup.handle_starttag` (Tag Interception):**
    * This is the core of the implementation. I added a small logic block at the **top** of the `handle_starttag` method.
    * This code checks if `self.soup_replacer` exists. If it does, it compares the current tag's `name` to `self.soup_replacer.og_tag`.
    * If they match, it changes the value of the local `name` variable to `self.soup_replacer.alt_tag` **before** the tag is officially created and processed. This ensures the replacement happens at parse-time with high efficiency.

### 3. New Tests

* **File Created:** `bs4/tests/test_soup_replacer.py`
* **Purpose:** I added a new test file to verify that the `SoupReplacer` functionality works as expected.
* **Test Case:** The `test_tag_replacement` case creates a `SoupReplacer("b", "blockquote")`, parses a string of HTML containing a `<b>` tag, and then asserts that the final `soup` object contains no `<b>` tag, but *does* contain a `<blockquote>` tag in the correct position with the correct content.

### 4. Application Script

* **File Created:** `apps/m2/task6.py`
* **Purpose:** This script demonstrates the usage of the new `SoupReplacer` feature and fulfills the requirement of Milestone 1's Task 6.
* **Functionality:** Instead of using `find_all()` and `.replace_with()`, this script passes the `SoupReplacer` instance directly into the `BeautifulSoup` constructor, achieving the `<b>` to `<blockquote>` replacement automatically during parsing.

---

