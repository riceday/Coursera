import sys, json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

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

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    d = createSentimentDict(sent_file)
    for tweet in tweet_file.readlines():
        print getTweetSentiment(d, tweet)

if __name__ == '__main__':
    main()
