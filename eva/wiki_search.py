import wikipediaapi

def generate_wiki_page(name):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(name)
    with open('paragraph.txt', "w", encoding="utf-8") as f:
        f.writelines(page_py.text)
