#파이썬 슬라이싱
"""
a라는 연속적인 객체들의 자료구조(리스트,튜플,문자열등)이 있다고 가정했을때
* a[start:end:step] 기본 형태는 이와 같음. 
- 각각 start,end,step은 양수 음수 가능 
- start : 슬라이싱 시작할 위치
- end : 슬라이싱을 끝낼 위치로 end는 포함하지 X
- step : 몇개씩 끊어서 가져올지와 방향정함. 옵션. 
- 양수 : 연속적인 객체들의 제일 앞에서부터 0을 시작으로 증가
- 음수 : 연속적인 객체들의 제일 뒤에서부터 -1을 시작으로 앞쪽으로

* 특정 시작위치부터 끝까지    : a[start:]
* 시작점부터 특정 위치까지    : a[:end]
* 특정 위치부터 특정 위치까지 : a[start:end]

"""

#join 메서드 다시 정리하기 
"""
.join(리스트)
'구분자'.join(리스트)
join함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 변환 하는 함수

1).join(리스트)
   매개변수로 들어온 ['a','b','c']리스트를 'abc' 문자열로 합쳐서 반환
2)'구분자'.join(리스트)
   리스트의 값과 값 사이에 '구분자'를 넣어서 하나의 문자열로 합쳐줌
   '-'.join(['a','b','c'])라 하면 'a_b_c' 형태의 문자열로 만들어 반환
"""

#split 메서드 
"""
 문자열.split() 
 문자열.split("구분자")
 문자열.split("구분자",분할횟수)
 문자열.split(sep='구분자',maxsplit=분할횟수) : 문자열을 maxsplit횟수만큼 sep 기준으로 구분
 * sep 파라미터 : 해당 파라미터의 기본값은 none이며 이때 동작은 띄어쓰기, 엔터를 구분자로하여 문자열을 자름
 * 문자열.split(sep=',')이면 문자열에서 "," 기준으로 자름 
 * sep은 생략하고 문자열.split(",")으로 써도 동일 
 * maxsplit 파라미터 : 해당 파라미터의 기본값은 -1 이며 이때 동작은 제한없이 자를 수 있을때까지 문자열 전체 자름
 * 문자열.split(maxsplit=1)이라 하면 , 문자열을 한번만 자르는 것 

 ** 문자열을 split으로 구분해서 print로 뽑으면 리스트에 담겨서 뽑힘 

"""

#sort 함수 설명 
"""
list.sort() 기본적으로 리스트 오름차순 정렬해주는 기능 
*새로운 정렬된 리스트를 반환 하는 함수는 sorted 함수이고
*리스트 자체를 정렬시켜버리는 것은 sort 함수 
list.sort(reverse=True) 하면 리스트가 내림차순으로 정렬 

- 숫자리스트.sort()의 결과 
  음수,0,양수 작은수부터 큰수로 오름차순 
- 소문자문자리스트.sort()의 결과
  우리가 알고 있는 알파벳 순 a,b,c,d,e, 순서로 잘 정렬 
- 대소문자리스트.sort()의 결과 
  대소문자리스트 sort()는 대문자ABCD순으로 다 나온후에, 소문자 abcd 순으로 정렬


"""


#61. price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만 출력 (슬라이싱)
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#62. 슬라이싱을 사용해서 홀수만 출력 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#63. 슬라이싱을 사용해서 짝수만 출력 
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums2[1::2])

#64. 슬라이싱을 사용해 리스트의 숫자를 역 방향으로 출력
nums3 = [1,2,3,4,5]
print(nums3[::-1])

#65. interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# 출력 예시 : 삼성전다, naver 
interest = ['삼성전자', 'LG전자', 'Naver']
#--> 리스트로 뽑아내는 방법 print(interest[::2])
print(interest[0],interest[2])

#66. join 메서드 
#출력 예시: 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
interest2 = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest2))

#67. 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우 이렇게 출력하기
print("/".join(interest2))

#68. interest2에 들어있는 애들 한줄씩 띄어서 출력하기
print("\n".join(interest2))

#69. split 메서드 
# 회사이름을 리스트로 분리 저장하기 
string = "삼성전자/LG전자/Naver"
string2 = string.split("/")
print(string2)

#70. 리스트 정렬 
# 리스트에 있는 값을 오름차순으로 정렬하세요 
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
#data.sort(reverse=True)
print(data)
data2= sorted(data)
print(data2) 

## sort와 sorted 다시 공부 하기 