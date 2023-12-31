"""
1) del을 이용하여 리스트에서 원소를 삭제할 수 있습니다. 
   리스트에서 어떤 값을 삭제하면 남은 값들은 새로 인덱싱됩니다. 
   따라서 여러 값을 삭제할 때는 어떤 값이 먼저 삭제된 후 남은 원소들에 대해서 순서를 새로 고려한 후 삭제해야 합니다.

2) remove()
   remove()는 list.remove("항목명")사용. 리스트 안에 있는 데이터의 이름을 알때. 
   단, 동일 값이 리스트에 2개 이상있을때 첫번째에 해당되는 항목만 지우게 됨

3) del()
   del()은 del list[항목위치]로 사용. 항목위치로 데이터 삭제. 

4) sum() , len() 
   sum()은 리스트 속 원자 값의 합 구하는 것 
   len()은 리스트 속 원자 개수 구하는 것 
   avg()는 존재하지 않음. 위 두개를 통해 구해야함. 
"""


#51. 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
# 1순위 닥터스트레인지, 2순위 스플릿, 3순위 럭키 
movie = ["닥터","스플릿","럭키"]
print(movie)

#52. 51번 리스트에 베트맨 추가 
#변수에 저장된 리스트에 값을 추가하려면 .append() 함수 사용하기 
movie.append("베트맨")
print(movie)

#53. movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
# 원하는 부분에 값을 집어넣기 위해선 insert(인덱스,값)을 사용하면 편리 
movie2=['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# --> 내가 생각한 답 (오답) : movie2[2].append("슈퍼맨")
movie2.insert(1,"슈퍼맨")
print(movie2)

#54. movie2에서 럭키를 삭제 
#remove와 del을 사용하는 것의 차이.... 인덱스로는 del 사용
# --> 내가 생각한 답 (되긴함) movie2.remove("럭키");
del movie2[3]
print(movie2)

#55. movie3에서 스플릿과 베트맨 삭제 
#기존에 삭제되어 리스트 인덱스가 재 할당 되니 그 부분 생각해서 인덱스값 써야함
movie3 = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie3[2]
del movie3[2] #--> 스플릿이 삭제되었으니 베트맨이 인덱스 2에 위치하게 됨
print(movie3)

#56. lang1과 lang2 리스트에서 그 원소를 모두 갖고 있는 langs 리스트 만들기
# 리스트를 더하면 두개가 합쳐짐 
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1+lang2
print(langs)

#57. 리스트에서 최대값과 최소값을 출력 
nums = [1,2,3,4,5,6,7]
min = min(nums);
max = max(nums);
print(min,max)

#58. 리스트의 합 출력 
nums2 = [1,2,3,4,5]
sum1 = sum(nums2)
print(sum1)

#59. 리스트에 저장된 데이터 개수 
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
# 내가 생각한 답 (오답) print(count(cook))
print(len(cook))

#60. 리스트의 평균 출력
nums3 = [1,2,3,4,5]
sum2 = sum(nums3)
len2 = len(nums3)
avg = sum2/len2
print(avg)
#내가 생각한 답 (오답) --> 함수 없음print(avg(num3))
#avg = sum(nums3) / len(nums3);
#print(avg)