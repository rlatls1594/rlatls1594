# [ Tuple, 튜플 ]
# - N개의 요소로 이루어진 집합
# - List와 유사한 구조를 갖는다.
# - Tuple을 정의 할 때에는 "()" 를 사용하며, 생략도 가능하다. 
# -- 하지만 선생님은 "튜플"임을 알 수 있도록 괄호를 생략하지 않는다.
# - Tuple로 정의 된 데이터 묶음은 변경이 불가능하다. (List와의 차이점)
# -- 데이터 변경이 불가능한 곳에서 묶음 처리할 때 사용하는 기능
# -- 데이터 변경 방지 목적으로 튜플을 많이 사용한다.
# -- 내부 색상표, 좌표값 등 고정값이 필요한 경우 튜플로 정의하는 경우가 많다.
# -- Tuple이랑 List의 사용법은 유사하지만 데이터 변경이 불가능하다라는 차이점이 있다.

# [예제.1]
# tu1 = (1,2,3)
# tu2 = 4,5,6
# tu3 = tu1 + tu2
# 여러 개의 값을 Tuple로 묶어주는 작업을 packing 패킹이라고 한다
# 두 개의 Tuple을 합쳐 새로운 Tuple을 정의할 수 있다
# print(tu1, type(tu1))
# print(tu2, type(tu2))
# print(tu3, type(tu3))
# print(tu1[0])
# print(tu2[0:2])
# List와 같이 범위 지정도 가능하다
# print(tu1[-1])
# 음수 접근도 가능하다

# a,b,c = tu1
# print(a,b,c)
# Tuple 튜플로 묶인 데이터를 해제하는 작업을 unpacking, 언패킹이라고 한다


# 튜플 함수
# 함수          설명
# count(value)  튜플에서 일치하는 값의 수를 반환 한다  
# index(value)  튜플에서 일치하는 값의 인덱스 번호를 반환 한다

# [예제.2]
# tu = (100,200,"String",100,123.456)
# print(tu.count(100))
# print(tu.index(123.456))

# for a in tu:
#   print(a)
# Tuple 튜플도 반복 가능하다

# [ Dictionary, 사전 자료형 ]
# - 사전 자료형은 (Key-Value) 쌍으로 데이터 목록을 구성한다.
# - 특정 Value에 각각의 Key를 연결하여 Key를 첨자(Index)로 사용한다.
# - 사전 자료형은 사람이 사용하기 편리하고 탐색속도가 빠른 장점이 있다.
# - 사전 자료형을 정의할 때에는 "{ }" 를 사용한다.

# *****[예제.3]*****
# student = {"학번":"1-10000", "이름":"홍길동", "학과":"IT학과"}
# : , 콜론을 기준으로 왼쪽은 키 , 오른쪽은 value
# student = {"학번":"1000", "이름":"홍길동", "학과":["컴퓨터공학","전자공학"]}
# print(student, type(student))
# print(student["학과"])

# student["등급"] = "A"
# print(student)
# 새로운 키와 값을 추가하면 실행 및 출력도 가능하다
# Index의 경우 기존 Index 틀을 유지하려 하기 때문에 새로운 값을 추가하게되면 out of range 오류가 난다
# Dictionary의 경우 Index 처럼 번호 값으로 값을 저장하는 것이 아니기 때문에 순서에 크게 상관이 없다
# 따라서 Dictionary의 경우 가끔 순서에 상관 없이 출력될 때도 있다. 
# 메모리에서 출력하기 편한 구조를 먼저 출력하기 때문.
# ***** 키 : value 구조는 반드시 습득하고 넘어갈 수 있도록 하자. *****

# [예제.4]
# dic1 = {}
# for i in range(3):
#   k = input("키입력: ")
#   v = input("값입력: ")
#   dic1[k] = v
# print(dic1)

# [예제.5]
# dic = {1:'A', 2:'B', 3:'C', 4:'D'}
# dic.update({5:'E'})
# print(dic)
# print(dic.get(3))
# print(dic.get(100))
# print(dic.keys())
# print(dic.values())
# key_lst = list(dic.keys())  # -> 사전 Dic -> 리스트 형 변환 기본값
# val_lst = list(dic.values())
# print(key_lst, val_lst)

