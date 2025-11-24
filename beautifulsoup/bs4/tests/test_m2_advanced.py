from . import SoupTest
from bs4 import SoupReplacer

class TestSoupReplacerAdvanced(SoupTest):
    """M2 进阶测试：验证 SoupReplacer 的健壮性"""

    def test_multiple_tag_pairs(self):
        """测试 1: 一次性替换多种不同的标签"""
        # 规则：把 <h1> 变成 <h2>，同时把 <i> 变成 <em>
        replacer = SoupReplacer("h1", "h2", "i", "em")

        markup = "<h1>Title</h1><p>This is <i>italic</i>.</p>"
        soup = self.soup(markup, soup_replacer=replacer)

        # 验证 h1 -> h2
        assert soup.find("h1") is None, "Should replace h1"
        assert soup.find("h2") is not None, "Should find h2"
        assert soup.h2.string == "Title"

        # 验证 i -> em
        assert soup.find("i") is None, "Should replace i"
        assert soup.find("em") is not None, "Should find em"
        assert soup.p.em.string == "italic"

    def test_attributes_are_preserved(self):
        """测试 2: 替换标签名时，原有的属性（class/id等）应该保留"""
        # 规则：把 <a> 变成 <link>
        replacer = SoupReplacer("a", "link")

        # 输入带有 href 和 class 的标签
        markup = '<a href="http://example.com" class="btn" id="my-link">Click Me</a>'
        soup = self.soup(markup, soup_replacer=replacer)

        # 验证旧标签没了
        assert soup.find("a") is None

        # 获取新标签
        new_tag = soup.find("link")
        assert new_tag is not None

        # 关键验证：属性还在吗？
        assert new_tag['href'] == "http://example.com"
        assert new_tag['id'] == "my-link"
        assert "btn" in new_tag['class']  # class 通常是列表

    def test_unrelated_tags_untouched(self):
        """测试 3: 不在规则里的标签不应受到影响"""
        replacer = SoupReplacer("b", "strong")

        markup = "<div><span>Text</span></div>"
        soup = self.soup(markup, soup_replacer=replacer)

        # 验证 div 和 span 还是原来的样子
        assert soup.find("div") is not None
        assert soup.find("span") is not None
        assert soup.div.name == "div"
