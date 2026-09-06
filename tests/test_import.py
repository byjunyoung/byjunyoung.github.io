import importlib.util, sys, unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('imp', Path(__file__).resolve().parents[1] / 'scripts/import_framer.py')
imp = importlib.util.module_from_spec(spec); spec.loader.exec_module(imp)

HTML = '''<html><body><div><p>works</p><p>Junyoung Kim</p><p>activities</p>
<a href="https://byjunyoung.github.io/resume/">resume</a></div>
<h1>Birdy</h1><p>부제입니다</p>
<h6>ORGANIZATION</h6><p>UNIST</p><h6>YEAR</h6><p>2021 (1y)</p><h6>ROLE</h6><p>리드 연구원</p>
<h6>RESPONSIBILITIES</h6><p>Research, Product Design</p>
<h6>LINK</h6><p><a href="https://x.y/z">Master's Thesis</a></p>
<img src="https://framerusercontent.com/images/logo.png?scale-down-to=512" alt="">
<img src="https://framerusercontent.com/images/hero.jpg?scale-down-to=1024" alt="">
<p>PROBLEM</p><p>——</p><p>문제 문단</p>
<img src="https://framerusercontent.com/images/a.jpg?scale-down-to=1024" alt="">
<p>APPROACH</p><ol><li><p><strong>첫째</strong>: 설명</p></li><li><p>둘째</p></li></ol>
<p>junyoung735@gmail.com</p><p>Select LanguageKorean</p></body></html>'''
CHROME = {'https://framerusercontent.com/images/logo.png'}

