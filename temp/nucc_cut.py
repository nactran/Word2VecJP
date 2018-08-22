# encoding: utf-8
import sys
from janome import tokenizer
import re

CorpusDir = "/Users/kohira/Documents/nucc/" #名大会話集を利用

results = []

for i in range (1,100): #トレイニング・セット　１−９９
    if(i < 10):
        filename = "data00" + str(i) + ".txt"
    else:
        filename = "data0" +str(i) + ".txt"

    print ("Processing file: "+ filename)
    text_file1 = open(CorpusDir + filename)
    bindata = text_file1.read()
    text = bindata
    t = tokenizer.Tokenizer()
    lines = text.split("\r\n")
    for line in lines:
        s = line
        s = re.sub(r"＠.*", "", s)
        s = re.sub(r"＊.*", "", s)
        s = re.sub(r"＜.*＞", "", s)
        s = re.sub(r"（.*）", "", s)
        s = re.sub(r".*：", "", s)
        s = re.sub(r"[、。？！]", "", s)
        s = s.strip()

        tokens = t.tokenize(s)
        r = []

        for tok in tokens:
            if tok.base_form == "*":
                w = tok.surface
            else:
                w = tok.base_form
            r.append(w)
            #ps = tok.part_of_speech
            #hinsi = ps.split(",")[0]
            #if hinsi in ["名詞", "形容詞", "動詞", "記号"]:
                #r.append(w)
        rl = (" ".join(r)).strip()
        results.append(rl)

text_file = "../output/nucc1_99.txt"
with open(text_file, "w") as fp:
    fp.write("\n".join(results))

