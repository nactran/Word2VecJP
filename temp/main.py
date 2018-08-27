# encoding: utf-8
import sys
from janome import tokenizer
import re
from gensim.models import word2vec
import numpy as np

ModelDir = "Jawiki.model"
InputDir = "/Users/kohira/documents//conversation.txt"#Use Ja_Wiki (part, size: 1G)
OutputDir = "data/conversation_segment.txt"
def word_segment():
    results = []
    # 打开语料文本
    text_file1 = open(InputDir)
    outputFile_Segment = open(OutputDir,'w', encoding='utf-8')

    # 读取语料文本中的每一行文
    bindata = text_file1.read()
    text = bindata
    t = tokenizer.Tokenizer()
    lines = text.split("\r\n")
    for line in lines:
            tokens = t.tokenize(line)
            r = []

            for tok in tokens:
                if tok.base_form == "*":
                    w = tok.surface
                else:
                    w = tok.base_form
                r.append(w)
            rl = (" ".join(r)).strip()
            results.append(rl)
            #print(segments)
            # 将分词后的语句，写进文件中
            outputFile_Segment.write("\n".join(results))

    text_file1.close()
    outputFile_Segment.close()

def XY():

    # 读取分词后的对话文本
    f = open(OutputDir, 'r', encoding='utf-8')
    subtitles = f.read()

    X = []
    Y = []

    # 将对话文本按段落切分
    subtitles_list = subtitles.split('E')

    # 将“问句”放入X中，将“答句”放入Y中
    for q_a in subtitles_list:
        # 检验段落中，是否含有"问-答"句；如果有，则分别追加到 X 和 Y 中
        if re.findall('.*M.*M.*', q_a, flags=re.DOTALL):
            q_a = q_a.strip()
            q_a_pair = q_a.split('M')

            X.append(q_a_pair[1].strip())
            Y.append(q_a_pair[2].strip())

    f.close()
    return X, Y

def XY_vector(X, Y):

    # 导入训练好的词向量
    model = word2vec.Word2Vec.load(ModelDir)

    # 将X-Y转换为词向量X_vector、Y_vector
    X_vector = []
    for x_sentence in X:
        x_word = x_sentence.split(' ')

        x_sentvec = [model[w] for w in x_word if w in model.wv.vocab]
        X_vector.append(x_sentvec)

    Y_vector = []
    for y_sentence in Y:
        y_word = y_sentence.split(' ')
        y_sentvec = [model[w] for w in y_word if w in model.wv.vocab]
        Y_vector.append(y_sentvec)

    # 计算词向量的维数
    word_dim = len(X_vector[0][0])

    # 设置结束词
    sentend = np.ones((word_dim,), dtype= np.float32)

    # 将问-答句的长度统一
    for sentvec in X_vector:
        if len(sentvec) > 14:
            # 将第14个词之后的全部内容删除，并将第15个词换为sentend
            sentvec[14:] = []
            sentvec.append(sentend)
        else:
            # 将不足15个词的句子，用sentend补足
            for i in range(15 - len(sentvec)):
                sentvec.append(sentend)

    for sentvec in Y_vector:
        if len(sentvec) > 15:
            sentvec[14:] = []
            sentvec.append(sentend)
        else:
            for i in range(15 - len(sentvec)):
                sentvec.append(sentend)

    return X_vector, Y_vector

if __name__ == '__main__':
    word_segment()
    X, Y = XY()
    X_vector, Y_vector = XY_vector(X, Y)

    print('第一条问句的词向量：')
    print(X_vector[0])

    print('第一条答句的词向量：')
    print(Y_vector[0])
