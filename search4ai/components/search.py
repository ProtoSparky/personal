try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")

def g_search(query):
    domains = []
    for j in search(query, num=10, stop=10, pause=2):
        domains.append(j)
    return domains



