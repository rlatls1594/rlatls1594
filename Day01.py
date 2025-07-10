# 한 줄 주석

'''
여러 줄 주석
여러 줄 주석
여러 줄 주석
여러 줄 주석
여러 줄 주석
'''

# [예제.1]
# print("Hello Python")
# print("Python Test!!!")
# print("안녕");print("하세요")

# [예제.2]
# print("10더하기20은", 10+20)
# print("10 + 20 =", 10+20)
# print("2곱하기2는", 2*2)
# print("2 * 2 = ", 2*2)

# [예제.3]
# print("라인\n변경\n테스트")
# print("AAA\tBBB\tCCC")
# print("!!!\t@@@\t###")
# print("123\t456\tCCC")
# print("내용 \"강조\"")
# print('내용 \'강조\'')
# print("내용 \\강조\\")
# print("내용 '강조'")
# print('내용 "강조"')

# [문제 정답코드]
# print('\t #### 회비 정보 ####')
# print('=' * 40)
# print('이름\t나이\t전화번호\t회비')
# print('=' * 40)
# print('김동완\t38\t010-1111-1111\t\\20,000')
# print('서지수\t24\t010-1234-5678\t\\30,000')
# print('이지은\t25\t010-2525-2345\t\\50,000')
# print('-' * 40)
# print('총합계\t\t\t\t\\100,000')
# print('=' * 40)

# [예제.5]
# 1. 단일 문자 및 문자열 출력
# print("{}{}".format("A","String"))
# print("AString")
# print("%c%s" %('A',"String"))

# 2. 소수점 수 출력
# print("키:{:f}/몸무게:{:f}".format(180.12, 83.12))
# print("키:{:.1f}/몸무게:{:.2f}".format(180.12, 83.12))
# print("키:{}/몸무게:{}".format(180.12, 83.12))

# 3. 고정길이 출력 및 값 정렬 ( 천단위 자동입력 )
# print("{}원".format(10000))
# print("{:10}원".format(10000))
# print("{:>10}원".format(10000))
# print("{:<10}원".format(10000))
# print("{:^10}원".format(10000))
# print("{:,}원".format(10000))
# print("{:0>10}원".format(10000))
# print("{:_>10}원".format(10000))

# [문제]
# print('\t\t{}' .format('파이썬 쇼핑몰'))
# print('번호 : {}' .format(1078718855))
# print('주소 : {}' .format('서울시 종로구 종로 3가'))
# print('성명 : {}' .format('강사'))
# print('전화 : {}' .format('070-1234-5678'))
# print('----------------------------------------------')
# print('\t{}\t\t{}\t{}\t{}' .format ('품명',' 단가',' 수량',' 금액'))
# print('----------------------------------------------')
# print('{:>10}\t{:,}\t{:>4}\t{:,}' .format('블루투스 이어폰',85000,1,85000))
# print('{:>12}\t\t{:>6,}\t{:>4}\t{:>6,}' .format('USB 3.0 8G',8000,1,8000))
# print('----------------------------------------------')
# print('{}\t\t\t\t\t{:,}' .format('소 계', 93000))
# print('----------------------------------------------')
# print('{}\t\t\t\t{:,}' .format('청구금액', 93000))
# print('{}\t\t\t{:>14,}' .format('받은금액', 100000))
# print('{}\t\t\t\t{:>6,}' .format('거스름돈', 7000))
# print('----------------------------------------------')

# [변수]
# - 한가지의 값으로 고정되어있지 않고, 여러 값으로 변할 수 있는 데이터 저장 공간 
# - 데이터를 사용하기위해 메모리의 공간을 할당 받아 해당 공간에 이름을 부여하여 사용

# [예제.6]
# var1 = 100
# var2 , var3 = 200, 300
# var4 = var5 = 500
# print("var1={}, var2={}, var3={}, var4={}, var5={}".format(var1,var2,var3,var4,var5))
# print(var1); print(var2);

# v1 = 100; v2 = 1.123; v3 = "123"
# print(v1, type(v1)); print(v2, type(v2)); print(v3, type(v3))

# A = v1 - int(v2)
# print(A, type(A))

# v1 = float(v1)
# print(v1, type(v1))

# v3 = int(v3)
# print(v3, type(v3))

# v3 = str(v3)
# print(v3, type(v3)) 

# v3 = "ASD"
# print(v3, type(v3))

# v3 = int(v3)
# print(v3, type(v3))

# [문제.1] : num1(10) + num2(20) = 30 출력해 주세요.
# 단, 10 , 20 , 30 은 변수를 이용하여 출력
num1 = 10
num2 = 20
print("num1({})+num2({})={}".format(num1,num2,num1+num2))


# [문제.2] 
# num1 = 7 
# num2 = 5
# 위 값의 연산 결과를 각각의 변수에 저장 후 출력 (+,-,*,/) 

num1 = 7
num2 = 5
sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
print("num1 + num2 = ", sum)
print("num1 - num2 = ", sub)
print("num1 * num2 = ", mul)
print("num1 / num2 = ", div)


# [문제.3]
# 1. 다음과 같이 나오도록 코딩 하세요. ( 단, 변수를 사용 할 것 ) Python 100점
# 2. 다음과 같이 나오도록 코딩 하세요. ( 단, 변수를 사용 할 것 ) 나는 20살입니다.
# 3. Python , C언어 , Java 3과목의 점수를 각 변수에 저장
# 합계와 평균을 구하는 프로그램을 만드시오. ( 평균은 소수점 2자리 까지 )

py1 = 100
print("Python {}점".format(py1))
py2 = 20
print("나는 {}살 입니다.".format(py2))

파이썬점수=100
C언어점수=70
Java점수=80

sum=파이썬점수+C언어점수+Java점수
avg=sum/3
print("3과목 총점은 = {}".format(sum))
print("3과목 평균은 = {:.2f}".format(avg))


# [문제.4]
# su = 100
# num ='100'
# fit = 1.111
# 위 변수들을 선언 후 위 변수를 이용하여 아래와 같은 출력 결과가 나오도록 코드를 완성하세요.
# 힌트 : 문자열 + 문자열은 문자열 이어붙이기가 된다.

# [출력결과]
# 200
# 101.111
# 100100

su = 100
num ='100'
fit = 1.111
print("{}".format(type(su)))
print("{}".format(type(num)))
print("{}".format(type(fit)))
print("정수 형변환 : {}".format(su+int(num)))
print("실수 형변환 : {:.3f}".format(su+fit))
print("문자열 형변환 : {}".format(str(su)+num))

