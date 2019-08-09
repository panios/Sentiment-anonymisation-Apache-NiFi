from nltk.sentiment.vader import SentimentIntensityAnalyzer
import sys
sid = SentimentIntensityAnalyzer()
ss = sid.polarity_scores(sys.argv[1])
#print('Compound {0} Negative {1} Neutral {2} Positive {3} '.format(ss['compound'],ss['neg'],ss['neu'],ss['pos']))
print('{0},{1},{2},{3}'.format(ss['compound'],ss['neg'],ss['neu'],ss['pos']))
#print('{0}'.format(ss['compound']))