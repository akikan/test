# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
import numpy as np
from sklearn.ensemble import RandomForestClassifier

csvfile = "Normal_MD.csv"
unknown = "Normal_MD_unknown.csv"
f = open(csvfile,"r")
uf= open(unknown,"r")
reader = csv.reader(f)
ureader= csv.reader(uf)
next(reader)# 1行目読み飛ばし
next(ureader)# 1行目読み飛ばし
trainning_labels = []
trainning_data = []
unknown_labels = []
unknown_data = []

for row in reader:
	trainning_labels.append(row[len(row)-1])# label取得
	del row[len(row)-1]           # 元データからラベル削除
	trainning_data.append(row)              # ラベル以外を別のとこに保存

f.close()

for urow in ureader:
	unknown_labels.append(urow[len(urow)-1])# label取得
	del urow[len(urow)-1]           # 元データからラベル削除
	unknown_data.append(urow)              # ラベル以外を別のとこに保存

uf.close()


model = RandomForestClassifier(n_estimators=1000)
model.fit(trainning_data, trainning_labels)#識別機作成

output = model.predict(unknown_data)
print model.score(unknown_data, unknown_labels)#正解率出力


#以下ファイル作成
wf = open('importance_tfidf.txt', 'w')
text = map(str,model.feature_importances_)
wf.writelines(",".join(text));
wf.close()


#ランダムフォレストの使い方は↓のURLでみてください
#http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier.predict
#