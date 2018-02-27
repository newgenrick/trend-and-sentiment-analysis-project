# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 17:01:33 2018

@author: Abhishek
"""
import nltk
from collections import Counter
import math

tf_scores = dict()
tf_scores_list = list()
doc_containing = dict()
idf_scores = dict()
tf_idf_scores_list = list()
tf_idf_scores = dict()
documents = ["this is the first document. this is test document",
        "this is the second document. this is test document"]
        

#s = set(text[0].split())        
for document in documents:
    words = nltk.word_tokenize(document)
    word_count = len(words)
    cnt  =  Counter(words)
    for word in set(words):
        tf_scores[word] = cnt[word]/word_count
        doc_containing[word] = doc_containing.get(word,0) + 1
    tf_scores_list.append(tf_scores)
    tf_scores = dict()


for word in doc_containing:
    idf_scores[word] = math.log(len(documents)/doc_containing[word])
   
# to find the tf-idf score of words in their respective documents we multiply tf_scores and idf_scores
i = 0
for tf in tf_scores_list:
    #print(tf)
    for key,value in tf.items():
        tf_idf_scores[key] = tf[key]*idf_scores[key]
    tf_idf_scores_list.append(tf_idf_scores)
    tf_idf_scores = dict()


for counter,tf in enumerate(tf_idf_scores_list):
    print("\n\nThe most important word of document " + str(counter) + " is " + max(tf,key = tf.get))
    

    
    
        
        
        
