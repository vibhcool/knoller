import nltk.classify.util
from nltk.corpus import wordnet 
from nltk.classify import NaiveBayesClassifier


#TODO: Applies Naive Bayes Algo to check to get top 5 urls from feeded trained data and
# check if url relevant using nlp, check if it is not social-media url
def refine_urls(url_list, related_word):
    pass




#TODO: Apply nlp and trained data to check it's relation from topics like tech, sports, etc
def select_imp_data(data_list, related_word):
	featureset = []
	req_data = []
	for relw in related_word:
		for sy in wordnet.synsets(relw):
    		for l in sy.lemmas():
        		featureset.append((l.name(),'required'))
    train_set = featureset
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    for data in data_list:
    	if classifier.classify(data) == 'required':
    		req_data.append(data)
    return req_data
    	
