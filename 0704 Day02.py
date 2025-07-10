# [input] : 입력함수
# - 데이터를 입력 받는 함수
# - 데이터를 입력 받을 경우 기본값 자료형 "문자열"
# - 값을 입력 받아 연산을 진행 할 경우 반드시 자료형 변환 작업을 수행해야 한다.
# 예시)
# A = "ASD"
# B = "QWE"
# C = A + B
# D = A * 5
# print(C)
# print(D)

# A = "100"
# B = "200"
# C = A + B
# print(C)
# -> 숫자를 입력함수를 이용해 계산하고 싶은 경우 int, 정수형으로 바꿔줘야한다
# -> 입력함수는 문자열로 취급되므로 단순 문자를 이어붙여주는 기능만 한다

# [예제.1]
# num1 = input("첫 번째 정수입력: ")
# num2 = input("두 번째 정수입력: ")
# num3 = num1 + num2
# print(num3)
# -> 100 / 200 = 100200 "문자열(str)" 출력

# 문자열을 정수형으로 형 변환
# num1 = input("첫 번째 정수입력: ")
# num2 = input("두 번째 정수입력: ")
# num3 = int(num1) + int(num2)
# print(num3)
# -> 100 / 200 = 300 "숫자값(int)" 출력
# -> 하지만 별로 바람직한 방법은 아니다. 
# -> 바람직한 방법은 아래와 같다

# 바람직한 코드
# num1 = int(input("첫 번째 정수입력: "))
# num2 = int(input("두 번째 정수입력: "))
# num3 = (num1) + (num2)
# print(num3)
# -> 100 / 200 = 300 "숫자값(int)" 출력
# -> 형 변환은 애초에 입력할 때 부터 처리되게끔 만들어주는 것이 바람직하다.
# -> 에러가 발생할 것 같은 지점에서부터 형 변환을 적용해서 에러를 예방하자는 의미

# num4 = float(input("첫 번째 실수입력: "))
# num5 = float(input("두 번째 실수입력: "))
# num6 = num4 + num5
# print(num6)
# -> 실수도 가능하다

# data = input("문자열 입력: ")
# print(data)
# -> 문자열로 인식되기 때문에 문자열로도 가능하다

# [ 입력 함수 Quiz ]
# 학생 이름과 국어, 영어, 수학 점수를 입력 받아 출력하시오
# 학생 이름 : 강사
# 국어 점수 : 1
# 영어 점수 : 2
# 수학 점수 : 2
# ===================학생 정보=====================
# 이름  국어  영어  수학  합계  평균
# 강사    1     2     2     5  1.67

# -> 정답 코드
# name = input("학생 이름 : ")
# kor = int(input("국어 점수 : "))
# eng = int(input("영어 점수 : "))
# mat = int(input("수학 점수 : "))
# total = kor + eng + mat
# avg = total / 3
# print("========================= 학생 정보 =============================")
# print("이름\t국어\t영어\t수학\t합계\t평균\t")
# print("{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(name, kor, eng, mat, total, avg))

# [ 문제 ]
# 앞에서 학습한 내용을 바탕으로 다음 문제를 풀어보세요
# 1. input() 으로 사용자 입력을 받고 이름과 나이를 출력하는 코드를 작성하시오
# 출력 예제 : 홍길동님의 나이는 38 세 입니다

# 2. input() 으로 2 개의 값을 받고 더하기 , 빼기 , 곱하기 , 나누기 연산을 하여 그 결과를 출력하는 코드를 작성하시오

# 3. 사용자로부터 이름 , 키 , 체중 값을 입력 받아 비만도를 구하고 출력하는 코드를 작성하시오
# 비만도 계산 식 : 비만도 (%) = 현재 체중 / 표준 체중 * 100
# 표준 체중 계산 식 : 표준 체중 = 현재 키 100) * 0.9
# 출력 예제 : 홍길동님의 비만도는 112.15% 입니다

# 1. input() 으로 사용자 입력을 받고 이름과 나이를 출력하는 코드를 작성하시오
# 출력 예제 : 홍길동님의 나이는 38세 입니다
# name = input("이름을 입력하세요 : ")
# age = int(input("나이를 입력하세요 : "))
# f스트링 활용
# print(f"{name}님의 나이는 {age} 세 입니다")
# or
# {}.format() 활용
# print("{}님의 나이는 {} 세 입니다".format(name, age))

