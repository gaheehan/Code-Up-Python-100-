'''
영문 소문자(a ~ z) 1개가 입력되었을 때,
a부터 그 문자까지의 알파벳을 순서대로 출력해보자.
'''

c = ord(input())  # ord(문자): 유니코드 정수 반환
t = ord('a')
while t<=c :
  print(chr(t), end=' ') # chr(숫자): 문자 반환
  t += 1
  
  

