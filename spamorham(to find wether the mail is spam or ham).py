#We'll cheat by using sklearn.naive_bayes to train a spam classifier! Most of the code is just loading our training data into a pandas DataFrame that we can play with:
'''The goal is to:
Read emails from a folder structure (spam and ham)
Extract only the message body,
Store it in a labeled dataset (as "spam" or "ham"),
Later use it for spam detection using machine learning
'''
import io #Used for opening files with a specific encoding (like latin1)
#Encoding tells Python how to read bytes as text.as files are stord in the computer as bytes
#by defualt the file in cpythin is stores as 
#When reading the file, Python must know which encoding was used — otherwise
#it might misinterpret the bytes and show weird symbols or crash.
import os #Lets you interact with the file system (e.g., walking through folders).
#A file system is the part of your operating system (like Windows or Linux) that:
#Organizes how files are stored on the disk
#Keeps track of file names, locations, and sizes
#Makes sure when you open a file, you get the correct data
import numpy
import panda as pd
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
'''Most machine learning algorithms (like Naive Bayes, Logistic Regression, etc.) require numerical input.
But text data is made of words, not numbers.
So we need to:
Convert text into numbers
Keep the meaning or structure useful for classification
That’s where CountVectorizer comes in — it turns text into numerical feature vectors using the Bag-of-Words model.
'''
''' HOW CountVectorizer WORKS (Step-by-Step)
Let’s walk through the steps in detail.

 1. Build Vocabulary
The first thing CountVectorizer does is build a vocabulary — a list of all unique words across your documents.
Example:
Input documents:
docs = [
    "The cat sat on the mat",
    "The dog barked",
    "The cat meowed"
]
Vocabulary (sorted alphabetically or by appearance):
["barked", "cat", "dog", "mat", "meowed", "on", "sat", "the"]
Every word gets an index like:

Word	Index
barked	0
cat	1
dog	2
mat	3
meowed	4
on	5
sat	6
the	7

 2. Count Word Occurrences (Bag-of-Words)
Each document is converted into a vector that counts how often each word appears.

For example:

Document: "The cat sat on the mat"
Vector:

[barked=0, cat=1, dog=0, mat=1, meowed=0, on=1, sat=1, the=2]
→ [0, 1, 0, 1, 0, 1, 1, 2]
Each position in the vector matches the word in the vocabulary.
So now:
We have converted a sentence into a list of numbers.
That list (vector) can now go into a machine learning model'''
#Why is it called "Bag"? Because it’s like dumping all words into a bag and just counting them — no order
#Using CountVectorizer, you convert this into a numerical matrix, then train MultinomialNB to classify between spam and ham.
'''docs = [
    "The cat sat on the mat",     # → Doc 1
    "The dog barked",             # → Doc 2
    "The cat meowed"              # → Doc 3
]
['barked' 'cat' 'dog' 'mat' 'meowed' 'on' 'sat' 'the']
[[0 1 0 1 0 1 1 2]  → Doc 1
 [1 0 1 0 0 0 0 1]  → Doc 2
 [0 1 0 0 1 0 0 1]]  → Doc 3
this is converted to number based on number of occurance'''

from sklearn.naive_bayes import MultinomialNB
''' How multinomialNB Works in Practice
Training: You pass a document-term matrix (from CountVectorizer) and the correct class labels (e.g 'spam' or 'ham').
Model learns:
how often each word appears in spam and ham
The overall probability of spam and ham emails
prediction:-
For a new email it multiplies the probabilities of the words it contains and chooses the class with the highest probability'''
'''Naive Bayes means a method of classifying things using probabilities based on past data, but with the naive assumption that all features are independent from each other.
In simple words:
It looks at your data and calculates how likely each class is.
It assumes that every feature (like words in a sentence or symptoms in a disease) contributes to the decision independently.
Then it picks the class with the highest probability.
Example:
If you’re trying to decide whether an email is spam:
Look at the probability of "free" appearing in spam vs non-spam.Do the same for "win", "offer", etc.Multiply those probabilities together for each class.Choose the class with the higher result

Example
We have two classes: Spam and Not Spam
The email: "win offer"
From our training data:
P(Spam)=0.6


P(Not Spam)=0.4


P("win"∣Spam)=0.5

P("offer"∣Spam)=0.4


P("win"∣Not Spam)=0.1

P("offer"∣Not Spam)=0.05

Step 1: For Spam
Multiply:
0.6×0.5×0.4=0.12
Step 2: For Not Spam
Multiply:
0.4×0.1×0.05=0.002
Step 3: Compare
Spam: 0.12
Not Spam: 0.002

 The bigger number (0.12) means the email is classified as Spam.
'''

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

examples = ['Free Viagra now!!!', "Hi Bob, how about a game of golf tomorrow?"]
example_counts = vectorizer.transform(examples)
predictions = classifier.predict(example_counts)
predictions

