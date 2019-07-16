## file open & close

- 사용 후 매번 close()해줘야 한다.

```python
f = open('만들 파일명', '행동')
```



## with 구문 (context manager)

- with이 끝나는 시점에 자동으로 close

```python
with open('with_ssafy.txt', 'w') as f:
```



## writelines

- list를 넣어주면, 요소 하나씩 저장된다.

```python
with open('ssafy.txt', 'w') as f:

​    f.writelines(['0\n', '1\n', '2\n', '3\n'])
```



## read

- 개행문자를 포함한 하나의 문자열

```python
with open('with_ssafy.txt', 'r') as f:
    all_text = f.read()
```



## readlines

- 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 list 로 만들어냄

```python
with open('with_ssafy.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
```



## DOCstring

> """
>
> 이 함수는 블라블라
>
> 누가 만들었고
>
> 어떻게 사용하고
>
> 이런 함수입니다.
>
> """



## reverse 함수

```python
reversed(목적 list)
```

- list의 순서를 뒤집는다.



## sort함수

```python
lines.sort(reverse=True)               # sort()는 반환하지 않음
lines = sorted(lines, reverse=True)     # sorted()함수는 반환함
```

- 주석을 참조할 것.



- #### encoding='utf-8' 추가해야 한글이 깨지지않는다.



## import관련

- import bs4의 경우 :  soup = bs4.BeautifulSoup() 의 형태로 사용
- from bs4 import BeautifulSoup의 경우 : soup = BeautifulSoup() 의 형태로 사용



## append함수

- 리스트에 요소를 추가하는 메서드 .append()
- list.append(1) : 리스트에 1을 추가한다.