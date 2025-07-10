# [for 반복문]
# - 주어진 반복 횟수에 따라 for의 종속문장을 반복 실행한다.
# - 변수를 정의하고, 범위를 설정하여 반복횟수를 결정
# - Range 함수 : range(시작값, 종료값, 증감값) 형식으로 사용
# - 시작값, 증감값은 생략이 가능 

# [예제.1]
# for i in range(0,10,1):
#   print("For문 출력")

# for i in range(10,0,-1):
#   print("for문 출력")

# for i in range(5,10):
#   print(i)

# for i in range(10): # 제일 많이쓰는 형식
#   print(i, end="★ " * i)
#   print()

# var = int(input("반복횟수 입력: "))
# for i in range(var):
#   print(i+1,"번 반복")

# for ch in "String":
#   print(ch)

# lst = [1,2,3,4,5]
# for i in lst:
#   print(i)

# [ Quiz ]
# 1. 1 ~ 10 까지 합을 구하세요. 단, 반복 문을 이용하세요.

# sum = 0
# for i in range (1,11,1):
# 	sum += i
# print("1부터 10까지의 합은 {}입니다.".format(sum))


# 2. For문과 IF문을 이용하여 아래와 같이 출력.
# - 힌트 : 5번 출력하고 줄 바꿈이 이루어져야 하므로, 5의 배수마다 줄 바꿈 처리하도록 조건을 설정한다.
#  1    2       3       4       5
#  6    7       8       9      10
# 11   12      13      14      15
# 16   17      18      19      20
# 21   22      23      24      25
# 26   27      28      29      30

# for i in range (1,31,1):
# 	print("{}\t".format(i),end='')
# 	if i % 5 == 0:
# 	  print()


# 3. 변수 st = 'It is a fun Python class' 다음 문자열 중에서 
# 알파벳 'a'의 개수와 's'의 개수를 구하시오.

# st = "It is a fun Python class"
# a = s = 0
# for i in st:
# 	if i == 'a':
# 		a+=1
# 	elif i == 's':
# 		s+=1
# print("a의 개수: {} , s의 개수: {}".format(a,s))


# 4. 수를 입력 받아 1 ~ 입력 받은 수 까지 짝수의 합과 홀수의 합을 출력 하시오.

# num1 = int(input("종료 값 입력:"))
# evensum,oddsum = 0,0
# for i in range (1, num1+1, 1):
# 	if i % 2 == 0:
# 		evensum+=i
# 	else:
# 		oddsum+=i
# print("1에서 {} 까지 짝수의 합 : {}".format(num1,evensum))
# print("1에서 {} 까지 홀수의 합 : {}".format(num1,oddsum))


# 5. 시작 값, 끝 값, 증가값(1) 입력받아 시작과 끝값 사이의 7의 배수를 출력 하시오.

# s = int(input("시작값:"))
# e = int(input("종료값:"))
# g = int(input("증가값:"))
# for i in range(s,e,g):
# 	if i % 7 == 0:
# 		print(i,end='')


# 6. 1 ~ 100 사이의 값 중 3의 배수 이며, 5의 배수에 해당하는 합을 구하시오.

# sum=0
# for i in range(1,100,1):
# 	if i % 3 == 0 and i % 5 == 0:
# 		sum+=i
# print(sum)


# 7. 두 수를 입력 받아 입력 받은 두 수의 범위 안의 합을 구하시오.

# su1 = int(input("start:"))
# su2 = int(input("end:"))
# sum = 0
# for i in range(su1,su2+1):
# 	sum+=i
# print(sum)


# 8. 첫날에 10원을 예금하고, 다음날에는 전날의 2배를 예금하는 방식으로
# 한달(30일) 동안 저축한 금액을 구하시오.
# (첫날 10, 둘째날 20 , 셋째날 40 . . . 무조건 2배씩 증가되는 값이다)

# won = 10
# Sum = 0
# for day in range(1,31):
# 	Sum += won
# 	won *= 2
# print(Sum)

# [예제.2]
# for x in range(1,4,1):
#   for y in range(1,6,1):
#     print("X:{} / Y:{}".format(x,y))
#   print("")

