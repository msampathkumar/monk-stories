import os, re, glob
from ebooklib import epub

def strip_front_matter(text):
    return re.sub(r'\A---\n.*?\n---\n', '', text, flags=re.S)

def main():
    book = epub.EpubBook()
    book.set_identifier('monk-stories-2026-11-04')
    book.set_title('Monk Stories: Ancient Wisdom for Modern Work')
    book.set_language('en')
    book.add_author('Monk')

    files = sorted(glob.glob(os.path.join('docs', 'posts', '*.md')))
    chapters = []
    spine = ['nav']

    for i, f in enumerate(files):
        if 'index.md' in f or '.authors.yml' in f:
            continue
        raw = open(f, encoding='utf-8').read()
        body = strip_front_matter(raw)
        title = next((l[2:].strip() for l in body.splitlines() if l.startswith('# ')), os.path.basename(f))
        
        html_body = f'<h1>{title}</h1>' + ''.join(
            f'<p>{line}</p>' if line and not line.startswith('#') else f'<h2>{line[3:]}</h2>' if line.startswith('###') else f'<h1>{line[2:]}</h1>' if line.startswith('#') else f'<pre>{line}</pre>' if line.startswith('```') else f'<p>{line}</p>'
            for line in body.splitlines()
        )
        
        c = epub.EpubHtml(title=title, file_name=f'post_{i:02d}.xhtml', lang='en')
        c.content = f'<html><body>{html_body}</body></html>'
        book.add_item(c)
        chapters.append(c)
        spine.append(c)

    book.toc = tuple(chapters)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = spine

    os.makedirs('dist', exist_ok=True)
    out = 'dist/monk-stories-2026-11-04.epub'
    epub.write_epub(out, book, {})
    print(f'Wrote {out} ({len(chapters)} chapters)')

if __name__ == '__main__':
    main()
