#!/usr/bin/python

f=open("input.txt")
report={}
for line in f.readlines():
	for c in line:
		if not(c in [" ","\n","\r","\t"]):
			if (report.has_key(c)):
				report[c] += 1
			else:
				report[c]=1
f=open("report.txt",'w')
f.write(str(report))
f.close()
