import wikipediaapi
from googlesearch import search

def get_wikipage_name(query):
    l = search(query + "wikipedia", tld="co.in", num=1, stop=1, lang="en")
    return next(l)
    # l = (list(filter(lambda x: "wikipedia" in x, \
    # search(query + "wikipedia", tld="co.in", num=1, stop=4, lang="en"))))
    # print(l[0])
def generate_wiki_page(query):
    name = get_wikipage_name(query).split("/")[-1]
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(name)
    with open('paragraph.txt', "w", encoding="utf-8") as f:
        f.writelines(page_py.text)

# generate_wiki_page("Where is the northernmost point of land in the world?")