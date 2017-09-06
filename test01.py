# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
import random

def readFile(unknown_fileReader, unknown_data, unknown_label, real_fileReader, real_data, real_label, parse):
	for row in unknown_fileReader:
		real_label.append(row[len(row)-1])# label取得
		del row[len(row)-1]           # 元データからラベル削除
		real_data.append(row)              # ラベル以外を別のとこに保存
	for row in real_fileReader:
		real_label.append(row[len(row)-1])# label取得
		del row[len(row)-1]           # 元データからラベル削除
		real_data.append(row)              # ラベル以外を別のとこに保存
	#ここまでで全データを読み込み

	#ここかｒらランダムにいくつか取得する

	sumLabel = len(real_label)
	array=[]
	num = sumLabel*parse/100
	for i in range(sumLabel):#全ラベル数の配列取得
		array.append(i)

	print int(num)
	randomArray = random.sample(array, num)#全データの中から指定されたパーセント分のデータだけ取得
	print randomArray
	for i in range(len(randomArray)):
		temp = randomArray[i]
		data = real_data[temp]
		label = real_label[temp]
		print i
		unknown_data.append(data)
		unknown_label.append(label)
		del real_data[temp]
		del real_label[temp]
		for j in range(len(randomArray)):
			if randomArray[j] > temp:
				randomArray[j] -= 1
		

	return unknown_data, unknown_label, real_data, real_label


f  = open("akarennga_NM.csv","r")
uf  = open("akarennga_NMu.csv","r")
reader = csv.reader(f)#ファイル読み込み
ureader= csv.reader(uf)#ファイル読み込み
r_label = []
r_data = []
u_label = []
u_data = []
u_data, u_label, r_data, r_label = readFile(ureader, u_data, u_label, reader, r_data, r_label, 70)

f.close()
uf.close()

print u_label
print len(u_label)
print r_label
print len(r_label)