# [ Quiz 1 ] : 중첩 For문을 이용하여 아래 구구단 표를 작성하세요.
# 2 X 1 = 2       2 X 2 = 4       2 X 3 = 6       2 X 4 = 8       2 X 5 = 10      2 X 6 = 12      2 X 7 = 14      2 X 8 = 16      2 X 9 = 18
# 3 X 1 = 3       3 X 2 = 6       3 X 3 = 9       3 X 4 = 12      3 X 5 = 15      3 X 6 = 18      3 X 7 = 21      3 X 8 = 24      3 X 9 = 27
# 4 X 1 = 4       4 X 2 = 8       4 X 3 = 12      4 X 4 = 16      4 X 5 = 20      4 X 6 = 24      4 X 7 = 28      4 X 8 = 32      4 X 9 = 36
# 5 X 1 = 5       5 X 2 = 10      5 X 3 = 15      5 X 4 = 20      5 X 5 = 25      5 X 6 = 30      5 X 7 = 35      5 X 8 = 40      5 X 9 = 45
# 6 X 1 = 6       6 X 2 = 12      6 X 3 = 18      6 X 4 = 24      6 X 5 = 30      6 X 6 = 36      6 X 7 = 42      6 X 8 = 48      6 X 9 = 54
# 7 X 1 = 7       7 X 2 = 14      7 X 3 = 21      7 X 4 = 28      7 X 5 = 35      7 X 6 = 42      7 X 7 = 49      7 X 8 = 56      7 X 9 = 63
# 8 X 1 = 8       8 X 2 = 16      8 X 3 = 24      8 X 4 = 32      8 X 5 = 40      8 X 6 = 48      8 X 7 = 56      8 X 8 = 64      8 X 9 = 72
# 9 X 1 = 9       9 X 2 = 18      9 X 3 = 27      9 X 4 = 36      9 X 5 = 45      9 X 6 = 54      9 X 7 = 63      9 X 8 = 72      9 X 9 = 81

# [ Quiz 2 ] : 중첩 For문을 이용하여 아래 구구단 표를 작성하세요.
# 2 X 1 = 2       3 X 1 = 3       4 X 1 = 4       5 X 1 = 5       6 X 1 = 6       7 X 1 = 7       8 X 1 = 8       9 X 1 = 9
# 2 X 2 = 4       3 X 2 = 6       4 X 2 = 8       5 X 2 = 10      6 X 2 = 12      7 X 2 = 14      8 X 2 = 16      9 X 2 = 18
# 2 X 3 = 6       3 X 3 = 9       4 X 3 = 12      5 X 3 = 15      6 X 3 = 18      7 X 3 = 21      8 X 3 = 24      9 X 3 = 27
# 2 X 4 = 8       3 X 4 = 12      4 X 4 = 16      5 X 4 = 20      6 X 4 = 24      7 X 4 = 28      8 X 4 = 32      9 X 4 = 36
# 2 X 5 = 10      3 X 5 = 15      4 X 5 = 20      5 X 5 = 25      6 X 5 = 30      7 X 5 = 35      8 X 5 = 40      9 X 5 = 45
# 2 X 6 = 12      3 X 6 = 18      4 X 6 = 24      5 X 6 = 30      6 X 6 = 36      7 X 6 = 42      8 X 6 = 48      9 X 6 = 54
# 2 X 7 = 14      3 X 7 = 21      4 X 7 = 28      5 X 7 = 35      6 X 7 = 42      7 X 7 = 49      8 X 7 = 56      9 X 7 = 63
# 2 X 8 = 16      3 X 8 = 24      4 X 8 = 32      5 X 8 = 40      6 X 8 = 48      7 X 8 = 56      8 X 8 = 64      9 X 8 = 72
# 2 X 9 = 18      3 X 9 = 27      4 X 9 = 36      5 X 9 = 45      6 X 9 = 54      7 X 9 = 63      8 X 9 = 72      9 X 9 = 81

# [가로출력]
# for i in range(2,10,1):
#   for x in range(1,10,1):
#     print("{} X {} = {}\t".format(i,x,i*x), end='')
#   print()
# print("\n\n")

# [세로출력]
# for i in range(1,10,1):
  # for x in range(2,10,1):
  #   print("{} X {} = {}\t".format(x,i,i*x), end='')
  # print()

# [while 반복문]
# - 조건식이 참인 동안 종속코드를 반복 실행한다.
# - 주로 반복횟수가 명확하게 정해지지 않는 경우 사용.

# [예제.3]
# i = 1
# odd = even = 0
# while i <= 10:
#   if i % 2 == 0:
#     even += i
#   else:
#     odd += i
#   i+=1
# print("1~10 짝수의 합: ", even)
# print("1~10 홀수의 합: ", odd)