class ImportTest(unittest.TestCase):
    def test_parse_page_title_meta_body(self):
        page = imp.parse_page(HTML, CHROME)
        self.assertEqual(page['title'], 'Birdy')
        self.assertEqual(page['subtitle'], '부제입니다')
        self.assertEqual(page['meta']['org'], 'UNIST')
        self.assertEqual(page['meta']['responsibilities'], 'Research, Product Design')
        self.assertEqual(imp.split_links(page['meta']['link']), [("Master's Thesis", 'https://x.y/z')])
        self.assertEqual(page['body'][0], ('img', 'https://framerusercontent.com/images/hero.jpg', 1))

    def test_render_body(self):
        page = imp.parse_page(HTML, CHROME)
        body, imgs = imp.render_body(page['body'], skip_url='https://framerusercontent.com/images/hero.jpg')
        self.assertIn('## PROBLEM', body)
        self.assertNotIn('——', body)
        note, _ = imp.render_body([('p', 'Note', False), ('p', '——', False), ('p', '한 단락', False)])
        self.assertIn('## NOTE', note)
        self.assertIn('![](./01.jpg)', body)
        self.assertIn('1. **첫째**: 설명', body)
        self.assertEqual(imgs, [('https://framerusercontent.com/images/a.jpg', '01.jpg')])

    def test_chrome_images(self):
        man = {f'p{i}': {'images': ['https://f/logo.png'] + (['https://f/only.png'] if i == 0 else [])} for i in range(4)}
        self.assertEqual(imp.chrome_images(man), {'https://f/logo.png'})

    def test_split_csv(self):
        self.assertEqual(imp.split_csv('Research, Product Design / UX'), ['Research', 'Product Design', 'UX'])

    def test_youtube_embed_block_in_order(self):
        html = ('<h1>T</h1><p>부제</p><h6>ORGANIZATION</h6><p>X</p><h6>YEAR</h6><p>2020</p><h6>ROLE</h6><p>R</p>'
                '<p>PROBLEM</p><p>첫 문단</p>'
                '<div><iframe title="Youtube Video" src="https://www.youtube.com/embed/YvDX9E_5jvk?rel=0&amp;x=1"></iframe></div>'
                '<p>둘째 문단</p><p>junyoung735@gmail.com</p>')
        page = imp.parse_page(html, set())
        body, imgs = imp.render_body(page['body'])
        i_first, i_embed, i_second = body.index('첫 문단'), body.index('class="embed"'), body.index('둘째 문단')
        self.assertTrue(i_first < i_embed < i_second)
        self.assertIn('https://www.youtube-nocookie.com/embed/YvDX9E_5jvk?rel=0&modestbranding=1', body)
        self.assertEqual(imgs, [])

    def test_cols_from_sizes(self):
        self.assertEqual(imp.cols_from_sizes('(min-width: 1200px) calc(min(100vw, 1200px) - 80px), (max-width: 809px) 100vw'), 1)
        self.assertEqual(imp.cols_from_sizes('(min-width: 1200px) max((min(100vw, 1200px) - 82px) / 2, 1px), (max-width: 809px) 100vw'), 2)
        self.assertEqual(imp.cols_from_sizes('(min-width: 1200px) 400px, (min-width: 810px) and (max-width: 1199px) 33vw'), 3)
        self.assertEqual(imp.cols_from_sizes('(min-width: 1200px) 1120px, (max-width: 809px) 100vw'), 1)
        self.assertEqual(imp.cols_from_sizes(''), 1)

    def test_render_groups_consecutive_images_by_cols(self):
        blocks = [('p', 'PROBLEM', False), ('p', '문단', False),
                  ('img', 'https://f/a.jpg', 2), ('img', 'https://f/b.jpg', 2), ('img', 'https://f/c.jpg', 2),
                  ('img', 'https://f/d.jpg', 1),
                  ('img', 'https://f/e.jpg', 3), ('img', 'https://f/f.jpg', 3), ('img', 'https://f/g.jpg', 3)]
        body, imgs = imp.render_body(blocks)
        lines = [l for l in body.splitlines() if l.startswith('![](')]
        self.assertEqual(lines, ['![](./01.jpg) ![](./02.jpg)', '![](./03.jpg)', '![](./04.jpg)',
                                 '![](./05.jpg) ![](./06.jpg) ![](./07.jpg)'])
        self.assertEqual([n for _, n in imgs], ['01.jpg', '02.jpg', '03.jpg', '04.jpg', '05.jpg', '06.jpg', '07.jpg'])

    def test_blank_line_after_list_before_image(self):
        blocks = [('li', '첫째', True), ('li', '둘째', True), ('img', 'https://f/a.jpg', 1)]
        body, _ = imp.render_body(blocks)
        self.assertIn('1. 둘째\n\n![](./01.jpg)', body)

    def test_control_chars_stripped(self):
        html = '<h1>T</h1><p>부제</p><h6>ROLE</h6><p>R</p><p>Note</p><p>가\x08나</p><p>junyoung735@gmail.com</p>'
        body, _ = imp.render_body(imp.parse_page(html, set())['body'])
        self.assertIn('가나', body)
        self.assertNotIn('\x08', body)

    def test_anchor_becomes_markdown_link(self):
        html = '<h1>T</h1><p>부제</p><h6>ROLE</h6><p>R</p><p>Note</p><p>앞 <a href="https://x.y/">링크</a> 뒤</p><p>junyoung735@gmail.com</p>'
        body, _ = imp.render_body(imp.parse_page(html, set())['body'])
        self.assertIn('앞 [링크](https://x.y/) 뒤', body)
        self.assertNotIn('<https://', body)

    def test_html_to_md_description(self):
        html = '<p dir="auto"><a href="https://a.b/" target="_blank"><strong>설계자들</strong></a>은 <a href="/activities/uxeed">UXeed</a>의 모임입니다.</p><p>둘째 문단<br>줄바꿈</p>'
        self.assertEqual(imp.html_to_md(html), '[**설계자들**](https://a.b/)은 [UXeed](/activities/uxeed)의 모임입니다.\n\n둘째 문단 줄바꿈')

    def test_links_from_html(self):
        self.assertEqual(imp.links_from_html('<p><a href="https://h/">Home</a> / <a href="https://i/">Instagram</a></p>'), [('Home', 'https://h/'), ('Instagram', 'https://i/')])
        self.assertEqual(imp.links_from_html('<p dir="auto"><br><br class="trailing-break"></p>'), [])

if __name__ == '__main__':
    unittest.main()
