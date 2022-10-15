from googlesearch import search
import nltk
import sys
import os
import nltk
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 10

# to search


def load_files(directory):
    files = os.listdir(directory)
    dictionary = {}
    for filename in files:
        text = ''
        with open(f'corpus/{filename}', 'r') as f:
            text = f.read()
        dictionary[filename] = text
    return dictionary


def tokenize(document):
    words = nltk.tokenize.word_tokenize(document)
    # print(words)
    i = 0
    while i < len(words):
        # print(words[i])
        words[i] = words[i].lower()
        
        
            
        if words[i] in nltk.corpus.stopwords.words("english"):
            del words[i]
            i -= 1
        else:
            for letter in string.punctuation:
                words[i] = words[i].replace(letter, '')
                # print(letter)
            if words[i] == '':
                del words[i]
                i -= 1
        i += 1
    return words
    

    


def compute_idfs(documents):
    words = {}
    for document in documents:
        for word in documents[document]:
            words[word] = 0
    # print(words)
    for word in words:
        for document in documents:
            if word in documents[document]:
                words[word] += 1
        words[word] = math.log(len(documents) / words[word])
    
    return words
    


def top_files(query, files, idfs, n):
    total_files = {}
    for f in files:
        total_files[f] = 0
        for word in query:
            if word in files[f]:
                occurrances = files[f].count(word)
                total_files[f] += occurrances * idfs[word]
        
    total_files = {k: v for k, v in sorted(total_files.items(), key=lambda item: item[1])}
    keys = list(total_files.keys())
    keys.reverse()
    return keys[:n]

def top_sentences(query, sentences, idfs, n):
    results = {}
    for sentence in sentences:
        results[sentence] = 0
        for word in query:
            if word in sentences[sentence]:
                results[sentence] += idfs[word]
    
    results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1])}
    keys = list(results.keys())
    keys.reverse()
    return keys[:n]


query = "cricket"
print(type(search(query, tld="co.in", num=10, stop=10, pause=2)))
l = []

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
  print(j)
  l.append(j)
<<<<<<< HEAD

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Cricket"
=======
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = l[0]
>>>>>>> 8a3ab627c5c6367de8a629c62877f5428b6b160e
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

for script in soup(["script", "style"]):
    script.extract() 
<<<<<<< HEAD

text = soup.body.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk)

files = {"cricket" : text}
#print(text)


# Check command-line arguments
#if len(sys.argv) != 2:
#    sys.exit("Usage: python questions.py corpus")

# Calculate IDF values across files
#files = load_files(sys.argv[1])
file_words = {
    filename: tokenize(files[filename])
    for filename in files
}
file_idfs = compute_idfs(file_words)

# Prompt user for query
query = set(tokenize(input("Query: ")))

# Determine top file matches according to TF-IDF
filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

# Extract sentences from top files
sentences = dict()
for filename in filenames:
    for passage in files[filename].split("\n"):
        for sentence in nltk.sent_tokenize(passage):
            tokens = tokenize(sentence)
            if tokens:
                sentences[sentence] = tokens

# Compute IDF values across sentences
idfs = compute_idfs(sentences)

# Determine top sentence matches
matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
for match in matches:
    print(match)
=======
text = soup.body
for data in text.find_all("p"):
    print(data.get_text())
    # text = da
# lines = (line.strip() for line in text.splitlines())
# chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# text = '\n'.join(chunk for chunk in chunks if chunk)
# print(text)
>>>>>>> 8a3ab627c5c6367de8a629c62877f5428b6b160e
