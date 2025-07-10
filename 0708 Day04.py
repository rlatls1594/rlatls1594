# >> random, 랜덤 함수
# - 0.0 ~ 1.0 미만의 임의의 값 생성
# from random import random **********  <- 매우 매우 중요
# print(random())

# - 0.0 ~ 10.0 미만의 임의의 값 생성
# from random import random
# print(random() * 10)

# - 0 ~ 10 미만의 임의의 값 생성
# from random import random
# print(int(random() * 10))

# - 1 ~ 10 까지의 임의의 값 생성
# from random import random
# print(int(random() * 10) +1)

# - 1 ~ 45 까지 임의의 값 6개 출력
# from random import random
# for x in range(6) :
# 	print(int(random() * 45) +1)

# [예제.1]
# c:\Users\itbank\AppData\Local\Programs\Python\Python313\Lib\random.py random.py에 random 함수를 호출 (현재 작업중인 소스파일)
# from random import random 
# from random import randint
# print(random()) # 0.0 ~ 1.0 미만의 임의의 값이 생성
# print(randint(10,50))

# -> random 함수 사용 시 "random" 값을 아래 경로에서 호출
# -> 강의실 컴퓨터 기준  경로 ;
# c:\Users\itbank\AppData\Local\Programs\Python\Python313\Lib\random.py
# -> random 함수 등 위 경로에 있는 라이브러리들은 별 다른 설치 없이 사용 가능 하지만 파이썬을 설치 했다고 모든 라이브러리를 사용할 수 있는 것이 아님
# -> 사용할 프레임워크를 설치하고 라이브러리에 다운로드 되어있어야 함
    # def random(self):
    #     """Get the next random number in the range 0.0 <= X < 1.0."""
    #     return (int.from_bytes(_urandom(7)) >> 3) * RECIP_BPF
# 위 경로, ramdom.py 중 random 명령어 기능이 사용되는 것


# c:\Users\itbank\AppData\Local\Programs\Python\Python313\Lib\random.py 해당 경로에 있는 .py 모듈 전체를 호출
# import random 
# print(random.random()) # 0.0 ~ 1.0 미만의 임의의 값이 생성
# print(random.randint(10,50))

# -> *****모듈 전체를 불러올 때에는 .(dot, 닷) 을 찍고 어떤 기능을 사용하겠다라고 명시해줘야함*****
# -> 이런 프레임워크 기능을 활용해서 작업 능률을 끌어 올릴 수 있다
# -> 프레임워크는 이미 숙련자들이 만들어놓은 "작업대", 라이브러리에서 어떤 기능을 불러와서 사용하기만 하면 된다.
# -> import 로 불러와서 사용하면 된다.
# -> 요즘 사용하는 언어들은 대부분 이런 식. 
# -> django 장고를 잘 사용할줄 알면 WEB에서 Spring Boot를 비교적 쉽게 받아 들일 수 있다

# 랜덤 함수 위치 찾기 명령어
# import random
# print(random.__file__)
 

# > 문제
# 앞에서 학습한 내용을 바탕으로 다음 문제를 풀어보세요.
# 1. 1 ~ 100 까지 랜덤 값을 6개 출력하는 코드를 작성하시오.
# 2. 1 ~ 100 까지 랜덤 값을 반복하여 출력하되 50이 출력되는 순간 반복을 종료하는 코드를 작성하시오.
# 3. 1 ~15 까지 랜덤 값을 중복 없이 3개 생성하여 출력하는 코드를 작성하시오.

# -> 풀이 및 정답 코드
# 1. 1 ~ 100 까지 랜덤 값을 6개 출력하는 코드를 작성하시오.
# from random import random
# for x in range(6) :
#   print(int(random() * 100) +1)

# import random으로 random 함수 전체를 불러오기
# import random
# for _ in range(6):
#     value = random.randint(1, 100)
#     print(value)

# 2. 1 ~ 100 까지 랜덤 값을 반복하여 출력하되 50이 출력되는 순간 반복을 종료하는 코드를 작성하시오.
# from random import randint
# while True:
#     x = randint(1, 100)
#     print(x)
#     if x == 50:
#         break