# 2. input() 으로 2개의 값을 받고 더하기, 빼기, 곱하기, 나누기 연산을 하여 그 결과를 출력하는 코드를 작성하시오
# A = int(input("첫 번째 입력 값 : "))
# B = int(input("두 번째 입력 값 : "))
# sum_result   = A + B
# diff_result  = A - B
# prod_result  = A * B
# div_result   = A / B if B != 0 else "무한대"

# f스트링 사용
# print(f"{A} + {B} = {sum_result}")
# print(f"{A} - {B} = {diff_result}")
# print(f"{A} * {B} = {prod_result}")
# print(f"{A} / {B} = {div_result}")
# or
# {}.format 사용
# print("{} + {} = {}".format(A, B, sum_result))
# print("{} - {} = {}".format(A, B, diff_result))
# print("{} * {} = {}".format(A, B, prod_result))
# print("{} / {} = {}".format(A, B, div_result))

# print("{} + {} = {}".format(A,B,A+B))
# print("{} - {} = {}".format(A,B,A-B))
# print("{} * {} = {}".format(A,B,A*B))
# print("{} / {} = {}".format(A,B,A/B))

# 3. 사용자로부터 이름, 키, 체중 값을 입력 받아 비만도를 구하고 출력하는 코드를 작성하시오 
# name   = input("이름을 입력하세요: ")
# height = float(input("키(cm)를 입력하세요: "))
# weight = float(input("체중(kg)을 입력하세요: "))

# 표준 체중과 비만도 계산
# standard_weight = (height - 100) * 0.9
# obesity_rate    = (weight / standard_weight) * 100

# 출력 (소수점 둘째 자리까지)
# f스트링 활용
# print(f"{name}님의 표준 체중은 {standard_weight:.2f}kg 입니다")
# print(f"{name}님의 비만도는 {obesity_rate:.2f}% 입니다")
# or 
# {}.format 활용
# print("{}님의 표준 체중은 {:.2f}kg 입니다".format(name, standard_weight))
# print("{}님의 비만도는 {:.2f}% 입니다".format(name, obesity_rate))


# 연산자는 해석하는 것에 초점을 맞춰야한다.
# 해석 방법만 정확하게 알고 있으면 연산자는 충분히 해석하고 활용할 수 있다.
# > 연산자
# 산술 연산자
# 연산자 	예제 		  설명
# + 		  3 + 2     두 값 을 더한 결과를 반환
# -		    3 - 2 	  두 값을 뺀 결과를 반환
# *		    3 * 2 		두 값을 곱한 결과를 반환
# /		    3 / 2 		두 값을 나눈 결과를 반환 실수 값
# //		  3 // 2    두 값을 나눈 결과의 몫 반환 정수 값***
# %		    3 % 2 	  두 값은 나눈 결과의 나머지 반환***
# **		  3 ** 2 	  거듭 제곱의 결과 반환***

# > *** 비교 연산자 ***
# 연산자	예제		  설명
# ==		  3 == 3   두 피 연산자 값을 비교하여 동일하면 True, 동일하지 않으면 False
# !=		  3 != 2 	 두 피 연산자 값을 비교하여 동일하면 False, 동일하지 않으면 True
# >		    3 > 2    두 피 연산자 값을 비교하여 왼쪽의 값이 크면 True, 그렇지 않으면 False
# <		    2 < 3 	 두 피 연산자 값을 비교하여 왼쪽의 값이 작으면 True, 그렇지 않으면 False
# >=		  3 >= 2   두 피 연산자 값을 비교하여 왼쪽의 값이 크거나 같으면 True, 그렇지 않으면 False
# <=		  3 <= 3   두 피 연산자 값을 비교하여 왼쪽의 값이 작거나 같으면 True, 그렇지 않으면 False
# -> 가장 많이 사용될 연산자, 비교 연산자

# > 논리 연산자
# 연산자	 예제						               설명
# and		  True and True, True and False	두 피 연산자가 전부 True 인 경우에만 True (논리곱)
# or		  True or True, True or False		두 피 연산자가 전부 False 인 경우에만 False (논리합)
# not		  not True, not False			      오른쪽 피 연산자에 대한 부정
# -> 예제 부분에서 실제로는 3>2 and 3<5 -> True 와 같이 활용 된다
# -> 산술 비교 논리 연산자로 거의 모든 작업을 수행할 수 있다. 

