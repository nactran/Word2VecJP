# 類似する語句を表示 - 2
from gensim.models import word2vec
model = word2vec.Word2Vec.load("/Users/kohira/documents/output/wiki03.model")
word =""
while(word != "*q"):
    word = input("Enter a word you want to analyze：")
    simwords = model.most_similar(positive=[word])
    n = [w[0] for w in simwords]
    print(word, "=", ",".join(n))


