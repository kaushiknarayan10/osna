def summarize():
    trump_tweets = load_file('trump_tweets.txt')
    hillary_tweets = load_file('hillary_tweets.txt')
    hillary_positives = load_file('hillary_positive.txt')
    hillary_negatives = load_file('hillary_negative.txt')
    trump_positives = load_file('trump_positive.txt')
    trump_negatives = load_file('trump_negative.txt')
    
    trump_tweets1 = [t for t in trump_tweets if 'user' in t]
    hillary_tweets1 = [t for t in hillary_tweets if 'user' in t]
    
    total = len(trump_tweets1) + len(hillary_tweets1)
    
    save_file('summary.txt','Total Users :')
    save_file('summary.txt',total)
    
    save_file('summary.txt','No of messages :')
    save_file('summary.txt',len(trump_tweets) + len(hillary_tweets))
    
    res = []
    for tweet, pos, neg in sorted(hillary_positives, key=lambda x: x[1], reverse=True):
        top pos = pos
        top neg = neg
        t = tweet
        res.append(pos,neg,tweet)
        save_file('summary.txt','Top positive sentiment tweet for Hillary :')
        save_file('summary.txt',res)
    
        break
        
    for tweet, pos, neg in sorted(hillary_negatives, key=lambda x: x[1], reverse=True):
        top pos = pos
        top neg = neg
        t = tweet
        res.append(pos,neg,tweet)
        save_file('summary.txt','Top negative sentiment tweet for Hillary :')
        save_file('summary.txt',res)
        break
        
    for tweet, pos, neg in sorted(trump_positives, key=lambda x: x[1], reverse=True):
        top pos = pos
        top neg = neg
        t = tweet
        res.append(pos,neg,tweet)
        save_file('summary.txt','Top positive sentiment tweet for Trump :')
        save_file('summary.txt',res)
        break
        
    for tweet, pos, neg in sorted(trump_negatives, key=lambda x: x[1], reverse=True):
        top pos = pos
        top neg = neg
        t = tweet
        res.append(pos,neg,tweet)
        save_file('summary.txt','Top negative sentiment tweet for Trump :')
        save_file('summary.txt',res)
        break