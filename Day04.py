# [예제.1]
# from random import random # ---> random 함수를 호출 (현재 작업중인 소스파일)
# from random import randint
# print(random()) # 0.0 ~ 1.0 미만의 임의의 값이 생성
# print(randint(10,50))

# import random
# print(random.random()) # 0.0 ~ 1.0 미만의 임의의 값이 생성
# print(random.randint(10,50))

# [문제]
# from random import randint
# for i in range(6):
#   print(randint(1,100))

# from random import randint
# while True:
#   rand = randint(1,100)
#   print(rand)
#   if rand == 50:
#     break

# from random import randint
# while True:
#   a = randint(1,15)
#   b = randint(1,15)
#   c = randint(1,15)
#   if a != b and a != c and b != c:
#     print(a,b,c)
#     break

# [ List ] 
# - 데이터의 목록을 다루는 자료형 
# - 리스트 안에는 어떠한 자료형이든지 넣어 사용 할 수 있다.
# - 리스트를 정의할때에는 "[]"를 사용한다.
# - 리스트 내부의 특정 데이터에 접근하기 위해서는 Index를 사용한다.

# [예제.2]
# lst = [1,2,3,4,5,123.456,"ASD"]
# print(lst, type(lst))
# for val in lst:
#   print(val)
# lst[0] = 100
# print(lst[0])
# print(lst[-1])
# print(lst[0:5])
# print(lst[:3])
# print(lst[5:])

# [List 복사]
# - 얇은 복사 : 원본 List의 주소값을 복사
# - 깊은 복사 : 원본 List의 데이터를 복사

# [예제.3]
# 얇은 복사
# lst1 = [1,2,3]
# print(lst1,id(lst1))
# lst2 = lst1
# print(lst2,id(lst2))

# lst2[0] = 100
# print(lst2)
# print(lst1)

# 깊은 복사
# from copy import copy
# lst1 = [1,2,3]
# print(lst1,id(lst1))
# lst2 = copy(lst1)
# print(lst2,id(lst2))

# lst2[0] = 100
# print(lst2)
# print(lst1)


# [예제.4]
# lst = [1,2,3]
# print(lst)

# lst.append(4)
# print(lst)

# lst.append(['A','B','C'])
# print(lst)
# print(lst[4][1])

# [예제.5]
# lst = [1,2,3]
# print(lst)

# lst.extend([100,200,300])
# print(lst)

# [예제.6]
# lst = [1,2,3]
# lst.insert(1,'A')
# print(lst)

# data = lst.pop(1)
# print(lst, data)

# data2 = lst.remove(3)
# print(lst, data2)

# lst.clear()
# print(lst)

# [예제.7]
# lst = [1,2,3,'A','B','C','A']
# print(lst.count('A'))
# print(lst.index('A'))
# print(lst.index('A',4))
# lst.reverse()
# print(lst)

# [예제.8]
# lst = [78,12,43,57,89]
# lst.sort(reverse=False) # 오름차순 정렬 ( 기본값 )
# print(lst)
# lst.sort(reverse=True) # 내림차순 정렬
# print(lst)

#[문제.1]
# numbers = [10,20,30,40,50,60,70]
# Sum = 0
# for value in numbers:
#   Sum+= value
# print(Sum)

# [문제.2]
# from random import randint
# numbers=[]
# cnt=0
# while True:
#   rand=randint(1,45)
#   if rand not in numbers:
#     numbers.append(rand)
#     cnt+=1
#     if cnt==6:
#       break
# print(numbers)

#[문제.3] 
# lst_sec = [['홍길동', '남', 36],
#           ['김수양', '여', 32],
#           ['박담소', '남', 28]]

# for value in lst_sec:
#   print('이름 : {}'.format(value[0]))
#   print('성별 : {}'.format(value[1]))
#   print('나이 : {}'.format(value[2]))
#   print(value,'\n')

# [문제.4]
# - 기존 gugu List에 추가로 9개의 List를 생성 하여 곱셈 결과를 저장
# - [[1단],[2단],[3단],[4단],[5단],[6단],[7단],[8단],[9단]]
# gugu = []
# for x in range(2,10):
#   gugu.append([]) 
#   for y in range(1,10):
#     gugu[x-2].append(x*y)
# for x in range(2, 10):
#   for y in range(1, 10):
#     print('{} X {} = {}'.format(x, y, gugu[x-2][y-1]))
# print(gugu)
# 위에서 저장 한 List를 출력


