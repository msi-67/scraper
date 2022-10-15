try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

# to search
query = "cricket"
print(type(search(query, tld="co.in", num=10, stop=10, pause=2)))
l = []
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
  print(j)
  l.append(j)
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = l[0]
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")
for script in soup(["script", "style"]):
    script.extract() 
text = soup.body
for data in text.find_all("p"):
    print(data.get_text())
    # text = da
# lines = (line.strip() for line in text.splitlines())
# chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# text = '\n'.join(chunk for chunk in chunks if chunk)
# print(text)