# import random으로 random 함수 전체를 불러오기
# import random
# while True:
#     value = random.randint(1, 100)
#     print(value)
#     if value == 50:
#         print("50이 출력되어 반복을 종료합니다.")
#         break
# while 함수 사용해서 무한으로 값 뽑아내기
# random int 1 ~ 100 범위 중 
# if, 만약 x 가 50이라면 break 로 중단

# 3. 1 ~15 까지 랜덤 값을 중복 없이 3개 생성하여 출력하는 코드를 작성하시오.
# from random import sample
# print(sample(range(1, 16), 3))

# import random으로 random 함수 전체를 불러오기
# import random
# values = random.sample(range(1, 16), 3)
# print(values)
# 주어진 시퀀스에서 중복 없이 임의의 요소를 추출할 때 사용 = sample 함수
# range((1,16),3) 으로 1 ~ 15 범위에서 무작위 3개 추출

# 선생님 코드
# from random import randint
# while True:
#    a = randint(1,15)
#    b = randint(1,15)
#    c = randint(1,15)
#    if a != b and a != c and b != c:
#       print(a,b,c,)
#       break



# [ List ]
# - 데이터의 목록을 다루는 자료형
# - 리스트 안에는 어떠한 자료형이든지 넣어 사용 할 수 있다.
# - 리스트를 정의할 때에는 "[ ]" 를 사용한다.
# - 리스트 내부의 특정 데이터의 접근하기 위해서는 Index를 사용한다.
# - 사기 = 다 파이썬을 사용하는 이유

# - 기본 사용법
# 변수명 = [ ]
# 변수명 = [ value1, value2, ... ]

# [100, 1.123, "String"]
# -> 자료형을 하나의 저장공간에 짬뽕으로 다 사용할 수 있음
# -> 이런 이유 때문에 파이썬이 사기라고 불리는 이유


# > Indexing(인덱싱)
# - 리스트의 특정 값에 접근 하기 위한 방법
#    0     1     2     3     4
# [ 100 , 200 , 300 , 400 , 500 ]
# -> lst = [1]
# -> lst = [1, 2, 3]
# -> lst = [] 를 사용해서 원하는 값에 접근 할 수 있음

# [예제.2]
# lst = [1,2,3,4,5]
# print(lst, type(lst))
# print(lst[0]) # -> 1
# print(lst[2]) # -> 3
# print(lst[4]) # -> 5
# print(lst[9]) # -> 인덱스 범위에 없는 값이므로 에러 출력

# lst = [1,2,3,4,5,123.456,"ASD"]
# print(lst, type(lst))
# for val in lst:
#   print(val)
# 리스트의 길이 만큼 반복
# lst에 저장된 값을 val 변수에 넣으면서 반복

# lst[0] = 100
# print(lst[0])
# 저장된 값을 유연하게 교체도 가능하다


# 참고로 알아두면 좋은 팁
# 음수 형태로도 접근이 가능하다
# -7 -6 -5 -4 -3    -2      -1
# [1, 2, 3, 4, 5, 123.456, "ASD"]
# lst = [1,2,3,4,5,123.456,"ASD"]
# print(lst[-1])
# -1 Index를 사용해서 가장 최신, 가장 마지막에 저장된 데이터를 쉽게 불러올 수 있다


# Sclicing (슬라이싱)
# > Sclicing (슬라이싱)
# - 리스트의 특정 값들의 범위에 접근하기 위한 방법
# 0	  1	  2	  3	  4	   5	      6
# [ 1,  2,  3,  4,  5,  123.456,  "ASD"]
# lst = [1,2,3,4,5,123.456,"ASD"]
# print(lst[0:5])
# print(lst[:3])
# print(lst[5:])
# print(lst[-4:-1])
# 범위를 나타내는 용도
# 범위의 앞 쪽과 뒤 쪽을 생략할 수도 있다. = [:3] : 처음 부터 ~ 3 까지 / [5:] : 5 부터 ~ 마지막 까지
# 음수 값으로도 접근이 가능하다


