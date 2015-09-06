import sys, json

def createSentimentDict(fp):
    d = {}
    for line in fp.readlines():
        word, sentiment = line.rsplit('\t')
        d[word] = int(sentiment)
    return d

def getTweetSentiment(d, tweet):
    tweet = json.loads(tweet)
    sentiment = 0
    text = tweet.get('text')
    if text:
        for w in text.split():
            sentiment += d.get(w, 0)
    return sentiment

def scoreTermSentiment(d, sentiment, tweet):
    tweet = json.loads(tweet)
    sentiment = 0
    text = tweet.get('text')
    if text:
        terms = text.split()
        term_sentiment = sentiment / float(len(terms))
        for w in terms:
            if not d.has_key(w):
                d[w] = term_sentiment

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    d = createSentimentDict(sent_file)
    for tweet in tweet_file.readlines():
        scoreTermSentiment(d, getTweetSentiment(d, tweet), tweet)

    for w, score in d.iteritems():
        print w.encode('utf8'), score

if __name__ == '__main__':
    main()
