from googlesearch import search
def serch(query):
    queries = []
    for current_link in search(query, tld="co.in", num=10, stop=10, pause=2):
        queries.append(current_link)
    return queries