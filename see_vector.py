from gensim.models import word2vec
model = word2vec.Word2Vec.load("model/wiki00.model")
word = ''
while(word != "*q"):
    word = input("Enter a word you want to analyze：")
    try:
        word_vec = model[word]
        print(word_vec)
    except:
        print("The word is not in dictionary!")
