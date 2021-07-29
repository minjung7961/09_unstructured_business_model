# *********************** 데이터 입력 받기 ***********************
import sys

N = int(sys.stdin.readline())
humans = []

for i in range(N):
    weight, tall = map(int,sys.stdin.readline().split())
    humans.append([weight, tall, 0])
    
# *********************** humans 등수 초기화 *******************
rank = [0]


for i in range(1,N):
    weight = humans[i][0]
    tall = humans[i][1]
    # print(f'\thuman{i+1} weight :{weight}, tall :{tall}')    
    for j in range(i):
        compare_weight = humans[j][0]
        compare_tall = humans[j][1]
        # print(f'\t\tcompare_human{j+1} compare_weight :{compare_weight}, compare_tall :{compare_tall}')
        if (weight > compare_weight) & (tall > compare_tall):
            # print('\t\t\t(weight > compare_weight) & (tall > compare_tall)',(weight > compare_weight) & (tall > compare_tall))
            humans[i][2] = humans[j][2] - 1
        elif (weight < compare_weight) & (tall < compare_tall):
            # print('\t\t\t(weight < compare_weight) & (tall < compare_tall)',(weight < compare_weight) & (tall < compare_tall))
            humans[i][2] = humans[j][2] + 1
        else:
            # print('\t\t\telse :')
            humans[i][2] = humans[j][2]
    # print('\tupdate rank : ',rank)
    rank.append(humans[i][2])
    
# *********************** 상대등수 범위 양수로 변환 ********************

scale = 1 - min(rank)

for i in range(N):
    humans[i][2] += 2
    
# *********************** 중복되는 등수 처리 ***********************

duplicate_number = {}

for i in range(1,N+1):
    duplicate_number[i] = 0

for i in range(N):    
    if rank[i] in rank:
        duplicate_number[humans[i][2]] += 1
        
    if duplicate_number[i] > 1:
        # print('\tduplicate_number[i] > 1 :',duplicate_number[i] > 1)
        duep_num = duplicate_number[i]
        # print('\tduep_num :',duep_num)
        
        for j in range(N,i,-1):
            
            # print('\t\tN :',N)
            # print('\t\tj :',j)
            # print('\t\tj+duep_num-1 :',j+duep_num-1)
            # print('\t\tN < j+duep_num-1 :',N < j+duep_num-1)
            
            if N < j+duep_num-1:               
                continue
            
            # print(f'\t\t    duplicate_number[{j}] :{duplicate_number[j]}')
            temp_dump = duplicate_number[j]
            duplicate_number[j+duep_num-1] = temp_dump
            duplicate_number[j] = 0
            
            for k in range(N):
                if humans[k][2] == j:
                    humans[k][2] = j+duep_num-1
               #  print(f'\t\t\t humans[{k}][2]',humans[k][2])
            # print('\t\t duplicate_number : ',duplicate_number)

# *********************** 결과 출력 ********************
for i in range(N):
    print(humans[i][2],end=' ')
            