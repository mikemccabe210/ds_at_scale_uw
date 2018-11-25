import sys
import json
from collections import defaultdict



def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def parse_tweets(tweet_file):
    word_count = defaultdict(lambda: 0)
    tweet_scores=[]
    total_words = 0
    for line in tweet_file:
        tweet = json.loads(line.strip())
        if 'text' in tweet:
            textsplit = tweet['text'].split()
            undef = []
            for word in textsplit:
                total_words +=1
                word_count[word]+=1
        for word in word_count:
            print word.encode('utf-8'), float(word_count[word])/float(total_words)
    return tweet_scores



def main():

    tweet_file = open(sys.argv[1])

    parse_tweets(tweet_file)

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
