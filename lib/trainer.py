import nltk.classify.util
from nltk.corpus import wordnet 
from nltk.classify import NaiveBayesClassifier
import pickle

data = []

with open('./train_data/bizz/bt_data','rb') as f:
    data.extend(pickle.load(f))

with open('./train_data/tech/tt_data','rb') as f:
    data.extend(pickle.load(f))

with open('./train_data/sports/st_data','rb') as f:
    data.extend(pickle.load(f))

#print(data)

## tain Naive Bayes Classifier 
classifier = nltk.NaiveBayesClassifier.train(data)

##Save classifier in ./classifier/classifier.pickle file
with open('./classifier/classifier.pickle','wb') as f:
    pickle.dump(data,f)
    