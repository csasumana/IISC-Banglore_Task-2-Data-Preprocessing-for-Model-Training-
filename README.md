# IISC-Banglore_Task-2-Data-Preprocessing-for-Model-Train
At the start I have unzip the data zip file
And then from the title of each file i have extracted article_id and category.
I have created a csv file with article_id, category and text as rows.
Read the csv file into dataframe using pandas
Initially, the text is tokenized using NLTK's word_tokenize function. This function splits the input text into individual words (tokens).
: Each word in the list of tokens is converted to lowercase (word.lower()) and filtered to include only alphanumeric characters (word.isalnum()). This step ensures uniformity in token casing and removes any non-alphabetic characters.
Removed stop words and tokens are lemmatized using NLTK's lemmatization functionality (lemmatizer.lemmatize(word)).
Vectorization
Used tfidf to vectorize the tokens 
calculated tfidf score for each and every word 
Converted TF-IDF features to a dense array and created a new dataframe 
Then concated category column into this new dataframe 
Finally created a csv file with the final dataframe 
Excel generally can't support this large csv file. Some data may get missed.
The final csv file size is more than 25 mb so unable to upload directly so sharing a link from google drive 
The link for final csv file  :  https://drive.google.com/file/d/1b-LwFW9SLXPeMejiHOyKYi8nhkBYFN00/view?usp=sharing 
