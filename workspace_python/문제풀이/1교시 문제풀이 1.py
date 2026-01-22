
# ① 문자 개수 세기 (리스트 활용)
# 문자열 "programming"에서 각 문자가 몇 번 등장하는지 세어,
# [['p', 1], ['r', 2], ['o', 1], ...] 형태의 리스트로 출력하세요.

a1 = "programming"
b1 = a1.count('p')  
print(b1)


# ② 대소문자 변환
# 문자열 "Hello World"를 모두 대문자로, 모두 소문자로 변환한 결과를 각각 출력하세요.
a2 = "Hello World"
b2 = a2.upper()
print(b2)
c2 = a2.lower()
print(c2)
 


# ③ 회문 판별
# 문자열을 입력받아 앞뒤가 똑같은 회문인지 판별하는 프로그램을 작성하세요.
# (예: "level" → 회문)

a3 = input('단어를 입력하세요: ')
 
b3 = True                 # 회문 판별값을 저장할 변수, 초깃값은 True
for i in range(len(a3) // 2):      # 0부터 문자열 길이의 절반만큼 반복
    if a3[i] != a3[-1 - i]:      # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
        b3 = False        # 회문이 아님
        break
 
print(b3)    


# ④ 단어 뒤집기
# "Python is fun"이라는 문장을 단어 단위로 뒤집어 "fun is Python"으로 출력하세요.



# ⑤ 모음 제거하기
# 문자열 "beautiful day"에서 모음(a, e, i, o, u)을 모두 제거한 결과를 출력하세요.



# ⑥ 문자열 압축
# 문자열 "aaabbcddd"를 "a3b2c1d3" 형태로 압축하는 프로그램을 작성하세요.



# ⑦ 가장 긴 단어 찾기
# "Life is short, use Python" 문장에서 가장 긴 단어를 찾아 출력하세요.



# ⑧ 특정 단어 개수 세기
# "banana bandana banana"에서 "banana"가 몇 번 등장하는지 세어 출력하세요.



# ⑨ 문자열 정렬
# 문자열 "zebra"의 문자들을 알파벳 순서대로 정렬하여 "aberz"를 출력하세요.



# ⑩ 부분 문자열 찾기
# 문자열 "abracadabra"에서 "abra"가 시작되는 모든 인덱스를 출력하세요.

