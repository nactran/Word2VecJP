from gensim.models import word2vec
text_file = "/Users/kohira/Documents/Corpus/std_wiki_03.txt"

data = word2vec.LineSentence(text_file)
model = word2vec.Word2Vec(data, size=120, window=1, hs=1, min_count=1, sg=1,iter = 5)
model.save("../output/wiki03.model")
print("Generated\n")




