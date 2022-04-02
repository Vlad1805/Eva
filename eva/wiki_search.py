import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')

page_py = wiki_wiki.page('Romania')
print(page_py.text)
with open('paragraph.txt', "w", encoding="utf-8") as f:
    f.writelines(page_py.text)
