data = 'ABC'
n = len(data)

# 순열
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if i == k or j == k:
                continue
            print(data[i], data[j], data[k])