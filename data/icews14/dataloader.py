import unicodedata

entities = {}
relations = {}
counten = 0
countre = 0


with open('train.txt') as fin, \
     open('entities.dict', 'w') as fout1, \
     open('relations.dict', 'w') as fout2:
    for line in fin.readlines():
        word = line.strip().split('\t')
        print(word)                                                                                                                                                  
        if word[0] not in entities.values():
            entities[counten] = unicodedata.normalize("NFKD", word[0])
            fout1.write(str(counten) + '\t' + word[0] + '\n')
            counten += 1
        if word[2] not in entities.values():
            entities[counten] = unicodedata.normalize("NFKD", word[2])
            fout1.write(str(counten) + '\t' + word[2] + '\n')
            counten += 1
        if word[1] not in relations.values():
            relations[countre] = unicodedata.normalize("NFKD", word[1])
            fout2.write(str(countre) + '\t' + word[1] + '\n')
            countre += 1