# key 값
# for val in dic:
#   print(val)
# value 값
# for val in dic.values()
#   print(val)

# for key,val in dic.items():
#   print(key, val)

# dic.pop(2)
# print(dic)
# data = dic.pop(2)
# print(dic ,data)
# data2 = dic.popitem()
# print(dic,data2)
# dic.clear()
# print(dic)

# get은 맵핑 되어있는 키의 값을 가져오는 기능과 더불어 데이터가 있는지 없는지 확인하는 기능 또한 수행한다.
# Index의 경우 잘못된 인덱스를 지정할 경우 에러가 발생한다.
# 하지만 dic.get은 에러가 발생하지 않고 None이 출력된다
# 위에서 3이라는 키의 값은 'C'
# 100이라는 키는 없으므로 None 출력
# dic.keys() 와 dic.values() 같은 경우 일반 List 형식으로 출력되지 않음
# dict_keys([1, 2, 3, 4, 5])
# dict_values(['A', 'B', 'C', 'D', 'E'])
# -> print(key_lst, val_lst) 처럼 List로 형 변환 해서 가져와야함 

# 반복문 돌릴 때도 키 값만 가지고 온다
# 전체 value 값이 필요할 때는 
# for val in dic.values():
#   print(val)
# key()키 값이 아니라 values()벨류 값을 가져오면 알아서 value 값을 가져오게 됨

# items 를 사용해서 key value 를 한 쌍으로 묶어서 한 번씩 가져올 수도 있다 
# Tuple 로 묶인 데이터를 Unpacking 언팩킹 한다

# pop 은 값을 추출 
# popitems 를 사용해서 마지막 키 - 값을 쌍으로 추출 할 수도 있지만 거의 사용하지 않는다
# clear 로 삭제, 초기화


# key_lst = [1,2,3,4,5]
# from_dic1 = {}.fromkeys(key_lst)
# from_dic2 = {}.fromkeys(key_lst,100)
# print(from_dic1)
# print(from_dic2)

# 특정 List에 들어있는 값을 키 값으로 정의할 수 있다
# from_dic1은 기본값 None으로 저장
# from_dic2는 100 지정했으므로 100으로 저장


