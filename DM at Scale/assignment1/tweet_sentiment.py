import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

state_list = [states[x] for x in states]

states_dict = {states[k]:k for k in states}
state_list.extend([x for x in states])


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
    state_dict = {x:0 for x in states}
    state_count = {x:0 for x in states}
    tweet_scores=[]
    for line in tweet_file:
        score = 0
        tweet = json.loads(line.strip())
        if 'text' in tweet:
            textsplit = tweet['text'].split()
            for word in textsplit:
                score += score_dict.get(word,0)
            for state in state_list:
                if state in tweet['user']['location'].encode('utf-8'):
                    state_dict[states_dict.get(state,state)]+=score
                    state_count[states_dict.get(state,state)]+=1
        tweet_scores.append(score)
    avg_state = {x:float(state_dict[x])/float(state_count[x]) for x in state_dict if state_count[x]!=0}
    print keywithmaxval(avg_state).strip()
    return tweet_scores

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values;
         b) return the key with the max value"""
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]


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
