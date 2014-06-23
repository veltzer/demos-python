#!/usr/bin/python

# this is a simple solution to the reverse hash function exercise

def rev_hash(o):
	""" reverse a hash (build a value=>key mapping)

	>>> rev_hash({"Israel":"Jerusalem","France":"Paris","Italy":"Rome","Egypt":"Cairo"})
	{'Paris': 'France', 'Cairo': 'Egypt', 'Rome': 'Italy', 'Jerusalem': 'Israel'}
	"""
	ret={}
	for k,v in o.items():
		ret[v]=k
	return ret

#orig={"Israel":"Jerusalem","France":"Paris","Italy":"Rome","Egypt":"Cairo"}
#rev=rev_hash(orig)
#print(rev)

import doctest
#print(dir(doctest))
doctest.testmod()
