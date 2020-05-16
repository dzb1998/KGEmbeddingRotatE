import unicodedata

def read_triple(file_path, entity2id, relation2id):
    '''                                                                                                                                                                                    
    Read triples and map them into ids.                                                                                                                                                    
    '''
    triples = []
    with open(file_path) as fin:
        count = 0
        for line in fin:
            # print(line)                                                                                                                                                                  
            h, r, t = line.strip().split('\t')
            # print(h, r, t)                                                                                                                                                               
            h_ = unicodedata.normalize("NFKD", h).strip()
            r_ = unicodedata.normalize("NFKD", r).strip()
            t_ = unicodedata.normalize("NFKD", t).strip()
            triples.append((entity2id[h_], relation2id[r_], entity2id[t_]))
            # if h_ in entity2id and r_ in relation2id and t_ in entity2id:
            #     triples.append((entity2id[h_], relation2id[r_], entity2id[t_]))
            # else:
            #     print(h_, r_, t_)
            print(h_, r_, t_, triples[count])
            count += 1
    return triples



with open('entities.dict') as fin:
    entity2id = dict()
    for line in fin:
        eid, entity = line.strip().split('\t')
        entity2id[entity] = int(eid)

with open('relations.dict') as fin:
    relation2id = dict()
    for line in fin:
        rid, relation = line.strip().split('\t')
        relation2id[relation] = int(rid)

print('triple:', read_triple('train.txt', entity2id, relation2id))