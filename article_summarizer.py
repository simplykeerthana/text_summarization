# -*- coding: utf-8 -*-

#article text summerizer using NLP

#importing the libraries

import bs4 as bs
import urllib.request
import re
import nltk
import heapq

#getting the data sources

source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Computer_science').read()

#print(source)

#parse the data and create the beautiful soup object 

soup = bs.BeautifulSoup(source, 'lxml') 

#fectch the data

text = ""
#find all paragraphs 
for paragraph in soup.find_all('p'):
    text += paragraph.text #append all the paragraphs to the text 
    
#print(text)
    
#preprocessing the data 

text = re.sub(r'\[[0-9]*\]', ' ', text)
text = re.sub(r'\s+', ' ', text)
clean_text = text.lower() # convert all the text to lower()
clean_text = re.sub(r'\W', ' ', clean_text) # remove all the non-words
clean_text = re.sub(r'\d', ' ', clean_text) # remove all the digits
clean_text = re.sub(r'\s+', ' ', clean_text) # remove all the strings

print()

#tokenize sentences
sentences = nltk.sent_tokenize(text)

print(sentences)

#stopword list
stop_words = nltk.corpus.stopwords.words('english')

#word counts
word2count = {} #dictionary of words

for word in nltk.word_tokenize(clean_text):
    if word not in stop_words:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1

#converting counts to wights 
            
max_count = max(word2count.values()) # finds the word_count of the values 


for key in word2count.keys():
    word2count[key] = word2count[key]/max_count

print(max_count)

#produce the sentence scores 

sent2score = {}

for sentence in sentences:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in word2count.keys():
            if len(sentence.split(' ')) < 25:
                if sentence not in sent2score.keys():
                    sent2score[sentence] = word2count[word]
                else:
                    sent2score[sentence] = word2count[word]
                    
            


            
#getting the N best lines, but we are getting 5 lines
                    
best_sentences = heapq.nlargest(10, sent2score, key=sent2score.get)
                    
print('==================The summarized text =================')

for sentence in best_sentences:
    print('- ' + sentence)
    print()


    
