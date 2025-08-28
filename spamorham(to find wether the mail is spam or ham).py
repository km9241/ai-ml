# by using sklearn.naive_bayes to train a spam classifier most of the code is just loading our training data into a pandas DataFrame that we can play with
'''The goal is to:
Read emails from a folder structure (spam and ham)
Extract only the message body,store it in a labeled dataset (as spam or ham),later use it for spam detection using machine learning(from sklearn.naive_bayes import MultinomialNB)
'''
import io #Used for opening files with a specific encoding (like latin1)
import os #Lets you interact with the file system ( walking through folders).
import numpy
import panda as pd
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
'''Most machine learning algorithms (like Naive Bayes, Logistic Regression, etc.) require numerical input not number
So we need to Convert text into numbers Thats where CountVectorizer comes in — it turns text into numerical feature vectors using the Bag-of-Words model.'''


from sklearn.naive_bayes import MultinomialNB
''' How multinomialNB Works in Practice
Training: You pass a document-term matrix (from CountVectorizer) and the correct class labels ('spam' or 'ham').
Model learns: how often each word appears in spam and ham folders
and the overall probability of spam and ham emails
prediction:-For a new email it multiplies the probabilities of the words it contains and chooses the class with the highest probability(bayerns therorum sort of thing)'''
'''Naive Bayes means a method of classifying things using probabilities based on past data, but with the naive assumption that all features are independent from each other
in simple words:It looks at your data and calculates how likely each class is
it asssumes that every feature (like words in a sentence ) contributes to the decision independently
then it picks the class with the highest probability.'''
# using a bag of word model
def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)

            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message


def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)

    return DataFrame(rows, index=index)

data = DataFrame({'message': [], 'class': []})

data = pd.concat([data, dataFrameFromDirectory("C:\ml couse file\MLCourse\emails", "spam")])
data = pd.concat([data, dataFrameFromDirectory("C:\ml couse file\MLCourse\emails", "ham")])

data.head()
'''Now we will use a CountVectorizer to split up each message into its list of words, and throw that into a MultinomialNB classifier. Call fit() and we've got a trained spam filter ready to go!'''
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)
classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)

examples = ['Free Viagra now!', "Hi drake how about we go to diddy party?"]
example_counts = vectorizer.transform(examples)
predictions = classifier.predict(example_counts)
predictions



