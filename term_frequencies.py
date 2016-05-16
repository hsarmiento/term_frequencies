#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
import string
from nltk import bigrams
from nltk import trigrams
from nltk.util import ngrams
from collections import defaultdict
import vincent
import ast
from xlwt import Workbook, easyxf


#modules created
from pre_processing import PreProcessing
from config import *


#arguments
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
import time
start_time = time.time()


if __name__ == '__main__':
	cur = DB.cursor() 
	count_all = Counter()
	punctuation = list(string.punctuation)
	stop = stopwords.words('spanish') + punctuation + ['rt', 'via']
	prepro = PreProcessing()
	cur.execute(COUNT)
	count_rows = cur.fetchone()[0]
	print "total rows:",count_rows
	for offset in xrange(0,count_rows,BATCH_SIZE):
		cur.execute(QUERY%(BATCH_SIZE,offset))
		for row in cur.fetchall():
			terms_stop = [term for term in prepro.preprocess(row[0]) if len(term) >= 3 and term not in stop]  #ignore terms with length <= 3
			ngram_term = ngrams(terms_stop,2)
			count_all.update(ngram_term)
	terms_max = count_all.most_common(250)

	print terms_max
	print("--- %s seconds ---" % (time.time() - start_time))


