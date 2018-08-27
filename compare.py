# 類似する語句を表示 - 2
from gensim.models import word2vec
model = word2vec.Word2Vec.load("/Users/kohira/documents/output/wiki03.model")

words = input("Enter 2 words you want to compare. Use 'space' to split them.：")
word = words.split()
sim = model.similarity(word[0],word[1])
print( "The similarity between %s and %s is: %f."%(word[0],word[1],sim))
