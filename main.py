from gensim.models import word2vec
model = word2vec.Word2Vec.load("model/wiki00.model")

def seeVector():
    word = ''
    while(word != "*q"):
        word = input("Enter a word you want to analyze：")
        word.strip()
        try:
            word_vec = model[word]
            print(word_vec)
        except:
            print("The word is not in dictionary!")
    return 0

def seeSimilar():
    word =''
    while(word != "*q"):
        word = input("Enter a word you want to analyze, enter *q to quit：")
        word.strip()
        try:
            simwords = model.most_similar(positive=[word])
            n = [w[0] for w in simwords]
            print(word, "=", ",".join(n))
        except:
            print("The word is not in dictionary!")
    return 0

def compareWords():
    words =''
    while(words != "*q"):
        words = input("Enter 2 words you want to compare. Use 'space' to split them.：")
        word = words.split()
        try:
            sim = model.similarity(word[0],word[1])
            print( "The similarity between %s and %s is: %f."%(word[0],word[1],sim))
        except:
            print("The word is not in dictionary!")
    return 0

if __name__ == '__main__':
    command = ''
    while(command != "**q"):
        print("Enter V to see the vector of the word. Enter S to see similar words of the word. ")
        print("Enter C to compare 2 words' similarity. Enter **q to quit.")
        command = input()
        if (command == 'V'): seeVector()
        elif (command == 'S'): seeSimilar()
        elif (command == 'C'): compareWords()
        else: print("Something wrong with your command")
