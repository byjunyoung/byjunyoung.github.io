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
        self.assertEqual(page['body'][0], ('img', 'https://framerusercontent.com/images/hero.jpg', ''))

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

if __name__ == '__main__':
    unittest.main()
