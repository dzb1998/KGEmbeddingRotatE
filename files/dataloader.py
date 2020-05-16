import csv 
import pandas as pd

allrow = []
alldate = []
allrowdate = []
row_1 = []
row_2 = []
row_3 = []
row_pred = []


# first 10
with open('output.csv') as fin, \
     open('test.txt') as testfin:
    for row in csv.reader(fin, delimiter=','):
        temp = []
        row_4_ = row[4].strip('][').split(', ')
        row_4 = [i.strip('\'') for i in row_4_]
        temp.append(row[0])
        temp.append(row[1])
        temp.append(row[2])
        temp.append(row[3])
        temp.append(row_4)
        allrow.append(temp)
        row_1.append(row[1])
        row_2.append(row[2])
        row_3.append(row[3])
        row_pred.append(row_4)

    for line in testfin.readlines():
        word = line.strip().split('\t')
        alldate.append(word[3])


    # since test duplicated
    alldate.extend(alldate[:])

    # print(len(row_1[1:]), len(row_2), len(row_3), len(alldate), len(row_pred))
    # print(row_1[1:])
    # print(alldate)

    output_dict1 = {'e1': row_1[1:8964], 'relation': row_2[1:8964], 'e2':row_3[1:8964], 'date':alldate[:8963], 'predictions': row_pred[1:8964]}
    df = pd.DataFrame(data=output_dict1)
    df.to_csv('head1.csv')
    output_dict2 = {'e1': row_1[8964:], 'relation': row_2[8964:], 'e2':row_3[8964:], 'date':alldate[8963:], 'predictions': row_pred[8964:]}
    df = pd.DataFrame(data=output_dict2)
    df.to_csv('tail1.csv')




row_1 = []
row_2 = []
row_3 = []
row_date = []
row_pred = []

with open('head1.csv') as fin:
    for row in csv.reader(fin, delimiter=','):
        # print(row)
        temp = row[5].strip('][').split(', ')
        row_5 = [i.strip('\'') for i in temp]
        if row[1] in row_5[:3]:
            row_1.append(row[1])
            row_2.append(row[2])
            row_3.append(row[3])
            row_date.append(row[4])
            row_pred.append(row_5)
    print(len(row_1), len(row_2), len(row_3), len(row_date), len(row_pred))

    output_dict = {'e1': row_1, 'relation': row_2, 'e2':row_3, 'date':row_date, 'predictions': row_pred}
    df = pd.DataFrame(data=output_dict)
    df.to_csv('output21.csv')


row_1 = []
row_2 = []
row_3 = []
row_date = []
row_pred = []

with open('head1.csv') as fin:
    for row in csv.reader(fin, delimiter=','):
        # print(row)
        temp = row[5].strip('][').split(', ')
        row_5 = [i.strip('\'') for i in temp]
        if row[1] in row_5[3:]:
            row_1.append(row[1])
            row_2.append(row[2])
            row_3.append(row[3])
            row_date.append(row[4])
            row_pred.append(row_5)
    print(len(row_1), len(row_2), len(row_3), len(row_date), len(row_pred))

    output_dict = {'e1': row_1, 'relation': row_2, 'e2':row_3, 'date':row_date, 'predictions': row_pred}
    df = pd.DataFrame(data=output_dict)
    df.to_csv('output31.csv')

row_1 = []
row_2 = []
row_3 = []
row_date = []
row_pred = []

with open('head1.csv') as fin:
    for row in csv.reader(fin, delimiter=','):
        # print(row)
        temp = row[5].strip('][').split(', ')
        row_5 = [i.strip('\'') for i in temp]
        if row[1] not in row_5:
            row_1.append(row[1])
            row_2.append(row[2])
            row_3.append(row[3])
            row_date.append(row[4])
            row_pred.append(row_5)
    # first row redundant        
    print(len(row_1[1:]), len(row_2[1:]), len(row_3[1:]), len(row_date[1:]), len(row_pred[1:]))

    output_dict = {'e1': row_1[1:], 'relation': row_2[1:], 'e2':row_3[1:], 'date':row_date[1:], 'predictions': row_pred[1:]}
    df = pd.DataFrame(data=output_dict)
    df.to_csv('output41.csv')


