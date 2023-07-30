
#11. 삼성 전자라는 변수로 50,000원을 바인딩 해보고, 삼성전자 주식 10주를 보유하고 있을 때 총 평가 금액 
삼성전자 = 50000
총평가금액 = 삼성전자*10
print(총평가금액)

#12. 삼성전자의 일부 투자 정보를 보고, 변수를 사용해서 시가총액/현재가/per 등을 바인딩 해보기 
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))
"""
type(변수) 쓰면, 해당 변수의 type을 알 수가 있음. 소수점은 float 타입
"""

#13. 문자열 출력 변수 s에는 "hello"/ t에는 "python"이 바인딩 되어 있음. hello! python 이렇게 출력해보기 
s = "hello"
t = "python"
print(s+"!",t)

#14. 파이썬을 이용한 값 계산
print(2+2*3)
print("답은 8")

#15. type 함수
a = 128
print(type(a))

#16. 문자열을 정수로 변환
num_str = "720"
#형변환 
num_int = int(num_str) #num_str 문자를 int 정수형으로 
print(num_int,type(num_int))

#17. 정수를 문자열 100으로 변환 
num = 100
#형변환 
num_str = str(num)
print(num_str,type(num_str))

#18. 문자열 "15.79"를 실수(float)타입으로 변환 
float_str = "15.79"
result = float(float_str)
print(result, type(result))

#19. year이라는 변수가 문자열 타입의 연도를 바인딩 하는 중. 이를 정수로 변환 후 최근 3년의 연도를 화면에 출력 
year = "2020"
print(int(year)+1) #2021
print(int(year)+2) #2022
print(int(year)+3) #2023

#20. 에어컨이 월 48,584원에 무이자 36개월 조건으로 홈쇼핑에 판매. 총 금액 계산 
월금액 = 48584
할부 = 36
총금액= 월금액*할부
print(총금액)
