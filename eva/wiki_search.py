import wikipediaapi
from googlesearch import search

def get_wikipage_name(query):
    l = search(query + "wikipedia", tld="co.in", num=2, stop=2, lang="en")
    l = list(filter(lambda x: "Wikipedia" in x, l))
    return l[0]
def generate_wiki_page(query):
    name = get_wikipage_name(query).split("/")[-1]
    print(name)
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(name)
    with open('paragraph.txt', "w", encoding="utf-8") as f:
        f.writelines(page_py.text)

generate_wiki_page("Who is the lead singer of band Vita de vie?")