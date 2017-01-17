from collections import Counter
import matplotlib.pyplot as plt
import networkx as nx
import sys
import time
from TwitterAPI import TwitterAPI
from collections import Counter
import pickle
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
import re

consumer_key = 'JyrZ4DEjv6NPw4da7x3VEX1lM'
consumer_secret = 'ACA0VFQLWntdWuC9GUyZ2VM7IopMjJ8LAskUnvWD6z4F9E6uKz'
access_token = '771134752929767424-VN16texnckjaNOj5Fe1278mdCyNU3ry'
access_token_secret = 'pXmyxBHg2lZ914WUaQu8itCSSg32iDYgdF8Psqcb6TgP6'

def get_twitter():
    return TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
    
    
def get_tweets():
    twitter = get_twitter()
    trump_tweets = []
    hillary_tweets = []
    n_tweets=500
    for r in twitter.request('statuses/filter', {'track': 'trump', 'language':'en'}):
        if 'text' in r.keys():
            trump_tweets.append(r)
            if len(trump_tweets) % 100 == 0:
                print('%d tweets' % len(trump_tweets))
            if len(trump_tweets) >= n_tweets:
                break
                
    for r2 in twitter.request('statuses/filter', {'track': 'hillary', 'language':'en'}):
        if 'text' in r2.keys():
            hillary_tweets.append(r2)
            if len(hillary_tweets) % 100 == 0:
                print('%d tweets' % len(hillary_tweets))
            if len(hillary_tweets) >= n_tweets:
                break
    save_file('trump_tweets.txt',trump_tweets)
    save_file('hillary_tweets.txt',hillary_tweets)


def afinn_down():
    url = urlopen('http://www2.compute.dtu.dk/~faan/data/AFINN.zip')
    zipfile = ZipFile(BytesIO(url.read()))
    afinn_file = zipfile.open('AFINN/AFINN-111.txt')
    afinn = dict()
    for line in afinn_file:
        parts = line.strip().split()
        if len(parts) == 2:
            afinn[parts[0].decode("utf-8")] = int(parts[1])
    save_file('afinn_data.txt',afinn)
    
def save_file(filename,data):
    out = open(filename,'ab+')
    pickle.dump(data,out)
    out.close()