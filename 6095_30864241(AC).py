# 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때, n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.

d = []           # 리스트 생성 []
for i in range(20):  
    d.append([])       # 리스트 안에 다른 리스트 추가
    for j in range(20):
        d[i].append(0)   # 리스트 안에 들어있는  리스트 안에 0 추가해 넣기
        
        
n = int(input())
for i in range(n):
    x, y = input().split()
    d[int(x)][int(y)] = 1
    
for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()
