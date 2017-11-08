import nltk.classify.util
from nltk.corpus import wordnet 
from nltk.classify import NaiveBayesClassifier
import pickle


#TODO: Applies Naive Bayes Algo to check to get top 5 urls from feeded trained data and
## check if url relevant using nlp, check if it is not social-media url
def refine_urls(url_list, related_word):
    return url_list[:20]
'''
    demo_train = ['wikipedia','blog','blogspot','research','wiki']
    #train_sets=[({i.lower() for i in demo_train],'req'}
    req_urls= []
    
    train_sets = [({'wikipedia':True},'req'),({'blog':True},'req'),({'blogspot':True},'req'),({'wiki':True,},'req'),({'facebook':False,'yahoo':False,'gnome':False},'notreq')]
    print(train_sets)
    unsense={'facebook':False,'yahoo':False,'gnome':False}
    classifier = nltk.NaiveBayesClassifier.train(train_sets)
    for url in url_list:
        if classifier.classify({url:True}):
            print(classifier.classify({url:True}))
            print(classifier.show_most_informative_features(9))

    
##urls=['https://en.wikipedia.org/wiki/Akbar','www.culturalindia.net','www.facebook.com']
##r=[]
##refine_urls(urls,r)

'''

#TODO: Apply nlp and trained data to check it's relation from topics like tech, sports, etc


#def select_imp_data(data_list, related_word, topic):    
#     featureset = []
#     req_data = []
#     for relw in related_word:
#         for sy in wordnet.synsets(relw):
#             for l in sy.lemmas():
#                 featureset.append((l.name(),topic))
#     train_set = featureset
#     classifier = nltk.NaiveBayesClassifier.train(train_set)
#     for data in data_list:
#         if classifier.classify(data) == topic:
#             req_data.append(data)
#     return req_data
    	
def select_imp_data(data_list, related_word, topic):
    fobj=open('./classifier/classifier.pickle','rb')
    classifier= pickle.load(fobj)
    fobj.close()
    imp_data=[]
    for req_data in data_list['text']:
        for key,value in req_data.items():
            if type(value) is list:
                arr=[]
                for par in value:
                   if classifier.classify(featureset(par)) == topic:
                      arr.append(par)
                imp_data.append({key,arr})
            else:
                if classifier.classify(featureset(value)) == topic:
                    imp_data.append({key,value})
    return imp_data



def featureset(s):
    return {s:True}
    
    
    
