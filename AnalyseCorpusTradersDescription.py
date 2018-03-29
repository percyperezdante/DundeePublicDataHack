#!/usr/bin/python 

# This is a code generated by the script main.codeGeneratorLDAAnalyserExecutor.sh

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import nltk
import gensim
from gensim import corpora

doc1 = "Puddledub,Farm produced pork, bacon, sausages, pies, and charcuterie."
doc2 = "Brewsters,Free range eggs, chicken, honey, smoked products.,,"
doc3 = "Wild Hearth Bakery,Range of speciality breads including white sourdough, Yorkshire whole-wheat, miche, ciabatta, baguettes, fig / orange / almond croissants, Danish pastries, pain au chocolat, pain au raisin, cinnamon scroll, bomboloni."
doc4 = "Hubertus Game,Wild shot venison and small game."
doc5 = "Eden Mill,The sale and sampling of gin, gin liqueurs, gin cocktails, beers, whisky, glassware and gift sets."
doc6 = "Paper & Jam,Homemade Preserves: Pink Grapefruit & Lime Marmalade, Red Pepper & Chilli Jam, Apple & Star Anise Jelly, Scottish Apple & Rowan, Lemon Grass & Ginger Jelly. Homemade Cakes: Spiced Fruit Cake and Dundee Cake. Homemade Confectionery: Paradise Rum & Ginger Balls, Tablet, Coconut Ice, Marshmallow, Rocky Road. Homemade Vietnamese Rice Paper Rolls (Seasonal March to October).,,"
doc7 = "Highland Drovers,Highland beef, Hebridean Lamb."
doc8 = "Berit Thomson Pewterware,Handmade pewterware.,,"
doc9 = "Dundee Cheesecakes,Baked New York Style Cheesecakes."
doc10 = "Cairn Mohr,Fruit wines, bottled ciders, award winning sparkling elderflower and elderberry non alcoholic drinks, and the Carse of Gowrie apple juice"
doc11 = "Arbroath Fisheries,Fresh and smoked fish, shellfish, fish cakes, seafood, fish soup, pies and quiches."
doc12 = "Rockin Robins Bakery,Gluten free vegan cupcakes and cookies, make your own cookie jars, and other seasonal items.,,"
doc13 = "Redcastle Brewery,Bespoke ales, gin and rums."
doc14 = "Devenick Dairy,Cheese, veal, pork, cheesecake."
doc15 = "Allan Chilli Products,Jars of award winning homemade chilli jellies and bottles of award winning sauces."
doc16 = "John Reid & Sons,Fresh fruit and vegetables, honey, eggs, jam.,,"
doc17 = "Inverness Fudge,Assortment of confectionery including chocolates, liquorice, fudge, tablet and toffees.,,"
doc18 = "Planet Soap,Soaps, candles, bath bombs and accessories all hand made."

# compiling documents
doc_complete = [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8, doc9, doc10, doc11, doc12, doc13, doc14, doc15, doc16, doc17, doc18]

#  Cleaning

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in doc_complete]    

#print(doc_clean)

# Creating the term dictionary of our courpus, where every unique term is assigned an index. 
dictionary = corpora.Dictionary(doc_clean)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
#print(doc_term_matrix)

# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=150)


# Printing results
# Expected results
# [(0, u'0.065*"driving" + 0.065*"pressure" + 0.064*"stress"'), (1, u'0.050*"spends" + 0.050*"practice" + 0.050*"around"'), (2, u'0.076*"sugar" + 0.076*"father" + 0.076*"sister"')]

print(ldamodel.print_topics(num_topics=3, num_words=3))