# > 멤버 연산자
# 연산자	예제				              설명
# in		  1 in (1, 2, 3)		       왼쪽 피 연산자의 값이 오른쪽 피 연산자 멤버 중 일치하는 값이 존재 하면 True
# not		  in 1 not in (1, 2, 3)	   왼쪽 피 연산자의 값이 오른쪽 피 연산자 멤버 중 일치하는 값이 존재하지 않으면 True
# -> 예제에서 1 in (1, 2, 3) 에서 1 대신 4로, 4 in (1, 2, 3) 일 경우 포함되어있지 않으니 false

# > 식별 연산자
# 연산자	예제				            설명
# is		  type(1) is int 		     두 피 연산자의 식별 값을 비교하였을 때 동일한 객체이면 True
# is not	type('1') is not int 	 두 피 연산자의 식별 값을 비교하였을 때 동일한 객체이면 False

# > 비트 연산자
# 연산자	예제				  설명
# &		    10 & 5 			 두 피 연산자의 and 비트 연산을 수행 한다
# |		    10 | 5 			 두 피 연산자의 or 비트 연산을 수행 한다
# ^		    10 ^ 5			 두 피 연산자의 xor 비트 연산을 수행 한다
# <<		  10 << 2 		 왼쪽 피 연산자의 비트를 왼쪽으로 2 개 비트 이동
# >>		  10 >> 2 		 왼쪽 피 연산자의 비트를 오른쪽으로 2 개 비트 이동
# -> 거의 사용하지 않으므로 그냥 넘어가도 되지만... 자격증 시험 등에 문제로 나오는 경우가 있다
# -> 메모리가 적은 용량의 시스템에서 비트연산자를 활용할 경우 좀 더 효율적으로 사용할 수 있다
# -> Java, Python은 용량이 커서 비트연산 의미가 없지만 C 언어에서는 유의미하다

# [ 비트 연산자 ]
# num1, num2 = 3,5
# bit = num1 & num2
# print(bit)

# AND 비트 연산
# 0 1 1 (3의 2진수 값)
# 1 0 1 (5의 2진수 값)
# ------
# 0 0 1 (001의 10진수 값 : 1)
# -> 11이 겹치는 칸은 ture = 1 / 겹치지 않고 0 이 있는 칸은 false = 0

# OR 비트 연산
# 0 1 1 (3의 2진수 값)
# 1 0 1 (5의 2진수 값)
# ------
# 1 1 1 (111의 10진수 값 : 7)
# -> 1이 하나라도 있으면 true = 1 

# XOR 비트 연산
# 0 1 1 (3의 2진수 값)
# 1 0 1 (5의 2진수 값)
# ------
# 1 1 0 (110의 10진수 값 : 6)
# -> 1과 0이 있으면 ture = 1 / 없으면 false = 0

# bit = 10
# print(bit << 2)
# print(bit >> 2)

# 1010 (10의 2진수 값)
# print(bit << 2) -> 왼쪽으로 두 칸 밀고 0이라는 비트 값을 채워넣음  -> 101000 -> 40의 2진수 값, 값이 작을 경우 값이 증가
# print(bit >> 2) -> 오른쪽으로 두 칸 밀고 뒤에 있던 값은 사라지고 왼쪽은 0으로 비트 값 채워넣음 -> 0010 -> 10의 2진수 값, 값이 작을 경우 값이 감소


# > [if (조건문)]
# - 조건식이 참일 경우 if의 종속문장을 실행
# - 참이 아닐 경우 if문의 종속문장은 실행되지 않는다.
# - Python에서 제어문의 종속문장을 표현 할 때에는 반드시 "들여쓰기"를 진행해야 한다.

# [예제.1]
# num = 100
# if num == 100:
#   print("종속문장 실행")
#   print("종속문장 실행")
#   print("종속문장 실행")
#   print("종속문장 실행")
# print("코드 종료")

# num = 100
# if num == 101:
#   print("종속문장 실행")
#   print("종속문장 실행")
#   print("종속문장 실행")
#   print("종속문장 실행")
# print("코드 종료")

# [예제.2]
# num = int(input("정수 입력: "))
# if num % 2 == 0:
#   print("num 변수의 값은 짝수입니다.")
# if num < 100:
#   print("num 변수의 값은 100보다 작다.")
# if num % 2 == 0 and num > 100:
#   print("num 변수의 값은 짝수이며, 100보다 크다.")

