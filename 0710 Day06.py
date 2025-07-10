# [Python 함수]
# - 함수 : 소스코드 내의 작은 프로그램 단위 (기능구현)
# -- Python 함수 : 특정 작업을 수행하는 코드 블럭을 이름으로 묶어 둔 것
# - 함수를 활용하여, 프로그램의 모듈화를 구현하여 유지 보수 및 운영에 이점을 가져올 수 있다.
# -- 코드 재사용을 돕고, 가독성을 높일 수 있다.
# - Python에서는 함수를 정의하기 위해 "def" 키워드를 사용한다.

# 함수 파트를 잘 해둬야 Class 파트에서도 수월하게 작업 할 수 있다. (Class 내부에 method가 함수의 기능을 함 )
# [예제.1]
# def func1(arg1, arg2):
#   print(arg1, arg2)
# ( ) 소괄호 안 arg1 과 arg2는 "매개변수"
# 실행하면 아무것도 출력되지 않는다
# 함수는 무조건 실행되는 것이 아니다
# 함수 호출이라는 작업이 행해져야 실행된다

# func1()
# func1(100, 200)
# func1(100, "ASD")
# func1(100, [1,2,3])
# 함수 호출은 함수의 이름으로 호출
# 호출에는 함수이름에 ( ) 소괄호를 붙여줘야한다
# 호출 시 ( ) 소괄호 안에 값은 "인자값"
# 함수 이름만 가지고 호출 시 에러가 난다 
# TypeError: func1() missing 2 required positional arguments: 'arg1' and 'arg2'
# def func1(arg1, arg2)에서 함수 정의는 했지만 func1()에 argument, 인자값이 없으므로 에러 출력
# 무조건 매개변수를 설정하지 않아도 된다. 내가 어떤 기능을 구현하고자 하는지에 따라 다르다
# 인자값에 100, "ASD" 와 같이 문자열을 넣어도, 어떠한 데이터(Tuple, List 등)를 넣어도 호출 및 출력이 가능하다

# def func2():
#   print("Func2 함수 실행")
# func2()
# 매개변수도 없고 인자값도 없지만 정상적으로 출력된다
# fun2()에 인자값을 설정할 경우 에러 출력
# 왜? 매개변수가 없는데 인자값을 설정했으므로 에러 출력
# 함수 자체는 쉬울 수 있지만 호출, 매개변수와 인자값 설정 개념이 어려울 수 있다

##### 기초, 기반지식을 쌓으려면 관련 내용의 책을 많이 읽어라. #####
# def func3(arg1=3):
#   print(arg1)
# func3()
# func3('A')
# 매개변수를 지정하고 함수 호출 시 인자값이 있어야하는데 인자값이 없는데도 출력이 되네?
# 위의 경우 default 매개변수를 지정해서 인자값 설정 없이도 출력이 가능
# arg1=3이 default 매개변수로 지정되어있으므로 3이 인자값으로 넘어가서 동작함
# 따라서 인자값이 있을 수도 있고, 없을 수도 있는 경우의 수를 대비하기 위해 default 매개변수를 활용한다

# def func4(*numbers):
#   print(numbers, type(numbers))
# func4(100)
# func4(100,200)
# func4(100,200,300)
# 매개변수가 하나, 두개 등으로 정의, 인자값을 하나를 넘길 수도, 둘, 셋 이상을 넘겨야 하는 경우
# 경우의 수를 생각해서 미리 셋팅해두는 것이 힘듦
# 이럴 때 가변 매개변수 기능을 사용할 수 있다
# 이 경우 여러 개의 인자값은 하나의 tuple로 묶인다


# [예제.2]
# def func(arg):
#   print(arg)
#   return arg * arg
# func(100)

# def func(arg):
#   print(arg)
#   return
# func(100)

# def func(arg):
#   print(arg)
#   return arg * arg
# data = func(100)
# print(data)
# return 값 없이 return만 사용하면 None 반환
# return 값 형태로 결과값을 돌려줄 수 있다
# returnd은 함수를 호출한 곳으로 되돌아가라
# 값을 가지고 return되는 경우 저장 할 변수가 있어야 함
# 값을 data 변수에 저장되어 출력되는 것
# data = func(100) 대입 연산자는 우측부터 해석  
# func(100) = arg = 100 
# return 100 * 100 -> 10000

