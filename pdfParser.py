import nltk
from tika import parser
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from tkinter import  *

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')



file_path = "Data/Christy new CV.pdf"

file_data = parser.from_file(file_path)

text = file_data['content']

print(text)

def tokenization(tex) :

    tokenz = word_tokenize(tex)

    return tokenz

tokens = tokenization(text)

print(tokens)


stop_words = set(stopwords.words('english'))
filtered_text = [w for w in tokens if not w in stop_words]
filtered_text = []

for w in tokens:
    if w not in stop_words:
        filtered_text.append(w)

print(filtered_text)











