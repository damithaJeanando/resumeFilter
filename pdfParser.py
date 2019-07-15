import nltk
from tika import parser
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')



# file_path = "Data/Christy new CV.pdf"



# print(text)

def findFilePath(file_path):
    file_data = parser.from_file(file_path)


    text = file_data['content']
    tokens = tokenization(text)

    print(tokens)

    stop_words = set(stopwords.words('english'))
    filtered_text = [w for w in tokens if not w in stop_words]
    filtered_text = []

    for w in tokens:
        if w not in stop_words:
            filtered_text.append(w)
    print(filtered_text)
    sent = posTagger(filtered_text)
    print(sent)
    return text



def tokenization(tex) :

    tokenz = word_tokenize(tex)

    return tokenz

def posTagger(sent):
    sent = nltk.pos_tag(sent)
    return sent