# def func_sum(arg1, arg2):
#   return arg1 + arg2
# sum = func_sum(100,200)
# print(sum)

# 매개변수와 인자값을 알고 있다면 인자값을 매개변수에 지정해서 사용할 수도 있다
# def func_sum(arg1, arg2):
#   return arg1 + arg2
# sum = func_sum(arg2=100, arg1=200)
# print(sum)

# func_sum(100,200) 인자값 가지고 호출 -> 100은 arg1에 , 200은 arg2에
# return 100 + 200
# func_sum = 300 
# sum = func_sum = 300
# sum = 300


# [예제.3]
# - 지역변수 : 한정된 지역(Local)에서만 사용되는 변수 (함수 내부에 선언)
# - 전역변수 : 프로그램 전체(Global)에서 사용가능한 변수 (함수 바깥쪽에 선언)

# def f1():
#   a = 100 # f1 함수의 지역 변수
#   print("f1의 a:", a)

# def f2():
#   a = 200 # f2 함수의 지역 변수
#   print("f1의 a:", a)

# f1()
# f2()
# 무슨 차이가 있을까?
# f1 함수를 호출하면 메모리(RAM)에 f1 함수를 실행할 프레임(영역)이 할당됨
# a = 100 일 경우 a라는 변수가 만들어지고 100을 저장
# 출력 시 프레임 영역을 초기화함. 왜? 작업이 끝났으니까 
# f2 함수를 호출하면 메모리(RAM)프레임(영역)이 할당됨
# a = 200 일 경우 a라는 변수가 다시 만들어지고 200을 저장
# 출력 시 역시 프레임 영역을 초기화함. 

# def f1():
#   print("f1의 a:", a)

# def f2():
#   print("f1의 a:", a)
# a = 300 # 전역 변수 a
# f1()
# f2()
# a = 100 , a = 200 은 함수 안에서 사용 : 지역 변수 /  a = 300 은 함수 밖에서 사용 : 전역 변수
# 변수가 메모리 어떤 영역에 만들어지느냐에 따라서 사용처, 사용법이 다르다
# 실행 파일 영역 안에 전역변수는 공간을 확보해서 300을 저장
# 함수가 호출되면 함수 프레임이 만들어지는데 실행파일 영역이 정의하고 있는 메모리 공간 안에 만들어짐
# f1 이라는 함수 영역이 만들어지고 프린트 할 것인데 
# a라는 전역변수 공간에 가서 300이라는 값을 출력하고
# 모든 작업이 끝나면 다시 초기화
# f2 도 똑같이 작동

# def f1():
#   a = 100 # f1 함수의 지역 변수
#   print("f1의 a:", a)

# def f2():
#   # a = 200 # f2 함수의 지역 변수
#   print("f1의 a:", a)
# a = 300 # 전역 변수 a
# f1()
# f2()
# func 라는 영역 안에 만들어진 a랑 func 영역 밖에 만들어진 a랑은 다르다
# a = 300 이라는 전역 변수 a 
# 지역 변수와 전역 변수의 충돌 발생 시 지역 변수가 우선 순위가 더 높다

# def f1():
#   global a
#   a = 100 # f1 함수의 지역 변수
#   print("f1의 a:", a)

# def f2():
#   # a = 200 # f2 함수의 지역 변수
#   print("f1의 a:", a)
# a = 300 # 전역 변수 a
# f1()
# f2()
# global은 지역 변수가 아님, 전역 변수 선언임
# 따라서 변수전에 global a 라고 선언해주게되면 a = 100 은 지역 변수가 아니라 전역 변수로 사용됨
# 특정 함수 내부에서 에서 전역 변수의 값을 변경하고 싶은 경우 사용 



# [ 문제 1]
# 앞에서 학습한 내용을 바탕으로 다음 문제를 풀어보세요
# 1. programInfo () 함수를 만들어서 다음과 같은 정보가 표시 될 수 있도록 하시오
# 	Version : 1.x
# 	Update Date : 2017-01-01
# 	Author : Project Python