# if num < 100:
#   print("num 변수의 값은 100보다 작다.")
# if num % 2 == 0 and num > 100:
#   print("num 변수의 값은 짝수이며, 100보다 크다.")  
# if num in (100,200,300,400,500):
#   print("num 변수의 값은 멤버에 속해있습니다.")

# [예제.3]
# if ~ else : 조건식이 참일 경우 if 종속문장 실행 / 거짓일 경우 else 종속문장 실행
# x = 100
# if x > 100:
#   print("x 변수의 값은 100보다 크거나 같다.")
# else:
#   print("x 변수의 값은 100보다 작다.")

# num = 100
# if num in (100,200,300,400,500):
#   print("num 변수의 값은 멤버에 속해있습니다.")
# else:
#   print("num 변수의 값은 멤버에 속해있지 않습니다.")


# [ IF문 문제 ]
# 1. 입력한 데이터가 3의 배수인 경우 출력하시오.
# 2. 절대값을 구하는 프로그램을 작성하시오.
# 3. 수를 입력 받아 짝, 홀수를 구분하여 출력하시오.
# 4. 두 수를 입력 받아 큰 수를 출력하시오.
# 5. 세 수를 입력 받아 큰 수를 출력하시오.
# 6. 두 수를 입력 받아 큰 수가 짝수이면 출력하시오.
# 7. 두 수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력하시오.

# # 1. 
# num = int(input("정수 입력 : "))
# if num % 3 == 0:
#     print(f"{num}은(는) 3의 배수입니다.")
# else:
#     print(f"{num}은(는) 3의 배수가 아닙니다.")
# # or
# if num % 3 == 0:
#     print("{}은(는) 3의 배수입니다.".format(num))
# else:
#     print("{}은(는) 3의 배수가 아닙니다.".format(num))

# # 2. 
# num = float(input("실수 입력 : "))
# if num < 0:
#     num = -num
# print(f"입력값의 절대값은 {num}입니다.")
# # or
# print("입력값의 절대값은 {}입니다.".format(num))


# # 3. 
# num = int(input("정수 입력 : "))
# if num % 2 == 0:
#     print(f"{num}은(는) 짝수입니다.")
# else:
#     print(f"{num}은(는) 홀수입니다.")
# # or
# if num % 2 == 0:
#     print("{}은(는) 짝수입니다.".format(num))
# else:
#     print("{}은(는) 홀수입니다.".format(num))

# # 4. 
# num1 = float(input("첫 번째 수 : "))
# num2 = float(input("두 번째 수 : "))
# if num1 > num2:
#     print(f"더 큰 수는 {num1}입니다.")
# else:
#     print(f"더 큰 수는 {num2}입니다.")
# # or
# if num1 > num2:
#     print("더 큰 수는 {}입니다.".format(num1))
# else:
#     print("더 큰 수는 {}입니다.".format(num2))

# # 5.
# num1 = float(input("첫 번째 수 : "))
# num2 = float(input("두 번째 수 : "))
# num3 = float(input("세 번째 수 : "))
# if num1 >= num2 and num1 >= num3:
#     maximum = num1
# elif num2 >= num1 and num2 >= num3:
#     maximum = num2
# else:
#     maximum = num3
# print(f"가장 큰 수는 {maximum}입니다.")
# # or
# if num1 >= num2 and num1 >= num3:
#     maximum = num1
# elif num2 >= num1 and num2 >= num3:
#     maximum = num2
# else:
#     maximum = num3
# print("가장 큰 수는 {}입니다.".format(maximum))

# # 6.
# num1 = float(input("첫 번째 수 : "))
# num2 = float(input("두 번째 수 : "))
# if num1 > num2 and num1 % 2 == 0:
#     print(f"조건을 만족하는 수는 {num1}입니다.")
# elif num2 > num1 and num2 % 2 == 0:
#     print(f"조건을 만족하는 수는 {num2}입니다.")
# else:
#     print("두 수 중 큰 수가 짝수가 아닙니다.")
# # or
# if num1 > num2 and num1 % 2 == 0:
#     print("조건을 만족하는 수는 {}입니다.".format(num1))
# elif num2 > num1 and num2 % 2 == 0:
#     print("조건을 만족하는 수는 {}입니다.".format(num2))
# else:
#     print("두 수 중 큰 수가 짝수가 아닙니다.")

