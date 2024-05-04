# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VwdF7hhffKKtzmxyynRDelJkZ4YTN71s
"""

from google.colab import files
uploaded = files.upload()

import csv
import os
import zipfile

# Path setup
zip_file_path = 'data.zip'
extracted_dir = 'BBC_articles'

# Creating the extracted directory
if not os.path.exists(extracted_dir):
    os.makedirs(extracted_dir)

# Extracting all data from the zip file(un zip)
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_dir)

# Creating a CSV file named bbc_articles to write into
with open('bbc_articles.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['article_id', 'text', 'category'] # 3 columns
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Iterating over each file within the extracted directory
    for root, dirs, files in os.walk(extracted_dir):
        for filename in files:
            # File path
            filepath = os.path.join(root, filename)

            # Checking if it's a file and has an underscore to split article_id and category
            if '_' in filename:
                # Separating based on underscore
                article_id, category = filename.split('_')
                category = category.split('.')[0]  # Removing file extension

                # Open and read the text file content
                with open(filepath, 'r', encoding='utf-8') as file:
                    text = file.read()

                    # Writing each row to the CSV file
                    writer.writerow({'article_id': article_id, 'text': text, 'category': category})

print("CSV file creation completed.") # easy to debug

import pandas as pd#reading into dataframes using pandas

df = pd.read_csv('bbc_articles.csv')
df.head()

import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Downloading  NLTK resources to perform preprocessing steps
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initializing NLTK components
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

import re
# Custom tokenizer function using NLTK
def custom_tokenizer(text):
    tokens = word_tokenize(text)  # Tokenization
     # a pattern to match words
    pattern = r'\b[A-Za-z]+\b'  # This pattern matches words

    # Using  findall method to extract all matching words from the text
    tokens = re.findall(pattern, text.lower())
    # Lowercasing and removing non-alphabetic characters
    tokens = [word.lower() for word in tokens if word.isalnum()]
     # Removing stopwords and lemmatizing
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return tokens

df['tokens'] = df['text'].apply(custom_tokenizer)#tokenizing the text and reading it into df

df

corpus = df['text']#assuming

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

#using tfidf for text vectorization
# Initializing TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit the vectorizer to the text data and transform the text into TF-IDF features
tfidf_features = tfidf_vectorizer.fit_transform(corpus)

print(tfidf_vectorizer.vocabulary_)#to know what are present wrt index


""

tfidf_vectorizer.get_feature_names_out()

all_feature_names = tfidf_vectorizer.get_feature_names_out()
#printing the tfidf score for each and every word
for word in all_feature_names:
  index = tfidf_vectorizer.vocabulary_.get(word)
  print(f"{word}  :  {tfidf_vectorizer.idf_[index]}")

print(tfidf_features.toarray())

import pandas as pd

# Converting TF-IDF features to a dense array
tfidf_dense = tfidf_features.toarray()

# Creating a new  DataFrame
tfidf_df = pd.DataFrame(tfidf_dense, columns=tfidf_vectorizer.get_feature_names_out())

# Concatenating  with  category column to get the final one
final_tfidf_df = pd.concat([tfidf_df, df[['category']]], axis=1)

print(final_tfidf_df)

final_tfidf_df.to_csv('vectorized_dataset.csv', index=False) # getting a csv file from data frame

final_tfidf_df.head()















