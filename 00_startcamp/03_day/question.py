'''
# 문제 1.
문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.
'''

str = input('문자를 입력하세요: ')

# 아래에 코드를 작성해 주세요.

print(f'{str[0]}, {str[len(str)-1]}')


'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

numbers = int(input('숫자를 입력하세요: '))

# 아래에 코드를 작성해 주세요.
for number in range(numbers):
    number = number + 1
    print(f'{number}')


'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

number = int(input('숫자를 입력하세요: '))

# 아래에 코드를 작성해 주세요.
if (number % 2) == 0:
    print('짝수')
else:
    print('홀수')

'''
문제 4.
표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
국어는 90점 이상,
영어는 80점 초과,
수학은 85점 초과, 
과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면 불합격)
다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 
'''

a = int(input('국어: '))
b = int(input('영어: '))
c = int(input('수학: '))
d = int(input('과학: '))

# 아래에 코드를 작성해 주세요.
if a >= 90 and b > 80 and c > 85 and d >= 80:
    print(True)
else:
    print(False)


'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''


prices = input('물품 가격을 입력하세요: ')

# 아래에 코드를 작성해 주세요.
prices = prices.split(';')
#prices.sort(reverse=True)
for i in range(len(prices)):
    prices[i] = int(prices[i])

prices = sorted(prices, reverse=True)
print(prices)

# 선생님 예문
makes = prices.split(';')

boxes = []
for make in makes:
    boxes.append(int(make))
boxes.sort(reverse=True)

for box in boxes:
    print(box)

# 리스트에 요소를 추가하는 메서드 .append()
# list.append(1) 리스트에 1을 추가한다.