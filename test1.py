#python test 2023-07-30

#1. 화면에 Hello World 문자열 출력 
print("Hello World")

#2. 화면에 Mary's cosmetics을 출력 
print("Mary's cosmetics")

#3. 신씨가 소리질렀다. "도둑이야". 출력하기
print('신씨가 소리질렀다. "도둑이야".')

#4. 화면에 C:\Windows를 출력하세요
print("C:\Windows")

#5. 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요 
print("안녕하세요. \n만나서\t\t반갑습니다.")
##\n은 줄바꿈 \t 는 띄어쓰기 

#6. print 함수에 두개의 단어를 입력했을 경우 
print("오늘은","일요일")
##띄어쓰기 형태로 나옴 

#7. print() 함수를 사용하여 naver;kakao;sk;samsung 출력
print("naver;kakao;sk;samsung")

#8. print() 함수를 사용하여 naver/kakao/sk/samsung 출력
print("naver/kakao/sk/samsung")

#9. 다음 코드를 수정하여 줄바꿈 없이 출력하세요. 
print("first");print("second") #이렇게 출력하면 줄바꿈 되서 나옴
"""
# - sep=" " 
 이 옵션을 이용하게 되면 print문의 출력문들 사이에 해당하는 내용을 넣을 수 있습니다. 기본 값으로는 공백이 들어가 있으며 이를 사용해 원하는 문자를 입력할 수 있습니다.
- end=" "
 이 옵션의 경우 print 문을 이용해 출력을 완료한 뒤의 내용을 수정할 수 있습니다. 기본 값으로는 개행(\n)이 들어가 있으며 이를 사용해 개행을 없애거나 원하는 문자를 입력할 수 있습니다.
"""
print("first",end="");print("second")

#10 5/3의 결과를 화면에 출력하세요
print(5/3)