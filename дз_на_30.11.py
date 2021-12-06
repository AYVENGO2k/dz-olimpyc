import copy

all_arr = []
arr = []
for i in range(50000):
    a = input()
    if a != '':
        all_arr.append(a)
    else:
        break

all_arr = set(all_arr)
all_arr = list(all_arr)

for i in range(0, len(all_arr)):
    arr.append(all_arr[i].split())

index = []
for i in range(len(arr)):
    index_arr = (f'{i+1}_{arr[i][0][0]}_{len(arr[i][1])},')
    index.append(index_arr)

#print(*arr)
print("Всего участников: ", len(all_arr))
print('Индексы: ', *index)

    
    

#алегрова мария 85
#алегрова мария 83
#подушко даниил 100
#никалаев максим 80
#морозов олег 70
#морозов олег 70
