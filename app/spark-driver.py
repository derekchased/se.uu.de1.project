#!/usr/bin/env python
# coding: utf-8

# ### Setup

# In[1]:


from pyspark.sql import SparkSession
from operator import add

import json

spark_session = SparkSession.builder.master("spark://sparkapp:7077")\
.appName("derek_worker_test")\
.config("spark.dynamicAllocation.enabled", True)\
.config("spark.dynamicAllocation.shuffleTracking.enabled",True)\
.config("spark.shuffle.service.enabled", False)\
.config("spark.dynamicAllocation.executorIdleTimeout","30s")\
.getOrCreate()
#         .config("spark.executor.cores",2)\
#         .config("spark.driver.port",9998)\
#         .config("spark.blockManager.port",10005)\
#         .getOrCreate()

# Old API (RDD)
spark_context = spark_session.sparkContext

spark_context.setLogLevel("ERROR")


# In[2]:


import json

posts = spark_context.textFile("reddit-volume/RC_2009-08").map(lambda x: json.loads(x))


# ### Print a sample from the loaded JSON file

# In[12]:


print('Sample JSON entry from read file:')
print(str(posts.take(1)))


# ### Define functions used to map posts to lists of words and controversiality scores

# In[4]:


import re

def get_words(post):
    content = post.get('body')
    
    if content is None:
        return None
    
    return [ re.sub(r'[^a-zA-Z0-9]', '', word).lower() for word in content.split(" ") ]

def get_words_controversiality(post):
    words = get_words(post)
    controversiality = post.get('controversiality')
    
    if words is None or controversiality is None:
        return None
    
    return [ (word, controversiality) for word in words ]


# ### Map posts to its words along with the controversiality of the post

# In[5]:


words = posts.flatMap(lambda post: get_words_controversiality(post)).filter(lambda entry: entry is not None)


# ### Append a count to each word specifying its number of occurances

# In[6]:


words_with_counts = words.map(lambda entry: (entry[0], (entry[1], 1)))


# ### Reduce words to combine their controversiality and count

# In[7]:


reduced = words_with_counts.reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1])) 


# ### Remove words occuring less than N times, to filter out words with insufficient data

# In[8]:


min_occurances = 100
filtered_words = reduced.filter(lambda word: word[1][1] >= min_occurances)


# ### Calculate percentage of how many of the words that occur in a controversial post, and sort them in descending order

# In[9]:


word_percentages = filtered_words.map(lambda word: (word[0], word[1][0] / word[1][1])).sortBy(lambda word: word[1], ascending=False)


# ### Print the results

# In[10]:


# Number of words to print
num = 100
print(f'Printing top {num} most controversial words')

# Get subset of length num from start of sorted word list
top_words = word_percentages.take(num)

# Find the length of the longest word to make formatting prettier
max_length = max([ len(word[0]) for word in top_words ])

# Define a format for printing words, where words are left-padded with spaces 
# to become max_length long
print_format = '{:>' + str(max_length) + '}: {:<8}'

# Iterate over all top words and print them
for entry in top_words:
    # Find the word from the tuple
    word = entry[0]
    
    # Multiply by 100 and round to two decimal points
    percentage = round(entry[1]*100, 2)
    
    # Print the word and percentage using the previously defined format
    print(print_format.format(entry[0], str(percentage) + '%'))

