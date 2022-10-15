from googlesearch import search

query = "studytonight"

for i in search(query, tld="co.in", num=5, stop=5, pause=2):
    print(i)
