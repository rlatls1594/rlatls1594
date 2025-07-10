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

def func_sum(arg1, arg2):
  return arg1 + arg2
sum = func_sum(100,200)
print(sum)

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















