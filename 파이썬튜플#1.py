
#튜플
"""
1. 리스트와의 차이점 
   1) t=(1,) 처럼 1개의 요소만 가질땐 요소 뒤에 쉼표를 반드시 붙이기
   2) t=1,2,3처럼 소괄호 생략이 가능하다. 
   3) 리스트 요소값은 변화가 가능. 튜플은 요소값 변화가 불가능  
2. 인덱싱하기 
   1) 문자열,리스트와 마찬가지로 t[0] 이런 인덱싱 가능 
3. 슬라이싱하기
   1) t1=(1,2,'a','b') >> t1[1:] >> (2,'a','b') 슬라이싱 가능 
4. 튜플 사칙연산
   1) 튜플 더하기 가능. 
   2) 튜플 곱하기 가능. 
5. 튜플 길이 구하기 len(t) 함수 가능 

6. 리스트변환 및 튜플 변환 
   1) list(튜플)/tuple(리스트)
   
7. range 함수 
   * range(stop)
   range(10)은 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 숫자를 생성한다.
   마지막 숫자 10(stop)은 포함되지 않는다.

   * range(start, stop)
   range(1, 11)은 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 숫자를 생성
   인자를 2개 전달하는 경우 첫번째 인자는 시작하는 숫자가 된다.

   * range(start, stop, step)
     range(0, 20, 2)
     0, 2, 4, 6, 8, 10, 12, 14, 16, 18
     마지막 인자 step은 숫자의 간격을 나타낸다.

     range(20, 0, -2)
     20, 18, 16, 14, 12, 10, 8, 6, 4, 2
     step으로 음수를 지정할 수 있다.

"""



#71. my_variable 이름의 비어있는 튜플을 만들라.
my_variable = ()
print(type(my_variable))

#72. movie_rank이름의 튜플에 순위 정보 저장하기 1.닥터 2.스플릿 3. 럭키
movie_rank =("닥터","스플릿","럭키")
print(movie_rank)

#73. 숫자 1이 저장된 튜플을 생성 
#--> 잘못된 예 num = (1)
#--> 하나의 정수값을 저장하면 튜플이 아니라 정수로 인식
#--> print(num,type(num)) 
#하나의 데이터가 저장되는 경우, 아래와 같이 쉼표를 입력해야함
num = (1, )
print(num,type(num))

#74. 다음 코드를 실행해보고 오류가 발생하는 원인을 설명 
"""
>> t = (1, 2, 3)
>> t[0] = 'a'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    t[0] = 'a'
TypeError: 'tuple' object does not support item assignment

--> tuple은 원소(element)의 값을 변경할 수 없음. 
"""

#75. t가 바인딩 하는 데이터 타입은? 
# 원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해 괄호 없이도 동작
t =1,2,3,4
print(t,type(t))

#76. 변수 t에는 아래 값 저장. 변수 t가 ('A','b','c')가리키도록 수정
t=('a','b','c');
#튜플 원소는 변경할수가 없음. t[0]='A' 이런거 안됨 
#새로운 튜플을 만들어 t 변수 업데이트 해야됨
t=('A','b','c')
print(t)

#77. 튜플을 리스트로 변환하기 
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)
print(interest, data)

#78. 리스트를 튜플로 
interest2 = ['삼성전자', 'LG전자', 'SK Hynix']
data2 = tuple(interest2)
print(interest2,data2)

#79. 튜플 언팩킹 . 다음 코드의 실행 결과 예상 
"""
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

--> apple banana cake 
"""

#80. range 함수. 1부터 99까지의 정수중 짝수만 저장된 튜플 생성 
data = tuple(range(2,100,2))
print(data)