"""
# [ Quiz ] : 학생의 인적 사항 등록 후 검색하는 프로그램을 만드시오.
# 레퍼런스 제공
# (학번, 이름, 주소, 등급(A,B,C,D,E,F), (dic = {'학번'{dic}}))

# 1. 학생 등록
# 2. 학생 검색
# 3. 학생 수정
# 4. 학생 삭제
# 5. 전체 학생 목록
# 6. 종료

# [ Quiz 참고 예제 , 레퍼런스 ]
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

# -> 풀이 및 해석 코드
# (학번, 이름, 주소, 등급(A,B,C,D,E,F), (dic = {'학번'{dic}})
students = {}
choice = 0
number = ""
name = ""
address = ""
grade = ""
wh = True
while wh:
    # 메뉴를 매번 직접 출력. 매번 직접 출력하고 싶지 않으면 def나 lambda 함수 사용해야하는데 안배움
    print("학생 등록 및 검색 프로그램")
    print("============메뉴============")
    print("1. 학생 등록")
    print("2. 학생 검색")
    print("3. 학생 정보 수정")
    print("4. 학생 삭제")
    print("5. 전체 학생 목록")
    print("6. 종료")
    print("===========================")
    choice = int(input("메뉴 선택: "))
# 학생 정보를 저장하는 Dictionary인 students 정의
# while = True 문을 사용해서 루프 반복, False를 만나면 종료
# 단순 메뉴 설정이므로 그냥 print로 출력
# if , elif , else로 분기 추가
# int로 정수 입력 제한
# 아래에서는 input으로 정보 입력

# 1. 학생 등록
    if choice == 1:
        number = input("학번 입력: ")
        if number in students:
            print("이미 등록된 학번입니다.")
        else:
            name = input("이름 입력: ")
            address = input("주소 입력: ")
            grade = input("등급 입력(A~F): ")
            if grade not in list("ABCDEF"):
                print("유효하지 않은 등급입니다. 등록 취소.")
            else:
                students[number] = {"이름": name, "주소": address, "등급": grade}
                print(f"{name} 학생의 정보가 정상적으로 등록 되었습니다.")
# 1번을 선택했을 때 나오는 내용을 만들어줌 : 학번, 이름, 주소, 등급(A,B,C,D,E,F)
# 중복 등록 방지를 위해서 학번을 학생에 정의. in을 사용해서 key : value 구조로 value 값이 있는지 확인 
# 등급은 A~F로 설정되어있으니 List로 만들고 List에 포함되어있지 않으면 유효하지 않은 등급을 알림
# 새 학생의 정보를 students[number]에 = {"이름": name, "주소": address, "등급": grade} 내용으로 저장

# 2. 학생 검색 (이름으로 검색 시 동명이인이 있을 수 있으므로 학번으로 검색하는 것이 나을려나?)
    elif choice == 2:
        number = input("검색할 학생의 학번 입력: ")
        info = students.get(number)
        if info:
            print(f"학번: {number} | 이름: {info["이름"]} | 주소: {info["주소"]} | 등급: {info["등급"]}")
        else:
            print("학번에 일치하는 학생이 없습니다. 확인 후 다시 입력 해주십시오")
# 학번 입력 후 students.get(number)로 해당 학생의 정보 출력
# get을 통해서 key 와 value 설정  
# info 변수를 지정해서 학생의 정보 대신
# info 변수를 통해서 학번 입력 시 이름, 주소, 등급이 출력되도록 함

# 3. 학생 정보 수정
    elif choice == 3:
        number = input("수정할 학생의 학번 입력: ")
        if number not in students:
            print("존재하지 않는 학번입니다.")
        else:
            print("현재 정보: ", students[number])
            name = input("새로운 이름 입력 (Enter 입력 시 변경 안 함): ")
            address = input("새로운 주소 입력 (Enter 입력 시 변경 안 함): ")
            grade = input("새로운 등급 입력(A~F, Enter 입력 시 변경 안 함): ")
            if name:
                students[number]["이름"] = name
            if address:
                students[number]["주소"] = address
            if grade:
                if grade in list("ABCDEF"):
                    students[number]["등급"] = grade
                else:
                    print("유효하지 않은 등급 입력. 등급 변경 안 함.")
            print(f"{name} 학생의 정보가 수정되었습니다.")    
# 학번을 입력 받아 해당 학생의 정보 존재 유무를 먼저 파악
# print("현재 정보: ", students[number])를 통해서 학생의 기본 정보를 출력
# 변경 사항을 입력 받고 Enter 입력 시 변경하지 않고 그냥 넘기는 조건 분기 추가
# 등급의 유효성을 확인하고 새로운 값들을 Dictionary에 저장

# 학번까지 수정하고 싶다면 아래와 같이 좀 복잡해짐 ################################
# elif choice == 3:
#     old_no = input("수정할 학생의 학번 입력: ")
#     if old_no not in students:
#         print("존재하지 않는 학번입니다.")
#     else:
#         print("현재 정보:", students[old_no])
#         field = input("수정 항목 입력(학번/이름/주소/등급): ")

#         if field == "학번":
#             new_no = input("새 학번 입력: ")
#             if new_no in students:
#                 print("이미 등록된 학번입니다. 변경 불가.")
#             else:
#                 # 1) 기존 레코드 꺼내기
#                 record = students.pop(old_no)
#                 # 2) 내부에 '학번' 필드도 함께 업데이트해야 한다면
#                 record["학번"] = new_no
#                 # 3) 새 키로 재등록
#                 students[new_no] = record
#                 print(f"학번이 {old_no}에서 {new_no}으로 변경되었습니다.")

#         elif field in ("이름", "주소", "등급"):
#             new_val = input(f"새 {field} 입력: ")
#             # 등급 유효성 체크
#             if field=="등급" and new_val not in list("ABCDEF"):
#                 print("유효하지 않은 등급입니다. 변경 취소.")
#             else:
#                 students[old_no][field] = new_val
#                 print(f"{field}이(가) 수정되었습니다.")

#         else:
#             print("수정 가능한 항목이 아닙니다.")
##########################################################################

# 4. 학생 삭제 (여기서 한 번 더 진짜 삭제 여부를 물어본다면?)
    elif choice == 4:
        number = input("삭제할 학생의 학번 입력: ")
        if number in students:
            confirm = input("정말 삭제하시겠습니까? (y/n): ")
            if confirm == "y":
                del students[number]
                print('학생 정보가 삭제되었습니다.')
            else:
                print("해당 학번의 학생이 없습니다.")
        else:
            print('해당 학번의 학생이 없습니다.')
# 학번 확인
# 삭제는 중요한 작업이므로 다시 한 번 검증
# 만약 해당 학번의 학생이 없는 경우 삭제 여부를 묻기 전에 없음을 출력
# del을 종속 문장으로 구성해서 삭제 여부 검증 후 Dictionary 삭제

# 5. 전체 학생 목록
    elif choice == 5:
        if not students:
            print("등록된 학생이 없습니다. 학생을 등록하여 주십시오.")
        else:
            print("전체 학생 목록: ")
            for number, info in students.items():
                print(f"학번: {number} | 이름: {info["이름"]} | 주소: {info["주소"]} | 등급: {info["등급"]}")  
# 등록된 학생이 있는지 없는지부터 확인 후
# in students.items()를 통해서 key와 value 값을 쌍으로 가져와서 : [ ] 에 각각 저장. 그리고 전체 학생 정보 출력

# 6. 종료
    elif choice == 6:
        wh = False
        print("학생 등록 및 검색 프로그램을 종료합니다.")
    else:
        print("입력하신 번호는 지원되지 않습니다. 다시 입력하여 주십시오.")
# while True로 반복했던 작업을 while Flase로 종료
"""

