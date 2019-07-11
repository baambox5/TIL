#딕셔너리 반복문 활용

lunch = {
    '중국집': '02-345-1245',
    '분식집': '031-123-2622',
    '일식집': '089-5124-3256'
}

# 기본 활용
for key in lunch:
    print(key)
    print(lunch[key])

# key, value 둘다 가져옴 .items()
for key, value in lunch.items():
    print(key, value)

# value 만 가져오기 .values()
for value in lunch.values():
    print(value)

# key 만 가져오기 .keys()
for key in lunch.keys():
    print(key)