import unittest
from bs4 import BeautifulSoup, SoupReplacer

class TestSoupReplacerM3(unittest.TestCase):
    """
    Test cases for the Milestone 3 functionality of SoupReplacer,
    focusing on name_xformer, attrs_xformer, and xformer.
    """

    def test_case_1_name_xformer_only(self):
        """
         Test Case 1: Test name_xformer in isolation.
        """
        # --- Setup ---
        def b_to_blockquote(tag):
            if tag.name == 'b':
                return 'blockquote'
            return tag.name  # Important: return original name otherwise it becomes None

        replacer = SoupReplacer(name_xformer=b_to_blockquote)
        html_input = "<p>This is <b>bold</b> text.</p>"

        # --- Steps ---
        soup = BeautifulSoup(html_input, 'html.parser', soup_replacer=replacer)

        # --- Expected Output ---
        self.assertIsNone(soup.find('b'))
        self.assertIsNotNone(soup.find('blockquote'))
        self.assertEqual(soup.find('blockquote').string, 'bold')
        self.assertEqual(str(soup), "<p>This is <blockquote>bold</blockquote> text.</p>")

    def test_case_2_attrs_xformer_only(self):
        """
        Test Case 2: Test attrs_xformer in isolation.
        """
        # --- Setup ---
        def add_class_to_p(tag):
            if tag.name == 'p':
                # Return a brand new attribute dictionary
                new_attrs = {'class': 'paragraph'}
                # Preserve existing attributes (if needed)
                if 'id' in tag.attrs:
                    new_attrs['id'] = tag.attrs['id']
                return new_attrs
            return tag.attrs # Important: return original attrs

        replacer = SoupReplacer(attrs_xformer=add_class_to_p)
        html_input = '<p id="main">Hello</p>'

        # --- Steps ---
        soup = BeautifulSoup(html_input, 'html.parser', soup_replacer=replacer)

        # --- Expected Output ---
        p_tag = soup.find('p')
        self.assertIsNotNone(p_tag)
        self.assertEqual(p_tag.get('class'), ['paragraph'])
        self.assertEqual(p_tag.get('id'), 'main')
        self.assertEqual(str(soup), '<p class="paragraph" id="main">Hello</p>')

    def test_case_3_xformer_only_side_effects(self):
        """
         Test Case 3: Test xformer in isolation (for side-effects).
        """
        # --- Setup ---
        def remove_class_attr(tag):
            # Modify the tag object directly
            if "class" in tag.attrs:
                del tag.attrs["class"]

        replacer = SoupReplacer(xformer=remove_class_attr)
        html_input = '<div class="main" id="content">Data</div>'

        # --- Steps ---
        soup = BeautifulSoup(html_input, 'html.parser', soup_replacer=replacer)

        # --- Expected Output ---
        div_tag = soup.find('div')
        self.assertIsNotNone(div_tag)
        self.assertIsNone(div_tag.get('class'))
        self.assertEqual(div_tag.get('id'), 'content')
        self.assertEqual(str(soup), '<div id="content">Data</div>')

    def test_case_4_m2_and_m3_name_interaction(self):
        """
         Test Case 4: Test M2 and M3 interaction (execution order).
        """
        # --- Setup ---
        # This xformer only activates if the tag name is 'strong'
        def strong_to_em(tag):
            if tag.name == 'strong':
                return 'em'
            return tag.name

        # M2: "b" -> "strong"
        # M3: "strong" -> "em"
        replacer = SoupReplacer("b", "strong", name_xformer=strong_to_em)
        html_input = "<p><b>Test</b></p>"

        # --- Steps ---
        soup = BeautifulSoup(html_input, 'html.parser', soup_replacer=replacer)

        # --- Expected Output ---
        # The final result should be <em>
        self.assertIsNone(soup.find('b'))
        self.assertIsNone(soup.find('strong'))
        self.assertIsNotNone(soup.find('em'))
        self.assertEqual(str(soup), "<p><em>Test</em></p>")

    def test_case_5_m3_all_xformers_chain(self):
        """
         Test Case 5: Test chain reaction of all M3 xformers (execution order).
        """
        # --- Setup ---
        def name_changer(tag):
            # 1. Runs first
            if tag.name == 'div':
                return 'span'
            return tag.name

        def attr_changer(tag):
            # 2. Runs second (tag.name is 'span' at this point)
            if tag.name == 'span':
                return {'class': 'changed'} # Intentionally discard id
            return tag.attrs

        def side_effect_changer(tag):
            # 3. Runs last (tag.name is 'span', tag.attrs is {'class': 'changed'})
            if tag.name == 'span' and tag.attrs.get('class') == ['changed']:
                tag['data-final'] = 'true' # Add a new attribute

        replacer = SoupReplacer(
            name_xformer=name_changer,
            attrs_xformer=attr_changer,
            xformer=side_effect_changer
        )
        html_input = '<div id="original">Content</div>'

        # --- Steps ---
        soup = BeautifulSoup(html_input, 'html.parser', soup_replacer=replacer)

        # --- Expected Output ---
        self.assertIsNone(soup.find('div'))
        span_tag = soup.find('span')
        self.assertIsNotNone(span_tag)
        self.assertIsNone(span_tag.get('id')) # Verify id was discarded by attr_changer
        self.assertEqual(span_tag.get('class'), ['changed'])
        self.assertEqual(span_tag.get('data-final'), 'true')
        self.assertEqual(str(soup), '<span class="changed" data-final="true">Content</span>')

    def test_case_6_m2_backward_compatibility_regression(self):
        """
         Test Case 6: Test M2 backward compatibility (regression test).
        """
        # --- Setup ---
        # Use M2's multiple-pair signature only
        replacer = SoupReplacer("b", "strong", "i", "em")
        html_input = "<p>This is <b>bold</b> and <i>italic</i>.</p>"

        # --- Steps ---
        soup = BeautifulSoup(html_input, 'html.parser', soup_replacer=replacer)

        # --- Expected Output ---
        self.assertIsNone(soup.find('b'))
        self.assertIsNone(soup.find('i'))
        self.assertIsNotNone(soup.find('strong'))
        self.assertIsNotNone(soup.find('em'))
        self.assertEqual(str(soup), "<p>This is <strong>bold</strong> and <em>italic</em>.</p>")

if __name__ == '__main__':
    unittest.main()