
#21. letters가 바인딩하는 문자열에서 첫번째와 세번재 문자를 출력하세요  letters = 'python'
"""
파이썬 문자열에서 한 글자를 가져오는 것을 인덱싱이라고 부름. 파이썬 인덱싱은 0부터 시작 
문자열[인덱스]/리스트[인덱스] 의 형태로 찾을 수 있음 
정답은 p와 t가 나와야함 
"""
str = 'python'
print(str[0],str[2])

#22. 자동차 번호가 다음과 같을때 뒤에 4자리만 출력하세요 
license_plate = "24가 2210";
carnum = license_plate
#첫번재 해결법 
print(carnum[4:9])
#두번째 해결법 
print(carnum[-4:])

#23. 문자열에서 '홀'만 출력  ==> 이해 안됨 
string ="홀짝홀짝홀짝"
print(string[::2])

#24. 문자열 거꾸로 뒤집어 출력하기 
string = "PYTHON"
print(string[::-1])

#25. 아래의 전화번호에서 하이픈('-')제거 하고 출력 
#replace 함수 사용
phone_number = "010-1111-2222"
phone = phone_number.replace('-'," ")
print(phone)

#26. 25번 문제의 전화번호를 띄어쓰기 없이 붙이기
phone2 = phone.replace(" ","")
print(phone2)

#27. url에 저장된 웹 페이지 주소에서 도메인을 출력 
url = "http://sharebook.kr"
url_split = url.split('.') 
print(url_split)# 해당 값을 기준으로 글자를 나눈후 list 에 넣게됨. ['http://sharebook', 'kr']
print(url_split[-1]) #리스트에 담긴 애들중 맨 마지막에 kr이 들어가있으므로 나오게끔 
print(url_split[1])

#28. >> lang = 'python' >> lang[0] = 'P' >> print(lang) 해당 코드 실행 결과 예상 
# 에러남. 리스트는 값을 재할당 하는게 가능하지만 문자열은 불가능함 

#29. 아래문자열에서 소문자'a'를 대문자 'A'로 변경하세요
string = 'abcdfe2a354a32a'
string2 = string.replace('a','A')
print(string2)

#30. 해당 코드의 실행결과 예상해보기
"""
>> string = 'abcd'
>> string.replace('b', 'B')
>> print(string)

"""
# abcd ==> string에 값을 넣고 변수에 넣어주면 변동이 되지만 저 상태로 바로 string.replace이런 함수를 써주면
# 적용이 되지 않음. 
string = 'abcd'
string.replace('b', 'B')
print(string)
