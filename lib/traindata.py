import json
import nltk
import pickle
trainer = []
topic=['tech','sports','buisness']
for i in range(200):
    fobj = open("news_"+'{:07}'.format(i)+".json")
    data = json.load(fobj)
    trainer.append(
        ({sentence: True for sentence in nltk.sent_tokenize(data["text"])}, topic[0]))
    fobj.close()
with open("t_data", 'wb') as f:
    pickle.dump(trainer, f)
