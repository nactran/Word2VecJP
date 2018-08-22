from gensim.models import word2vec
model = word2vec.Word2Vec.load("nucc.model")

word = input("Enter a word you want to analyze：")
if word in model.wv.vocab:
    word_vec = model[word]
print(word_vec)
