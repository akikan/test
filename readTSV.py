# -*- coding: utf-8 -*-


#改行は削除しない
def readTSV(fileName):
	f = open(fileName, 'r')
	temp = []
	for line in f:
	    temp.append(line.split('\t'))
	return temp

#各行の最大を選ぶ
def splitAndChoose(file,delimita):
	Ymax = len(file)
	Xmax = len(file[0])
	ret = []
	for y in range(Ymax):
		maxim = 0
		char  = ""
		for x in range(Xmax):
			temp = file[y][x].split(delimita)
			if float(temp[-1]) > maxim:
				maxim = float(temp[-1])
				char = temp[-2]
		ret.append(char)
	return ret

file = readTSV("sample.tsv")
print(splitAndChoose(file, '^'))
