with open('data.txt', 'r') as document:
    answer = {}
    for line in document:
        pom1=line.replace('\n', '')
        pom2=pom1.split(';')
        answer[int(pom2[0])] = pom2[1:]
#print (answer)

for id in answer:

    answer[id][4]= answer[id][4].split(',')
    for friend in range(len(answer[id][4])):
        answer[id][4][friend]=int(answer[id][4][friend])

    if answer[id][2]=='':
        continue
    else:
        answer[id][2]=int(answer[id][2])
#print (answer)

def is_friend(id1,id2):
    for friend in answer[id1][4]:
        if friend==id2:
            return True
            break
    else:
        return False

#print (is_friend(1,4))
    
#najpodesnija struktura za cuvanje friendova svih friend-ova je skup - set(), zbog operacija koj je moguće nad set-ovima vršiti, ali ja sam radio sa list-ama jer imam više rada sa njima

def shortest_way(id1, id2, put=[]):
    put = put + [id1]
    if id1 == id2:
        return put
    najkraci = None
    for friend in answer[id1][4]:
        if friend not in put:
            nov_put = shortest_way(friend, id2, put)
            if nov_put:
                if not najkraci or len(nov_put) < len(najkraci):
                    najkraci = nov_put
    return najkraci
    
print (shortest_way(10,15))