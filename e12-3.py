import urllibfhand = urllib.urlopen('http://www.py4inf.com/code/romeo-full.txt')total = list()for line in fhand:	words = line.split()	for word in words:		total.append(word)			print total[:1656],len(total)