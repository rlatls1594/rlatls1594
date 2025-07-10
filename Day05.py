# [Tuple]
# - N개의 요소로 이루어진 집합
# - List와 유사한 구조를 갖는다.
# - Tuple을 정의 할 때에는 "()"를 사용하며, 생략도 가능하다.
# - Tuple로 정의 된 데이터 묶음은 변경이 불가능하다. ( List와의 차이점 )

# [예제.1]
# tu1 = (1,2,3)
# tu2 = 4,5,6
# tu3 = tu1 + tu2
# print(tu1, type(tu1))
# print(tu2, type(tu2))
# print(tu3, type(tu3))
# print(tu1[0])
# print(tu2[0:2])
# print(tu1[-1])
# a,b,c = tu1
# print(a,b,c)

# [예제.2]
# tu = (100,200,"String",100,123.456)
# print(tu.count(100))
# print(tu.index(123.456))

# [Dictionary]
# - 사전 자료형은 (Key-Value) 쌍으로 데이터를 목록을 구성한다.
# - 특정 Value에 각각의 Key를 연결하여 Key를 첨자(index)로 사용한다.
# - 사전 자료형은 사람이 사용하기 편리하고 탐색속도가 빠른 장점이 있다.
# - 사전 자료형을 정의 할 때에는 "{}"를 사용한다.

# [예제.3]
# student = {"학번":1000, "이름":"홍길동", "학과":["컴퓨터공학","전자공학"]}
# print(student, type(student))
# print(student["학과"])
# student["등급"] = "A"
# print(student)

# [예제.4]
# dic1 = {}
# for i in range(3):
#   k = input("키입력: ")
#   v = input("값입력: ")
#   dic1[k] = v
# print(dic1)

#[예제.5]
# dic = {1:'A', 2:'B', 3:'C', 4:'D'}
# dic.update({5:'E'})
# print(dic)
# print(dic.get(3))
# print(dic.get(100))
# print(dic.keys())
# print(dic.values())
# key_lst = list(dic.keys()) # ---> 사전 -> 리스트 형변환 기본값
# val_lst = list(dic.values())
# print(key_lst, val_lst)

# for val in dic.values():
#   print(val)

# for key,val in dic.items():
#   print(key, val)

# data = dic.pop(2)
# print(dic, data)
# data2 = dic.popitem() # XX
# print(dic, data2)
# dic.clear()
# print(dic)

# key_lst = [1,2,3,4,5]
# from_dic1 = {}.fromkeys(key_lst)
# from_dic2 = {}.fromkeys(key_lst,100)
# print(from_dic1)
# print(from_dic2)

# [Quiz 참고 예제]
# menu = {}
# num = 0
# wh = True
# while wh :
#   print('================')
#   print('1.메뉴 등록') ; print('2.메뉴 별 가격') ; print('3.메뉴 가격 수정') ; print('4.종료')
#   print('================')
#   num = int(input('번호 입력:'))
#   if num == 1:
#     name = input('메뉴 이름:')
#     if menu.get(name) == None:
#       menu[name] = input('가격:');
#     else:
#       print('입력하신 메뉴는 이미 존재 합니다.')
#   elif num == 2:
#     for key, value in menu.items():
#       print(key,'\t',value)
#   elif num == 3:
#     name = input('수정 할 메뉴 이름:')
#     if menu.get(name) == None:
#       print('입력 하신 메뉴는 존재 하지 않습니다.')
#     else: 
#       menu[name] = input('가격:')
#   elif num == 4:
#     wh = False
#     print('프로그램을 종료 합니다.')
#   else:
#     print('번호를 다시 입력하세요.')

# [ Quiz ]: 학생의 인적 사항 등록 후 검색 하는 프로그램을 만드시오.
# (학번, 이름, 주소, 등급(A,B,C,D,E,F), (dic = {'학번'{dic}})
# 1.학생 등록
# 2.학생 검색
# 3.학생 수정
# 4.학생 삭제
# 5.전체 학생 목록
# 6.종료

