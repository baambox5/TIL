### print 함수 활용

- align left =` '{:>10}'.format('test')`
- align right = `'{:10}'.format('test')`
- center align=`'{:^10}'.format('test')`
- (\_)를 채워넣기=`'{:_<10}'.format('test')`



### 함수 return시 주의사항

- return을 print로 하면 함수가 종료되었을 시에 None이 출력될 수 있다.
- return을 잘 사용할 것.



### 재귀함수

- RecursionError : 파이썬으로 재귀함수를 사용시 제한이 있다.



#### Parameter & Argument

- 보통 혼용해서 많이 사용한다.

  ```python
  # x == parameter(매개변수)
  # 매개변수는 함수의 정의 부분에서 볼 수 있다.
  def func(x):
      return x +2
  
  # 2 == argument(인자, 전달인자)
  # 인자는 함수를 호출하는 부분에서 볼 수 있다.
  func(2)
  ```




### data structure

- 불변인 타입은 파이썬이 hash table이라는 것으로 만드는데 이 hash table에 정해진 순서가 존재합니다.
- 현재 파이썬 실행환경에서 set.pop()이 계속 같은 이유는 처음 만들어진 set이 같은 hash table 값으로 이루어져 있기 때문이다.
- 파이썬 실행환경이 바뀌어야 pop으로 나오는 인자가 바뀐다. (즉, 파이썬 실행환경이 바뀌면 만들어지는 hash table도 바뀌기 때문.)