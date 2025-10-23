
import sys
from bs4 import BeautifulSoup
# 确保你可以从修改后的源码中导入 SoupReplacer
from bs4 import SoupReplacer 

if len(sys.argv) < 2:
    print("Usage: python task6.py <html_file>")
    sys.exit(1)

html_file = sys.argv[1]

# 1. 创建你的 SoupReplacer 实例
b_to_blockquote_replacer = SoupReplacer("b", "blockquote")

print(f"--- Processing {html_file} with SoupReplacer ---")

try:
    # 你需要确保你的 Python 环境能找到你修改过的 bs4 库
    # 而不是系统安装的。
    with open(html_file, 'r', encoding='utf-8') as f:
        # 2. 在构造 BeautifulSoup 时就传入 replacer
        soup = BeautifulSoup(
            f, 
            'html.parser', 
            soup_replacer=b_to_blockquote_replacer # <-- 使用新功能
        )

    # 3. 打印结果。
    print(soup.prettify())

except FileNotFoundError:
    print(f"Error: File '{html_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")