# Web

- 서버를 통해 홈페이지 제작이라기보다 웹서비스를 제공

- URI : URL을 포함한 더 큰 개념



## HyperText

- 링크를 통해 기존의 한 방향 흐름에서 다중 방향으로 변화 가능



## HTML

- 프로그래밍 언어가 아니라 문서를 보기 위한 Markup language(텍스트)
- JavaScript만 프로그래밍 언어



### IE를 안 쓰는 이유

- 웹 표준을 지키지 않음

- 모바일 대응 하지 않음

- 성능 개선 X, 느림 X

  

- 모든 사용자가 같은 브라우저를 사용하는 것이 아니기 때문에, IE에도 어느정도 대응을 해야함.

  -> Cross Browsing



### Open Graph(OG)

- 링크를 붙여넣었을 때 해당 정보가 뜸.
- 헤드에 작성함.



### HTML VScode 설정

- 들여쓰기는 공백 2문자를 사용

  > ctr+shift+p => json 검색 => open setting => 
  >
  > "[html]": {
  >
  > ​        "editor.tabSize": 2    
  >
  > ​    },
  >
  > ​    "[css]": {
  >
  > ​        "editor.tabSize": 2
  >
  > ​    }
  >
  > 추가



## 웹 기본 표준

- html에서 속성값은 큰따옴표로

- 들여쓰기는 공백 2개

- 태그, 속성, 속성값 등에는 모두 소문자

- 속성명에서 '='사이에 띄면 너무 길어지므로 띄지말 것

- 최상위 html 태그에는 lang 속성을 주어 문서의 기본 언어를 지정한다.(스크린리더는 lang을 통해 언어를 인식하여 자동으로 음성을 변환하거나 해당 언어에 적합한 발음을 제공한다. => 모든 사용자를 위한 접근성)

- 모바일 설정

  ```html
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  ```

  

- IE는 특정 META 태그를 사용해 페이지가 특정 버전에 맞게 세팅되도록 지정해준다.

  ```html
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  ```



- Boolean 속성 값은 따로 명시하지 않는다.



### 웹 기본 설명

- 주석

  > ctr+/	=> 주석 자동

- 여는 태그, 닫는 태그

- 닫는 태그가 없는 경우도 있음

- href : 속성명

- 같은 열은 형제 관계

- div : 공간 분할



> chrome extension에서 web developer 검색해서 설치
>
> VS code에서 'open in brower' 설치(VS code에서 alt+b 누르면 바로 창이 뜬다.)(혹시 안 뜨는 경우에는 ctr+shift+p로 Keyboard Shortcuts검색 => open with 검색 후 뜨는 것 등록)
>
> VS code에서 'Beautify' 설치 => Keyboard Shortcuts에서 beautify검색 => Beautify selection을 ctr+alt+b 등록(다른 사람 코드를 받았을 때, 한번씩 이걸로 정렬해줄 것)



### Semantic Tag

- div 태그와 동일하지만, 컨텐츠의 의미를 설명하고 검색엔진 등에 활용할 수 있다.
- 구글에서는 해당 semantic tag를 기준으로 검색 결과를 보여준다.(검색 엔진 최적화)
- 프론트엔드쪽에서는 필수적인 부분이 되었음.
- 의미가 없는 부분은 div를 그대로 사용할 것. 



### H Tag

- h1태그는 기본적으로 하나만 사용



### Bold Tag

- <b>와 <strong>의 차이 : 둘다 굵게 표시하지만 'strong'의 경우 강조의 의미가 들어있음.



### Italic Tag

- <i>와 <em> 또한 Bold와 마찬가지.



### Highlight

- <mark>를 사용



### Del / Ins

- Del : 취소선, Ins : 밑줄



### Sub / Sup

- Sub : 밑 첨자, Sup : 윗 첨자



> ctr+alt+화살표 : 멀티화살표, 휠을 누른상태로 돌려도 된다.
>
> alt+화살표 : 해당 부분 이동
>
> alt+shift+화살표 : 해당 방향으로 복붙



### P tag

- 문단 나누기



### ol / ul / li

- ol : 순서가 있음
- ul : 순서가 없음
- li : 리스트



### headline

- \<hr>을 사용



### q / blockquote

- q : 쌍 따옴표
- blockquote : 인용시에 사용



### pre

- 코드가 깨지지 않음





