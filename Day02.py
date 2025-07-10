# [input] : 입력함수
# - 데이터를 입력받는 함수 
# - 데이터를 입력 받을 경우 기본값 자료형 "문자열"
# - 값을 입력받아 연산을 진행 할 경우 반드시 자료형 변환 작업을 수행해야 한다.

# A = "ASD"
# B = "QWE"
# C = A + B
# D = A * 5
# print(C)
# print(D)

# [예제.1]
# num1 = int(input("첫 번째 정수입력: "))
# num2 = int(input("두 번째 정수입력: "))
# num3 = num1 + num2
# print(num3)

# num4 = float(input("첫 번째 실수입력: "))
# num5 = float(input("두 번째 실수입력: "))
# num6 = num4 + num5
# print(num6)

# data = input("문자열 입력: ")
# print(data)

# [ 입력 함수 Quiz ]
# 학생 이름과 국어, 영어, 수학 점수를 입력 받아 출력하시오
# 학생 이름 : 강사
# 국어 점수 : 1
# 영어 점수 : 2
# 수학 점수 : 2
# =================학생 정보==================
# 이름  국어  영어  수학  합계  평균
# 강사    1     2     2    5   1.67

# name = input("학생 이름: ")
# kor = int(input("국어 점수: "))
# eng = int(input("영어 점수: "))
# mat = int(input("수학 점수: "))
# print("=================학생 정보==================")
# print("이름\t국어\t영어\t수학\t합계\t평균\t")
# print("{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(name,kor,eng,mat,kor+eng+mat,(kor+eng+mat)/3))

# [문제.1]
# name = input("이름: ")
# age = int(input("나이: "))
# print("{}님의 나이는{}살 입니다.".format(name,age))

# [문제.2]
# su1 = int(input("첫 번째 정수입력: "))
# su2 = int(input("두 번째 정수입력: "))
# print("{} + {} = {}".format(su1,su2,su1+su2))
# print("{} - {} = {}".format(su1,su2,su1-su2))
# print("{} * {} = {}".format(su1,su2,su1*su2))
# print("{} / {} = {}".format(su1,su2,su1/su2))

# [문제.3]
# name = input("이름: ")
# tall = float(input("키: "))
# weight = float(input("체중: "))
# std_weight = (tall - 100) * 0.9
# pat = weight / std_weight * 100
# print("{}님의 비만도는 {:.2f}% 입니다.".format(name,pat))

# [비트 연산자]
# num1, num2 = 3,5
# bit = num1 ^ num2
# print(bit)

# AND 비트 연산
# 0 1 1 (3의 2진수 값)
# 1 0 1 (5의 2진수 값)
# ------
# 0 0 1 (001의 10진수 값 : 1)

# OR 비트 연산
# 0 1 1 (3의 2진수 값)
# 1 0 1 (5의 2진수 값)
# ------
# 1 1 1 (111의 10진수 값 : 7)

# XOR 비트 연산
# 0 1 1 (3의 2진수 값)
# 1 0 1 (5의 2진수 값)
# ------
# 1 1 0 (110의 10진수 값 : 6)

# bit = 10
# print(bit << 2)
# print(bit >> 2)

# [if (조건문)]
# - 조건식이 참일 경우 if의 종속문장을 실행
# - 참이 아닐 경우 if문의 종속문장은 실행되지 않는다.
# - Python에서 제어문의 종속문장을 표현할때에는 반드시 "들여쓰기"를 진행해야 한다.

# [예제.1]
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
# if num in (100,200,300,400,500):
#   print("num 변수의 값은 멤버에 속해있습니다.")

# [예제.3]
# if ~ else : 조건식이 참일 경우 if 종속문장 실행 / 거짓일 경우 else 종속문장 실행
# x = 99
# if x >= 100:
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
# 3. 수를 입력 받아 짝,홀수를 구분하여 출력하시오.
# 4. 두수를 입력 받아 큰 수를 출력하시오.
# 5. 세수를 입력 받아 큰 수를 출력하시오.
# 6. 두수를 입력 받아 큰 수가 짝수이면 출력하시오.
# 7. 두수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력하시오.

# # [ 정답 코드 ]
# # 3의 배수
# num = int(input('수 입력 : '))
# if num % 3 == 0 :
#   print(num,'3의 배수')
# else:
#   print("3의 배수가 아닙니다.")

# # 절대값
# num = int(input('수 입력 : '))
# if num>0 :
#   print(num)
# if num<0 :
#   print(-num)

# # 짝,홀수 구분 출력
# num = int(input('수 입력 : '))
# if num%2==0 :
#   print(num,'짝수')
# else :
#   print(num,'홀수')

# # 두 수를 입력 받아 큰 수를 출력
# num1 = int(input('수 입력 : '))
# num2 = int(input('수 입력 : '))
# if num1>num2 :
#   print('{}이(가) {}보다 크다'.format(num1,num2))
# else :
#   print('{}이(가) {}보다 크다'.format(num2,num1))

# # 세 수를 입력 받아 큰 수를 출력
# num1 = int(input('수 입력 : '))
# num2 = int(input('수 입력 : '))
# num3 = int(input('수 입력 : '))
# if num1>num2 and num1>num3:
#   print('제일 큰 수',num1)
# if num2>num1 and num2>num3:
#   print('제일 큰 수',num2)
# if num3>num2 and num3>num1:
#   print('제일 큰 수',num3)

# # 두 수를 입력 받아 큰 수가 짝수이면 출력
# num1 = int(input('수 입력 : '))
# num2 = int(input('수 입력 : '))
# if num1>num2 and num1%2==0:
#   print(num1,':num1이 크면서 짝수다')
# if num2>num1 and num2%2==0:
#   print(num2,':num2가 크면서 짝수다')

# # 두 수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력
# num1 = int(input('수 입력 : '))
# num2 = int(input('수 입력 : '))
# Sum = num1+num2
# if Sum %2==0 and Sum % 3 ==0:
#   print('두수의 합은 짝수이며 3의 배수이다')

# [중첩 if문] : if문의 종속문장으로 또 다른 if문이 정의 
# [예제.4]
# su = int(input("수 입력: "))
# if su % 3 == 0:
#   if su % 2 == 0:
#     print("3의 배수이며, 짝수!")
#   else:
#     print("3의 배수이지만, 짝수가 아닙니다.")
# else:
#   print("3의 배수가 아닙니다.")

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

# [정답코드]
# [1번]
# name = input('이름:')
# k = float(input('키:'))
# w = float(input('체중:'))
# s = (k-100) * 0.9
# b = w / s * 100

# if b < 100:
#   a = '저 체중'
# elif b >= 100 and b < 110:
#   a = '정상 체중'
# elif b >= 110 and b < 120:
#   a = '과 체중'
# elif b >= 120 and b < 130:
#   a = '비만'
# else:
#   a = '고도 비만'

# print('{}님의 비만도는 {:.2f}%로 {}입니다.'.format(name,b,a))


# [2번]
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

# - 평년이면 2월은 28일까지, 윤년이면 29일까지
# - 또한 윤년은 4년 주기마다 오지만 100년 주기는 제외하고
# - 400년 주기마다 윤년이 돌아오게 된다.