# [ List 복사 ]
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
# lst1 =  1, 2, 3 이라는 값이 메모리 공간에 주소값으로 저장됨
# lst2 = lst1 에서 일반적인 대입 연산자 " = " 를 사용하게 되면 데이터가 아닌 주소값을 복사하는 것
# 그럼 메모리에서는 같은 공간, 같은 주소값에 lst1 과 lst2가 저장 되게 됨
# 결국 lst2 = lst1 같은 명령어가 의미가 없어짐
# 따라서 우리가 아는 복사는 "깊은 복사"를 의미 한다
# 깊은 복사를 할 경우 새로운 공간이 만들어지고, 새로운 공간에 같은 값이 저장되고, lst2라는 이름으로 저장됨

# 깊은 복사
# from copy import copy
# lst1 = [1,2,3]
# print(lst1,id(lst1))
# lst2 = copy(lst1)
# print(lst2,id(lst2))

# lst2[0] = 100
# print(lst2)
# print(lst1)
# 실행하면 주소값이 다르다 
# 또한 lst2[0] = 100 으로 대입했을 때, lst2는 대입된 값으로 바뀌어 출력되고 lst1은 정상적으로 출력된다.
# 따라서 copy 함수, copy module을 사용해서 원본은 유지한 채 새로 복사해서 사용 해야 한다.(깊은 복사)


# > 리스트 함수
# 함수				          설명
# append(value)		      리스트 끝에 값을 추가 한다.
# extend(iter)			    리스트 끝에 list, tuple, dict 의 값을 하나씩 추가 한다
# insert(idx value)		  특정 인덱스 위치에 값을 추가 한다
# pop([idx]) 			      마지막 인덱스의 값을 반환 후 삭제 한다 . 인덱스 번호를 지정 할 수도 있다
# remove(value)		      특정 값에 해당하는 것을 찾아 삭제 한다
# clear()			          모든 값을 삭제하여 빈 리스트만 남긴다
# count(value)		      리스트에서 일치하는 값의 수를 반환 한다
# index(value)		      리스트에서 일치하는 값의 인덱스 번호를 반환 한다
# reverse()			        리스트의 모든 값을 뒤집어 나열 한다
# sort([reverse=False])	리스트의 값을 오름차순(False), 내림차순(True) 정렬 한다.
# -> 리스트 자체가 제공하는 함수
# -> 외우고 있으면, 많이 알고 있으면 많이 도움되는 기능

# [예제.4]
# lst. 도트 연산자를 사용하게 되면 list object 가 만들어짐 
# object라는 객체를 메모리에 만들어 내고 리스트 함수라는 기능들을 담고 있다
# 따라서 기능을 사용할 수 있다
# append : 리스트 끝에 값을 추가 

# > 리스트 - append()
# - append 예제
# lst = [1, 2, 3]
# lst.append('a')
# lst.append([4, 'b'])

# lst = [1,2,3]
# lst[3] = 100
# lst.append()
# -> IndexError: list assigment index out of range 오류남

# lst = [1,2,3]
# print(lst)

# lst.append(4)
# print(lst)

# lst.append(['A','B','C'])
# print(lst)
# print(lst[4][1])
# ['A','B','C'] 중에서 'B' 만 가져오고 싶다면
# lst[4]로 Index 번호 4를 통해 하위 lst를 지정해주고
# 그 중 'B'를 가져오려면 다시 [1]로 Index 번호 1을 통해 'B'를 지정
# 2차원 구조 append


# [예제.5]
# extend : 확장(하나로 합쳐짐)
# > 리스트 - extend()
# - extend 예제
# lst = [1, 2, 3]
# lst.extent(['a', 'b', 'c'])
# lst = [1,2,3]
# print(lst)

# lst.extend([100,200,300])
# print(lst)


