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

  