import nltk
from tika import parser
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from string import Template


from nltk.chunk import conlltags2tree, tree2conlltags, ne_chunk
from pprint import pprint

import resumeTemplate

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')



# file_path = "Data/Christy new CV.pdf"

# sent = []

# print(text)
tokens = []
def findFilePath(file_path):
    file_data = parser.from_file(file_path)

    # what's the content?
    text = file_data['content']
    global tokens
    tokens = tokenization(text)

    print(tokens)

    stop_words = set(stopwords.words('english'))
    # filtered_text = [w for w in tokens if not w in stop_words]
    filtered_text = []

    for w in tokens:
        if w not in stop_words:
            filtered_text.append(w)
    print(filtered_text)
    sent = posTagger(filtered_text)

    print(sent)



    pattern_name = 'NP: {<NNP>?<NNP>}'
    cp = nltk.RegexpParser(pattern_name)
    cs = cp.parse(sent)
    print(cs)

    iob_tagged = tree2conlltags(cs)
    pprint(iob_tagged)
    # extract_email = extract_email_addresses(sent)
    # print(extract_email)

    # extractName(tokens)
    # extractData(tokens)
    # ne_tree = ne_chunk(iob_tagged)
    # print(ne_tree)
    return text



def tokenization(tex) :

    tokenz = word_tokenize(tex)

    return tokenz

def posTagger(sent):
    sent = nltk.pos_tag(sent)
    return sent

# pattern = 'NP: {<DT>?<JJ>*<NN>}'


# def extract_email_addresses(string):
#     r = re.compile(r'[\w\.-]+@[\w\.-]+')
#     return r.findall(string)

def extractName(sent):
    name = (sent[0] +" "+ sent[1])
    print(name)
    return name


def extractAddress(sent):
    i = 0
    start = 0
    end = 0
    addr = ""
    for w in sent:
        i = i + 1
        if w == "ADDRESS":
            start = i
        if w == "PHONE":
            end = i
            break

    while start < end - 1:
        addr = addr + " " + sent[start]
        start = start + 1
    return addr

def extractPhoneNumber(sent):
    i = 0
    start = 0
    end = 0
    number = ""
    for w in sent:
        i = i + 1
        if w == "PHONE":
            start = i
        if w == "EMAIL":
            end = i
            break

    while start < end - 1:
        number = number + " " + sent[start]
        start = start + 1
    return number

def extractEmail(sent):
    i = 0
    start = 0
    end = 0
    email = ""
    for w in sent:
        i = i + 1
        if w == "EMAIL":
            start = i
        if w == "SKILLS":
            end = i
            break

    while start < end - 1:
        email = email + " " + sent[start]
        start = start + 1
    return email

def extractSkills(sent):
    i = 0
    start = 0
    end = 0
    skills = ""
    for w in sent:
        i = i + 1
        if w == "SKILLS":
            start = i
        if w == "PROFILE":
            end = i
            break

    while start < end - 1:
        skills = skills + " " + sent[start]
        start = start + 1
    return skills

def extractTitle(sent):
    i = 0
    start = 0
    end = 0
    title = ""
    for w in sent:
        i = i + 1
        if w == sent[1]:
            start = i
        if w == "INFO":
            end = i
            break

    while start < end - 1:
        title = title + " " + sent[start]
        start = start + 1
    return title

def extractExperience(sent):
    i = 0
    start = 0
    end = 0
    experience = ""
    for w in sent:
        i = i + 1
        if w == "EMPLOYMENT":
            start = i + 1
        if w == "EDUCATION":
            end = i
            break

    while start < end - 1:
        experience = experience + " " + sent[start]
        start = start + 1
    return experience

def extractEducation(sent):
    i = 0
    start = 0
    end = 0
    education = ""
    for w in sent:
        i = i + 1
        if w == "EDUCATION":
            start = i
            end = len(sent)
            break

    while start < end:
        education = education + " " + sent[start]
        start = start + 1
    return education
# #open file
# templatein = open( 'Template.txt' )
#
# #read file
# src = Template(templatein.read())
#
# #data
# def extractData():
#     name = "Name:"+extractName(tokens)
#     title = "Title:"
#     address = "Address:"+extractAddress(tokens)
#     phone = "Phone Number:"+extractPhoneNumber(tokens)
#     email = "Email:"+extractEmail(tokens)
#     skills = "Skills:"+extractSkills(tokens)
#     experience = "Experience:"
#     education_qualification = "Education Qualification:"
#     d = {'name':name, 'title':title, 'address':address, 'phone':phone, 'email':email, 'skills':skills, 'experience':'\n'.join(experience),'education_qualification':'\n'.join(education_qualification)}
#
#     #substitution
#     result = src.substitute(d)
#
#     print(result)
#     return result


def return_name():
    return extractName(tokens)

def return_title():
    return extractTitle(tokens)

def return_address():
    return extractAddress(tokens)

def return_phoneNumber():
    return extractPhoneNumber(tokens)

def return_email():
    return extractEmail(tokens)

def return_skills():
    return extractSkills(tokens)

def return_experience():
    return extractExperience(tokens)

def return_education():
    return  extractEducation(tokens)