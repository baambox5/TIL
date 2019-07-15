### text program

- Vscode 이외에 sublimetext가 가볍고 빠른 테스트 가능
- brackets - frontend개발자가 많이 사용하는 텍스트



- 안드로이드는 kotlin



## Jupyter

- jupyter로 실습 예정(데이터 사이언스쪽에서 자주 사용 - 그래프를 찍어줌)

- 설치 방법 및 실행방법

  > $ pip install jupyterlab
  >
  > $ python -m notebook => 해당 폴더에서 실행 (= $ jupyter notebook)

- 단축명령어 지정

  > $ code ~/.bashrc
  >
  > alias jp="jupyter notebook" 저장
  >
  > $ source ~/.bashrc

- **사용 끝난뒤에는 꼭 ctr+C로 끌 것**

- jupyter extension

  > jupyter extension 검색 -> $ pip install jupyter_contrib_nbextensions
  >
  > -> $ jupyter contrib nbextension install --user
  >
  > $ jp 실행 -> Nbextensions tap에서 table 검색 -> 제일 앞에 뜨는 거 check



- edit mode : 초록색
- command mode : 파란색
- command mode -> edit mode : 마우스 더블클릭 or 엔터



- #### edit mode 단축키

  - ctr + enter = 현재 셀 실행
  - shift + enter = 실행 + 다음셀 선택(다음 셀 없으면 새로운 셀 생성)
  - alt + enter = 실행 + 다음셀 생성

- #### command mode 단축키

  - d 연타 = 선택된 셀 삭제
  - z = 실행 취소
  - a = 선택된 셀 위쪽에 새로운 셀 생성
  - b = 선택된 셀 아래쪽에 새로운 셀 생성
  - shift 누른채로 d + d = 여러 셀 삭제

- 무한루프에 빠졌을때(in[*]인 경우(여기서 *은 대기중일때도 있음))

  > 위쪽의 kernel -> restart & clear output
  
- gitignore 설정

  > gitignore.io에서 jupyter검색 후 2줄 .gitignore에 복붙할 것



-----

### programming fonts

- 일정한 고정폭, Sans-serif(I와 l, O와 0을 비교하기 편해야 한다.), 가독성과 명확한 구분을 위해서

- Source Code Pro, Monaco, HACK, Dejavu sans mono 등이 유명하다

  > C:\Windows\Fonts\ 에 설치했던 것을 복붙할 것.
  >
  > chrome 설정 -> font 검색 -> 글꼴 맞춤설정 -> 고정폭 글꼴 -> 원하는 글꼴 설정
  >
  > vs code settings -> font 검색 ->  글꼴 이름 입력 -> Font Ligatures check