# [예제.6]
# insert : 특정 인덱스 위치에 값 추가. 앞 쪽에 반드시 인덱스 번호를 입력해줘야함.
# pop : 특정 인덱스 값을 빼내옴 = 추출
# remove : 특정 인덱스 값을 삭제
# clear : 초기화

# > 리스트 -insert()
# - insert 예제
# lst = [1, 2, 3]
# lst.insert(1, 'b')

# > 리스트 - pop()
# - pop 예제
# lst = [1, 2, 3]
# lst.pop()
# lst.pop(0)

# > 리스트 - remove()
# - remove 예제
# lst = [1, 2, 3]
# lst.remove(2)

# > 리스트 - clear()
# - clear 예제
# lst = [1, 2, 3]
# lst.clear()

# lst = [1,2,3]
# lst.insert(1,'A')
# print(lst)

# lst.pop()
# print(lst)

# lst.pop(1)
# print(lst)

# data = lst.pop(1)
# print(lst, data)

# data2 = lst.remove(3)
# print(lst, data2)

# lst.clear()
# print(lst)


# [예제.7]
# count : 내가 지정한 값이 몇 개 인지
# index : 내가 지정한 값의 index 값이 몇 번 인지
# reverse : 

# > 리스트 - count()
# - count 예제
# lst = [1, 2, 3, 1]
# lst.count(1)

# > 리스트 - index()
# - index 예제
# lst = [1, 2, 3, 1]
# lst.index(2)

# > 리스트 -reverse()
# - reverse 예제
# lst = [1, 3, 2]
# lst.reverse()

# lst = [1,2,3,'A','B','C','A']
# print(lst.count('A'))
# print(lst.index('A'))
# # 'A' 가 두 개 이므로 앞쪽 'A'만 출력됨
# print(lst.index('A',4))
# # 두 번째 'A' 의 Index 번호를 알고 싶으면 4 라고 시작점을 알려줘야함
# lst.reverse()
# print(lst)
# # -> [1,2,3,'A','B','C','A'] 를 뒤집어서 출력 -> ['A', 'C', 'B', 'A', 3, 2, 1]

# [예제.8]
# sort : 오름차순, 내림차순으로 정렬
# >리스트 - sort()
# - sort 예제
# lst = [1, 3, 2]
# lst.sort()
# lst.sort(reverse=True)

# lst = [78,12,43,57,89]
# lst.sort(reverse=False) # 오름차순 정렬 (기본값)
# print(lst)
# lst.sort         # <- (reverse=False)는 생략 가능
# print(lst)

# lst.sort(reverse=True) # 내림차순 정렬
# print(lst)


# > 문제
# 1, 2는 풀 줄 알아야한다. 3은 약간의 응용, 4는 어려움
# 앞에서 학습한 내용을 바탕으로 다음 문제를 풀어보세요.
# 1. numbers = [10, 20, 30, 40, 50, 60, 70]
# 	위 리스트의 모든 값을 더한 결과를 출력 하시오
# 2. 1 ~ 45 까지 임의의 값을 중복 없이 6 개 생성하여 출력하는 코드를 작성 하시오
# 3. lst_sec = 홍길동 ', 남 ', 36], [김수양 ', 여 ', 32], [박담소 ', 남 ', 28]]
# 	위의 2 차 리스트 자료를 다음과 같은 형식으로 출력 하시오
# 	이름 : 홍길동
# 	성별 : 남
# 	나이 : 36
# 4. 구구단을 출력하는 코드를 작성하되 , 2 차 리스트에 결과 값을 저장하고 출력 할 수 있도록 하시오

# 1. numbers = [10, 20, 30, 40, 50, 60, 70] 위 리스트의 모든 값을 더한 결과를 출력 하시오
# 쉬운 방법 1
# numbers = [10,20,30,40,50,60,70]
# total = sum(numbers)
# print(total)

# for 함수 사용
# total = 0
# for num in numbers:
#     total += num
# print(total)
# total = 0 으로 초기화

