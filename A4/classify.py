def afinn_score(terms, afinn):
    pos = 0
    neg = 0
    for t in terms:
        if t in afinn:
            if afinn[t] > 0:
                pos += afinn[t]
            else:
                neg += -1 * afinn[t] 
    return pos, neg


def tokenize(tweets):
    tokens = []
    for tweet in tweets:
        text = tweet['text'].lower()
        text = re.sub('@\S+', ' ', text)
        text = re.sub('http\S+', ' ', text)
        tokens.append(re.findall('[A-Za-z]+', text))
    return tokens


def load_file(filename):
    inputfile = open(filename,'rb')
    data = pickle.load(inputfile)
    return data
    
def sentiment_analysis():
    tokens = []
    trump_tweets = load_file('trump_tweets.txt')
    hillary_tweets = load_file('hillary_tweets.txt')
    afinn = load_file('afinn_data.txt')
    trump_tokens = tokenize(trump_tweets)
    hillary_tokens = tokenize(hillary_tweets)
    trump_positives = []
    trump_negatives = []
    hillary_positives = []
    hillary_negatives = []
    for token_list, tweet in zip(trump_tokens, trump_tweets):
        pos, neg = afinn_score(token_list, afinn)
        if pos > neg1:
            trump_positives.append((tweet['text'], pos, neg))
                
        elif neg > pos:
            trump_negatives.append((tweet['text'], pos, neg))
    
    save_file('trump_positive.txt',trump_positives)
    save_file('trump_negative.txt',trump_negatives)
    
    for token_list, tweet in zip(hillary_tokens, hillary_tweets):
        pos, neg = afinn_score(token_list, afinn)
        if pos > neg:
            hillary_positives.append((tweet['text'], pos, neg))
                
        elif neg > pos:
            hillary_negatives.append((tweet['text'], pos, neg))
    
    save_file('hillary_positive.txt',hillary_positives)
    save_file('hillary_negative.txt',hillary_negatives)