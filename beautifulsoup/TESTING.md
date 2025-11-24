# BeautifulSoup 测试指南

本文档说明如何运行 BeautifulSoup 项目的测试。

## 快速开始

### 方法1：使用测试脚本（最简单）

```bash
cd beautifulsoup

# 查看帮助
./run_tests.sh

# 运行所有测试
./run_tests.sh all

# 运行M2测试（SoupReplacer基础功能）
./run_tests.sh m2

# 运行M3测试（高级转换功能）
./run_tests.sh m3

# 运行M4测试（迭代器功能）
./run_tests.sh m4

# 快速测试（简洁模式）
./run_tests.sh quick
```

### 方法2：直接使用pytest

```bash
cd beautifulsoup

# 运行所有测试
pytest bs4/tests/

# 运行特定测试文件
pytest bs4/tests/test_soup_replacer.py -v
pytest bs4/tests/test_soup_replacer_m3.py -v
pytest bs4/tests/test_tree.py -v

# 运行特定测试类
pytest bs4/tests/test_tree.py::TestSoupIteration -v

# 运行特定测试方法
pytest bs4/tests/test_soup_replacer_m3.py::TestSoupReplacerM3::test_name_xformer_only -v
```

## pytest 常用选项

```bash
# 详细输出模式
pytest bs4/tests/ -v

# 显示print输出
pytest bs4/tests/ -v -s

# 简洁模式（只显示摘要）
pytest bs4/tests/ -q

# 只运行失败的测试
pytest bs4/tests/ --lf

# 停在第一个失败的测试
pytest bs4/tests/ -x

# 显示最慢的10个测试
pytest bs4/tests/ --durations=10

# 运行特定标记的测试
pytest bs4/tests/ -k "iteration"
```

## 测试文件说明

### M2 功能测试
- **文件**: `bs4/tests/test_soup_replacer.py`
- **测试内容**: SoupReplacer 简单标签替换功能
- **运行**: `pytest bs4/tests/test_soup_replacer.py -v`

### M3 功能测试
- **文件**: `bs4/tests/test_soup_replacer_m3.py`
- **测试内容**: 
  - name_xformer（标签名转换）
  - attrs_xformer（属性转换）
  - xformer（副作用转换）
  - M2和M3组合使用
- **运行**: `pytest bs4/tests/test_soup_replacer_m3.py -v`

### M4 功能测试
- **文件**: `bs4/tests/test_tree.py::TestSoupIteration`
- **测试内容**: BeautifulSoup对象迭代器功能
- **运行**: `pytest bs4/tests/test_tree.py::TestSoupIteration -v`

### 核心功能测试
- **文件**: `bs4/tests/test_tree.py`, `bs4/tests/test_soup.py` 等
- **测试内容**: BeautifulSoup 所有核心功能
- **运行**: `pytest bs4/tests/ -v`

## 测试应用程序

### M2 应用程序测试
```bash
cd beautifulsoup/apps/m2

# 运行单个任务
PYTHONPATH=/home/runner/workspace/beautifulsoup:$PYTHONPATH python task6.py test.html

# 运行所有M2任务
./run_all_tasks.sh
```

### M3 应用程序测试
```bash
cd beautifulsoup/apps/m3

# 运行M3任务
PYTHONPATH=/home/runner/workspace/beautifulsoup:$PYTHONPATH python task7_m3.py test.html
```

## 预期测试结果

成功运行所有测试应该看到：
```
632 passed, 216 skipped in 4.31s
```

- **632 passed**: 所有关键测试通过
- **216 skipped**: 需要额外依赖（如lxml, html5lib）的测试被跳过

## 常见问题

### Q: 为什么有测试被跳过？
A: 有些测试需要可选的依赖库（如lxml、html5lib），在当前环境中不可用。这是正常的。

### Q: 如何只运行我的新功能测试？
A: 使用测试脚本或直接运行特定的测试文件：
```bash
./run_tests.sh m2  # M2功能
./run_tests.sh m3  # M3功能
./run_tests.sh m4  # M4功能
```

### Q: 如何调试失败的测试？
A: 使用 `-v -s` 选项查看详细输出：
```bash
pytest bs4/tests/test_soup_replacer.py -v -s
```

## 在Replit中运行测试

1. **打开Shell工具**：在左侧工具栏中找到Shell图标
2. **导航到项目目录**：`cd beautifulsoup`
3. **运行测试**：使用上述任何命令

你也可以配置Workflow来自动运行测试，但对于开发调试，直接在Shell中运行更方便。
