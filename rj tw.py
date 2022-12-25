import tweepy
import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns

# Access
acces_token='1189193716210126851-BctMQL5GbsbCBE096ihwyfVIFOme84'
acces_token_secret='e78h2f2X1GjXEMyfX064OAotIrOT0C7F8LYIV5AYKPXWT'

#Consumer
consumer_key='L3RNiywgtzucRJBT3YH44g3yZ'
consumer_secret='el1NLHZMsjXPdP6j4GDcOqoJcSZsjXX4ZkqFUci255VKd1CTWV'

# We import our access keys:
 
def twitter_setup():
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(acces_token, acces_token_secret)
    
    api = tweepy.API(auth)
    return api


extractor = twitter_setup()
 
#tweets = extractor.user_timeline(screen_name="NarendraModi", count = 200)
tweets=[tweet for tweet in tweepy.Cursor(extractor.user_timeline,screen_name="NarendraModi").items()]
print("number of tweets extracted: {}.\n".format(len(tweets)))
 
print("5 recent tweets:\n")
for tweet in tweets[:5]:
    print(tweet.text)
    print()


data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweets'])
 
display(data.head(10))


data.columns,data.shape,data.dtypes,data.head()


# We print info from the first tweet:
 
print(tweets[0].id)
print(tweets[0].created_at)
print(tweets[0].source)
print(tweets[0].favorite_count)
print(tweets[0].retweet_count)
print(tweets[0].geo)
print(tweets[0].coordinates)
print(tweets[0].entities)


# We add relevant data
data['len'] = np.array([len(tweet.text) for tweet in tweets])
data['ID'] = np.array([tweet.id for tweet in tweets])
data['Date'] = np.array([tweet.created_at for tweet in tweets])
data['Source'] = np.array([tweet.source for tweet in tweets])
data['Likes'] = np.array([tweet.favorite_count for tweet in tweets])
data['RTs'] = np.array([tweet.retweet_count for tweet in tweets])


display(data.head(10))


data.to_csv('Narendra_Modi_Latest')
data.columns


# Visualization and basic stats
 
# We extract the mean of length
 
mean = np.mean(data['len'])
print("the length's average in tweets: {}".format(mean))


# We extract the tweet with more FAVs and mote RTs:
 
fav_max = np.max(data['Likes'])
rt_max = np.max(data['RTs'])
 
fav = data[data.Likes == fav_max].index[0]
rt = data[data.RTs == rt_max].index[0]
 
# Max FAVs:
print("the tweet with more likes is: \n{}".format(data['tweets'][fav]))
print("Number of likes: {}".format(fav_max))
print("{} character.\n".format(data['len'][fav]))
 
# Max RTs:
print("The tweet with more retweets is: \n{}".format(data['tweets'][rt]))
print("Number of retweets: {}".format(rt_max))
print("{} character.\n".format(data['len'][rt]))


tlen = pd.Series(data = data['len'].values)   #, index=data['Data'])
tfav = pd.Series(data = data['Likes'].values)   #, index=data['Data'])
tret = pd.Series(data = data['RTs'].values) #, index=data['Data']
