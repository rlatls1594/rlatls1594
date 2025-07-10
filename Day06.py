# [Python 함수]
# - 함수: 소스코드내의 작은 프로그램 단위 ( 기능구현 )
# - 함수를 활용하여, 프로그램의 모듈화를 구현하여 유지 보수 및 운영에 이점을 가져올 수 있다.
# - Python에서는 함수를 정의하기 위해 "def" 키워드를 사용한다.

# [예제.1]
# def func1(arg1, arg2):
#   print(arg1, arg2)
# func1(100, 200) # 함수 호출

# def func2():
#   print("Func2 함수 실행")
# func2()

# def func3(arg1=3):
#   print(arg1)
# func3('A')

# def func4(*numbers):
#   print(numbers, type(numbers))
# func4(100)
# func4(100,200)
# func4(100,200,300)

# [예제.2]
# def func(arg):
#   print(arg)
#   return arg * arg
# data = func(100)
# print(data)

# def func_sum(arg1, arg2):
#   print(arg1, arg2)
#   return arg1 + arg2
# sum = func_sum(arg2=100, arg1=200)
# print(sum)

# [예제.3]
# - 지역변수 : 한정 된 지역(Local)에서만 사용되는 변수 (함수 내부에 선언)
# - 전역변수 : 프로그램 전체(Global)에서 사용가능한 변수 (함수 바깥쪽에 선언)

# def f1():
#   global a 
#   a = 100 # f1 함수의 지역변수
#   print("f1의 a:", a)
# def f2():
#   # a = 200 # f2 함수의 지역변수
#   print("f2의 a:", a)
# a = 300 # 전역변수 a
# f1(); f2()

# [문제 정답 코드 ]
# # 1
# def programInfo():
#   print('Version : 1.x')
#   print('Update Date : 2017-01-01')
#   print('Author : Project Python')
# programInfo()

# # 2
# def inc(number):
#   print(number + 1)
# def dec(number):
#   print(number - 1)
# inc(10); dec(10)

# # 3
# def inc(number):
#   return number + 1
# def dec(number):
#   return number - 1
# print(inc(10)); print(dec(10))

# # 4
# from random import randint
# def rangeRand(number):
#   return randint(0,number)
# print(rangeRand(20))

# # 5
# from random import randint
# def rangeRand(start, end):
#   if start > end:
#     return -1
#   return randint(start, end)
# print(rangeRand(10,20))

# # 6
# def calc(num1, num2=1, op='+'):
#   if op=='+':
#     return num1 + num2
#   elif op=='-':
#     return num1 - num2
#   elif op=='*':
#     return num1 * num2
#   elif op=='/':
#     return num1 / num2

# print(calc(2,1,"-"))
# print(calc(2,1))
# print(calc(3))
# print(calc(3,op="-"))

# # 7
# def vSum(*numbers):
#   tot = 0
#   for x in numbers:
#     tot = tot + x
#   return tot

# print(vSum(1,2))
# print(vSum(1,2,3))
# print(vSum(1,2,3,4,5))

# from calc import *
# print(sumFunc(10,20))
# print(subFunc(10,20))
# print(divFunc(10,20))
# print(mulFunc(10,20))

# import pack.sum
# print(pack.sum.sumFunc(10,20))

# from pack import sub
# print(sub.subFunc(20,10))

# from pack.sum import sumFunc
# print(sumFunc(10,20))


# [ Python 파일 입출력 ]
# - Disk상에 존재하는 특정 파일을 읽을 수 있다.
# - 새로운 파일을 Disk에 저장 할 수 있다.

# [ 특정 파일에 엑세스하기 위한 과정 ]
# - open 함수를 이용하여 파일 Open
# - read or write 등의 함수를 이용하여 파일에 대한 처리작업 진행
# - close 함수를 이용하여 열린 파일 닫기

#       [지정한 파일이 존재하는 경우]        [지정한 파일이 존재하지 않는 경우]
# "r"   File을 "읽기전용"으로 Open          파일이 존재하지 않을 경우 "r" 사용불가
# "w"   기존 내용 삭제 후 "쓰기"모드로 Open  새로운 파일 생성 후 "쓰기"모드로 Open
# "a"   기존 내용 유지 및 "쓰기"모드로 Open  새로운 파일 생성 후 "쓰기"모드로 Open

# [ Python 예외 처리 ]
# 예외 : 프로그램에서 벌어지는 예외적인 상황을 의미
# - 파일을 읽고자 할 때 그 파일이 존재하지 않을 경우
# - 어떠한 값을 0으로 나누고자 할때  
# - 배열의 인덱스를 범위를 벗어 났을때
# - 사용자의 요구대로 진행이 안 될때 

# [예제.4]
# try:
#   raise Exception("Error 발생")
#   su1 = int(input("정수 입력: "))
#   su2 = int(input("정수 입력: "))
#   ret = su1 / su2
#   print(ret)
# except ZeroDivisionError:
#   print("0으로 나누기 금지!")
# except ValueError:
#   print("정수값만 입력 가능!")
# except Exception as e:
#   print(e)
# else:
#   print("정상적으로 실행되었습니다.")
# finally:
#   print("무조건 실행")

# [ Quiz ]
# - 인증 프로그램 제작 
# - 90년생 부터는 "가입불가" 출력
# - 90년생 미만은 "가입가능" 출력
# - A,ㅁ,ㅋ 이러한 값 입력시 "잘못입력 숫자를 입력하세요" 문구출력

# try:
#   sn = input("주민번호 앞자리 입력(EX:900402): ")
#   if sn[0] > '9':
#     raise Exception("잘못 입력, 숫자를 입력하세요")
#   elif sn[0] >'8':
#     raise Exception("가입불가")
# except Exception as e:
#   print(e)
# else:
#   print("가입가능")
# finally:
#   print("프로그램을 종료합니다.")