# # 7. 
# num1 = float(input("첫 번째 수 : "))
# num2 = float(input("두 번째 수 : "))
# sum = num1 + num2
# if sum % 2 == 0 and sum % 3 == 0:
#     print(f"두 수의 합 {sum}은(는) 짝수이고 3의 배수입니다")
# else:
#     print(f"두 수의 합 {sum}은(는) 조건을 만족하지 않습니다.")
# # or
# if sum % 2 == 0 and sum % 3 == 0:
#     print("두 수의 합 {}은(는) 짝수이고 3의 배수입니다.".format(sum))
# else:
#     print("두 수의 합 {}은(는) 조건을 만족하지 않습니다.".format(sum))


# [중첩 if문] : if문의 종속문장으로 또 다른 if문이 정의 (if안에 if형태)
# [예제.4]
# su =int(input("수 입력: "))
# if su % 3 == 0:
#   if su % 2 == 0:
#     print("3의 배수이며, 짝수!")
#   else:
#     print("3의 배수이지만, 짝수가 아닙니다.")
# else:
#   print("3의 배수가 아닙니다.")

# -> if ~ else 안에 다른 if ~ else 가 속해 있는 형태
# -> 중첩 if문
# -> if su % 3 == 0: 이 참이면 다음 if su % 2 == 0: 으로 내려감
# -> if su % 2 == 0: 이 참이면 3의 print("3의 배수이며, 짝수!") 출력
# -> if su % 2 == 0: 이 거짓이면 print("3의 배수이지만, 짝수가 아닙니다.") 출력
# -> if su % 3 == 0: 자체가 거짓이면 print("3의 배수가 아닙니다.") 출력
# -> 결국 if Sum %2==0 and Sum % 3 ==0: 처럼 and 구조와 비슷하다.

# [다중 if문] : if문의 조건식이 거짓일 경우 또 다른 조건식을 만나도록 함
# num = int(input("1~4사이의 값을 입력: "))
# if num == 1: 
#   print("1입력")
# elif num == 2:
#   print("2입력")
# elif num == 3:
#   print("3입력")
# elif num == 4:
#   print("4입력")
# else:
#   print("잘못 된 입력")

# 아래는 if문 하나씩 독립적
# if num == 1: 
#   print("A")
# if num == 2:
#   print("A")
# if num == 3:
#   print("A")
# if num == 4:
#   print("A")
# -> 출력 결과물은 위와 같지만 동작하는 방식이 다르다
# -> elif를 사용할 경우 한 번의 동작이지만, if를 4번 쓰는 경우 네 번의 동작
# -> 메모리에 부하를 주는 요인이 될 수 있다.


# [문제]
# 앞에서 학습한 내용을 바탕으로 다음 문제를 풀어보세요
# 1. 사용자로부터 이름 , 키 , 체중 값을 입력 받아 비만도를 구하고
# 결과를 출력 할 때 비만도 값 100 을 기준으로 100 미만이면 저체
# 중 , 100 이상 110 미만은 정상 , 110 이상 120 미만 과제중 ,
# 120 이상 130 미만 비만 , 130 이상은 고도비만으로 출력 하시오
# 비만도 계산 식 : 비만도 (%) = 현재 체중 / 표준 체중 * 100
# 표준 체중 계산 식 : 표준 체중 = 현재 키 100) * 0.9
# 출력 예제 : 홍길동님의 비만도는 112.15% 로 과체중 입니다

# 2.
# turtle 을 사용하여 3 ~ 10 까지의 값을 입력 받아 삼각형 부터
# 십각형까지 그릴 수 있는 코드를 작성하시오 위 입력 값의 범위
# 를 초과하는 경우 그릴 수 없습니다 .” 라는 메시지를 출력
# -> turtle 함수는 과감하게 건너뛰었으니 시간 되면 앞에서 찾아서 풀어볼 것. 

# 3.
# 윤년을 구하는 코드를 작성 하시오
# - 4 의 배수는 윤년이 된다 . 그 외는 평년
# - 4 의 배수 면서 100 의 배수인 경우는 평년이다 . 그 외는 윤년
# - 4 그리고 100 의 배수이면서 400 의 배수인 경우 윤년이다 . 그 외는 평년

