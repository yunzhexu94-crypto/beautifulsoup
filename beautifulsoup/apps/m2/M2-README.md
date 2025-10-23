# Milestone-2
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

## Part 3: Program Debugging and Testing

This section documents the debugging process and test results for all M2 task programs.

### Testing Environment Setup

**Test File Created:** `apps/m2/test.html`

A test HTML file was created with the following structure:
- Multiple `<a>` tags with different href values
- Tags with `id` attributes (title, div, nav, ul, footer)
- Two `<b>` tags for testing the SoupReplacer functionality
- Nested structure to test parent-child relationships

**Python Environment:**
- Python 3.11
- BeautifulSoup library installed in development mode from local source
- PYTHONPATH configured to use the modified bs4 library

### Task 2: Find All Links (task2.py)

**Purpose:** Uses `SoupStrainer` to parse only `<a>` tags from an HTML file.

**Test Command:**
```bash
PYTHONPATH=/home/runner/workspace/beautifulsoup:$PYTHONPATH python apps/m2/task2.py apps/m2/test.html
```

**Test Result:** ✅ SUCCESS

**Output:**
```
--- Task 2: Finding links in apps/m2/test.html ---
<a href="https://example.com">Example Link</a>
<a href="/about">About</a>
<a href="/contact">Contact Us</a>
<a href="/item1">Item 1</a>
<a href="/item2">Item 2</a>
```

**Analysis:** 
- Successfully found all 5 `<a>` tags in the test file
- The `SoupStrainer("a")` correctly filtered out all other HTML elements
- Only anchor tags were parsed, improving efficiency

---

### Task 3: List All Tags (task3.py)

**Purpose:** Uses `SoupStrainer(name=True)` to parse all HTML tags (excluding text nodes).

**Test Command:**
```bash
PYTHONPATH=/home/runner/workspace/beautifulsoup:$PYTHONPATH python apps/m2/task3.py apps/m2/test.html
```

**Test Result:** ✅ SUCCESS

**Output:**
All HTML tags from the document were successfully parsed and displayed, including:
- `<html>`, `<head>`, `<title>`, `<body>`
- `<div>` (with id attributes)
- `<h1>`, `<nav>`, `<a>`, `<p>`, `<b>`, `<ul>`, `<li>`, `<footer>`

**Analysis:**
- The `SoupStrainer(name=True)` correctly parsed all tag elements
- Text content was excluded as expected
- All nested tags were captured with proper structure

---

### Task 4: Find Tags with ID (task4.py)

**Purpose:** Uses `SoupStrainer(attrs={"id": True})` to find only tags with an `id` attribute.

**Test Command:**
```bash
PYTHONPATH=/home/runner/workspace/beautifulsoup:$PYTHONPATH python apps/m2/task4.py apps/m2/test.html
```

**Test Result:** ✅ SUCCESS

**Output:**
```
--- Task 4: Finding tags with 'id' in apps/m2/test.html ---
<title id="page-title">Test Page</title>
<div id="header">...</div>
<div id="content">...</div>
<footer id="footer">...</footer>
```

**Tags Found:**
- `<title id="page-title">`
- `<div id="header">`
- `<nav id="navigation">` (inside header div)
- `<div id="content">`
- `<ul id="list">` (inside content div)
- `<footer id="footer">`

**Analysis:**
- Successfully filtered and found 6 tags with `id` attributes
- The attribute filter worked correctly, including nested tags with IDs
- Demonstrated efficient parsing by only loading tags that match the criteria

---

### Task 6: SoupReplacer Tag Replacement (task6.py)

**Purpose:** Demonstrates the new `SoupReplacer` feature to replace `<b>` tags with `<blockquote>` tags during parsing.

**Test Command:**
```bash
PYTHONPATH=/home/runner/workspace/beautifulsoup:$PYTHONPATH python apps/m2/task6.py apps/m2/test.html
```

**Test Result:** ✅ SUCCESS

**Key Features Demonstrated:**
1. Created a `SoupReplacer("b", "blockquote")` instance
2. Passed it to BeautifulSoup constructor via `soup_replacer` parameter
3. All `<b>` tags were automatically replaced with `<blockquote>` during parsing

**Before (Original HTML):**
```html
<p>This is a <b>bold text</b> example.</p>
<p>Another paragraph with <b>more bold</b> content.</p>
```

**After (Processed Output):**
```html
<p>
  This is a
  <blockquote>
    bold text
  </blockquote>
  example.
</p>
<p>
  Another paragraph with
  <blockquote>
    more bold
  </blockquote>
  content.
</p>
```

**Analysis:**
- ✅ The `SoupReplacer` successfully replaced both `<b>` tags with `<blockquote>` tags
- ✅ No `<b>` tags remained in the final output
- ✅ Replacement happened during parsing (more efficient than post-processing)
- ✅ The new API integrates seamlessly with BeautifulSoup's constructor

---

### Debug Issues Encountered and Solutions

#### Issue 1: Import Error
**Problem:** Initial runs failed with `ImportError: cannot import name 'BeautifulSoup' from 'bs4'`

**Root Cause:** Python was unable to locate the modified bs4 library in the beautifulsoup directory.

**Solution:** Set `PYTHONPATH` environment variable to include the beautifulsoup directory:
```bash
PYTHONPATH=/home/runner/workspace/beautifulsoup:$PYTHONPATH
```

#### Issue 2: SoupReplacer Not Exported
**Problem:** `SoupReplacer` class was defined but couldn't be imported.

**Root Cause:** The class was not included in the `__all__` list in `bs4/__init__.py`.

**Solution:** Added `"SoupReplacer"` to the `__all__` list at line 42 of `bs4/__init__.py`:
```python
__all__ = [
    ...
    "SoupReplacer",
    ...
]
```

---

### Testing Summary

All four M2 task programs were successfully debugged and tested:

| Task | Status | Key Feature |
|------|--------|-------------|
| task2.py | ✅ PASS | SoupStrainer for tag filtering |
| task3.py | ✅ PASS | SoupStrainer with name=True |
| task4.py | ✅ PASS | SoupStrainer with attribute filtering |
| task6.py | ✅ PASS | SoupReplacer for tag replacement |

**Conclusion:**
- All programs run successfully without errors
- The `SoupStrainer` API demonstrates efficient selective parsing
- The new `SoupReplacer` API works as designed
- The modifications integrate well with the existing BeautifulSoup architecture