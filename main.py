from gensim.models import word2vec
model = word2vec.Word2Vec.load("model/wiki00.model")

def wordSubtraction(words = ''):
    while(words != "*q"):
        words = input("Enter 3 words you want to analyze in form of 'w1 - w2 = ??? - w3'. Use space to split them.\n"
                      " Enter *q to exit.：\n")
        word = words.split()
        try:
            print("%s - %s = ??? - %s"%(word[0],word[2],word[1]))
            simwords = model.most_similar(positive=[word[0],word[1]], negative = [word[2]])#[札幌市] - [北海道] = ??? - [沖縄県]
            n = [w[0] for w in simwords]
            print("??? =", ",".join(n))
        except:
            print('One of your word is not in dictionary.\n')

def findSimilarWord(word = ''):
    while(word != "*q"):
        word = input("Enter a word you want to analyze. Enter *q to exit.：\n")
        try:
            simwords = model.most_similar(positive=[word])
            n = [w[0] for w in simwords]
            print(word, "=", ",".join(n))
        except:
            print('Your word is not in dictionary.\n')

def seeVector(word = ''):
    while(word != '*q'):
        word = input("Enter a word you want to see. Enter *q to exit.：\n")
        try:
            word_vec = model[word]
            print(word_vec)
        except:
            print('Your word is not in dictionary.\n')

if __name__ == '__main__':
    order = ''
    funcs = [wordSubtraction,findSimilarWord,seeVector]
    while(order != '*Q'):
        order = input("Enter 1 to invoke 'word substraction', enter 2 to invoke 'find similar word',"
                      " enter 3 to invoke 'see vector'.\n Enter *q to exit.：\n")
        order.split()
        try:
            funcs[int(order)-1]()
        except:
            print('There is something wrong with your command. Please try again.\n')