# -> 선생님 코드 (너무 어려운데????????????????)
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
#         os.system("pause") # os모듈을 통해서 cmd 창에서 실행 
#         os.system("cls") # cmd 창에서는 매우 빠르게 처리되므로 pause랑 cls cmd창 명령어를 입력
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
# 위 프로그램의 데이터는 종료 시, 컴퓨터 종료 시 사라진다
# 왜? RAM에 저장되는 데이터이므로
# 그럼 데이터를 유지하려면 DB를 사용해야함
# 데이터를 DB에 저장해야 영구적으로 데이터 사용이 가능 



# >> String 문자열
# 메모리에 데이터가 저장될 때 문자 자체가 그대로 저장되는 것이 아님. 
# 아래처럼 1byte, 한 글자씩 저장됨 
# st = 'string indexing'
# ->
# st = |'s|t|r|i|n|g| |i|n|d|e|x|i|n|g'|

# > string 함수
# 함수				설명
# find(str) 			문자열에서 특정 문자열을 찾아 해당 문자의 Index 값을 반환 한다
# count(str) 			문자열에서 특정 문자열을 찾아 해당 문자열의 수를 반환 한다
# lower()			문자열에서 영문자를 소문자로 변경하여 반환 한다
# upper()			문자열에서 영문자를 대문자로 변경하여 반환 한다
# strip()				문자열의 앞뒤 공백을 제거한다
# lstrip				문자열의 왼쪽 공백을 제거한다
# rstrip				문자열의 오른쪽 공백을 제거한다
# replace(old, new)	 	문자열의 특정 문자열을 변경한다
# split(str)			문자열의 특정 문자열을 기준으로 분리한다.


# [예제.6]
# st = "String Indexing"
# print(st)
# print(st[0])
# print(st[10])
# print(st[0:6])

# for val in st:
#     print(val)
# 문자열 + 문자열은 이어붙이기 / 문자열 * 3 등 곱하기는 반복 등 기억하기
 

# [예제.7]
# st = "python is Easy, Programming"
# print(st)
# print(st.upper())
# print(st.lower())
# print(st.title())
# print(st.swapcase())
# 그대로 출력
# upper는 모두 대문자로 변환해서 출력
# lower는 모두 소문자로 변환해서 출력
# title은 title만 대문자로 변환해서 출력
# swapcase는 소문자, 대문자를 반대로 변환해서 출력

# print(st.count('a'))
# print(st.count("Easy"))
# print(st.count("AAA"))
# 'a'는 2개
# "Easy"는 1개
# "AAA"는 없으니까 0개

