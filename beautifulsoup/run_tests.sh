#!/bin/bash
# BeautifulSoup 测试运行脚本

echo "================================"
echo "BeautifulSoup 测试套件"
echo "================================"
echo ""

# 颜色定义
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 选项1：运行所有测试
if [ "$1" == "all" ]; then
    echo -e "${BLUE}运行所有测试...${NC}"
    pytest bs4/tests/ -v
    exit 0
fi

# 选项2：运行M2测试
if [ "$1" == "m2" ]; then
    echo -e "${BLUE}运行M2测试 (SoupReplacer基础功能)...${NC}"
    pytest bs4/tests/test_soup_replacer.py -v
    exit 0
fi

# 选项3：运行M3测试
if [ "$1" == "m3" ]; then
    echo -e "${BLUE}运行M3测试 (高级转换功能)...${NC}"
    pytest bs4/tests/test_soup_replacer_m3.py -v
    exit 0
fi

# 选项4：运行M4测试
if [ "$1" == "m4" ]; then
    echo -e "${BLUE}运行M4测试 (迭代器功能)...${NC}"
    pytest bs4/tests/test_tree.py::TestSoupIteration -v
    exit 0
fi

# 选项5：快速测试（简洁模式）
if [ "$1" == "quick" ]; then
    echo -e "${BLUE}快速测试（简洁模式）...${NC}"
    pytest bs4/tests/ -q
    exit 0
fi

# 默认：显示帮助
echo "用法: ./run_tests.sh [选项]"
echo ""
echo "选项:"
echo "  all     - 运行所有测试（详细模式）"
echo "  m2      - 运行M2测试（SoupReplacer基础功能）"
echo "  m3      - 运行M3测试（高级转换功能）"
echo "  m4      - 运行M4测试（迭代器功能）"
echo "  quick   - 快速运行所有测试（简洁模式）"
echo ""
echo "示例:"
echo "  ./run_tests.sh all     # 运行所有测试"
echo "  ./run_tests.sh m2      # 只运行M2测试"
echo "  ./run_tests.sh quick   # 快速测试"