# import os,copy,collections
# info={}; info2=collections.OrderedDict()
# wh=True; num=0; number=""; name=""; addr=""; gr=""
# while wh:
#   print("===============================")
#   print("1.학생 등록");print("2.학생 검색")
#   print("3.학생 수정");print("4.학생 삭제")
#   print("5.전체 학생 목록");print("6.종료")
#   print("===============================")
#   num = int(input("번호 선택 >> "))
#   if num == 1:
#     number = input("학번 입력: ")
#     if info.get(number) == None:
#       name = input("학생 이름 입력: ")
#       addr = input("학생 주소 입력: ")
#       gr = input("학생 등급 입력: ")
#       info2["학번"]=number; info2["이름"]=name; info2["주소"]=addr; info2["등급"]=gr
#       info[number] = copy.deepcopy(info2)
#       info2.clear()
#       print("등록 완료")
#     else:
#       print("이미 등록 된 학번 입니다.")
#   elif num == 2:
#     number = input("검색 학번 입력: ")
#     if info.get(number) == None:
#       print("입력 하신 학번은 존재하지 않습니다.")
#     else:
#       print("학번 {}의 정보는 {}입니다.".format(number,info[number]))
#   elif num == 3:
#     number = input("수정 하실 학번 입력: ")
#     if info.get(number) == None:
#       print("입력하신 학번은 존재하지 않습니다.")
#     else:
#       print("학번 {}의 정보는 {} 입니다.".format(number,info[number]))
#       val = input("수정 항목 입력: ")
#       if val not in info[number].keys():
#         print("수정 항목을 확인해주세요.")
#         print("메뉴선택 화면으로 돌아갑니다.")
#         os.system("pause")
#         os.system("cls")
#         continue
#       change = input("변경 정보 입력: ")
#       if val == "학번":
#         if info.get(change) == None:
#           info[number][val] = change
#           tmp = info[number]
#           info.pop(number)
#           info.update({change:tmp})
#           print("수정 완료")
#         else:
#           print("이미 등록 된 학번 입니다.")
#       else:
#         info[number][val] = change
#         print("수정 완료")
#   elif num == 4:
#     number = input("삭제 하실 학번 입력:")
#     if info.get(number) == None :
#       print("입력 하신 학번은 존재하지 않습니다.")
#     else :
#       print("학번 {}의 정보는 {} 입니다.".format(number,info[number]))
#       info.pop(number)
#       print("삭제 완료")
#   elif num == 5:
#     for k,v in info.items():
#       print(k,"\t",v)
#   elif num == 6:
#     wh = False
#     print("프로그램 종료")
#   else:
#     print("번호를 잘 못 선택하셨습니다.")
#   os.system("pause")
#   os.system("cls")

# [예제.6]
# st = "String Indexing"
# print(st)
# print(st[0])
# print(st[10])
# print(st[0:6])

# for val in st:
#   print(val)

# [예제.7]
# st = "python is Easy, Programming"
# print(st)
# print(st.upper())
# print(st.lower())
# print(st.title())
# print(st.swapcase())

# print(st.count('a'))
# print(st.count("Easy"))
# print(st.count("AAA"))

# print(st.find('a'))
# print(st.index('a'))
# print(st.find('a',12))
# print(st.index('a',12))

# [예제.8]
# st1 = " Python "
# print("*{}*".format(st1))
# print("*{}*".format(st1.strip()))
# print("*{}*".format(st1.lstrip()))
# print("*{}*".format(st1.rstrip()))

# st2 = "2024/07/09"
# print(st2)
# st2 = st2.replace('/','.')
# st2 = st2.replace(st2[0:4],"2025")
# print(st2)

# st3 = "Never Ever Give Up"
# print(st3)
# print(st3.split())
# st3 = st3.replace(' ',':')
# print(st3)
# lst = st3.split(':')
# print(lst)
# st4 = " ".join(lst)
# print(st4)

# st5 = """Never Ever Give Up
# Never Ever Give Up
# Never Ever Give Up"""

# print(st5)
# print(st5.splitlines())

# [문제 정답코드]
userin = input("이름과 나이 입력 (공백 구분!):")
name,age = userin.split(' ')
print("이름:{},나이:{}".format(name,age))


expression = input('수식을 입력 하세요. :(ex: 5 * 5) ')
if '+' in expression:
  num1, num2 = expression.split('+')
  num1 = int(num1.strip())
  num2 = int(num2.strip())
  print(num1 + num2)
elif '-' in expression:
  num1, num2 = expression.split('-')
  num1 = int(num1.strip())
  num2 = int(num2.strip())
  print(num1 - num2)
elif '*' in expression:
  num1, num2 = expression.split('*')
  num1 = int(num1.strip())
  num2 = int(num2.strip())
  print(num1 * num2)
elif '/' in expression:
  num1, num2 = expression.split('/')
  num1 = int(num1.strip())
  num2 = int(num2.strip())
  print(num1 / num2)