# 2. 1 ~ 45 까지 임의의 값을 중복 없이 6 개 생성하여 출력하는 코드를 작성 하시오
# sample 함수 사용
# from random import sample
# print(sample(range(1,46),6))

# 선생님 방법
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

# 3. lst_sec = [[홍길동 ', 남 ', 36], [김수양 ', 여 ', 32], [박담소 ', 남 ', 28]]
# 	위의 2 차 리스트 자료를 다음과 같은 형식으로 출력 하시오
# 	이름 : 홍길동
# 	성별 : 남
# 	나이 : 36

# lst_sec = [["홍길동", "남", 36],["김수양", "여", 32],["박담소", "남", 28]]

# for who in lst_sec:
#     name, gender, age = who
#     print("이름 :", name)
#     print("성별 :", gender)
#     print("나이 :", age)
#     print()

# 선생님 방법
# lst_sec = [['홍길동', '남', 36], 
# ['김수양', '여', 32], 
# ['박담소', '남', 28]]

# for value in lst_sec:
#   print('이름 : {}'.format(value[0]))
#   print('성별 : {}'.format(value[1]))
#   print('나이 : {}'.format(value[2]))
#   print(value,'\n')
# lst_sec 는 2차원 리스트


# 매우 어렵다. 
# 4. 구구단을 출력하는 코드를 작성하되 , 2 차 리스트에 결과 값을 저장하고 출력 할 수 있도록 하시오
# 구구단 데이터 생성
# times_table = []
# for Xtimes_table in range(2, 10):
#     multiplication_result = []
#     for i in range(1, 10):
#         multiplication_result.append(Xtimes_table * i)
#     times_table.append(multiplication_result)

# 저장된 결과 출력
# for index, multiplication_result in enumerate(times_table, start=2):
#     print(f"{index}단:", multiplication_result)

# times_table = []
# – 구구단 전체 결과를 담을 빈 리스트(일차원)를 하나 생성
# – 이후 각 단 별 결과(이차원 리스트)를 일차원 리스트에 차례로 추가할 예정

# 2단 for문 사용
# - 바깥쪽 for Xtimes_table in range(2, 10):
# - Xtimes_table이 2부터 9까지 변하며 2단 부터 9단 까지 처리
# - 안쪽 multiplication_result = []
# - 각 단의 곱셈 결과를 담을 빈 리스트(이차원 행)를 만듦
# - 가장 안쪽 for i in range(1, 10):
# - i가 1부터 9까지 변해가며 곱셈 값을 계산
# - multiplication_result.append(Xtimes_table * i)로, append를 사용해서 2단일 땐 2×1, 2×2, …, 2×9 값을 순서대로 추가
# - times_table.append(multiplication_result)
# - 완성된 한 행(row)을 전체 리스트에 추가합니다.
# - 이렇게 하면 최종적으로 8개의 행(2단~9단)이 들어 있는 2차원 리스트가 만들어집니다.

# enumerate 로 결과 출력
# - for index, multiplication_result in enumerate(times_table, start=2):
# - times_table의 첫 번째 단은 2단, 두 번째 단은 3단이기 때문에 start=2로 지정하면 index가 2부터 시작해 실제 단수와 일치
# - print(f"{index}단:", multiplication_result)
# - index값(단수)과 그 단의 곱셈 결과 리스트를 함께 print 로 출력

# + 리스트 컴프리헨션으로 더 간결하게 구현할 수도 있다
# times_table = [[dan * i for i in range(1, 10)] for dan in range(2, 10)]

# 선생님 방법
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
# 위에서 저장한 List 출력

# gugu라는 비어있는 List 하나 생성
# x 의 값은 2부터 9까지 변경되며 동작
# 비어있는 gugu 리스트에 append 추가 하겠다 [] 다시 비어있는 리스트를
# y 의 값도 1부터 9까지 변경되며 동작
# gugu[x-1] 는 인덱스 번호를 지정하기위해 -1 붙여줌
# x = 2 일 경우 1번 인덱스에 append 추가한다 2부터 9까지
# 9단 끝날 때까지 계속 반복















