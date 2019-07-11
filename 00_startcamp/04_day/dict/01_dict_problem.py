"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
scores = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
total_score = 0
for subject_score in scores.values():
    total_score = total_score + subject_score
average_score = total_score / len(scores)
print(average_score)

# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
total_score = 0
for student, subject in scores.items():
    for score in subject.values():
        total_score += score
average_score = total_score / (len(scores) * len(subject))
print(average_score)

# 선생님 풀이
total_score = 0
count = 0

for person_score in scores.values():
    for indivisual_score in person_score.values():
        total_score = total_score + indivisual_score
        # total_score += indivisual_score
        count = count + 1
        # count += 1

avg_score = total_score / count
print(avg_score)
#

# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# seoul_total_temperature = 0
# daejeon_total_temperature = 0
# gwangju_total_temperature = 0
# busan_total_temperature = 0
# seoul_count = 0
# daejeon_count = 0
# gwanju_count = 0
# busan_count = 0
# for city, temperature in city.items():
#     for i in range(len(temperature)):
#         if city == '서울':
#             seoul_total_temperature += temperature[i]
#             seoul_count += 1
#         elif city == '대전':
#             daejeon_total_temperature += temperature[i]
#             daejeon_count += 1
#         elif city == '광주':
#             gwangju_total_temperature += temperature[i]
#             gwanju_count += 1
#         else:
#             busan_total_temperature += temperature[i]
#             busan_count += 1
# print(f'서울 : {seoul_total_temperature/seoul_count}값')
# print(f'대전 : {daejeon_total_temperature/daejeon_count}값')
# print(f'광주 : {gwangju_total_temperature/gwanju_count}값')
# print(f'부산 : {busan_total_temperature/busan_count}값')
for name, temp in city.items():
    avg_temp = sum(temp) / len(temp)
    print(f'{name} : {avg_temp}')


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
count = 0
for name, temp in city.items():
    if count == 0:
        hot_temp = max(temp)
        cold_temp = min(temp)
        hot_city = name
        cold_city = name
        count += 1
    else:
        if max(temp) > hot_temp:
            hot_temp = max(temp)
            hot_city = name
        if min(temp) < cold_temp:
            cold_temp = min(temp)
            cold_city = name
print(f'가장 더웠던 도시는 {hot_city}이며, {hot_temp}이었습니다.')
print(f'가장 추웠던 도시는 {cold_city}이며, {cold_temp}이었습니다.')



# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
if 2 in city['서울']:
    print('네 있어요')
else:
    print('아니요 없어요')