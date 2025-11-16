import sys
import os
# We must import 'bs4' itself first so sys.modules is populated
import bs4
# Now we can import the class
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag

# --- Key Step ---
# Ensure we import our locally modified bs4 library, not the system-installed one
# 1. Get the directory of the current script (m4_iteration_demo.py)
#    .../beautifulsoup/apps/m4/
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Go up to the 'beautifulsoup' root directory (parent of 'apps')
#    .../beautifulsoup/
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))

# 3. Add the root directory to the very beginning of the Python search path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# ------------------




# --- CORRECTED LINE ---
# Get the module name from the class (BeautifulSoup.__module__),
# which is 'bs4', and then look up that module in sys.modules
# to get its __file__ attribute.
print(f"--- Successfully loaded BeautifulSoup from local path ---")
print(f"--- Location: {sys.modules[BeautifulSoup.__module__].__file__} ---")
print("\n" + "="*50)
print("     Milestone 4: Application Task Demo")
print("="*50 + "\n")

# 1. Prepare a simple HTML document
html_doc = """
<html>
    <head><title>M4 Demo</title></head>
    <body>
        <p>This is paragraph 1.</p>
        <b>This is bold.</b>
    </body>
</html>
"""

print("--- Creating Soup object ---")
soup = BeautifulSoup(html_doc, 'html.parser')
print("--- Soup object created successfully ---")

print("\n--- Starting 'for node in soup:' loop (M4 feature) ---")

try:
    node_count = 0
    for node in soup:
        node_count += 1
        node_type = ""

        # Determine node type
        if isinstance(node, Tag):
            node_type = f"Tag: <{node.name}>"
        elif isinstance(node, NavigableString) and node.strip():
            node_type = f"String: '{node.strip()}'"

        if node_type:
            print(f"  Node {node_count}: {node_type}")

    print("\n--- Loop successful! ---")
    print(f"Iterated over a total of {node_count} nodes.")

except TypeError as e:
    print("\n" + "!"*50)
    print("  ERROR: Iteration failed!")
    print("  This likely means the __iter__ method was not added correctly to bs4/__init__.py.")
    print(f"  Error detail: {e}")
    print("!"*50)

print("\n--- Application Task demo finished ---")