# 2. number 인자를 사용하는 inc (number), dec (number) 함수를 만들어 함수로 전달한 number 값에 대해 inc 함수는 +1 증가, dec 함수는 1 감소한 값을 출력하게 하시오

# 3. 위의 문제에서 값을 출력하지 말고 반환 할 수 있도록 하시오

# 4. number 인자를 사용하는 rangeRand (number) 함수를 만들어 number 값에 따라 0 ~ number 까지 랜덤 값을 반환 하도록 하시오

# 5. start, end 인자를 사용하는 rangeRand (start, end) 함수를 만들고 start ~ end 까지 랜덤 값을 반환 하도록 하시오

# -> 풀이 및 해석 코드
# 1. programInfo () 함수를 만들어서 다음과 같은 정보가 표시 될 수 있도록 하시오
# def programInfo():
#     print("Version\t\t: 1.x")
#     print("Update Date\t: 2017-01-01")
#     print("Author\t\t: Project Python")
# 프로그램 정보를 출력
# 	Version : 1.x
# 	Update Date : 2017-01-01
# 	Author : Project Python
# 사용 예 : programInfo()

# 2. number 인자를 사용하는 inc (number), dec (number) 함수를 만들어 함수로 전달한 number 값에 대해 inc 함수는 +1 증가, dec 함수는 1 감소한 값을 출력하게 하시오
# def inc(number):
#     print(number + 1)

# def dec(number):
#     print(number - 1)
# inc와 dec 수를 정의하고 inc는 +1 , dec는 -1
# 사용 예 : inc(5) -> # 출력: 6 / dec(5) -> # 출력: 4

# 3. 위의 문제에서 값을 출력하지 말고 반환 할 수 있도록 하시오
# def inc(number):
#     return number + 1

# def dec(number):
#     return number - 1
# print로 출력하지말고 return으로 반환
# 사용 예 : result1 = inc(5) -> # 6 / result2 = dec(5) -> # 4

########################### 4번, 5번이 어려움 #########################################
# 4. number 인자를 사용하는 rangeRand (number) 함수를 만들어 number 값에 따라 0 ~ number 까지 랜덤 값을 반환 하도록 하시오
# import random
# def rangeRand(number):
#     return random.randint(0, number)
# 하나의 인자를 받아 0부터 number 까지의 랜덤 정수 반환
# 사용 예 : print(rangeRand(10))  # 0 ~ 10 사이 랜덤 정수

# isinstence 기능을 추가하여 검사 기능까지 추가
# import random
# def rangeRand(number):
# # 하나의 인자를 받아 0부터 number까지의 랜덤 정수 반환
#     if not isinstance(number, int) or number < 0:
#         raise ValueError("number는 0 이상의 정수여야 합니다.")
#     return random.randint(0, number)
# isinstence isinstance는 주어진 값이 특정 클래스(자료형)의 인스턴스인지 확인하는 내장 함수 
# 참(True) 또는 거짓(False)을 반환해 조건 분기나 오류 검사에 자주 사용
# 사용 예 : isinstance(값, 클래스_또는_튜플)
# 첫 번째 인자에 검사할 값을 입력
# 두 번째 인자에 클래스나 자료형(또는 클래스의 튜플)을 지정
# 값이 해당 클래스(들)에 속하면 True, 그렇지 않으면 False를 반환
# raise는 예외를 직접 발생시켜 프로그램의 흐름을 즉시 멈추고 에러를 알리는 역할

# 5. start, end 인자를 사용하는 rangeRand (start, end) 함수를 만들고 start ~ end 까지 랜덤 값을 반환 하도록 하시오
# import random
# def rangeRand(start, end):
#     return random.randint(start, end)
# 두 개의 인자를 받아 start부터 end까지의 랜덤 정수 반환
# 사용 예 : print(rangeRand(5, 15))  # 5 ~ 15 사이 랜덤 정수

# isinstence 기능을 추가하여 검사 기능까지 추가
# import random
# def rangeRand(start, end):
# # 두 개의 인자를 받아 start부터 end까지의 랜덤 정수 반환
#     if not all(isinstance(x, int) for x in (start, end)):
#         raise ValueError("start와 end는 정수여야 합니다.")
#     if start > end:
#         raise ValueError("start는 end보다 작거나 같아야 합니다.")
#     return random.randint(start, end)