# 정답 코드
# 1.
# name = input("이름을 입력하십시오 : ")
# height = float(input("키(cm)를 입력하십시오 : "))
# weight = float(input("체중(kg)을 입력하십시오 : "))
# 표준 체중 계산 식
# standard_weight = (height - 100) * 0.9
# 비만도 계산 식
# obesity_rate    = weight / standard_weight * 100

# 저체중, 정상, 과체중, 비만, 고도비만 총 5개
# if obesity_rate < 100:
#     status = "저체중"
# elif obesity_rate < 110:
#     status = "정상"
# elif obesity_rate < 120:
#     status = "과체중"
# elif obesity_rate < 130:
#     status = "비만"
# else:
#     status = "고도비만"
# print(f"{name}님의 비만도는 {obesity_rate:.2f}%로 {status} 입니다.")
# # or
# print("{}님의 비만도는 {:.2f}%로 {} 입니다".format(name, obesity_rate, status))

##################################################################
# 2. Turtle로 3~10각형 그리기
# import turtle

# n = int(input("몇 각형을 그리시겠습니까? (3~10): "))

# if 3 <= n <= 10:
#     angle = 360 / n
#     side  = 100
#     for _ in range(n):
#         turtle.forward(side)
#         turtle.left(angle)
#     turtle.done()
# else:
#     print("그릴 수 없습니다.")
##################################################################

# 3. 
# year = int(input("연도를 입력하십시오 : "))
# 윤년 조건: 4의 배수이면서 (100의 배수가 아니거나 400의 배수)
# {}.format() 사용1
# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     result = "윤년"
# else:
#     result = "평년"
# print("{}년은 {}입니다".format(year, result))
# -> 4의 배수이면서 100의 배수는 평년, 그 외는 윤년
# -> 4의 배수이면서 100의 배수가 아니거나 400의 배수는 윤년

# {}.format() 사용2
# or elif 사용
# if year % 400 == 0:
#     result = "윤년"
# elif year % 100 == 0:
#     result = "평년"
# elif year % 4 == 0:
#     result = "윤년"
# else:
#     result = "평년"
# print("{}년은 {}입니다".format(year, result))

# or f스트링 사용1
# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     result = "윤년"
# else:
#     result = "평년"
# print(f"{year}년은 {result}입니다")

# or f스트링 사용2
# or elif 사용
# if year % 400 == 0:
#     result = "윤년"
# elif year % 100 == 0:
#     result = "평년"
# elif year % 4 == 0:
#     result = "윤년"
# else:
#     result = "평년"
# print(f"{year}년은 {result}입니다")
# if - elif 조건은 하나의 구조이므로 위에서부터 아래로 조건을 평가해서 가장 먼저 참이 되는 분기만 실행하고 나머지는 건너뛴다.
# 만약, 문제의 지문 대로 year % 4 == 0: 을 맨 위에 두면, 100의 배수인 해(예: 1900년, 2000년, 2100년)도 모두 "윤년"으로 분류 된다.
# 즉, 100의 배수의 예외(평년)가 단 한번도 적용되지 않는다.
# 400의 배수 -> 무조건 윤년
# 100의 배수 -> 무조건 평년 *예외*
# 4의 배수 -> 윤년
# 그외 평년

# -> 선생님 코드
# [정답코드]
# [1번]
# name = input('이름:')
# k = float(input('키:'))
# w = float(input('체중:'))
# s = (k-100) * 0.9
# b = w / s * 100

# if b < 100 :
#   a = '저 체중'
# elif b >= 100 and b < 110 :
#   a = '정상 체중'
# elif b >= 110 and b < 120 :
#   a = '과 체중'
# elif b >= 120 and b < 130 :
#   a = '비만'
# else : 
#   a = '고도 비만'

# print('{}님의 비만도는 {:.2f}%로 {} 입니다.'.format(name,b,a))


# [3번] *****
# year = int(input('년도를 입력하시오 : '))
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print(year, '년도는 윤년 입니다.')
#     else:
#       print(year, '년도는 평년 입니다.')
#   else:
#     print(year, '년도는 윤년 입니다.')
# else:
#   print(year, '년도는 평년 입니다.')
# -> 이 방식이 더 문제에 직관적으로 접근 할 수 있다.

# - 평년이면 2월은 28일까지, 윤년이면 29일까지
# - 또한 윤년은 4년 주기마다 오지만 100년 주기는 제외하고
# - 400년 주기마다 윤년이 돌아오게 된다.









