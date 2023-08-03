#41. upper 메서드 해당 문자열을 대문자로 변경
ticker = "btc_krw";
print(ticker.upper())

#42. lower 메서드 해당 문자열을 대문자로 변경
ticker2 = "BTC_KRW"
print(ticker2.lower())

#43. capitalize 메서드 'hello'를 'Hello'로 변경
# capitalize 는 첫글자는 대문자로, 나머지는 소문자로 변환하는 함수 
# 문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자로, 나머지는 소문자로 변환하는건 title()함수 
a = "hello";
print(a.capitalize())

#44. endswith 메서드
#문자열이 지정 문자열로 끝나는지 체크. 
#true or false 로 반환함 
file_name = "file.xlsx";
#print(file_name.endswith("xlsx"))

#45. 파일이름이 xlsx로 끝나는지 xls로 끝나는지 확인해보기 
# 둘중 하나라도 true이면 true 반환. 
file = "file.xlsx";
#file.endswith(("xlsx","xls"))

print(file.endswith(("xlsx","xls")))
print(file.endswith("xls")) 
#문자열 자체가 일치하면 true 반환 

#46. startswith 메서드 
file2="2020_보고서.txt";
print(file2.startswith("2020"))
print("------")

#47.split 메서드. 문자열이 있을때 공백을 기준으로 문자열 나누기
a = "hello world";
print(a.split(" "))
print(a.split())
#그냥 split 쓰면 공백 기준으로 문자열 나눠짐 

#48. split 다음 문자열 btc 와 krw로 나누기
ticker = "btc_krw"
print(ticker.split("_"))

#49. 날짜를 표현하는 문자열에서 연도, 월, 일로 나누기 
date = "2020-05-01"
print(date.split("-"))

#50. 오른쪽 공백 있을때.. rstrip 
data = "123    "
print(data.rstrip())

data2="    123"
print(data.lstrip())
###########################################
#변수.함수()방식과 함수(변수) 방식 구분해보기
###########################################