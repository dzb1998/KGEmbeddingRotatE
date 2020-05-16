
with open('entities.dict', 'r') as fin, \
     open('entities1.dict', 'w') as fout:
    for line in fin.readlines():
        word = line.strip().split('\t')

        if word[0] == '3428':
            continue
        elif word[0] < '3428':
            fout.write(word[0] + '\t' + word[1] + '\n')
        else:
            fout.write(str(int(word[0])-1) + '\t' + word[1] + '\n')
