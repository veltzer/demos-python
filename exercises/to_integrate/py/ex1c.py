#!/usr/bin/python3

digits=set(['0','1','2','3','4','5','6','7','8','9'])
found=True
while found:
	input_string=raw_input("Please give me some digits... \n")
	found=False
	for character in input_string:
		if not character in digits:
			# we have a non digit!
			print("Error, you gave me non digits")
			found=True
			break
print("starting real work on",input_string)
