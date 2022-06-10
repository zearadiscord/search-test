from googlesearch import search

def get(word):
  return print("\n".join(f"[{search.title}]({search.url}) - {search.description}" for search in search(content, lang="jp",num_results = 5,advanced=True)))
