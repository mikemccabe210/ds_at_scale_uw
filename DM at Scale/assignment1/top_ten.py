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
        if 'entities' in tweet:
            for tag in tweet['entities']['hashtags']:
                word_count[tag['text']]+=1

    for x in range(0,10):
        a = keywithmaxval(word_count)
        print a.encode('utf-8'),word_count[a]
        word_count[a]=0

    return tweet_scores

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values;
         b) return the key with the max value"""
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]



def main():

    tweet_file = open(sys.argv[1])

    parse_tweets(tweet_file)

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
