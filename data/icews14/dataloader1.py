import unicodedata


with open('orig/train.txt') as fin, \
     open('train1.txt', 'w') as fout:
    for line in fin.readlines():
        word = line.split('\t')
#        print(word)                                                                                                                                                  
#        fout.write(unicodedata.normalize("NFKD", word[0]) + '\t' + unicodedata.normalize("NFKD", word[1]) + '\t' + unicodedata.normalize("NFKD", word[2]) + '\n')
        fout.write(word[0] + '\t' + word[1] + '\t' + word[2] + '\n')
