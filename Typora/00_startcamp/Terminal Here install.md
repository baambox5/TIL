## Terminal Here

- 검색탭에서 terminal here 검색 -> install

- ctr+shift+p에서 shortcut -> preferences ~~~(JSON없는 것) ->

  그 안 검색에서 키보드 버튼 반응 on -> ctr+` -> toggle terminal 삭제 -> terminal here 검색 ->

  더블 클릭 -> ctr+` 입력 후 enter



-----

### f-string

- 괄호 안에서 함수 사용가능!



### os(예제는 파일 이름 바꿈)

- os를 import한다

  import os

- 해당 폴더로 들어간다.

  os.chdir(r'경로')

  > 윈도우 \의 경우 이스케이프 문법으로 인식하기 때문에 '경로'앞에 r을 붙인다.

- 폴더 안의 모든 파일 이름을 돌면서 바꾼다. (for문 활용)

  > os.listdir('디렉토리 주소') 위의 chdir로 갔을 경우에는 주소를 .으로 설정
  >
  > os.rename(이전파일명, 바꿀파일명)

- 여기에서 또 수정해야할 경우

  > os.rename(filename, filename.replace('수정전 문구', '수정후 문구'))



> ssafy slack방 : ssafy-02-djpy2