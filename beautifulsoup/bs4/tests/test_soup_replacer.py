# 在 bs4/tests/test_soup_replacer.py

from . import SoupTest  # 导入测试基类
from bs4 import BeautifulSoup
from bs4 import SoupReplacer # 导入你的新类

class TestSoupReplacer(SoupTest):
    """测试 SoupReplacer 功能"""

    def test_tag_replacement(self):
        """测试在解析时标签是否被正确替换"""

        # 1. 创建一个 replacer
        replacer = SoupReplacer("b","b")

        # 2. 准备 HTML 
        markup = "<p>Here is some <b>bold</b> text.</p>"

        # 3. 使用 self.soup() 辅助函数进行解析，并传入 replacer
        soup = self.soup(markup, soup_replacer=replacer)

        # 4. 断言（Assert）结果

        # 确保 <b> 标签已不存在
        assert soup.find("b") is None, "<b> tag should not exist"

        # 确保 <blockquote> 标签存在
        assert soup.blockquote is not None, "<blockquote> tag should exist"

        # 确保 <blockquote> 标签在正确的位置并有正确的内容
        assert soup.p.blockquote.string == "bold"

        # 确保最终的 HTML 结构正确
        assert str(soup) == "<p>Here is some <blockquote>bold</blockquote> text.</p>"