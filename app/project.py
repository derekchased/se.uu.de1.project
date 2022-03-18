#!/usr/bin/env python
# coding: utf-8

# ### Setup

# In[1]:


from pyspark.sql import SparkSession
from operator import add
from argparse import ArgumentParser

import json

parser = ArgumentParser()
parser.add_argument("-s", "--print-sample",
                    action="store_false", dest="sample", default=True,
                    help="Print a sample entry from input file")

parser.add_argument("-r", "--print-result",
                    action="store_false", dest="result", default=True,
                    help="Print results")

parser.add_argument("-o", "--output", dest="output",
                    help="Output file to append stats to")
                    
parser.add_argument("-c", "--cores",
                    dest="cores", type=int, default=None,
                    help="Number of cores to use")

parser.add_argument("-i", "--input", dest="input",
                    help="Input dataset file. Must exist on all spark workers")

args = parser.parse_args()

print_sample = args.sample if args.sample is not None else True
print_result = args.result if args.result is not None else True

builder = SparkSession.builder.master("spark://sparkapp:7077")\
    .appName("simon_converted_1")\
    .config("spark.dynamicAllocation.enabled", True)\
    .config("spark.dynamicAllocation.shuffleTracking.enabled",True)\
    .config("spark.shuffle.service.enabled", False)\
    .config("spark.dynamicAllocation.executorIdleTimeout","30s")

if args.cores is not None:
    builder = builder\
        .config("spark.dynamicAllocation.maxExecutors", args.cores)\
        .config("spark.dynamicAllocation.minExecutors", args.cores)

spark_session = builder.getOrCreate()
    #         .config("spark.executor.cores",2)\
    #         .config("spark.driver.port",9998)\
    #         .config("spark.blockManager.port",10005)\
    #         .getOrCreate()

# Old API (RDD)
spark_context = spark_session.sparkContext

spark_context.setLogLevel("ERROR")

# In[2]:


import json

posts = spark_context.textFile(args.input).map(lambda x: json.loads(x)) # "reddit/data/RC_2009-05"


# ### Print a sample from the loaded JSON file

# In[12]:

if print_sample:
    print('Sample JSON entry from read file:')
    print(str(posts.take(1)))

import time
start = time.time()

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

    # Determine "controversiality" by counting what percentage of votes are downvotes
    score = post.get('score')
    
    if words is None or score is None:
        return None

    # The following was used previously: post.get('controversiality') 
    # But the controversiality field appears to always be 0 for 2009-05, for example. 
    # So it may not be reliable to use it
    
    return [ (word, score) for word in words ]


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


word_percentages = filtered_words.map(lambda word: (word[0], word[1][0] / word[1][1]))


def print_words(input_word_percentages, num=100, ascending=False, output_result=True):
    # Get subset of length num from start of sorted word list
    key_func_factor = 1 if ascending else -1
    top_words = input_word_percentages.takeOrdered(num, key=lambda x: key_func_factor * x[1])

    # Find the length of the longest word to make formatting prettier
    ignore_longer_than = 30
    max_length = min(max([ len(word[0]) for word in top_words if len(word[0]) < ignore_longer_than ]), ignore_longer_than)

    if not output_result:
        return

    # Define a format for printing words, where words are left-padded with spaces 
    # to become max_length long
    print_format = '{:>' + str(max_length) + '}: {:<8}'

    # Iterate over all top words and print them
    for entry in top_words:
        # Find the word from the tuple
        word = entry[0]
        
        # Multiply by 100 and round to two decimal points
        votes_per_occurance = round(entry[1], 2)
        
        # Print the word and percentage using the previously defined format
        print(print_format.format(entry[0], str(votes_per_occurance) + ' score/occurance'))


number_of_outputs = 100

if print_result:
    print(f'Printing {number_of_outputs} best words that contribute to upvotes')

print_words(word_percentages, ascending=False, output_result=print_result)

if print_result:
    print(f'Printing {number_of_outputs} best words that contribute to downvotes')

print_words(word_percentages, ascending=True, output_result=print_result)

end = time.time()
stat_text = f"{args.input},{args.cores},{end - start}"
print(stat_text)

if args.output is not None:
    output_file = open(args.output, 'a')
    output_file.write(stat_text + "\n")
    output_file.close()
    print("Appended stats to output file.")

# ### Print the results

# In[10]:




