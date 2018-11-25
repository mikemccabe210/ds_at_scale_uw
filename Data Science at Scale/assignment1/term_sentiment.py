import sys
import json
from collections import defaultdict



def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def create_dict(score_file):

    scores = {} # initialize an empty dictionary
    for line in score_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    return scores

def parse_tweets(tweet_file,score_dict):
    term_list = defaultdict(lambda: [0,0])
    tweet_scores=[]
    for line in tweet_file:
        flag = 0
        score = 0
        tweet = json.loads(line.strip())
        if 'text' in tweet:
            textsplit = tweet['text'].split()
            undef = []
            for word in textsplit:
                score += score_dict.get(word,0)
                if score_dict.get(word,0) == 0:
                    undef.append(word)
                else:
                    flag=1
            if flag==1:
                for word in undef:
                    term_list[word]=[term_list[word][0]+score/len(textsplit),term_list[word][1]+1]
        for k in term_list:
            print k.encode('utf-8'), term_list[k][0]/term_list[k][1]
        tweet_scores.append(score)
    return tweet_scores



def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scoredict = create_dict(sent_file)
    parse_tweets(tweet_file,scoredict)

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
