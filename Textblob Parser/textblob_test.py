from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import re
import nltk

nltk.download('punkt')
'''
PATTERN 1
[To] 2 Prs [Pairs] Girls Stays N 7 [at] 6/6
[To] 2 Prs [Pairs] Womens Stays [N] 2 [at] 12/6
[To] 2 Prs [Pairs] Do [Womens] Do [Stays] [N ]4 [at] 18/

PATTERN 2
[To] Nathaniel Grigsby 0..4..[0]
[To] Lewis Renoe 0..5..9
[To] Ambrose Hewlitt 0..2..[0]
'''

train = [('[To] 2 Prs [Pairs] Girls Stays N 7 [at] 6/6', 1), ('[To] 2 Prs [Pairs] Womens Stays [N] 2 [at] 12/6', 1), ('[To] 2 Prs [Pairs] Do [Womens] Do [Stays] [N ]4 [at] 18/',1), ('[To] Nathaniel Grigsby 0..4..[0]',2),('[To] Lewis Renoe 0..5..9',2),('[To] Ambrose Hewlitt 0..2..[0]',2)]

cl = NaiveBayesClassifier(train)

'''
TO CLASSIFY:
PATTERN 1:
[To] 2 Prs [Pairs] Girls Stays N 6 [at] 4/4
[To] 2 Prs [Pairs] Womens Stays [N] 5 [at] 14/7
[To] 2 Prs [Pairs] Do [Womens] Do [Stays] [N ]5 [at] 19/

PATTERN 2:
[To] William Tredaway 0..15..[0]
[To] Daniel Smith 0..15..2
[To] Thomas Reeves 3..0..0 
'''

to_classify = ['[To] 2 Prs [Pairs] Girls Stays N 6 [at] 4/4','[To] 2 Prs [Pairs] Womens Stays [N] 5 [at] 14/7','[To] 2 Prs [Pairs] Do [Womens] Do [Stays] [N ]5 [at] 19/','[To] William Tredaway 0..15..[0]','[To] Daniel Smith 0..15..2','[To] Thomas Reeves 3..0..0']

for s in to_classify:
    print(str(cl.classify(s)))

