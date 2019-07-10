# DOCstring
"""
이 함수는 블라블라
누가 만들었고
어떻게 사용하고
이런 함수입니다.
"""

"""
다음과 같은 내용의 파일 quest.txt 가 있다.
0
1
2
3

이 파일의 내용을 다음과 같이 역순으로 reverse_quest.txt 라는 파일로 저장하시오.
3
2
1
0
"""

# 1. 읽고
with open('quest.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
# 2. 뒤집고    
    #lines.sort(reverse=True)               # sort()는 반환하지 않음
    lines = sorted(lines, reverse=True)     # sorted()함수는 반환함
    print(lines)    
# 3. 작성하고
with open('reverse_quest.txt', 'w') as f:
    f.writelines(lines)