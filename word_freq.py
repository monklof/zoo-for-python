import pandas as pd
import numpy as np
import PyPDF2
# import textract
import re
import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer


from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn

from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer


# 获取单词的词性
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

text = open("/Users/monk/Downloads/test.txt", 'rt').read()
# text = text.lower()
import wordninja

tokens_init = word_tokenize(text)  # 分词
tokens = []
for tok in tokens_init:
    if len(tok) >= 30:
        # print("split: ", tok)
        splits = wordninja.split(tok)
        # print("splits: ", splits)
    else:
        splits = [tok]
    tokens.extend(splits)


tagged_sent = pos_tag(tokens)  # 获取单词词性

wnl = WordNetLemmatizer()
lemmas_sent = []
for tag in tagged_sent:
    # print(tag)
    wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
    pp = wnl.lemmatize(tag[0], pos=wordnet_pos)# 词形还原
    # print(pp)
    lemmas_sent.append(pp)


#
# word_stemmer = SnowballStemmer('english')#  PorterStemmer()
#

# filename = '/Users/monk/Documents/Books/20220113 The New Taxonomy of Educational Objectives.pdf'
#
# pdfFileObj = open(filename, 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# num_pages = pdfReader.numPages
#
# count = 0
# text = ""
#
# while count < num_pages:
#     pageObj = pdfReader.getPage(count)
#     count += 1
#     text += pageObj.extractText()
#     text += " "
#
# if text != "":
#     text = text
# else:
#     # text = textract.process('words.txt', method='tesseract', language='eng')
#     raise Exception

stopwords = []
stopwords += ['a', 'about', 'above', 'across', 'after', 'afterwards']
stopwords += ['again', 'against', 'all', 'almost', 'alone', 'along']
stopwords += ['already', 'also', 'although', 'always', 'am', 'among']
stopwords += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
stopwords += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
stopwords += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
stopwords += ['because', 'become', 'becomes', 'becoming', 'been']
stopwords += ['before', 'beforehand', 'behind', 'being', 'below']
stopwords += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
stopwords += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
stopwords += ['co', 'con', 'could', 'couldnt', 'cry', 'de']
stopwords += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
stopwords += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
stopwords += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
stopwords += ['every', 'everyone', 'everything', 'everywhere', 'except']
stopwords += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
stopwords += ['five', 'for', 'former', 'formerly', 'forty', 'found']
stopwords += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
stopwords += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
stopwords += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
stopwords += ['herself', 'him', 'himself', 'his', 'how', 'however']
stopwords += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
stopwords += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
stopwords += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
stopwords += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
stopwords += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
stopwords += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
stopwords += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
stopwords += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
stopwords += ['off', 'often', 'on','once', 'one', 'only', 'onto', 'or']
stopwords += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
stopwords += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
stopwords += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
stopwords += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
stopwords += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
stopwords += ['some', 'somehow', 'someone', 'something', 'sometime']
stopwords += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
stopwords += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
stopwords += ['then', 'thence', 'there', 'thereafter', 'thereby']
stopwords += ['therefore', 'therein', 'thereupon', 'these', 'they']
stopwords += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
stopwords += ['three', 'through', 'throughout', 'thru', 'thus', 'to']
stopwords += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
stopwords += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
stopwords += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
stopwords += ['whatever', 'when', 'whence', 'whenever', 'where']
stopwords += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
stopwords += ['wherever', 'whether', 'which', 'while', 'whither', 'who']
stopwords += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with']
stopwords += ['within', 'without', 'would', 'yet', 'you', 'your']
stopwords += ['yours', 'yourself', 'yourselves']
stopwords += ['new']

stopwords = set(stopwords)

# text = text.encode('ascii', 'ignore').lower()
# text_decoded = text.decode()


# words = text.split(" ")
# words = text_decoded.split()

keywords = {}
total = 0

for w in lemmas_sent:
    p = w.strip().lower()
    m = re.search(r'[a-zA-Z]+', p)
    if not m:
        continue
    p = m.group(0)
    if len(p) < 3 or len(p) > 30:
        continue
    if p in stopwords:
        continue
    # p = word_stemmer.stem(p)
    if p not in keywords:
        keywords[p] = 0
    keywords[p] += 1
    total += 1

def sortFreqDict(freqdict):
    aux = [(freqdict[key], "%.4f" % (freqdict[key]/total, ), key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux


df = pd.DataFrame(sortFreqDict(keywords), columns=['freq', 'ratio', 'keyword'])
df.to_csv('out_put.csv', index=True)
print("total: ", len(keywords))
print(df.to_string())
