from gensim.models import word2vec
text_file = "../output/nucc1_99.txt"

data = word2vec.LineSentence(text_file)
model = word2vec.Word2Vec(data, size=100, window=1, hs=1, min_count=1, sg=1)
model.save("../output/nucc.model")
print("Generated\n")


