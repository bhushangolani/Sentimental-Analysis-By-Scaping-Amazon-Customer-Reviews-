
import pandas as pd
import re
import string

def clean_text_round1(text): 
#Making the complete text free of Punctuation marks, making the text lowercase and removing numbers
    text = text.lower() #Making the text lowercase
    text = re.sub('(https|http)?:\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', text) #Removes all kinds of websites
    text = re.sub('www\.\S+\.com', '', text) #Removes websites
    text = re.sub('rt|cc', '', text) #Removes retweets
    text = re.sub('@\S+', '', text) #Removing user mentions
    text = re.sub('[^\x00-\x7F]+', '', text) #Removing emojis
    text = re.sub('<.*?>', '', text) #Removing HTML tags
    text = re.sub(' +', ' ', text) #removing extra spaces
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text) #Making all the punctuations disappear
    text = re.sub('\w*\d\w*', '', text) #Making all the numbers disappear
    text = re.sub("'","", text )
    return text

round1 = lambda x: clean_text_round1(x)
data_clean = pd.read_csv("DATA.csv")
data_clean = pd.DataFrame(data_clean.Review.apply(round1))


#Now starting the process of sentimental analysis
from textblob import TextBlob
pol = lambda x: TextBlob(x).sentiment.polarity
sub = lambda x: TextBlob(x).sentiment.subjectivity


data=pd.read_csv("DATA.csv")

data_clean['polarity'] = data_clean['Review'].apply(pol)
data_clean['subjectivity'] = data_clean['Review'].apply(sub)

data['polarity']=data_clean['polarity']
data['subjectivity']=data_clean['subjectivity']

data.to_csv('RESULT.csv') 