# while True: # ->> 이런 표현도 가능 while 1:  
#   data = int(input("10보다 작은 정수 입력: "))
#   if data < 10:
#     print("10보다 작은값 입력")
#     break
#   else:
#     print("다시 입력하세요!")
#     continue
# print("반복 종료")

# i = 1
# while i<5:
#   print(i)
#   i+=1
# else:
#   print("while 조건식이 거짓일 경우 실행")

# [ 제어문 종합 Quiz ]
# [ Quiz .1 ] 
# 쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있다. 
# 쥐 한 마리가 하루에 20g씩의 쌀을 먹고, 10일 (10,20,30) 마다 쥐의 수가 2배씩 증가한다. 
# 며칠 만에 창고의 쌀이 모두 쥐의 먹이가 될까. 그리고 쥐는 총 몇 마리 인가? 
# ( 쌀 한 통 = 1kg ) ( 쌀을 먹은 후 2배 증가하는 조건 )

# rice = 100000; mouse = 2; day=1; # 쌀을 KG -> G으로 단위 변환, 초기 쥐의 수와 날짜 정의
# while True: # 조건으로 100kg의 쌀이 0보다 작을 때 까지 반복
#   rice -= mouse * 20 # 쌀의 무게에서 쥐의 수 * 20하여 줄어드는 쌀의 무게를 rice에 저장
#   if day % 10 == 0: # 만약 날짜가 10의 배수일 때 쥐의 수는 2배 증가
#     mouse *= 2 # 기존 쥐의 수 * 2배 
#   if rice <= 0: # 쌀의 무게가 0g이 될 경우 while문 종료
#     break
#   day+=1 # 한번 반복할 때 마다, 날짜 증가
# print(day,'일',mouse,'마리')

# [ Quiz .2 ] : 별 찍기, 홀수를 입력 받아 입력 받은 홀수 라인 만큼 마름모 형태의 별이 나타나도록 하세요.
# [ EX ] :홀수의 줄 수를 입력 : 5
#    ★
#  ★★★
# ★★★★★
#  ★★★
#    ★
# 힌트 : Flag ( 기준점 설정 하기 ) , 공백은 ( 감소 후 증가 ) , 별은 ( 증가 후 감소 ) , IF문 , For문을 활용 
# 공백의 시작은 전체 라인에서 나누기 2한 몫이 시작 값 , 별은 초기 값이 항상 1로 시작 된다. 

# wh = 1
# while wh:
#   line = int(input("홀수의 줄 수 입력: "))
#   mid = line // 2 + 1
#   for i in range(1, mid+1):
#     print("_" * (mid-i),end="")
#     print("☆" * (i * 2 - 1))
#   for j in range(mid-1, 0, -1):
#     print("_" * (mid-j),end="")
#     print( "☆" * (j * 2 - 1))
#   wh = int(input("계속(1), 종료(0): "))

# i,j,num=0,0,1;
# while num:
#   ln = int(input('홀수의 줄 수를 입력 : '))
#   flag=0; sp = ln//2; st = 1;
#   for i in range (ln):
#     for j in range (sp): print(" ",end="")
#     for j in range (st): print("★",end="")
#     print()
#     if i==(ln//2): flag=1
#     if flag==0: sp-=1; st+=2
#     else: sp+=1; st-=2
#   num = int(input('0.종료 1.계속 : '))

# [과제 주제] : 형상관리의 이해 및 Git 시스템 사용

# 1. 형상관리의 의미 및 필요성 정리

# 2-1. Git 시스템 구조 및 명령어 정리 
#  -> 기본개념 : staging, commit, tag, branch, head 등
#  -> 협업기능 : pull request, Merge 등
#  -> 가상의 시나리오를 선정하여 실제 작업과정 정리 (PR, Merge 필수 포함)

# 2-2. Git 저장소 종류 정리 (Local, Remote)
#  -> Local Repository, Remote Repository 
#  -> Remote Repository는 반드시 Git-Hub 사용 
#  -> Git-Hub 저장소에서 지원하는 인증방식 및 실제 인증작업 수행

# 3. VScode에서 사용가능한 유용한 확장 도구 설치 및 사용
#  -> EX:) 각종 편집 도구, Git-Hub 연동, Gemini Code Assist 등

# [제출 결과물] -----> 기술 문서 
# 기술 문서 : 모든 과정이 상세하게 기술되어있는 문서 
# 어떠한 기술을 구현 했을때 증거로 사용 될 수 있어야 한다.


