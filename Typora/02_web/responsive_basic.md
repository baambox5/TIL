# responsive web

- flex는 gird와 달리 1차원적인 한줄 정렬
- flex container(이름 정해진 것 아님)라는 부모
- flex items 그 안의 애들
- .head>style>.container에 display: flex로 flex 속성을 줌
- 방향은 row가 default



#### flex-grow

- 이것의 숫자는 남는 여백을 어느정도 차지할지 결정.



- x축을 움직일때는 자식들을 움직여야 하기에 부모에 적용



#### order

- 기본적으로 0이라고 생각.
- 숫자가 작을수록 왼쪽으로 감(음수도 가능)



### 정리

- x 축 : justify
- y 축 : align
  - (reverse를 썼을 경우에는 row는 column으로, column은 row로 정렬되므로 주의!)
- 한줄 : items
- 여러줄 : content
- 개별요소 : self