# 4번과 5번을 묶어서 사용할 수도 있다
# 4. number 인자를 사용하는 rangeRand (number) 함수를 만들어 number 값에 따라 0 ~ number 까지 랜덤 값을 반환 하도록 하시오
# 5. start, end 인자를 사용하는 rangeRand (start, end) 함수를 만들고 start ~ end 까지 랜덤 값을 반환 하도록 하시오
# import random
# def rangeRand(*args):
#     if len(args) == 1:
#         start, end = 0, args[0]
#     elif len(args) == 2:
#         start, end = args
#     else:
#         raise TypeError("rangeRand() takes 1 or 2 positional arguments but {} were given".format(len(args)))
#     return random.randint(start, end)
# len() 함수는 시퀀스나 컬렉션(String, List, Typle, Dictionary 등)의 **길이(요소 개수)**를 반환

# 최종 실행 결과물
# import random
# def programInfo():
#     print("Version       : 1.x")
#     print("Update Date   : 2017-01-01")
#     print("Author        : Project Python")

# def inc(number):
#     return number + 1
# def dec(number):
#     return number - 1

# def rangeRand(number):
#     return random.randint(0, number)
# def rangeRandRange(start, end):
#     return random.randint(start, end)

# # 스크립트로 직접 실행할 때만 실행하도록 함
# if __name__ == "__main__":
#     programInfo()                                    # 정보 출력
#     print("inc(5)   =", inc(5))                      # 함수 반환값 출력
#     print("dec(5)   =", dec(5))
#     print("rangeRand(10)      =", rangeRand(10))     # 0~10 랜덤
#     print("rangeRandRange(5,15)=", rangeRandRange(5, 15))


# [ 문제 2 ]
# 앞에서 학습한 내용을 바탕으로 다음 문제를 풀어보세요
# 1. 총 3 개의 인자를 받는 calc (num1, num2, op) 함수를 만들어 간단한 사칙 연산을 수행 할 수 있도록 하시오 . 단 , 아래와 같이 사용 가능해야 합니다
# 	calc(2, 1, '-')
# 	calc(2, 1) 			# 결과 값 : 3
# 	calc(3) 			# 결과 값 : 4
# 	calc(3, op=‘-’) 		# 결과 값 : 2

# 2. vSum () 함수를 만들어 인자로 전달된 모든 값을 더하는 함수를 만드시오
# 	vSum(1, 2) 			# 결과 값 : 3
# 	vSum(1, 2, 3) 		# 결과 값 : 6
# 	vSum(1, 2, 3, 4, 5)		# 결과 값 : 15

# -> 풀이 및 해석 코드
# 1. 총 3 개의 인자를 받는 calc (num1, num2, op) 함수를 만들어 간단한 사칙 연산을 수행 할 수 있도록 하시오
def calc(num1, num2=1, op='+'):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            raise ZeroDivisionError("0으로 나눌 수 없습니다.")
        return num1 / num2
    else:
        raise ValueError(f"지원하지 않는 연산자입니다: {op}")
# num1, num2 두 수에 대해 연산자 op를 적용한 결과를 반환
# op는 사칙연산 기호 + , - , * , / 중 하나
# raise 로 num2를 0 으로 가정하고 나눌 경우 경고 출력 
# raise 로 사칙연산 기호 + , - , * , / 가 아닌 다른 기호 사용 시 경고 출력
# return 으로 결과 값 반환
# 사용 예
print(calc(2, 1, '-'))    # 결과 값 : 1
print(calc(2, 1))         # 결과 값 :3
print(calc(3))            # 결과 값 :4  (num2=1, op='+')
print(calc(3, op='-'))    # 결과 값 :2  (num2=1)

# 2. vSum () 함수를 만들어 인자로 전달된 모든 값을 더하는 함수를 만드시오
def vSum(*args):
    return sum(args)
# 가변 인자로 전달된 모든 값을 더해 반환. 인자를 하나도 넘기면 0 반환
# 사용 예
print(vSum(1, 2))            # 결과 값 : 3
print(vSum(1, 2, 3))         # 결과 값 : 6
print(vSum(1, 2, 3, 4, 5))   # 결과 값 : 15