# print(st.find('a'))
# print(st.index('a'))
# print(st.find('AAA'))
# print(st.index('AAA'))
# find와 index의 결과 값은 같음
# index는 있음이 확실 할 때 사용
# find는 있음이 긴가민가 할 때 사용
# 결과적으로 데이터가 없을 경우 find는 -1이라는 값을 출력 / index는 에러가 출력됨

# print(st.find('a'))
# print(st.index('a'))
# print(st.find('a',12))
# print(st.index('a',12))
# 첫 번째 'a' 위치
# 인덱스 12부터 다음 'a' 위치


# [예제.8]
# st1 = " Python "         #st 엘 l 이 아님. st 일 1 임
# print("*{}*".format(st1))
# print("*{}*".format(st1.strip()))
# print("*{}*".format(st1.lstrip()))
# print("*{}*".format(st1.rstrip()))
# 문자열 가공처리를 쉽게 할 수 있다
# 공백 및 특정 문자값 등을 쉽게 제거 할 수 있다
# 변경 및 출력

# st1 = "-Python-"
# print("*{}*".format(st1))
# print("*{}*".format(st1.strip('-')))
# print("*{}*".format(st1.lstrip('-')))
# print("*{}*".format(st1.rstrip('-')))
# () 값에 공백이면 공백을 지우겠다
# () 값에 '-' 등 특정 값을 넣으면 특정 값을 지우겠다
# 변경 및 출력 / 저장해서 출력하려면 st1 = 이라고 저장해줘야함

# st2 = "2024/07/09"
# print(st2)
# print(st2.replace('/','.'))
# print(st2.replace(st2[0:4],"2025"))
# print(st2)
# 변경 및 출력

# st2 = "2024/07/09"
# print(st2)
# st2 = st2.replace('/','.')
# st2 = st2.replace(st2[0:4],"2025")
# print(st2)
# 변경 및 저장 후 출력

# st3 = "Never Ever Give Up"
# print(st3)
# print(st3.split())
# st3 = st3.replace(' ',':')
# print(st3)
# print(st3.split())
# print(st3.split(':'))
# split은 내가 지정한 기준대로 문자열을 자름
# 자른 문자열을 List로 출력 -> lst로 저장 가능

# lst = st3.split(':')
# print(lst)
# split으로 쪼개서 lst에 저장함

# st4 = " ".join(lst)
# print(st4)
# st4 = "$".join(lst)
# print(st4)
# 쪼개진 lst 요소들을 join으로 다시 합쳐줌

# st5 = """Never Ever Give Up
# Never Ever Give Up
# Never Ever Give Up"""
# print(st5)
# print(st5.splitlines())
# 라인을 기준으로 자르겠다


# 풀어보고 싶으면 풀어볼 것 #
# 문제
# 앞에서 학습한 내용을 바탕으로 다음 문제를 풀어보세요
# 1. input() 함수로 이름과 나이 값을 입력 받을 때 한 번에 입력 받아 처리하고 출력 하는 코드를 작성 하시오
# 2. input() 함수로 입력 받은 더하기 , 빼기 , 곱하기 , 나누기의 간단한 수식을 처리 할 수 있도록 코드를 작성 하시오

# 선생님 풀이 코드
# userin = input("이름과 나이 입력 (공백 구분!):")
# name,age = userin.split(' ')
# print("이름:{},나이:{}".format(name,age))

# expression = input('수식을 입력 하세요. :(ex: 5 * 5) ')
# if '+' in expression:
#   num1, num2 = expression.split('+')
#   num1 = int(num1.strip())
#   num2 = int(num2.strip())
#   print(num1 + num2)
# elif '-' in expression:
#   num1, num2 = expression.split('-')
#   num1 = int(num1.strip())
#   num2 = int(num2.strip())
#   print(num1 - num2)
# elif '*' in expression:
#   num1, num2 = expression.split('*')
#   num1 = int(num1.strip())
#   num2 = int(num2.strip())
#   print(num1 * num2)
# elif '/' in expression:
#   num1, num2 = expression.split('/')
#   num1 = int(num1.strip())
#   num2 = int(num2.strip())
#   print(num1 / num2)


# -----------------오늘은 여기까지----------------------------






